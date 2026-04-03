"""
QuadrupedMazeAndRampChallenge


Single-scene Isaac Sim builder using NVIDIA / Isaac built-in assets.
Style matched to the user's notebook examples:
- get_assets_root_path()
- add_reference_to_stage()
- Core API / USD stage operations

Usage inside Isaac Sim Script Editor:
1) Open a fresh stage.
2) Run this file directly.
3) The scene will be generated under QuadrupedMazeAndRampChallenge.
"""

import math
import carb
import omni
import omni.client
import omni.usd
import numpy as np

from pxr import Gf, Sdf, UsdGeom, UsdLux
from isaacsim.core.api.objects import DynamicCuboid, VisualCuboid
from isaacsim.core.prims import XFormPrim
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path

# =========================
# helpers
# =========================

def _stage():
    return omni.usd.get_context().get_stage()


def _assets_root():
    root = get_assets_root_path()
    if root is None:
        raise RuntimeError("Could not find Isaac Sim assets folder")
    return root.rstrip("/")


def _asset_exists(full_path: str) -> bool:
    try:
        result, _ = omni.client.stat(full_path)
        return result == omni.client.Result.OK
    except Exception:
        return False


def _ensure_xform(path: str):
    st = _stage()
    if not st.GetPrimAtPath(path).IsValid():
        UsdGeom.Xform.Define(st, path)
    return st.GetPrimAtPath(path)


def _remove_prim(path: str):
    st = _stage()
    prim = st.GetPrimAtPath(path)
    if prim.IsValid():
        st.RemovePrim(path)


def _quat_from_yaw_deg(yaw_deg: float):
    yaw = math.radians(yaw_deg)
    return np.array([[math.cos(yaw / 2.0), 0.0, 0.0, math.sin(yaw / 2.0)]], dtype=np.float32)


def _set_pose(path: str, pos, yaw_deg=0.0, scale=None):
    _ensure_xform(path)
    xf = XFormPrim(prim_paths_expr=path)
    xf.set_world_poses(positions=np.array([pos], dtype=np.float32), orientations=_quat_from_yaw_deg(yaw_deg))
    if scale is not None:
        xf.set_local_scales(np.array([scale], dtype=np.float32))


def _set_translate_rotate_scale_usd(path: str, translate=None, rotate_xyz_deg=None, scale=None):
    st = _stage()
    prim = st.GetPrimAtPath(path)
    if not prim.IsValid():
        _ensure_xform(path)
        prim = st.GetPrimAtPath(path)
    xform = UsdGeom.Xformable(prim)
    if translate is not None:
        if not prim.HasAttribute("xformOp:translate"):
            xform.AddTranslateOp().Set(Gf.Vec3f(*translate))
        else:
            prim.GetAttribute("xformOp:translate").Set(Gf.Vec3f(*translate))
    if rotate_xyz_deg is not None:
        if not prim.HasAttribute("xformOp:rotateXYZ"):
            xform.AddRotateXYZOp().Set(Gf.Vec3f(*rotate_xyz_deg))
        else:
            prim.GetAttribute("xformOp:rotateXYZ").Set(Gf.Vec3f(*rotate_xyz_deg))
    if scale is not None:
        if not prim.HasAttribute("xformOp:scale"):
            xform.AddScaleOp().Set(Gf.Vec3f(*scale))
        else:
            prim.GetAttribute("xformOp:scale").Set(Gf.Vec3f(*scale))


def _try_add_asset(relative_candidates, prim_path: str, pos=None, yaw_deg=0.0, scale=None):
    root = _assets_root()
    for rel in relative_candidates:
        full = root + "/" + rel.lstrip("/")
        if _asset_exists(full):
            add_reference_to_stage(usd_path=full, prim_path=prim_path)
            if pos is not None:
                _set_pose(prim_path, pos, yaw_deg=yaw_deg, scale=scale)
            carb.log_info(f"Loaded asset: {full} -> {prim_path}")
            return full
    carb.log_warn(f"Could not locate asset for {prim_path}. Candidates: {relative_candidates}")
    return None


