from typing import Tuple, List

def total_salary(path: str) -> Tuple[float, float]:
    """
    Analyzes a text file containing developer salaries and returns
    the total and average salary, both rounded to two decimal places.

    :param path: Path to the text file with data.
    :return: A tuple (total_salary_sum, average_salary) or (0.0, 0.0) in case of an error.
    """
    total_sum: float = 0.0
    average_salary: float = 0.0
    developer_count: int = 0
    salaries: List[float] = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line: str = line.strip()
                if not cleaned_line:
                    continue

                try:
                    name: str
                    salary_str: str
                    name, salary_str = cleaned_line.split(',')

                    salary: float = float(salary_str)

                    salaries.append(salary)
                    developer_count += 1

                except ValueError:
                    print(f"Warning: Line '{cleaned_line}' contains an invalid salary format (expected a number).")
                    continue
                except IndexError:
                    print(f"Warning: Line '{cleaned_line}' has an invalid format (no comma separator).")
                    continue

    except FileNotFoundError:
        print(f"Error: File at path '{path}' not found.")
        return (total_sum, average_salary)
    except Exception as e:
        print(f"An unexpected error occurred while processing the file: {e}")
        return (total_sum, average_salary)

    total_sum = sum(salaries)

    if developer_count > 0:
        average_salary = total_sum / developer_count

    return (round(total_sum, 2), round(average_salary, 2))

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
