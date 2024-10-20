from typing import Callable


class HelperError(BaseException):
    """Base exception for helper errors."""


def input_error(func: Callable[..., str]) -> Callable[..., str]:
    """Decorator to handle errors in the input."""

    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except HelperError as e:
            return str(e)
        except (ValueError, KeyError):
            return "Error: Invalid input."

    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Parses user input and returns the command and arguments.

    param: user_input: The user input.
    return: The command in lowercase and list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Adds a contact to the contacts dictionary.

    param: args: List with 2 values: name and phone.
    param: contacts: Contacts dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        raise HelperError("Invalid command format. Use: add [name] [phone]")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Changes the phone number of a contact in the contacts dictionary.

    param: args: List with 2 values: name and new phone.
    param: contacts: Contacts dictionary to modify.
    return: str: Result message.
    """
    if len(args) != 2:
        raise HelperError("Invalid command format. Use: change [name] [new phone]")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Shows the phone number of a contact from the contacts dictionary.

    param: args: List with 1 value: name.
    param: contacts: Contacts dictionary to read from.
    return: str: Result message.
    """
    if len(args) != 1:
        raise HelperError("Invalid command format. Use: phone [name]")
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict[str, str]):
    """Shows all contacts from the contacts dictionary.

    param: contacts: Contacts dictionary to read from.
    return: str: Result message.
    """
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "No contacts found."


def main():
    """Main function to run the assistant bot."""

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
        command, args = parse_input(user_input)
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print(
                    "Invalid command. Please try again. \nAllowed commands: hello, add, change, phone, all, close, exit"
                )


if __name__ == "__main__":
    main()
