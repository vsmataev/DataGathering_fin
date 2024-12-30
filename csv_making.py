import os
import pandas as pd

# Путь к тренировочной папке
training_set_path = "/Users/mc724rs/PycharmProjects/Сбор_и_Разметка_Данных/final_HW/training_set"

# Список для хранения данных
data = []

# Чтение всех файлов
for file in os.listdir(training_set_path):
    file_path = os.path.join(training_set_path, file)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Извлекаем метку из имени файла
    label = file.split("_")[-1].replace(".txt", "")  # Последняя часть имени файла
    data.append({"filename": file, "text": content, "label": label})

# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение в CSV (опционально)
df.to_csv("/Users/mc724rs/PycharmProjects/Сбор_и_Разметка_Данных/final_HW/training_set.csv", index=False)

print("Все получилось.")
