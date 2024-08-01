# wolf sound recognition
В этом репозитории лежат инструменты, которые использовались для создания модели для классификации волков и собак на аудио
  
## Установка библиотек
```
pip install -r requirements.txt
```
  
## Датасеты
Основной [датасет для обучения](https://www.kaggle.com/datasets/ivankadilenko/wolf-dog-cutted-dataset)  
Тестовый [датасет](https://www.kaggle.com/datasets/ivankadilenko/wolf-dog-val)    
Другие используемые нами [датасеты](https://www.kaggle.com/ivankadilenko/datasets)

## Основная модель
Ноутбук для обучения - `main_train_test_notebooks/wav2vec2-base-wolf.ipynb`  
Ноутбук для тестирования - `main_train_test_notebooks/wav2vec2-base-wolf-val.ipynb`  
Лучшая обученная модель - `best_model/best.pth`

### wav2vec2-base-wolf.ipynb
Эта версия ноутбука использовалась при обучении лучшей полученной модели. В файле представлены наш класс модели, датасета, аугментации, циклы обучения и валидация. В нём автоматически создаётся csv файл с путями и метками классов для каждой аудиозаписи из датасет.

### wav2vec2-base-wolf-val.ipynb
Получение метрик на тестовом датасете, вывод матрицы ошибок

### best.pth
Лучшая обученная версия модели. Параметры обучения можно посмотреть в `best_model/params.txt`. Её метрики на валидации и тесте можно посмотреть в `best_model/metrics.txt`

## Альтернативное решение
В этом решении обрабатываются не аудиофайлы, а их спектрограммы  
Ноутбук - `alternative_model_notebooks/QWEEWQQWEEWQQWEEWQWEEWQQWE`

## Дополнительные программы
### AudioSetParser
Файлы и скрипт нужные для скачивания данный из [AudioSet](https://research.google.com/audioset/)

### speech-extractor
Программа вырезающая человеческую речь из аудио

### noise_processing.ipynb
Обработка и удаление шума из аудиофайлов

### split_and_merge_audio.ipynb
Скрипт, который использовался для нарезки данных для основного [датасета](https://www.kaggle.com/datasets/ivankadilenko/wolf-dog-cutted-dataset). Если аудио слишком короткое, к нему присоединяются другие аудио того же, либо нулевого класса до тех пор, пока длинна не станет нужной. Если же оно слишком длинное, из его середины вырезается то количество фрагментов, которое туда помещается (Такие файлы лучше прослушать после нарезки). 
