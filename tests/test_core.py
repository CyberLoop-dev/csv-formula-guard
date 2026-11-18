import unittest
from main import is_formula_like, scan_rows

class FormulaGuardTests(unittest.TestCase):
    def test_detects_formula_prefixes(self):
        self.assertTrue(is_formula_like("  =SUM(A1:A2)"))
        self.assertTrue(is_formula_like("@cmd"))
    def test_ignores_plain_text(self):
        self.assertFalse(is_formula_like("hello"))
        self.assertFalse(is_formula_like(""))
    def test_reports_cell_coordinates(self):
        result=scan_rows([["name","value"],["x","=1+1"]])
        self.assertEqual((result[0]["row"],result[0]["column"]),(2,2))

if __name__=="__main__": unittest.main()
