import numpy as np
from functools import reduce


class Polynomial:
    def __init__(self, other):
        if isinstance(other, (list, tuple)):
            self.coefficients = np.array(other)
        elif isinstance(other, np.ndarray):
            self.coefficients = other
        elif isinstance(other, Polynomial):
            self.coefficients = other.coefficients
        else:
            raise TypeError('Incorrect argument type. Expected: list, tuple, numpy.ndarray')
        self.coefficients = delete_first_zeros(self.coefficients)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            max_len = max(len(self.coefficients), len(other.coefficients))
            return Polynomial(padding_by_zeros(self.coefficients, max_len) + padding_by_zeros(other.coefficients,
                                                                                              max_len))
        elif isinstance(other, int):
            p = Polynomial(self.coefficients)
            p.coefficients[-1] += other
            return p
        else:
            raise TypeError('Incorrect argument type. Expected: int, Polynomial')

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Polynomial((-1) * self)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return (-self).__radd__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Polynomial(self.coefficients * other)
        elif isinstance(other, Polynomial):
            self_len = len(self.coefficients)
            return reduce(lambda p1, p2: p1 + p2,
                          map(lambda i: Polynomial(np.concatenate(((other * int(self.coefficients[i])).coefficients,
                                                                   np.zeros(self_len - i - 1))
                                                                  )
                                                   ),
                              range(self_len)
                              )
                          )
        else:
            raise TypeError('Incorrect argument type. Expected: int, Polynomial, but got {}'.format(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if len(self.coefficients) != len(other.coefficients):
                return False
            else:
                return (self.coefficients == other.coefficients).all()
        else:
            raise TypeError('Incorrect argument type. Expected: Polynomial')

    def __str__(self):
        self_len = len(self.coefficients)
        if self_len == 1:
            return str(self.coefficients[0])
        else:
            def get_coefficient(coefficient):
                return str(abs(coefficient)) if coefficient != 1 else ''

            def get_degree(degree):
                return '^{}'.format(degree) if degree != 1 else ''

            def get_sign(index):
                return '+' if self.coefficients[index] > 0 else '-'

            result = '{}{}x{}'.format('-' if self.coefficients[0] < 0 else '',
                                      '' if abs(self.coefficients[0]) == 1 else str(abs(self.coefficients[0])),
                                      get_degree(self_len - 1))

            for i in np.arange(1, self_len - 1):
                current_coefficient = self.coefficients[i]
                current_degree = self_len - i - 1

                if current_coefficient != 0:
                    result += ' {} {}x{}'.format(get_sign(i),
                                                 get_coefficient(current_coefficient),
                                                 get_degree(current_degree))

            return result if self.coefficients[-1] == 0 \
                else result + ' {} {}'.format(get_sign(-1), abs(self.coefficients[-1]))

    def __repr__(self):
        return 'Polynomial({})'.format(repr(self.coefficients.tolist()))


def delete_first_zeros(list_):
    if len(list_) == 0:
        return np.array([0])
    else:
        first_number = 0
        while first_number < len(list_) and list_[first_number] == 0:
            first_number += 1
        return list_[first_number:] if first_number != len(list_) else np.array([0])


def padding_by_zeros(list_, len_):
    if len_ == 0:
        return np.array([0])
    elif len(list_) == len_:
        return list_
    else:
        result = np.zeros(len_, dtype=int)
        result[-len(list_):] = list_
        return result
