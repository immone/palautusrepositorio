from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or

class Pino():

    def __init__(self):
        self._l = []
        self._s = None

    def add(self, i):
        self._l.append(i)

    def b(self):
        return And(self._l)

    def l(self):
        return self._l

    def set_l(self, l):
        self._l = l

class QueryBuilder:

    def __init__(self, stack = Pino()):
        self.stack_object = stack
        self._stack_l = []

    def oneOf(self, a,b):
        self._stack_l = [a,b]
        return self

    def build(self):
        if self._stack_l != []:
            temp = Or([self._stack_l[0],self._stack_l[1]] )
            self.stack_object = Pino()
            self._stack_l = []
            return temp
        else:
            temp = self.stack_object.b()
            self.stack_object = Pino()
            return temp

    def playsIn(self, team):
        self.stack_object.add(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self.stack_object.add(HasAtLeast(value, attr))
        return self

    def Not(self, m):
        self.stack_object.add(Not(m))
        return self

    def hasFewerThan(self, value, attr):
        self.stack_object.add(HasFewerThan(value, attr))
        return self

