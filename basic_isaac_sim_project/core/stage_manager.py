from utils.logging_utils import log_info, log_warn

def delete_prim_if_exists(prim_path: str) -> None:
    try:
        import omni.usd  # type: ignore
        stage = omni.usd.get_context().get_stage()
        prim = stage.GetPrimAtPath(prim_path)
        if prim and prim.IsValid():
            stage.RemovePrim(prim_path)
            log_info(f"Deleted prim: {prim_path}")
    except Exception:
        log_warn(f"Could not delete prim: {prim_path}")

def define_xform(stage, prim_path: str):
    from pxr import UsdGeom
    return UsdGeom.Xform.Define(stage, prim_path)
