import os
import rembg

input_folder = 'input_imgs'
output_folder = 'output_imgs'

# Создание папки для выходных изображений
os.makedirs(output_folder, exist_ok=True)

# Обработка каждого изображения в папке Input_imgs
for file_name in os.listdir(input_folder):
    # Проверка, что файл является изображением
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Загрузка изображения
        with open(os.path.join(input_folder, file_name), 'rb') as f:
            img = rembg.remove(f.read())

        # Получение имени файла без расширения
        file_name_without_ext = os.path.splitext(file_name)[0]

        # Сохранение результата в формате PNG
        output_path = os.path.join(output_folder, f'{file_name_without_ext}_output.png')
        with open(output_path, 'wb') as f:
            f.write(img)