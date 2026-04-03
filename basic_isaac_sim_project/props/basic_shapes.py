from core.prims import define_cube
from core.transform_ops import set_translate, set_scale

def create_box(stage, prim_path: str, translate=(0, 0, 0), scale=(1, 1, 1), size: float = 1.0):
    cube = define_cube(stage, prim_path, size=size)
    if cube:
        prim = stage.GetPrimAtPath(prim_path)
        set_translate(prim, translate)
        set_scale(prim, scale)
    return cube
