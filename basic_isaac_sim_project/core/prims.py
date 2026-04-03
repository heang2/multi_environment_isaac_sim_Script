from utils.logging_utils import log_warn

def define_cube(stage, prim_path: str, size: float = 1.0):
    try:
        from pxr import UsdGeom
        cube = UsdGeom.Cube.Define(stage, prim_path)
        cube.GetSizeAttr().Set(size)
        return cube
    except Exception:
        log_warn(f"Could not define cube at {prim_path}")
        return None

def define_plane(stage, prim_path: str):
    try:
        from pxr import UsdGeom
        return UsdGeom.Mesh.Define(stage, prim_path)
    except Exception:
        log_warn(f"Could not define plane at {prim_path}")
        return None
