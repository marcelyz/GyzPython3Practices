class Fraction(object):
    def __init__(self, top, bottom):
        self.num = top   # numerator：分子
        self.den = bottom   # denominator：分母

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    @staticmethod
    def gcb(a, b):   # Greatest common divisor：最大公约数 [欧几里得算法求最大公约数]
        while a % b != 0:
            r = a % b
            a = b
            b = r
        return b

    def __add__(self, otherfraction):  # add：加
        new_num = self.num * otherfraction.den + self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        common = Fraction.gcb(new_num, new_den)
        return Fraction(new_num // common, new_den // common)  # /:浮点数除法；//:整数除法

    def __sub__(self, otherfraction):  # subtract：减
        new_num = self.num * otherfraction.den - self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        common = Fraction.gcb(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, otherfraction):  # multiply：乘
        new_num = self.num * otherfraction.num
        new_den = self.den * otherfraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, otherfraction):  # divide：除(/)
        new_num = self.num * otherfraction.den
        new_den = self.den * otherfraction.num
        return Fraction(new_num, new_den)

    def __eq__(self, otherfraction):  # 深相等：一种数值上相等，却并不一定是相同指向的相等方式   equal：等于
        first_num = self.num * otherfraction.den
        second_num = otherfraction.num * self.den
        return first_num == second_num

    def __lt__(self, otherfraction):  # less than：小于
        first_num = self.num * otherfraction.den
        second_num = otherfraction.num * self.den
        return first_num < second_num

    def __gt__(self, otherfraction):  # greater than：大于
        first_num = self.num * otherfraction.den
        second_num = otherfraction.num * self.den
        return first_num > second_num


if __name__ == "__main__":
    f1 = Fraction(1, 4)
    f2 = Fraction(1, 2)
    print(f1, f2)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 == f2)
    print(f1 > f2)
    print(f1 < f2)
