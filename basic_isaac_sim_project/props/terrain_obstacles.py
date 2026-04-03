from props.basic_shapes import create_box

def create_ramp(stage, prim_path: str, translate=(0, 0, 0.2), scale=(3.0, 1.5, 0.4)):
    return create_box(stage, prim_path, translate=translate, scale=scale)

def create_platform(stage, prim_path: str, translate=(0, 0, 0.6), scale=(2.0, 2.0, 0.4)):
    return create_box(stage, prim_path, translate=translate, scale=scale)
