from props.basic_shapes import create_box

def create_bed_cluster(stage, root_path: str, count: int = 3, spacing: float = 3.0):
    for i in range(count):
        create_box(stage, f"{root_path}/Bed_{i}", translate=(0, i * spacing, 0.4), scale=(2.0, 1.0, 0.8))
