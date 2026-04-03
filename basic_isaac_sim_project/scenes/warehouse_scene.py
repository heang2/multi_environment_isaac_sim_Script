from scenes.common_scene_setup import prepare_single_scene
from environments.warehouse_environment import load_warehouse_environment
from robots.mobile_robots import load_nova_carter, load_jetbot
from robots.manipulators import load_franka
from props.shelves import create_shelf_block
from props.pallets import create_pallet_row
from core.app_context import get_stage

def build_warehouse_mixed_fleet_scene():
    ctx = prepare_single_scene("WarehouseMixedFleetComplex")
    load_warehouse_environment(f"{ctx.scene_root_path}/Environment")
    load_nova_carter(f"{ctx.scene_root_path}/Robots/NovaCarter")
    load_jetbot(f"{ctx.scene_root_path}/Robots/Jetbot")
    load_franka(f"{ctx.scene_root_path}/Robots/Franka")
    stage = get_stage()
    if stage is not None:
        create_shelf_block(stage, f"{ctx.scene_root_path}/Shelves", rows=2, cols=4)
        create_pallet_row(stage, f"{ctx.scene_root_path}/Pallets", count=6)
    return ctx
