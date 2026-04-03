from typing import Iterable, Tuple

Vector3 = Tuple[float, float, float]

def add_xyz(a: Vector3, b: Vector3) -> Vector3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / max(1, len(values))
