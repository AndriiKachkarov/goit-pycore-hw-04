from typing import Tuple, List, Dict, Optional, Literal

Contacts = Dict[str, str]

QuoteType = Literal["'", '"']


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parses the user input string into a command and its arguments using a
    state machine approach (cycle over the string).
    Supports multi-word arguments enclosed in double (") or single (') quotes.
    Nested quotes (e.g., 'text with "inner" quotes') are treated as literal text.
    The command is case-insensitive.
    """

    args: List[str] = []

    current_arg: str = ""
    in_quotes: Optional[Literal] = None

    # Pre-process the input by normalizing spaces and stripping leading/trailing whitespace
    user_input = ' '.join(user_input.split())

    if not user_input:
        return "", []

    parts = user_input.split(maxsplit=1)
    command = parts[0].strip().lower()

    if len(parts) == 1:
        return command, []

    args_string = parts[1]

    for char in args_string:
        if in_quotes is not None:
            if char == in_quotes:
                in_quotes = None
            else:
                current_arg += char
        else:
            if char in ('"', "'"):
                in_quotes = char
            elif char == ' ':
                if current_arg:
                    args.append(current_arg)
                current_arg = ""
            else:
                current_arg += char

    if current_arg or (current_arg == "" and in_quotes is None and args_string.endswith(('"', "'")) and not args):
        # Add the last collected argument, or handle case where input ends with an argument in quotes
        args.append(current_arg)

    # Check for unclosed quotes after processing
    if in_quotes is not None:
        # If quotes are unclosed, treat the whole remaining part as one argument
        # For this simple bot, we'll just return the arguments collected so far,
        # but in a real app, this would be an error.
        pass

    return command, args


def add_contact(args: List[str], contacts: Contacts) -> str:
    """
    Adds a new contact (name and phone) to the contacts dictionary.
    Expects exactly two arguments: [name, phone].
    """
    if len(args) != 2:
        return "Invalid number of arguments for 'add'. Use: add [name] [phone]"

    if args[0] in contacts:
        return "Error: Contact name already exists."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Contacts) -> str:
    """
    Changes the phone number for an existing contact.
    Expects exactly two arguments: [name, new_phone].
    """
    if len(args) != 2:
        return "Invalid number of arguments for 'change'. Use: change [name] [new_phone]"

    name, new_phone = args

    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact name not found."


def show_phone(args: List[str], contacts: Contacts) -> str:
    """
    Retrieves and displays the phone number for a given contact name.
    Expects exactly one argument: [name].
    """
    if len(args) != 1:
        return "Invalid number of arguments for 'phone'. Use: phone [name]"

    name = args[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact name not found."


def show_all(contacts: Contacts) -> str:
    """
    Displays all stored contacts and their phone numbers.
    """
    if not contacts:
        return "No contacts saved."

    all_contacts: List[str] = []
    for name, phone in contacts.items():
        all_contacts.append(f"{name}: {phone}")

    return "\n".join(all_contacts)


def main() -> None:
    """
    The main function that manages the command processing loop.
    """
    contacts: Contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input: str = input("Enter a command: ").strip()

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
