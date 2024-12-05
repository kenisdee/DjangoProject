from PIL import Image


def resize_image(image_path, max_size=400):
    """
    Уменьшает изображение пропорционально до размера с большей стороной max_size пикселей.

    Args:
        image_path (str): Путь к изображению.
        max_size (int): Максимальный размер большей стороны.
    """
    with Image.open(image_path) as img:
        # Определяем текущие размеры изображения
        width, height = img.size

        # Определяем коэффициент масштабирования
        if width > height:
            new_width = max_size
            new_height = int(height * (max_size / width))
        else:
            new_height = max_size
            new_width = int(width * (max_size / height))

        # Уменьшаем изображение
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Сохраняем уменьшенное изображение
        img.save(image_path)
