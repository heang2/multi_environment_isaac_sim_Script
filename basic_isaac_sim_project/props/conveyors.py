from props.basic_shapes import create_box

def create_conveyor(stage, prim_path: str, length: float = 6.0):
    return create_box(stage, prim_path, translate=(0, 0, 0.25), scale=(length, 0.8, 0.3))
