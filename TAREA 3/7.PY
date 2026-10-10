class Documento:
    def __init__(self, titulo: str, autor: str, editorial: str, anio_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
    def __str__(self):
        return f"{self.titulo} ({self.anio_publicacion})"
    def clonar(self):
        pass
class Libro(Documento):
    def __init__(self, titulo: str, autor: str, editorial: str, anio_publicacion: int):
        super().__init__(titulo, autor, editorial, anio_publicacion)
    def clonar(self):
        return Libro(self.titulo, self.autor, self.editorial, self.anio_publicacion)
class Revista(Documento):
    def __init__(self, titulo: str, autor: str, editorial: str, anio_publicacion: int, volumen: int, numero: int, mes_salida: str):
        super().__init__(titulo, autor, editorial, anio_publicacion)
        self.volumen = volumen
        self.numero = numero
        self.mes_salida = mes_salida
    def clonar(self):
        return Revista(self.titulo, self.autor, self.editorial, self.anio_publicacion, self.volumen, self.numero, self.mes_salida)
class RevistaInvestigacion(Revista):
    def __init__(self, titulo: str, autor: str, editorial: str, anio_publicacion: int, volumen: int, numero: int, mes_salida: str, campo_investigacion: str):
        super().__init__(titulo, autor, editorial, anio_publicacion, volumen, numero, mes_salida)
        self.campo_investigacion = campo_investigacion
    def clonar(self):
        return RevistaInvestigacion(self.titulo, self.autor, self.editorial, self.anio_publicacion, self.volumen, self.numero, self.mes_salida, self.campo_investigacion)
class DocumentoCD(Documento):
    def __init__(self, titulo: str, autor: str, editorial: str, anio_publicacion: int, formato_cd: str, tipo_licencia: str):
        super().__init__(titulo, autor, editorial, anio_publicacion)
        self.formato_cd = formato_cd
        self.tipo_licencia = tipo_licencia
    def clonar(self):
        return DocumentoCD(self.titulo, self.autor, self.editorial, self.anio_publicacion, self.formato_cd, self.tipo_licencia)
class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.documentos = []
    def agregar_documento(self, doc: Documento):
        self.documentos.append(doc)
    def total_documentos(self) -> int:
        return len(self.documentos)
    def total_revistas(self) -> int:
        return sum(1 for doc in self.documentos if isinstance(doc, Revista))
    def total_libros(self) -> int:
        return sum(1 for doc in self.documentos if isinstance(doc, Libro))
    def comparar_con(self, otra_biblioteca):
        print(f"\n--- Comparación: {self.nombre} vs {otra_biblioteca.nombre} ---")
        if self.total_documentos() > otra_biblioteca.total_documentos():
            print(f"Mayor cantidad de documentos: {self.nombre} ({self.total_documentos()})")
        elif otra_biblioteca.total_documentos() > self.total_documentos():
            print(f"Mayor cantidad de documentos: {otra_biblioteca.nombre} ({otra_biblioteca.total_documentos()})")
        else:
            print("Ambas tienen la misma cantidad de documentos.")
        if self.total_revistas() > otra_biblioteca.total_revistas():
            print(f"Mayor cantidad de revistas: {self.nombre} ({self.total_revistas()})")
        elif otra_biblioteca.total_revistas() > self.total_revistas():
            print(f"Mayor cantidad de revistas: {otra_biblioteca.nombre} ({otra_biblioteca.total_revistas()})")
        else:
            print("Ambas tienen la misma cantidad de revistas.")
    def copia_de_seguridad(self):
        nueva_biblioteca = Biblioteca(self.nombre + " - Backup")
        for doc in self.documentos:
            nueva_biblioteca.agregar_documento(doc.clonar())
        return nueva_biblioteca
def reorganizar_bibliotecas(bib1: Biblioteca, bib2: Biblioteca):
    revistas_bib2 = [doc for doc in bib2.documentos if isinstance(doc, Revista)]
    bib2.documentos = [doc for doc in bib2.documentos if not isinstance(doc, Revista)]
    bib1.documentos.extend(revistas_bib2)
    libros_bib1 = [doc for doc in bib1.documentos if isinstance(doc, Libro)]
    bib1.documentos = [doc for doc in bib1.documentos if not isinstance(doc, Libro)]
    bib2.documentos.extend(libros_bib1)
biblio_central = Biblioteca("Biblioteca Central")
biblio_ingenieria = Biblioteca("Biblioteca Ingeniería")
biblio_central.agregar_documento(Libro("Don Quijote", "Cervantes", "Alfaguara", 1605))
biblio_central.agregar_documento(Libro("El Aleph", "Borges", "Losada", 1949))
biblio_central.agregar_documento(Revista("National Geographic", "Varios", "NatGeo", 2026, 150, 5, "Mayo"))
biblio_ingenieria.agregar_documento(DocumentoCD("Visual Studio", "Microsoft", "MS", 2022, "ISO", "Comercial"))
biblio_ingenieria.agregar_documento(RevistaInvestigacion("IEEE Transactions", "Varios", "IEEE", 2026, 50, 1, "Enero", "Inteligencia Artificial"))
biblio_ingenieria.agregar_documento(Revista("PC World", "Varios", "IDG", 2025, 200, 10, "Octubre"))
biblio_central.comparar_con(biblio_ingenieria)
reorganizar_bibliotecas(biblio_central, biblio_ingenieria)
print(f"\nTraslado completado. Revistas en Central: {biblio_central.total_revistas()}, Libros en Central: {biblio_central.total_libros()}")
print(f"Traslado completado. Revistas en Ingeniería: {biblio_ingenieria.total_revistas()}, Libros en Ingeniería: {biblio_ingenieria.total_libros()}")
backup_central = biblio_central.copia_de_seguridad()
backup_ingenieria = biblio_ingenieria.copia_de_seguridad()
print(f"\nCopias de seguridad creadas exitosamente:")
print(f"- {backup_central.nombre}: {backup_central.total_documentos()} documentos clonados.")
print(f"- {backup_ingenieria.nombre}: {backup_ingenieria.total_documentos()} documentos clonados.")