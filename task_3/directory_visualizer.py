import sys
from pathlib import Path
from typing import List
from colorama import init, Fore, Style

init(autoreset=True)

DIR_COLOR: str = Fore.BLUE
FILE_COLOR: str = Fore.GREEN

def visualize_directory_structure(path: Path, depth: int = 0) -> None:
    """
    Recursively prints the directory structure using only indentation for nesting.

    :param path: The current path (directory) to visualize.
    :param depth: The current level of indentation.
    """
    indent: str = "    " * depth

    try:
        contents: List[Path] = sorted(list(path.iterdir()))
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied: {path.name}{Style.RESET_ALL}")
        return
    except Exception as e:
        print(f"{indent}{Fore.RED}Error accessing directory {path.name}: {e}{Style.RESET_ALL}")
        return

    for item in contents:
        if item.is_dir():
            print(f"{indent}{DIR_COLOR}{item.name}/")
            visualize_directory_structure(item, depth + 1)
        else:
            print(f"{indent}{FILE_COLOR}{item.name}")

def main():
    """
    Main function to handle command-line arguments and start visualization.
    """
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {Path(sys.argv[0]).name} <path_to_directory>{Style.RESET_ALL}")
        sys.exit(1)

    target_path_str: str = sys.argv[1]
    target_path: Path = Path(target_path_str)

    if not target_path.exists():
        print(f"{Fore.RED}Error: Path '{target_path_str}' does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"{Fore.RED}Error: Path '{target_path_str}' is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Style.BRIGHT}Directory structure for: {target_path_str}{Style.RESET_ALL}")

    print(f"{DIR_COLOR}{target_path.name}/{Style.RESET_ALL}")

    visualize_directory_structure(target_path, 1)

if __name__ == "__main__":
    main()