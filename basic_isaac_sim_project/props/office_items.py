from props.basic_shapes import create_box

def create_desk_cluster(stage, root_path: str, count: int = 4, spacing: float = 2.5):
    for i in range(count):
        create_box(stage, f"{root_path}/Desk_{i}", translate=(i * spacing, 0, 0.4), scale=(1.4, 0.8, 0.8))
