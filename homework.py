import os

def total_salary(path: str) -> tuple[float, float]:

    if not os.path.exists(path):
        print(f"Error: The file '{path}' does not exist.")
        return 0.0, 0.0

    total = 0.0
    count = 0

    try:
        # Використовуємо менеджер контексту with та вказуємо кодування utf-8
        with open(path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                # Розділяємо дані за допомогою split(',')
                parts = line.split(',')
                if len(parts) != 2:
                    print(f"Warning: Corrupted data format on line {line_num}: '{line}'. Expected 'Name,Salary'.")
                    return 0.0, 0.0  # Файл пошкоджений

                name, salary_str = parts
                try:
                    salary = float(salary_str)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Warning: Invalid salary value on line {line_num}: '{salary_str}'.")
                    return 0.0, 0.0  # Файл пошкоджений

        if count == 0:
            print("Warning: The file contains no valid salary data.")
            return 0.0, 0.0

        average = total / count
        return total, average

    except OSError as e:
        print(f"Error: An OS error occurred while reading the file '{path}': {e}")
        return 0.0, 0.0
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return 0.0, 0.0
total, average = total_salary(r"C:\Users\g8902\Desktop\piton\Python Core\Модуль 4\salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # Приклад використання функції
    