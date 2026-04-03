from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence, Tuple

from isaacsim.core.api import World
from isaacsim.core.utils.stage import add_reference_to_stage, get_current_stage
from isaacsim.storage.native import get_assets_root_path

try:
    from pxr import Gf, UsdGeom, UsdLux
except Exception:
    Gf = None
    UsdGeom = None
    UsdLux = None


DEFAULT_OUTPUT_DIR = Path.cwd() / "sensor_outputs"


def ensure_output_dir(path: Optional[str] = None) -> Path:
    output_dir = Path(path) if path else DEFAULT_OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def create_world() -> World:
    return World(stage_units_in_meters=1.0)


def add_default_ground(prim_path: str = "/World/GroundPlane") -> None:
    try:
        from isaacsim.core.api.objects import GroundPlane
        GroundPlane(prim_path=prim_path)
    except Exception:
        pass


def add_dome_light(prim_path: str = "/World/DomeLight", intensity: float = 3000.0) -> None:
    if UsdLux is None:
        return
    stage = get_current_stage()
    light = UsdLux.DomeLight.Define(stage, prim_path)
    light.CreateIntensityAttr(intensity)


def get_asset_path(relative_path: str) -> str:
    assets_root = get_assets_root_path()
    if not assets_root:
        raise RuntimeError("Could not resolve Isaac Sim assets root path.")
    return assets_root + relative_path


def try_add_asset(prim_path: str, candidate_relative_paths: Sequence[str]):
    last_error = None
    for rel_path in candidate_relative_paths:
        try:
            usd_path = get_asset_path(rel_path)
            add_reference_to_stage(usd_path, prim_path)
            return usd_path
        except Exception as exc:
            last_error = exc
    if last_error is not None:
        print(f"Failed to add asset at {prim_path}: {last_error}")
    return None


def add_default_environment() -> None:
    candidates = [
        "/Isaac/Environments/Grid/default_environment.usd",
        "/Isaac/Environments/Simple_Warehouse/full_warehouse.usd",
    ]
    try_add_asset("/World/Environment", candidates)


def add_robot_jetbot(prim_path: str = "/World/Jetbot"):
    candidates = [
        "/Isaac/Robots/Jetbot/jetbot.usd",
        "/Isaac/Robots/Jetbot/jetbot_with_sensors.usd",
    ]
    return try_add_asset(prim_path, candidates)


def add_robot_nova_carter(prim_path: str = "/World/NovaCarter"):
    candidates = [
        "/Isaac/Robots/Carter/nova_carter.usd",
        "/Isaac/Robots/Nova_Carter/nova_carter.usd",
    ]
    return try_add_asset(prim_path, candidates)


def translate_prim(prim_path: str, xyz: Tuple[float, float, float]) -> None:
    if UsdGeom is None:
        return
    stage = get_current_stage()
    prim = stage.GetPrimAtPath(prim_path)
    if not prim.IsValid():
        return
    xformable = UsdGeom.Xformable(prim)
    translate_ops = [op for op in xformable.GetOrderedXformOps() if op.GetOpType() == UsdGeom.XformOp.TypeTranslate]
    if translate_ops:
        translate_ops[0].Set(Gf.Vec3d(*xyz))
    else:
        xformable.AddTranslateOp().Set(Gf.Vec3d(*xyz))


def initialize_basic_scene() -> World:
    world = create_world()
    add_default_environment()
    add_default_ground()
    add_dome_light()
    world.reset()
    return world


def print_stage_prim_exists(prim_path: str) -> None:
    stage = get_current_stage()
    prim = stage.GetPrimAtPath(prim_path)
    print(f"{prim_path}: {'FOUND' if prim and prim.IsValid() else 'MISSING'}")
