from fields import Name, Phone

class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        phone = phone.strip()
        if any(p.value == phone for p in self.phones):
            raise ValueError(f"Phone {phone} already exists in contacts")
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        phone = phone.strip()
        self.phones = list(filter(lambda p: p.value != phone, self.phones))
        print(f"Phone {phone} successfully removed")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        if not new_phone.isdigit() or len(new_phone) != 10:
            raise ValueError("New phone must be a number of length 10")
        if any(p.value == new_phone for p in self.phones):
            raise ValueError(f"Phone {new_phone} already exists in contacts")
        found_phone = self.find_phone(old_phone.strip())
        found_phone.value = new_phone
        print(f"New phone {new_phone} successfully replaced old phone {old_phone}")

    def find_phone(self, phone: str) -> Phone:
        phone = phone.strip()
        found_phone = next((p for p in self.phones if p.value == phone), None)
        if found_phone is None:
            raise Exception(f"Phone {phone} not found in contacts")
        return found_phone

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones) if self.phones else "No phones"
        return f"Contact name: {self.name.value}, phones: {phones}"
