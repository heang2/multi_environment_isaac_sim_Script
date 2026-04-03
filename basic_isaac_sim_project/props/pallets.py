from props.basic_shapes import create_box

def create_pallet_row(stage, root_path: str, count: int = 4, spacing: float = 2.0):
    for i in range(count):
        create_box(stage, f"{root_path}/Pallet_{i}", translate=(i * spacing, 0, 0.1), scale=(1.2, 1.0, 0.2))
