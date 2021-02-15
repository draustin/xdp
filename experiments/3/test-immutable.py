from dataclasses import dataclass

@dataclass(eq=False, frozen=True)
class PlainDataClass:
    d: list

print(PlainDataClass([3]) == PlainDataClass([3]))
{PlainDataClass([1]):2}

@dataclass(frozen=True, eq=True)
class FrozenEq:
    d: list

@dataclass(frozen=True, eq=False)
class FrozenNotEq:
    d: list



class PlainClass:
    def __init__(self, x):
        self.x = x

print(FrozenEq([4]) == FrozenEq([4]))
{FrozenEq([2]):4}

print(FrozenNotEq([3]) == FrozenNotEq([3]))
{FrozenNotEq(3):2}



print(PlainDataclass(2) == PlainDataclass(2))
{PlainDataclass(3):3}

