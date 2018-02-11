#!/usr/bin/env python
"""Usando pytest con unittest."""
import unittest
from test_multiplicar import multiplica_por_dos


class MultiplicarTest(unittest.TestCase):
    """Clase para testear la función Multiplicar."""

    @classmethod
    def setUpClass(cls):
        """Se ejecuta cuando empieza la clase (MultiplicarTest) de test."""

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta cuando termina la clase (MultiplicarTest) de test."""

    def setUp(self):
        """Se ejecuta antes de cada test."""

    def tearDown(self):
        """Se ejecuta despues de cada test."""

    def test_multiplica_por_dos(self):
        """Comprueba si la multiplicación por dos es correcta."""
        retultado_multiplica_5_por_dos = multiplica_por_dos(5)
        retultado_multiplica_10_por_dos = multiplica_por_dos(10)
        retultado_multiplica_2_por_dos = multiplica_por_dos(2)
        retultado_multiplica_50_por_dos = multiplica_por_dos(50)

        self.assertEqual(
            retultado_multiplica_5_por_dos,
            10,
            msg="Debería salir 10",
        )
        self.assertEqual(
            retultado_multiplica_10_por_dos,
            20,
            msg="Debería salir 20",
        )
        self.assertEqual(
            retultado_multiplica_2_por_dos,
            4,
            msg="Debería salir 4",
        )
        self.assertEqual(
            retultado_multiplica_50_por_dos,
            100,
            msg="Debería salir 50",
        )
        self.assertNotEqual(
            retultado_multiplica_50_por_dos,
            200,
            msg="No debería salir 200",
        )


def setUpModule():
    """Se ejecuta antes de testear todas las clases del módulo."""


def tearDownModule():
    """Se ejecuta despues de testear todas las clases del módulo."""


if __name__ == '__main__':
    # Ejecutamos todas las clases de tests que encuentre en el módulo
    unittest.main()
