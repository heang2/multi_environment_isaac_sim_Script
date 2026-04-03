from utils.logging_utils import log_warn

def create_dome_light(stage, prim_path: str = "/World/DomeLight", intensity: float = 2500.0):
    try:
        from pxr import UsdLux
        light = UsdLux.DomeLight.Define(stage, prim_path)
        light.CreateIntensityAttr(intensity)
        return light
    except Exception:
        log_warn("Could not create dome light.")
        return None

def create_distant_light(stage, prim_path: str = "/World/DistantLight", intensity: float = 3000.0):
    try:
        from pxr import UsdLux
        light = UsdLux.DistantLight.Define(stage, prim_path)
        light.CreateIntensityAttr(intensity)
        return light
    except Exception:
        log_warn("Could not create distant light.")
        return None
