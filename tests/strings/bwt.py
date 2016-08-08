from strings.bwt import build_bwt_matrix, bwt, inverse_bwt

from unittest import TestCase


class BWTTestCase(TestCase):
    def test_simple_matrix(self):
        text = 'AB$'
        matrix = build_bwt_matrix(text)
        self.assertEqual(len(matrix), 3)
        self.assertEqual(matrix[0], '$AB')
        self.assertEqual(matrix[1], 'AB$')
        self.assertEqual(matrix[2], 'B$A')

    def test_simple_bwt(self):
        text = 'AB$'
        result = bwt(text)
        self.assertEqual('B$A', result)

    def test_simple_inverse_bwt(self):
        text = 'AB$'
        bwt_str = 'B$A'
        result = inverse_bwt(bwt_str)
        self.assertEqual(result, text)
