# DataAnalytics_lab2
Система извлечения данных

## Описание проекта
Проект представляет собой систему для автоматического извлечения характеристик товаров из CSV-файла с помощью LLM-модели DeepSeek через API.

Для каждого товара из датасета формируется текстовое описание на основе всех заполненных колонок, после чего модель извлекает:

- название
- бренд
- категорию
- цену

Результат сохраняется в JSON-файл.


## Запуск

### 1. Клонирование репозитория

```bash
git clone <repo_url>
cd <repo_name>
```


### 2. Создание виртуального окружения

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```


### 3. Установка зависимостей 

```bash
pip install -r requirements.txt
```


### 4. Настройка

#### Создание  `.env`

Необходимо создать файл `.env` в корне проекта:

```env
DEEPSEEK_API_KEY=your_api_key
```


### 5. Запуск

Запустите скрипт:

```bash
python main.py
```

После запуска скрипт запросит путь к CSV-файлу:

```text
Введите путь к CSV файлу:
```

Пример:

```text
data/products.csv
```


## Формат входных данных 

Пример CSV-файла:

```csv
title,description,price
iPhone 15,Apple smartphone with OLED display,999
Galaxy S24,Samsung flagship smartphone,899
```


## Формат выходных данных

Пример json-файла:

```json
[
  {
    "название": "iPhone 15",
    "бренд": "Apple",
    "категория": "smartphone",
    "цена": "999"
  },
  {
    "название": "Galaxy S24",
    "бренд": "Samsung",
    "категория": "smartphone",
    "цена": "899"
  }
]
```


## Демонстрация запуска и результата

https://github.com/user-attachments/assets/08039d1d-7c9c-4124-aa25-a3f35d7439a8



## Файл с входными данными

[FashionData_10.csv](https://github.com/user-attachments/files/27799023/FashionData_10.csv)


## Файл с реальными результатами работы скрипта

[output.json](https://github.com/user-attachments/files/27799041/output.json)

