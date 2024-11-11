import re
from abc import ABC, abstractmethod

# Clase Documento: Representa cada documento con atributos como id, contenido, fecha, autor, etc.
class Documento:
    def __init__(self, doc_id, contenido, fecha, autor):
        self.doc_id = doc_id
        self.contenido = contenido
        self.fecha = fecha
        self.autor = autor

# Clase IndiceInvertido: Estructura que asocia cada término con una lista de documentos en los que aparece.
class IndiceInvertido:
    def __init__(self, estrategia_indexacion, estrategia_busqueda):
        self.indice = {}
        self.estrategia_indexacion = estrategia_indexacion 
        self.estrategia_busqueda = estrategia_busqueda

    def agregar_documento(self, documento):     
        self.estrategia.indexar_documento(documento, self)

    # Función para agregar un término y el documento en el que aparece
    def agregar_termino(self, termino, documento):
        # Verificamos si el término ya existe, si no, inicializamos la lista
        # Esto es necesario al usar el diccionario común, hay librerías que permiten saltarnos este paso
        if termino not in self.indice:
            self.indice[termino] = []
        self.indice[termino].append(documento)

    # Mostrar el índice invertidoz
    def mostrar_indice(self):
        for termino, documentos in self.indice.items():
            print(f"Termino: {termino} - Documentos: {[doc.doc_id for doc in documentos]}")

    def buscar(self, termino): 
        return self.estrategia_busqueda.buscar(termino, self)

# Función para normalizar texto: convertir a minúsculas y eliminar signos de puntuación
def normalizar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar signos de puntuación utilizando una expresión regular
    #\w elimina caracteres tipo [a-zA-Z0-9_]
    #\s elimina espacios en blanco, (saltos de pagina, tabulaciones,etc)
    # Así esta especificado en la librería regex
    # |_  use esto para eliminar el guión bajo
    # La verdad es que falta agregar caracteres especiales como el arroba , etc, con estos bastan por el momento
    texto = re.sub(r'[^\w\s]|_', '', texto)
    return texto

# Función para tokenizar el texto usando expresiones regulares
def tokenizar(texto):
    # Utilizar re para dividir el texto en palabras (tokens), considerando solo letras y números
    return re.findall(r'\b\w+\b', texto)

# Función de indexación
def indexar_documento(documento, indice_invertido):
    # Normalizar el contenido del documento
    contenido_normalizado = normalizar_texto(documento.contenido)
    # Tokenizar el contenido
    palabras = tokenizar(contenido_normalizado)

    # Agregar los términos al índice invertido
    for palabra in palabras:
        indice_invertido.agregar_termino(palabra, documento)

class EstrategiaIndexacion(ABC):
    @abstractmethod
    def indexar_documento(self, documento, indice_invertido):
        pass

class EstrategiaIndexacionBasica(EstrategiaIndexacion):
    def indexar_documento(self, documento, indice_invertido):
        contenido_normalizado = normalizar_texto(documento.contenido)
        palabras = tokenizar(contenido_normalizado)
        for palabra in palabras:
            indice_invertido.agregar_termino(palabra, documento)

class EstrategiaBusqueda(ABC):
    @abstractmethod
    def buscar(self, termino, indice_invertido):
        pass

class EstrategiaBusquedaBasica(EstrategiaBusqueda):
    def buscar(self, termino, indice_invertido):
        termino_normalizado = normalizar_texto(termino)
        return indice_invertido.indice.get(termino_normalizado, [])


# Ejemplo de uso
if __name__ == "__main__":
    # Crear documentos
    # clase Documento y Atributos: (doc_id , contenido , fecha ,autor ) 
    doc1 = Documento(1, "El profesor ´´ ´me califico bajo en el parcial ---", "2024-11-11", "Brian")
    doc2 = Documento(2, "El profesor de___Desarrollo de Software se llama César Lara", "2024-11-11", "Cesar")
    doc3 = Documento(3, "Tower Defense es el proyecto de Desarrollo de Software", "2024-11-11", "Breimer")

    # Crear las estrategias (Estrategia Indexación, Estrategia busqueda)
    estrategia_indexacion = EstrategiaIndexacionBasica() 
    estrategia_busqueda = EstrategiaBusquedaBasica()    

    # Crear el índice invertido
    #indice_invertido = IndiceInvertido()

    # Crear el índice invertido con las estrategias 
    indice_invertido = IndiceInvertido(estrategia_indexacion,estrategia_busqueda)

    # Indexar los documentos
    indexar_documento(doc1, indice_invertido)
    indexar_documento(doc2, indice_invertido)
    indexar_documento(doc3, indice_invertido)

    # Mostrar el índice invertido
    indice_invertido.mostrar_indice()

    # Buscar un término (3 ejemplos)
    resultado1 = indice_invertido.buscar("profesor") 
    resultado2 = indice_invertido.buscar("calificacion") 
    resultado3 = indice_invertido.buscar("califico") 
    print(f"Resultados de la búsqueda para 'profesor': {[doc.doc_id for doc in resultado1]}")
    print(f"Resultados de la búsqueda para 'calificación': {[doc.doc_id for doc in resultado2]}")
    print(f"Resultados de la búsqueda para 'califico': {[doc.doc_id for doc in resultado3]}")