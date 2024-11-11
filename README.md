PC3 Desarrollo de Software
Tema: 4
Implementaciones: DevContainer   OK


Parte 1
Item 1
```java
import re

# Clase Documento: Representa cada documento con atributos como id, contenido, fecha, autor, etc.
class Documento:
    def __init__(self, doc_id, contenido, fecha, autor):
        self.doc_id = doc_id
        self.contenido = contenido
        self.fecha = fecha
        self.autor = autor

# Clase IndiceInvertido: Estructura que asocia cada término con una lista de documentos en los que aparece.
class IndiceInvertido:
    def __init__(self):
        self.indice = {}

    # Función para agregar un término y el documento en el que aparece
    def agregar_termino(self, termino, documento):
        # Verificamos si el término ya existe, si no, inicializamos la lista
        # Esto es necesario al usar el diccionario común, hay librerías que permiten saltarnos este paso
        if termino not in self.indice:
            self.indice[termino] = []
        self.indice[termino].append(documento)

    # Mostrar el índice invertido
    def mostrar_indice(self):
        for termino, documentos in self.indice.items():
            print(f"Termino: {termino} - Documentos: {[doc.doc_id for doc in documentos]}")

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

# Ejemplo de uso
if __name__ == "__main__":
    # Crear documentos
    # clase Documento y Atributos: (doc_id , contenido , fecha ,autor ) 
    doc1 = Documento(1, "El profesor ´´ ´me califico bajo en el parcial ---", "2024-11-11", "Brian")
    doc2 = Documento(2, "El profesor de___Desarrollo de Software se llama César Lara", "2024-11-11", "Cesar")
    doc3 = Documento(3, "Tower Defense es el proyecto de Desarrollo de Software", "2024-11-11", "Breimer")

    # Crear el índice invertido
    indice_invertido = IndiceInvertido()

    # Indexar los documentos
    indexar_documento(doc1, indice_invertido)
    indexar_documento(doc2, indice_invertido)
    indexar_documento(doc3, indice_invertido)

    # Mostrar el índice invertido
    indice_invertido.mostrar_indice()
```
Salida:
```plaintext
root@39196564846c:/workspace# python indice.py
Termino: el - Documentos: [1, 1, 2, 3]
Termino: profesor - Documentos: [1, 2]
Termino: me - Documentos: [1]
Termino: califico - Documentos: [1]
Termino: bajo - Documentos: [1]
Termino: en - Documentos: [1]
Termino: parcial - Documentos: [1]
Termino: dedesarrollo - Documentos: [2]
Termino: de - Documentos: [2, 3, 3]
Termino: software - Documentos: [2, 3]
Termino: se - Documentos: [2]
Termino: llama - Documentos: [2]
Termino: césar - Documentos: [2]
Termino: lara - Documentos: [2]
Termino: tower - Documentos: [3]
Termino: defense - Documentos: [3]
Termino: es - Documentos: [3]
Termino: proyecto - Documentos: [3]
Termino: desarrollo - Documentos: [3]
```
