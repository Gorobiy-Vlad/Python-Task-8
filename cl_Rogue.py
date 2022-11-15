from cl_Unit import Unit
import random as rand


class Rouge(Unit):

    _Health_Rouge = 1

    @property
    def Health_Rouge(self):
        return self._Health_Rouge

    Health_Rouge = Unit.Health

    @Unit.Health.setter
    def Health(self, val):
        if rand.randint(0, 1) == 1 and self._Health != 1:
            print("Evaded damage ")
            Unit.Health = Rouge.Health_Rouge
            print(f"Helth {self.Name} --> {self._Health}")
            print("*" * 100)
            return Unit.Health
        else:
            if val < 0:
                raise ValueError
            elif val == 0:
                print(f"Unit {self.Name} is dead (")

        self._Health = val