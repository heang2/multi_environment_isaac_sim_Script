from props.basic_shapes import create_box

def create_barrier_line(stage, root_path: str, count: int = 6, spacing: float = 1.5, axis: str = "x"):
    for i in range(count):
        x = i * spacing if axis == "x" else 0
        y = i * spacing if axis == "y" else 0
        create_box(stage, f"{root_path}/Barrier_{i}", translate=(x, y, 0.5), scale=(1.0, 0.2, 1.0))
