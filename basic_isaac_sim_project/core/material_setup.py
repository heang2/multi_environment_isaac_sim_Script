from utils.logging_utils import log_warn

def create_preview_material(stage, material_path: str):
    try:
        from pxr import UsdShade
        return UsdShade.Material.Define(stage, material_path)
    except Exception:
        log_warn(f"Could not create material at {material_path}")
        return None
