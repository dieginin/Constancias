class Cliente:
    def __init__(
        self, uid: int, nombre: str, estado: str, municipio: str, localidad: str
    ):
        self.uid = uid
        self.nombre = nombre
        self.estado = estado
        self.municipio = municipio
        self.localidad = localidad

    def __str__(self) -> str:
        return f"{self.nombre}"

    def __repr__(self) -> str:
        return f"({self.uid}) {self.nombre}"
