import unittest
from unittest.mock import MagicMock
from indice import Documento, IndiceInvertido, EstrategiaIndexacionBasica, EstrategiaBusquedaBasica, indexar_documento

class TestIndiceInvertido(unittest.TestCase):

    # Prueba para verificar la indexación de documentos
    def test_indexar_documento(self):
        # Crear documentos de prueba
        doc1 = Documento(1, "El profesor me calificó bajo en el parcial", "2024-11-11", "Brian")
        doc2 = Documento(2, "El profesor de Desarrollo de Software se llama César Lara", "2024-11-11", "Cesar")

        # Crear las estrategias de indexación y búsqueda
        estrategia_indexacion = EstrategiaIndexacionBasica()
        estrategia_busqueda = EstrategiaBusquedaBasica()

        # Crear el índice invertido
        indice_invertido = IndiceInvertido(estrategia_indexacion, estrategia_busqueda)

        # Mock de agregar_termino
        indice_invertido.agregar_termino = MagicMock()

        # Indexar los documentos
        indexar_documento(doc1, indice_invertido)
        indexar_documento(doc2, indice_invertido)

        # Verificar los términos tokenizados
        print(f"Términos indexados: {indice_invertido.indice}")

        # Verificar que se ha llamado a agregar_termino correctamente
        indice_invertido.agregar_termino.assert_called()

        # Imprimir el número de llamadas realizadas para cada término
        print(f"Cantidad de llamadas a agregar_termino: {indice_invertido.agregar_termino.call_count}")

        # Verificar el número de llamadas (ajustar según el número correcto de términos)
        self.assertEqual(indice_invertido.agregar_termino.call_count, 18)  # Ajusta este número según lo que veas en el print


    # Prueba para verificar la búsqueda en el índice invertido
    def test_buscar_termino(self):
        # Crear documentos de prueba
        doc1 = Documento(1, "El profesor me calificó bajo en el parcial", "2024-11-11", "Brian")
        doc2 = Documento(2, "El profesor de Desarrollo de Software se llama César Lara", "2024-11-11", "Cesar")
        
        # Crear las estrategias de indexación y búsqueda
        estrategia_indexacion = EstrategiaIndexacionBasica()
        estrategia_busqueda = EstrategiaBusquedaBasica()
        
        # Crear el índice invertido
        indice_invertido = IndiceInvertido(estrategia_indexacion, estrategia_busqueda)
        
        # Indexar los documentos
        indexar_documento(doc1, indice_invertido)
        indexar_documento(doc2, indice_invertido)
        
        # Elegimos el término profesor para simular la búsqueda
        resultado = indice_invertido.buscar("profesor")
        
        # Verificar que el resultado contenga los documentos correctos
        self.assertEqual(len(resultado), 2)  # El término "profesor" debe aparecer en ambos documentos
        self.assertEqual([doc.doc_id for doc in resultado], [1, 2])

    # Prueba con fake para simular la indexación sin un archivo real
    def test_fake_documento(self):
        # Creamos una clase fake para simular documentos sin necesidad de un archivo real
        class FakeDocumento:
            def __init__(self, doc_id, contenido, fecha, autor):
                self.doc_id = doc_id
                self.contenido = contenido
                self.fecha = fecha
                self.autor = autor
        
        # Crear documentos fake
        fake_doc1 = FakeDocumento(1, "Crearemos un documento con fake para hacer el item 3", "2024-11-11", "El faker Author")
        fake_doc2 = FakeDocumento(2, "Otro documento con fake para corroborar", "2024-11-11", "El faker Author")
        
        # Crear las estrategias de indexación y búsqueda
        estrategia_indexacion = EstrategiaIndexacionBasica()
        estrategia_busqueda = EstrategiaBusquedaBasica()
        
        # Crear el índice invertido
        indice_invertido = IndiceInvertido(estrategia_indexacion, estrategia_busqueda)
        
        # Indexar los documentos fake
        indexar_documento(fake_doc1, indice_invertido)
        indexar_documento(fake_doc2, indice_invertido)
        
        # Verificar que los documentos fake se han indexado correctamente
        resultado = indice_invertido.buscar("fake")  #Buscamos 
        self.assertEqual(len(resultado), 2)
        self.assertEqual([doc.doc_id for doc in resultado], [1, 2])

if __name__ == "__main__":
    unittest.main()
