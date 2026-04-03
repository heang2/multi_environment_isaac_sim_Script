from typing import List, Tuple

Vector3 = Tuple[float, float, float]

def grid_positions(rows: int, cols: int, spacing_x: float, spacing_y: float, z: float = 0.0) -> List[Vector3]:
    positions: List[Vector3] = []
    for r in range(rows):
        for c in range(cols):
            positions.append((c * spacing_x, r * spacing_y, z))
    return positions

def line_positions(count: int, spacing: float, axis: str = "x", fixed=(0.0, 0.0, 0.0)):
    out = []
    for i in range(count):
        x, y, z = fixed
        if axis == "x":
            x += i * spacing
        elif axis == "y":
            y += i * spacing
        else:
            z += i * spacing
        out.append((x, y, z))
    return out
