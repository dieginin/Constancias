from tinydb import Query, TinyDB

from models import Cliente


class Database:
    def __init__(self) -> None:
        db = TinyDB("database.json")
        self._clientes = db.table("clientes")

    @property
    def clientes(self) -> list[Cliente]:
        return [
            Cliente(c["uid"], c["nombre"], c["estado"], c["municipio"], c["localidad"])
            for c in self._clientes.all()
        ]

    def obtener_cliente(self, nombre: str) -> Cliente:
        cliente = self._clientes.get(Query().nombre == nombre)
        if cliente:
            return Cliente(
                cliente["uid"], cliente["nombre"], cliente["estado"], cliente["municipio"], cliente["localidad"]  # type: ignore
            )
        return Cliente(0, *4 * ["None"])

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

    def modificar_cliente(
        self,
        uid: int,
        nombre: str | None = None,
        estado: str | None = None,
        municipio: str | None = None,
        localidad: str | None = None,
    ) -> str:
        if self._clientes.contains(Query().nombre == nombre):
            return f"{nombre} ya existe"

        updates = {}
        if nombre:
            updates["nombre"] = nombre
        if estado:
            updates["estado"] = estado
        if municipio:
            updates["municipio"] = municipio
        if localidad:
            updates["localidad"] = localidad

        self._clientes.update(updates, doc_ids=[uid])
        cliente = self._clientes.get(doc_id=uid)
        return f"{cliente["nombre"]} actualizado"  # type: ignore

    def borrar_cliente(self, uid: int) -> str:
        cliente = self._clientes.get(doc_id=uid)
        self._clientes.remove(doc_ids=[uid])[0]
        return f"{cliente["nombre"]} eliminado"  # type: ignore
    
