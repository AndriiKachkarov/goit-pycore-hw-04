from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Reads a text file with cat information and returns a list of dictionaries.
    Each dictionary contains the cat's id, name, and age.

    :param path: Path to the text file with data (e.g., 'id,name,age').
    :return: A list of dictionaries, where each dict is a cat's record,
             or an empty list if an error occurs.
    """
    cats_list: List[Dict[str, str]] = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line: str = line.strip()
                if not cleaned_line:
                    continue

                try:
                    parts: List[str] = cleaned_line.split(',')

                    if len(parts) != 3:
                        # TODO: think of a better way to handle this case (maybe it's possible to extract partial data)
                        print(f"Warning: Line '{cleaned_line}' has an invalid number of fields (expected 3). Skipping.")
                        continue

                    cat_id: str = parts[0]
                    cat_name: str = parts[1]
                    cat_age: str = parts[2]

                    cat_dict: Dict[str, str] = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": cat_age
                    }

                    cats_list.append(cat_dict)

                except Exception as e:
                    print(f"Warning: Failed to parse line '{cleaned_line}'. Error: {e}. Skipping.")
                    continue

    except FileNotFoundError:
        print(f"Error: File at path '{path}' not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return []

    return cats_list

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

