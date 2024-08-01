import pandas as pd
from pytube import YouTube
from pydub import AudioSegment
import os

# Для загрузки данных из других csv поменять на соответсвующее пути. Csv для загрузки:
# balanced_train_segments.csv, eval_segments.csv, unbalanced_train_segments.csv
segments_file = 'csv_files/unbalanced_train_segments.csv'
labels_file = 'csv_files/class_labels_indices.csv'

# Путь, куда будут сохраняться аудио
save_path = 'dataset/dog/'

# Классы, для которых будут скачиваться аудио
#classes = ['Wind', 'Thunderstorm', 'Water', 'Fire']
#classes = ['Water', 'Wind', 'Thunderstorm', 'Fire', 'Rain', 'Waterfall', 'Stream', 'Wind noise (microphone)', 'Rustling leaves', 'Thunder']
#classes = ['Dog', 'Bark', 'Howl', 'Growling', 'Whimper (dog)']
classes = ['Dog']
classes_count = {class_name: 0 for class_name in classes}

segments_df = pd.read_csv(segments_file, delimiter=', ', on_bad_lines='skip')
labels_df = pd.read_csv(labels_file, on_bad_lines='skip')

class_mids = labels_df[labels_df['display_name'].isin(classes)][['mid', 'display_name']].to_dict('records')
filtered_segments = segments_df[segments_df['positive_labels'].apply(lambda x: any(mid['mid'] in x for mid in class_mids))]
mid_to_display = {mid['mid']: mid['display_name'] for mid in class_mids}
print(class_mids, '\n', len(filtered_segments), '\n', mid_to_display)
filtered_segments.head()

def download_and_trim_audio(youtube_id, start_time, end_time, save_path, filename):
    try:
        yt = YouTube(f'https://www.youtube.com/watch?v={youtube_id}')
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(output_path='/tmp')
        
        # Обрезка аудио
        audio = AudioSegment.from_file(audio_file)
        trimmed_audio = audio[start_time*1000:end_time*1000]  # pydub работает в миллисекундах

        #перевод в 16Khz и моно
        transformed_audio = trimmed_audio.set_frame_rate(16000).set_channels(1)

        # Сохранение аудио
        transformed_audio.export(os.path.join(save_path, filename), format="wav")
        
        # Удаление временного файла
        os.remove(audio_file)
        return True
    except Exception as e:
        print(f"Error downloading {youtube_id}: {e}")
        return False
    
for class_name in classes:
    class_path = os.path.join(save_path, class_name)
    os.makedirs(class_path, exist_ok=True)

full_count = 0
error_count = 0
for index, row in filtered_segments.iterrows():
    youtube_id = row['YTID']
    start_time = row['start_seconds']
    end_time = row['end_seconds']

    # Определение меток для текущего сегмента
    positive_labels = [label.replace('"', '') for label in row['positive_labels'].split(',')]
    
    for mid in positive_labels:
        if mid in mid_to_display:
            class_name = mid_to_display[mid]
            if classes_count[class_name] > 1500:
                continue
            class_path = os.path.join(save_path, class_name)
            filename = f"{youtube_id}.wav"
            
            full_count += 1
            if download_and_trim_audio(youtube_id, start_time, end_time, class_path, filename):
                classes_count[class_name] += 1

                print(f"Processed {youtube_id} for class {class_name}, count: {classes_count[class_name]} | total: {full_count}")
            else:
                error_count += 1
            break

print(f"Done! Error count: {error_count}, full count: {full_count}")