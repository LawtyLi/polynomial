class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add or Sub):
            if isinstance(self.p2, Add or Sub):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add or Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add or Sub):
            if isinstance(self.p2, Add or Sub):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add or Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)


poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)

# (X + 1) * (3 - X)
print(Mul(Add(X(), Int(1)), Sub(Int(3), X())))

# (X / (1 + 2)) * 3
print(Mul(Div(X(), Add(Int(1), Int(2))), Int(3)))

# 4 / (X + 2)
print(Div(Int(4), Add(X(), Int(2))))

# (X + 2) / (X - 1)
print(Div(Add(X(), Int(2)), Sub(X(), Int(1))))
