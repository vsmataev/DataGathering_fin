import os
import shutil

# Путь к исходным папкам
base_path = "/Users/mc724rs/PycharmProjects/Сбор_и_Разметка_Данных/final_HW/dataset"
categories = ["pos", "neu", "neg"]

# Путь к новой папке для тренировочного набора
output_path = "/Users/mc724rs/PycharmProjects/Сбор_и_Разметка_Данных/final_HW/training_set"
os.makedirs(output_path, exist_ok=True)

# Копирование файлов
for category in categories:
    category_path = os.path.join(base_path, category)
    selected_files = os.listdir(category_path)[:1000]  # Берем первые 1000 файлов

    for file in selected_files:
        # Полный путь исходного файла
        src = os.path.join(category_path, file)

        # Новое имя файла с добавлением категории
        new_file_name = f"{os.path.splitext(file)[0]}_{category}.txt"
        dst = os.path.join(output_path, new_file_name)

        # Копирование файла
        shutil.copy(src, dst)

print(f"Файлы скопированы в: {output_path}")
