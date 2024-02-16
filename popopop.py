class ComplexNumber:

    def init(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, another):
        return ComplexNumber(self.x + another.x, self.y + another.y)

    def sub(self):
        return f'{self.re}' + (f' + {self.im}i' if self.im >= 0 else f' - {self.im}')

    def mul(self):
        return f'{self.re}' + (f' + {self.im}i' if self.im >= 0 else f' - {self.im}')

    def div(self):
        return f'{self.re}' + (f' + {self.im}i' if self.im >= 0 else f' - {self.im}')