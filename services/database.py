from typing import List

from tinydb import Query, TinyDB
from tinydb.table import Document


class Database:
    def __init__(self) -> None:
        db = TinyDB("database.json")
        self._clients = db.table("clients")

    @property
    def clients(self) -> List[Document]:
        return self._clients.all()

    def get_client(self) -> Document | List[Document] | None:
        return self._clients.get(Query().name == "name")

    def insert_client(self) -> int:
        return self._clients.insert({"name": "name"})

    def modify_client(self) -> int:
        return self._clients.update({"name": "name"}, doc_ids=[0])[0]

    def delete_client(self) -> int:
        return self._clients.remove(doc_ids=[0])[0]
