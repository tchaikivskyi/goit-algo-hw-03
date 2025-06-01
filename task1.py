import os
import shutil

EXCLUDED_DIRS = {"dist", ".git", "__pycache__", ".vscode"}

def is_hidden(path):
    return any(part.startswith('.') for part in path.split(os.sep))

def copy_files_recursively(source_folder, destination_folder):
    for item in os.listdir(source_folder):
        path = os.path.join(source_folder, item)

        if item in EXCLUDED_DIRS or is_hidden(path):
            continue

        if os.path.isdir(path):
            copy_files_recursively(path, destination_folder)
        elif os.path.isfile(path):
            extension = os.path.splitext(item)[1][1:] or "no_extension"
            ext_folder = os.path.join(destination_folder, extension)
            os.makedirs(ext_folder, exist_ok=True)

            dest_path = os.path.join(ext_folder, item)

            if os.path.abspath(path) != os.path.abspath(dest_path):
                shutil.copy2(path, dest_path)
                print(f"Скопійовано: {item} -> {ext_folder}")

source = input("Введіть шлях до вихідної папки: ").strip()
destination = input("Введіть шлях до папки призначення (або Enter для 'dist'): ").strip()

if not os.path.exists(source):
    print("Папку не знайдено, буде використано поточну директорію.")
    source = os.getcwd()

if destination == "":
    destination = "dist"

os.makedirs(destination, exist_ok=True)

copy_files_recursively(source, destination)
print("Копіювання завершено.")
