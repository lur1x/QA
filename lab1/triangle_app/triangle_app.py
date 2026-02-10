import sys
from enum import Enum
from typing import Optional

class TriangleType(Enum):
    EQUILATERAL = "equilateral"
    ISOSCELES = "isosceles"
    SCALENE = "scalene"
    NOT_A_TRIANGLE = "not_a_triangle"
    UNKNOWN_ERROR = "unknown_error"

def triangle_type(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a <= 0 or b <= 0 or c <= 0:
            return TriangleType.NOT_A_TRIANGLE

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return TriangleType.NOT_A_TRIANGLE

        if (a == b == c):
            return TriangleType.EQUILATERAL

        if (a == b or a == c or c == b):
            return TriangleType.ISOSCELES

        return TriangleType.SCALENE

    except (ValueError, TypeError):
        return TriangleType.NOT_A_TRIANGLE
    except Exception:
        return TriangleType.UNKNOWN_ERROR


class Triangle:

    def __init__(self, a: float, b: float, c: float):

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be positive")

        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_strings(cls, a_str: str, b_str: str, c_str: str) -> Optional['Triangle']:
        try:
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
            return cls(a, b, c)
        except (ValueError, TypeError):
            return None
        except ValueError:
            return None

    def is_valid(self) -> bool:
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.c + self.b > self.a)

    def get_type(self) -> TriangleType:
        if (self.a == self.b == self.c):
            return TriangleType.EQUILATERAL

        if (self.a == self.b or self.a == self.c or self.c == self.b):
            return TriangleType.ISOSCELES

        return TriangleType.SCALENE

    def analyze(self) -> TriangleType:
        if not self.is_valid():
            return TriangleType.NOT_A_TRIANGLE

        return self.get_type()


def run_triangle_classifier() -> TriangleType:

    if len(sys.argv) != 4:
        return TriangleType.UNKNOWN_ERROR

    side1, side2, side3 = sys.argv[1], sys.argv[2], sys.argv[3]

    triangle = Triangle.from_strings( side1, side2, side3)

    if triangle is None:
        return TriangleType.NOT_A_TRIANGLE

    try:
        return triangle.analyze()
    except Exception:
        return TriangleType.UNKNOWN_ERROR


def main() -> int:
    result_type = run_triangle_classifier()
    print(result_type.value)

    return 0


if __name__ == "__main__":
    sys.exit(main())