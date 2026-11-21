import os
from clawdos import ClawDOS

def create_directory_and_copy_files(directory_name, files_to_copy):
    """
    Создает директорию и копирует указанные файлы в нее.
    Использует ИИ-агент ClawDOS для генерации кода.
    """
    # Инициализация агента ClawDOS
    agent = ClawDOS()

    # Генерация кода для создания директории
    create_dir_code = agent.generate_code(f"Создание директории {directory_name}")
    os.system(create_dir_code)

    # Генерация кода для копирования файлов
    for file in files_to_copy:
        copy_file_code = agent.generate_code(f"Копирование файла {file} в директорию {directory_name}")
        os.system(copy_file_code)

if __name__ == "__main__":
    directory_name = "test_dir"
    files_to_copy = ["file1.txt", "file2.txt"]
    
    create_directory_and_copy_files(directory_name, files_to_copy)