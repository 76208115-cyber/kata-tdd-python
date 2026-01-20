def test_conjunto_unElemento_retornaValor(self):
    conjunto = Conjunto([5])
    self.assertEqual(5, conjunto.promedio())
