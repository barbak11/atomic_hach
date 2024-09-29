# Хакатон АтомикХак 2.0.
![АтомикХак](https://github.com/Konstagit/AtomicHack2/blob/master/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-19%20180143.png)

## Обзор
Этот репозиторий содержит проект, разработанный для Хакатона АтомикХак 2.0.  
Проект включает модель и веб-сервис детекции дефектов сварных швов

### Задача
**Проблематика**:
Человеческий фактор визуального контроля качества сварки швов обуславливает долгий процесс выполнения и не может обеспечить желаемой точности детекции дефектов
**Задача**:
Необходимо на основании готовго размеченного датасета реализовать модель для выявлений аномалий и сервис для взаимодействия пользователя с моделью.

### Данные
Был предоставлен готовый датасет из 1000+ изображений в формате YOLO label с размеченными дефектами на сварном шве:
![Дата1](https://github.com/Konstagit/AtomicHack2/blob/master/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-19%20173329.png)
![Дата2](https://github.com/Konstagit/AtomicHack2/blob/master/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-19%20173356.png)
#### Распределение
![Распределение](https://github.com/Konstagit/AtomicHack2/blob/master/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-19%20173903.png)

### Решение
За основу взята предобученная модель YOLOv8.Проведенны эксперименты с аугментацией данных,создан сервис на Streamlit для взаимодейсвтия с моделью
#### Архитектура
![Архитектура](https://github.com/Konstagit/AtomicHack2/blob/master/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-19%20174149.png)
#### Метрики
![Метрики](https://github.com/Konstagit/AtomicHack2/blob/master/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-19%20180527.png)
#### Сервис
![Сервис](https://github.com/Konstagit/AtomicHack2/blob/master/images/appStreamlit-GoogleChrome2024-06-1603-15-14-ezgif.com-video-to-gif-converter.gif)
## Содержимое
- `train_model`: Код по модели,эксперминеты с данными,разделение на train,test,val
- `service`: Каталог, содержащий все необходимое для запуска веб приложения на Streamlit.Здесь же лучшие веса модели.
- `images`: Изображенния для README

## Использование веб приложения

Сервис для определения деффектов сварных швов "ДефектоскопИИст"

### Предназначение

Сервис позволяет загрузить .zip архив или картинку для анализа и получить на выходе картинку с выделенными деффектами и информацией по ним

### Установка

#### Клонируйте репозиторий:
```bash
git clone https://github.com/Konstagit/AtomicHack2
```

#### Установка зависимостей
```bash
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

#### Запуск модели
```bash
python yolo\_app.py
```

#### Запуск web-сервиса
```bash
python app.py
```

## Обучение модели
Клонируйте репозиторий:
```bash
git clone https://github.com/Konstagit/AtomicHack2
 ```
   
Откройте Jupyter Notebook: :
```bash
python -m notebook train_model\fit_predict_yolo.ipynb
```