def _add_light(path: str, intensity=3000, translate=(0, 0, 12), rotate_xyz=(0, -60, 0)):
    st = _stage()
    light = UsdLux.DistantLight.Define(st, Sdf.Path(path))
    light.CreateIntensityAttr(intensity)
    _set_translate_rotate_scale_usd(path, translate=translate, rotate_xyz_deg=rotate_xyz)


def _add_dome_light(path: str, intensity=800):
    st = _stage()
    light = UsdLux.DomeLight.Define(st, Sdf.Path(path))
    light.CreateIntensityAttr(intensity)


def _add_grid_env(parent: str):
    env_path = parent + "/Environment"
    loaded = _try_add_asset(
        [
            "Isaac/Environments/Grid/default_environment.usd",
            "Isaac/Environments/Grid/gridroom_black.usd",
        ],
        env_path,
        pos=(0, 0, 0),
    )
    return loaded


def _add_env(parent: str, kind: str):
    env_path = parent + "/Environment"
    if kind == "full_warehouse":
        loaded = _try_add_asset(
            ["Isaac/Environments/Simple_Warehouse/full_warehouse.usd"], env_path, pos=(0, 0, 0)
        )
    elif kind == "warehouse_multiple_shelves":
        loaded = _try_add_asset(
            ["Isaac/Environments/Simple_Warehouse/warehouse_multiple_shelves.usd"], env_path, pos=(0, 0, 0)
        )
    elif kind == "warehouse_with_forklifts":
        loaded = _try_add_asset(
            ["Isaac/Environments/Simple_Warehouse/warehouse_with_forklifts.usd"], env_path, pos=(0, 0, 0)
        )
    elif kind == "small_warehouse_digital_twin":
        loaded = _try_add_asset(
            ["Isaac/Environments/Simple_Warehouse/small_warehouse_digital_twin.usd"], env_path, pos=(0, 0, 0)
        )
    elif kind == "simple_room":
        loaded = _try_add_asset(["Isaac/Environments/Simple_Room/simple_room.usd"], env_path, pos=(0, 0, 0))
    elif kind == "office":
        loaded = _try_add_asset(["Isaac/Environments/Office/office.usd"], env_path, pos=(0, 0, 0))
    elif kind == "hospital":
        loaded = _try_add_asset(["Isaac/Environments/Hospital/hospital.usd"], env_path, pos=(0, 0, 0))
    else:
        loaded = None

    if loaded is None:
        _add_grid_env(parent)
    return loaded


def _add_robot(asset_key: str, prim_path: str, pos, yaw_deg=0.0, scale=None):
    asset_db = {
        "franka": ["Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"],
        "jetbot": [
            "Isaac/Robots/NVIDIA/Jetbot/jetbot.usd",
            "Isaac/Robots/Jetbot/jetbot.usd",
        ],
        "nova_carter": ["Isaac/Robots/Carter/nova_carter.usd"],
        "carter_v1": ["Isaac/Robots/Carter/carter_v1.usd"],
        "forklift_b": ["Isaac/Robots/Forklift/forklift_b.usd"],
        "forklift_c": ["Isaac/Robots/Forklift/forklift_c.usd"],
        "kaya": ["Isaac/Robots/Kaya/kaya.usd"],
        "leatherback": ["Isaac/Robots/Leatherback/leatherback.usd"],
        "iw_hub": ["Isaac/Robots/Idealworks/iw_hub.usd"],
        "iw_hub_sensors": ["Isaac/Robots/Idealworks/iw_hub_sensors.usd"],
        "create3": ["Isaac/Robots/IRobot/create_3.usd"],
        "spot": ["Isaac/Robots/BostonDynamics/spot/spot.usd"],
        "go1": ["Isaac/Robots/Unitree/Go1/go1.usd"],
        "go2": ["Isaac/Robots/Unitree/Go2/go2.usd"],
        "anymal_c": ["Isaac/Robots/ANYbotics/anymal_c.usd", "Isaac/Robots/ANYbotics/anymal_c/anymal.usd"],
        "dingo": ["Isaac/Robots/Clearpath/Dingo/dingo.usd"],
        "jackal": ["Isaac/Robots/Clearpath/Jackal/jackal.usd"],
    }
    if asset_key not in asset_db:
        raise ValueError(f"Unknown robot asset key: {asset_key}")
    return _try_add_asset(asset_db[asset_key], prim_path, pos=pos, yaw_deg=yaw_deg, scale=scale)


