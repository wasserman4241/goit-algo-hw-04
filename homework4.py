def parse_input(user_input: str) -> tuple[str, list[str]]:
    
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Додає новий контакт у словник contacts. Очікує, що args містить ім'я та номер телефону.
    """
    if len(args) < 2:
        return "Error: Please provide both name and phone number."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Оновлює номер телефону існуючого контакту. Очікує, що args містить ім'я та новий номер телефону.
    """
    if len(args) < 2:
        return "Error: Please provide both name and phone number."
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Показує номер телефону для заданого контакту. Очікує, що args містить ім'я контакту.
    """
    if len(args) < 1:
        return "Error: Please provide a contact name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(contacts: dict[str, str]) -> str:
    """
    Функція для відображення всіх контактів у словнику contacts. Повертає рядок з усіма контактами.
    """
    if not contacts:
        return "No contacts stored yet."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)

        if not command:
            continue

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
