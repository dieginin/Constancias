from tinydb import Query, TinyDB

from models import Cliente


class Database:
    def __init__(self) -> None:
        db = TinyDB("database.json")
        self._clientes = db.table("clientes")
        self._constancias = db.table("constancias")

    @property
    def clientes(self) -> list[Cliente]:
        return [
            Cliente(c["uid"], c["nombre"], c["estado"], c["municipio"], c["localidad"])
            for c in self._clientes.all()
        ]

    def obtener_cliente(self, uid: int) -> Cliente:
        cliente = self._clientes.get(doc_id=uid)
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
            "uid": 0,
            "nombre": nombre,
            "estado": estado,
            "municipio": municipio,
            "localidad": localidad,
        }
        uid = self._clientes.insert(data_cliente)
        self._clientes.update({"uid": uid}, doc_ids=[uid])
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
        return f"{self.obtener_cliente(uid).nombre} actualizado"

    def borrar_cliente(self, uid: int) -> str:
        cliente = self.obtener_cliente(uid)
        self._clientes.remove(doc_ids=[uid])
        return f"{cliente.nombre} eliminado"

    def insertar_constancia(
        self, uid: int, no_organismos: int, costo_unitario: float
    ) -> str:
        data_constancia = {
            "folio": 0,
            "uid": uid,
            "no_organismos": no_organismos,
            "costo_unitario": costo_unitario,
        }
        folio = self._constancias.insert(data_constancia)
        self._constancias.update({"folio": folio}, doc_ids=[folio])
        return f"Constancia {folio} agregada exitosamente"