def _add_visual_box(path, pos, size=1.0, scale=(1, 1, 1), color=(0.7, 0.7, 0.7)):
    VisualCuboid(
        prim_path=path,
        name=path.split("/")[-1],
        position=np.array(pos, dtype=np.float32),
        size=size,
        scale=np.array(scale, dtype=np.float32),
        color=np.array(color, dtype=np.float32),
    )


def _add_dynamic_box(path, pos, size=1.0, scale=(1, 1, 1), color=(0.9, 0.4, 0.1)):
    DynamicCuboid(
        prim_path=path,
        name=path.split("/")[-1],
        position=np.array(pos, dtype=np.float32),
        size=size,
        scale=np.array(scale, dtype=np.float32),
        color=np.array(color, dtype=np.float32),
    )


def _add_pallet_stack(parent, base_xy, layers=3, color=(0.62, 0.42, 0.22)):
    x, y = base_xy
    for i in range(layers):
        _add_visual_box(
            f"{parent}/pallet_{i}",
            pos=(x, y, 0.08 + i * 0.18),
            size=1.0,
            scale=(1.2, 1.0, 0.12),
            color=color,
        )


def _add_barrier_line(parent, start_xy, count=8, spacing=1.1, along="x"):
    sx, sy = start_xy
    for i in range(count):
        x = sx + i * spacing if along == "x" else sx
        y = sy if along == "x" else sy + i * spacing
        _add_visual_box(
            f"{parent}/barrier_{i}",
            pos=(x, y, 0.45),
            size=1.0,
            scale=(0.6, 0.12, 0.9),
            color=(1.0, 0.5, 0.0),
        )


def _add_maze(parent, x_min=-8, x_max=8, y_min=-8, y_max=8, wall_h=1.2):
    # border
    _add_visual_box(f"{parent}/wall_n", (0, y_max, wall_h / 2), scale=(x_max - x_min + 1, 0.25, wall_h), color=(0.3, 0.3, 0.35))
    _add_visual_box(f"{parent}/wall_s", (0, y_min, wall_h / 2), scale=(x_max - x_min + 1, 0.25, wall_h), color=(0.3, 0.3, 0.35))
    _add_visual_box(f"{parent}/wall_e", (x_max, 0, wall_h / 2), scale=(0.25, y_max - y_min + 1, wall_h), color=(0.3, 0.3, 0.35))
    _add_visual_box(f"{parent}/wall_w", (x_min, 0, wall_h / 2), scale=(0.25, y_max - y_min + 1, wall_h), color=(0.3, 0.3, 0.35))
    # internal walls
    walls = [
        ((-5, -2, wall_h / 2), (0.25, 9.0, wall_h)),
        ((-1, 3, wall_h / 2), (0.25, 7.0, wall_h)),
        ((3, -3, wall_h / 2), (0.25, 8.0, wall_h)),
        ((0, 5.5, wall_h / 2), (8.0, 0.25, wall_h)),
        ((2.5, 0, wall_h / 2), (6.0, 0.25, wall_h)),
        ((-3.5, -5.5, wall_h / 2), (6.0, 0.25, wall_h)),
    ]
    for i, (pos, scl) in enumerate(walls):
        _add_visual_box(f"{parent}/inner_wall_{i}", pos, scale=scl, color=(0.25, 0.25, 0.30))


