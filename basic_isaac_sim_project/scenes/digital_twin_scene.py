from scenes.common_scene_setup import prepare_single_scene
from environments.warehouse_environment import load_warehouse_environment
from robots.mobile_robots import load_jackal, load_nova_carter
from robots.manipulators import load_franka
from props.pallets import create_pallet_row
from props.conveyors import create_conveyor
from core.app_context import get_stage

def build_digital_twin_loading_zone_scene():
    ctx = prepare_single_scene("WarehouseDigitalTwinLoadingZoneComplex")
    load_warehouse_environment(f"{ctx.scene_root_path}/Environment")
    load_jackal(f"{ctx.scene_root_path}/Robots/Jackal")
    load_nova_carter(f"{ctx.scene_root_path}/Robots/NovaCarter")
    load_franka(f"{ctx.scene_root_path}/Robots/Franka")
    stage = get_stage()
    if stage is not None:
        create_pallet_row(stage, f"{ctx.scene_root_path}/InboundPallets", count=5)
        create_conveyor(stage, f"{ctx.scene_root_path}/TransferConveyor", length=10.0)
    return ctx
