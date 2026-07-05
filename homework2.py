import os

def get_cats_info(path: str) -> list[dict[str, str]]:
    
    if not os.path.exists(path):
        print(f"Error: The file '{path}' does not exist.")
        return []

    cats_info = []

    try:
        # Безпечне читання файлу за допомогою context manager та встановлення кодування
        with open(path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                # Розділяємо дані за допомогою split(',')
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Warning: Corrupted data on line {line_num}: '{line}'. Expected 'id,name,age'.")
                    return []  # Повертаємо порожній список, якщо файл пошкоджений

                cat_id, name, age = parts
                cats_info.append({
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                })
        
        return cats_info

    except OSError as e:
        print(f"Error: An OS error occurred while reading the file '{path}': {e}")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return []
    
cats_info = get_cats_info("C:/Users/g8902/Desktop/piton/Python Core/Модуль 4/cats.txt")
print(cats_info)  # Приклад використання функції