from utils.logging_utils import log_warn

def set_translate(prim, xyz):
    try:
        from pxr import UsdGeom, Gf
        xform = UsdGeom.Xformable(prim)
        xform.AddTranslateOp().Set(Gf.Vec3d(*xyz))
    except Exception:
        log_warn(f"Could not set translation for {prim}")

def set_rotate_xyz(prim, xyz):
    try:
        from pxr import UsdGeom, Gf
        xform = UsdGeom.Xformable(prim)
        xform.AddRotateXYZOp().Set(Gf.Vec3f(*xyz))
    except Exception:
        log_warn(f"Could not set rotation for {prim}")

def set_scale(prim, xyz):
    try:
        from pxr import UsdGeom, Gf
        xform = UsdGeom.Xformable(prim)
        xform.AddScaleOp().Set(Gf.Vec3f(*xyz))
    except Exception:
        log_warn(f"Could not set scale for {prim}")
