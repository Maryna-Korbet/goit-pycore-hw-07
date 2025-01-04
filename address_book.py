from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.last_id = 0

    def add_record(self, record: Record) -> None:
        self.last_id += 1
        self.data[self.last_id] = record

    def find(self, name: str) -> tuple[int, Record] | None:
        for key, record in self.data.items():
            if record.name.value == name:
                return key, record
        return None

    def delete(self, name: str):
        key = next((key for key in self.data.keys() if self.data[key].name.value == name), None)
        if key is None:
            print(f"Record with name {name} not found in contacts")
            return
        del self.data[key]
        print(f"Record {name} successfully deleted")