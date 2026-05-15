import os
import json
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from config import FILE_NAME

load_dotenv(FILE_NAME)

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

csv_path = input("Введите путь к CSV файлу: ")

try:
    df = pd.read_csv(csv_path)
except Exception as e:
    print(f"Ошибка загрузки CSV: {e}")
    exit()

# CSV в текст
csv_data = df.to_csv(index=False)

prompt = f"""
Из текстового описания каждого товара {csv_data} необходимо извлечь следующую информацию: название, бренд, категорию и цену. Сохрани результат в формате JSON.

Пример ответа:
[
  {{
    "id": 0,
    "название": "...",
    "бренд": "...",
    "категория": "...",
    "цена": "..."
  }}
]
"""

try:

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": (
                    "Система извлечения иформации о товаре из текстового описания"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    # Удаление markdown
    if content.startswith("```json"):
        content = content.replace("```json", "").replace("```", "").strip()

    elif content.startswith("```"):
        content = content.replace("```", "").strip()

    parsed_json = json.loads(content)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(parsed_json, f, ensure_ascii=False, indent=2)

    print("Результат сохранён в файл 'output.json'")

except Exception as e:
    print(e)
