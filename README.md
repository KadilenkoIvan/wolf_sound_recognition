# wolf sound recognition
В этом репозитории лежат инструменты, которые использовались для создания модели для классификации волков и собак на аудио
  
## Установка библиотек
```
pip install -r requirements.txt
```
  
## Датасеты
Основной [датасет для обучения](https://www.kaggle.com/datasets/ivankadilenko/wolf-dog-cutted-dataset)  
Тестовый [датасет](https://www.kaggle.com/datasets/ivankadilenko/wolf-dog-val) 

## Основная модель
Ноутбук для обучения - main_train_test_notebooks/wav2vec2-base-wolf.ipynb
Ноутбук для тестирования - main_train_test_notebooks/wav2vec2-base-wolf-val.ipynb
  Лучшая обученная модель - best_model/best.pth