def _add_ramp(path, center, scale=(2.5, 1.8, 0.2), rotate_xyz=(0, -18, 0), color=(0.4, 0.4, 0.45)):
    _add_visual_box(path, pos=center, scale=scale, color=color)
    _set_translate_rotate_scale_usd(path, translate=center, rotate_xyz_deg=rotate_xyz, scale=scale)


def _add_worktable(path, center, table_scale=(1.6, 0.8, 0.1), leg_h=0.7):
    x, y, z = center
    _add_visual_box(path + "/top", (x, y, z), scale=table_scale, color=(0.5, 0.5, 0.55))
    dx, dy = table_scale[0] * 0.4, table_scale[1] * 0.35
    for i, (sx, sy) in enumerate([(dx, dy), (dx, -dy), (-dx, dy), (-dx, -dy)]):
        _add_visual_box(path + f"/leg_{i}", (x + sx, y + sy, z - leg_h / 2), scale=(0.08, 0.08, leg_h), color=(0.35, 0.35, 0.38))


def _add_conveyor(path, center, length=5.0, width=0.9):
    _add_visual_box(path + "/belt", center, scale=(length, width, 0.18), color=(0.1, 0.1, 0.12))
    x, y, z = center
    for i in range(6):
        _add_visual_box(path + f"/roller_{i}", (x - length / 2 + 0.5 + i * 0.8, y, z), scale=(0.08, width * 0.9, 0.08), color=(0.55, 0.55, 0.6))

def build_scene_5(parent: str):
    """Quadruped maze + ramps + elevated platforms."""
    _add_grid_env(parent)
    _add_light(parent + "/SunLight", intensity=4500, translate=(0, 0, 16), rotate_xyz=(25, -35, 0))
    _add_dome_light(parent + "/DomeLight", intensity=550)

    _add_robot("spot", parent + "/Spot", pos=(-7.0, -7.0, 0.0), yaw_deg=45)
    _add_robot("go2", parent + "/Go2", pos=(-6.0, -5.5, 0.0), yaw_deg=20)
    _add_robot("anymal_c", parent + "/AnymalC", pos=(6.0, -6.0, 0.0), yaw_deg=135)

    _add_maze(parent + "/Maze")

    _add_ramp(parent + "/RampA", center=(-2.5, 6.0, 0.6), scale=(3.0, 1.8, 0.2), rotate_xyz=(0, -20, 0))
    _add_ramp(parent + "/RampB", center=(4.0, 4.0, 0.7), scale=(2.6, 2.0, 0.2), rotate_xyz=(0, 22, 35))

    _add_visual_box(parent + "/PlatformA", pos=(-0.5, 7.5, 1.15), scale=(3.2, 2.2, 0.35), color=(0.35, 0.35, 0.4))
    _add_visual_box(parent + "/PlatformB", pos=(6.0, 6.5, 1.45), scale=(2.8, 2.2, 0.35), color=(0.35, 0.35, 0.4))

    for i, pos in enumerate([(-7, 2, 0.3), (-6, 2.8, 0.6), (5.5, -0.8, 0.4), (6.2, 0.0, 0.75)]):
        _add_dynamic_box(parent + f"/Debris/debris_{i}", pos=pos, scale=(0.5, 0.5, 0.5), color=(0.8, 0.25 + 0.1 * i, 0.15))

# =========================
# top-level build
# =========================
CLEAR_OLD_GENERATED = True
ROOT_PATH = "/World/QuadrupedMazeAndRampChallenge"
SCENE_DISPLAY_NAME = "QuadrupedMazeAndRampChallenge"


def _init_root():
    _ensure_xform("/World")
    if CLEAR_OLD_GENERATED:
        _remove_prim(ROOT_PATH)
    _ensure_xform(ROOT_PATH)


def build():
    _init_root()
    build_scene_5(ROOT_PATH)
    carb.log_info(f"Built scene: {SCENE_DISPLAY_NAME} -> {ROOT_PATH}")


build()
print(f"Done. Scene={SCENE_DISPLAY_NAME}, ROOT_PATH={ROOT_PATH}")
