from typing import List

from tinydb import Query, TinyDB
from tinydb.table import Document


class Database:
    def __init__(self) -> None:
        db = TinyDB("database.json")
        self._clientes = db.table("clientes")

    @property
    def clientes(self) -> List[Document]:
        return self._clientes.all()

    def obtener_cliente(self) -> Document | List[Document] | None:
        return self._clientes.get(Query().name == "name")

    def insertar_cliente(
        self, nombre: str, estado: str, municipio: str, localidad: str
    ) -> str:
        if self._clientes.contains(Query().nombre == nombre):
            return f"{nombre} ya existe"

        data_cliente = {
            "uid": len(self._clientes) + 1,
            "nombre": nombre,
            "estado": estado,
            "municipio": municipio,
            "localidad": localidad,
        }
        self._clientes.insert(data_cliente)
        return f"{nombre} agregado exitosamente"

    def modificar_cliente(self) -> int:
        return self._clientes.update({"nombre": "nombre"}, doc_ids=[1])[0]

    def borrar_cliente(self) -> int:
        return self._clientes.remove(doc_ids=[1])[0]
