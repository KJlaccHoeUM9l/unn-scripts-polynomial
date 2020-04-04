import unittest

from pure_python.polynomial import Polynomial, delete_first_zeros


class UnitTests(unittest.TestCase):
    def test_can_init_with_list(self):
        coefficients = [1, 2, 4]
        p = Polynomial(coefficients)
        self.assertEqual(coefficients, p.coeffs)

    def test_can_init_with_tuple(self):
        coefficients = (1, 2, 4)
        p = Polynomial(coefficients)
        self.assertEqual([*coefficients], p.coeffs)

    def test_can_init_with_other_polynomial(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial(p1)
        self.assertEqual(p1, p2)

    def test_polynomial_is_copied_at_creation(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial(p1)
        p2.coeffs[0] = 100
        self.assertNotEqual(p1, p2)

    def test_can_add_polynomial(self):
        p1 = Polynomial([2, 2, 4])
        p2 = Polynomial([-1, -2, -4])
        self.assertEqual((p1 + p2).coeffs, [1, 0, 0])

    def test_can_add_polynomial_different_size(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial([-1, -2, -4, 5])
        self.assertEqual((p1 + p2).coeffs, [-1, -1, -2, 9])

    def test_can_add_number_left(self):
        p1 = Polynomial([1, 2, 4])
        number = -1
        self.assertEqual((p1 + number).coeffs, [1, 2, 3])

    def test_can_add_number_right(self):
        p1 = Polynomial([1, 2, 4])
        number = -1
        self.assertEqual((number + p1).coeffs, [1, 2, 3])

    def test_can_lower_degree_by_add(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial([-1, 2, 4])
        self.assertEqual(p1 + p2, Polynomial([4, 8]))

    def test_can_add_number_to_zero_polynomial_right(self):
        p1 = Polynomial([])
        number = -1
        self.assertEqual((number + p1).coeffs, [-1])

    def test_can_inverse_coefficients(self):
        p1 = Polynomial([1, 2, 4])
        p2 = -p1
        self.assertEqual(p2.coeffs, [-1, -2, -4])

    def test_can_sub_polynomial(self):
        p1 = Polynomial([2, 2, 4])
        p2 = Polynomial([1, 2, 4])
        self.assertEqual((p1 - p2).coeffs, [1, 0, 0])

    def test_can_sub_polynomial_different_size(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial([1, 2, 4, 5])
        self.assertEqual((p1 - p2).coeffs, [-1, -1, -2, -1])

    def test_can_sub_number_left(self):
        p1 = Polynomial([1, 2, 4])
        number = 1
        self.assertEqual((p1 - number).coeffs, [1, 2, 3])

    def test_can_sub_number_right(self):
        p1 = Polynomial([1, 2, 4])
        number = 1
        self.assertEqual((number - p1).coeffs, [-1, -2, -3])

    def test_can_lower_degree_by_sub(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial([1, 2, 4])
        self.assertEqual(p1 - p2, Polynomial([]))

    def test_can_mul_number_left(self):
        p1 = Polynomial([1, 2, 4])
        number = -1
        self.assertEqual((p1 * number).coeffs, [-1, -2, -4])

    def test_can_mul_number_right(self):
        p1 = Polynomial([1, 2, 4])
        number = -1
        self.assertEqual((number * p1).coeffs, [-1, -2, -4])

    def test_can_kill_polynomial_by_number_mul(self):
        p1 = Polynomial([1, 2, 4])
        number = 0
        self.assertEqual((number * p1).coeffs, [0])

    def test_can_mul_zero_polynomial_by_number(self):
        p1 = Polynomial([])
        number = 10
        self.assertEqual((number * p1).coeffs, [0])

    def test_can_mul_polynomials(self):
        p1 = Polynomial([3, 0, 0])
        p2 = Polynomial([4, -5, 7])
        self.assertEqual(p1 * p2, Polynomial([12, -15, 21, 0, 0]))

    def test_str_one(self):
        self.assertEqual('x^2 + 2x + 4', str(Polynomial([1, 2, 4])))

    def test_str_two(self):
        self.assertEqual('-x^3 - 2x - 4', str(Polynomial([-1, 0, -2, -4])))

    def test_str_three(self):
        self.assertEqual('-x^3 - 2x', str(Polynomial([-1, 0, -2, 0])))

    def test_str_four(self):
        self.assertEqual('-1', str(Polynomial([-1])))

    def test_str_five(self):
        self.assertEqual('0', str(Polynomial([])))

    def test_repr(self):
        self.assertEqual('Polynomial([1, 2, -4])', repr(Polynomial([1, 2, -4])))

    def test_can_modify_coefficients(self):
        p1 = Polynomial([2, 2, 4])
        p1.coeffs[0] -= 1
        p1.coeffs[-1] -= 1
        self.assertEqual(p1, Polynomial([1, 2, 3]))

    def test_can_compare_with_identity_polynomial(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial([1, 2, 4])
        self.assertEqual(p1 == p2, True)

    def test_can_compare_with_different_polynomial(self):
        p1 = Polynomial([1, 2, 4])
        p2 = Polynomial([1, 2, 4, 0])
        self.assertEqual(p1 == p2, False)

    def test_can_delete_zeros(self):
        self.assertEqual(delete_first_zeros([0, 0, 1, 2, 0, 3]), [1, 2, 0, 3])

    def test_can_kill_list(self):
        self.assertEqual(delete_first_zeros([0, 0, 0, 0]), [0])


if __name__ == '__main__':
    UnitTests.run()
