from address_book import AddressBook
from record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me the command and arguments."
        except KeyError:
            return "This contact does not exist."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

def parse_input(user_input: str):
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
# def add_contact(args, contacts: dict):
#     """Add a new contact."""
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
# def change_contact(args, contacts: dict):
#     """Change an existing contact's phone number."""
#     name, phone = args
#     existing_phone = contacts.get(name)
#     if not existing_phone:
#         return f"Contact with name {name} does not exist."
#     contacts[name] = phone
#     return "Contact updated."
def change_contact(args, book: AddressBook):
    """Change an existing contact's phone number."""
    name, old_phone, new_phone = args

    if len(args) != 3:
        raise ValueError('To change contact specify: <name>, <old_phone>, <new_phone>')

    existing_contact = book.find(name)
    if not existing_contact:
        return f"Contact with name {name} does not exist."
    
    try:
        existing_contact.edit_phone(old_phone, new_phone)
        return f"Old phone {old_phone} was replaced by new phone {new_phone} for contact {name}."
    except Exception as e:
        return f"Error while changing phone: {e}"



@input_error
# def show_phone(args, contacts: dict):
#     """Show a contact's phone number."""
#     [name] = args
#     existing_phone = contacts.get(name)
#     if not existing_phone:
#         return f"Contact with name {name} does not exist."
#     return existing_phone
def show_phone(args, book: AddressBook):
    """Show a contact's phone number."""
    name, *_ = args

    if not name:
        raise ValueError('Please enter contact name')
    
    contact = book.find(name)

    if not contact:
        return f"Contact with name {name} does not exist."

    """ return f"Phone number for contact {name}: {contact.phones[0].value}" """
    return f"Phone number for contact {name}: {contact.phone}"


@input_error
# def show_all(contacts: dict):
#     """Show all contacts."""
#     if not contacts:
#         return "There are no contacts in the list."
#     result = [f"{name}: {phone}" for name, phone in contacts.items()]
#     return "\n".join(result)
def show_all(book: AddressBook):
    """Show all contacts."""
    if not book.data.keys():
        return "There are no contacts in the list."
    result = []

    for contact in book.data.values():
        result.append(f"{contact}")

    return "\n".join(result)

def main():
    print("Welcome to the assistant bot!")
    print("Type 'hello' to start or 'exit' to quit.")
    book = AddressBook()

    while True:
        user_input = input("Enter command: ").strip()
        if not user_input:
            continue  

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print("Enter the argument for the command (name and phone):")
            user_input = input("Enter command: ").strip()
            command, *args = parse_input(user_input)
            print(add_contact(args,  book))
        elif command == 'change':
            print("Enter the argument for the command (name and phone):")
            user_input = input("Enter command: ").strip()
            command, *args = parse_input(user_input)
            print(change_contact(args,  book))
        elif command == 'phone':
            print("Enter the argument for the command (name):")
            user_input = input("Enter command: ").strip()
            command, *args = parse_input(user_input)
            print(show_phone(args,  book))
        elif command == 'all':
            print(show_all( book))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()