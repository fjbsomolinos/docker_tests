# -*- coding: utf-8 -*-
import unittest
from datetime import datetime
import sys, os
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path

from Hitos.Hitos import Hitos

class TestHitos(unittest.TestCase):

    def setUp(self):
        self.hitos = Hitos()

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.hitos, Hitos, "Objeto creado correctamente")

    def test_should_have_hitos_stored_correctly( self):
        self.assertIsInstance( self.hitos.todos_hitos(), dict, "El objeto hitos contiene un diccionario")
        self.assertEqual(self.hitos.cuantos(), 4, "El número de hitos es incorrecto")

    def test_should_return_hitos_correctly_and_raise_error(self):
        self.assertEqual( self.hitos.uno(1)["fecha"],  "15/09/2018" )
        with self.assertRaises(IndexError):
            zape = self.hitos.uno(-1)

        with self.assertRaises(IndexError):
            zipi = self.hitos.uno(99)
    def test_fecha_hito_posterior(self):
        tam_lista_hitos=len(self.hitos.hitos['hitos'])
        for i in range(1,tam_lista_hitos):
            fecha_hito_anterior = datetime.strptime(str(self.hitos.uno(i-1)["fecha"]), "%d/%m/%Y")
            fecha_hito=datetime.strptime(str(self.hitos.uno(i)["fecha"]), "%d/%m/%Y")
            self.assertLess(fecha_hito_anterior, fecha_hito, "Los hitos no estan ordenados")

    def test_incluye_hito_correctamente(self):
        tam_lista_hitos=len(self.hitos.hitos['hitos'])
        with self.assertRaises(TypeError):
            self.hitos.nuevo( 1, 2, 3 )
        with self.assertRaises(TypeError):
            self.hitos.nuevo( "Prueba", 2, 3 )
        with self.assertRaises(ValueError):
            self.hitos.nuevo( "Prueba", "Prueba", "Noesfecha" )
        self.hitos.nuevo( "0.Repositorio", "Prueba", "10/11/1912" )
        with self.assertRaises(ValueError):
            self.hitos.nuevo( "0.Repositorio", "Prueba", "10/11/1912" )

        filename = "2.CI"
        self.hitos.nuevo( filename, "Integración Continua", "10/11/2017" )
        self.assertLess( tam_lista_hitos, len(self.hitos.hitos['hitos']), "Uno añadido" )
        nuevo_hito = self.hitos.uno( self.hitos.cuantos()-1)
        print( nuevo_hito )
        self.assertEqual( nuevo_hito['file'], filename, "Título correcto")
            
if __name__ == '__main__':
    unittest.main()
