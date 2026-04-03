from scenes.common_scene_setup import prepare_single_scene
from environments.office_environment import load_office_environment
from robots.mobile_robots import load_jetbot, load_create3, load_kaya
from props.office_items import create_desk_cluster
from core.app_context import get_stage

def build_office_scene():
    ctx = prepare_single_scene("OfficeDeliveryMultiRobotComplex")
    load_office_environment(f"{ctx.scene_root_path}/Environment")
    load_jetbot(f"{ctx.scene_root_path}/Robots/Jetbot")
    load_create3(f"{ctx.scene_root_path}/Robots/Create3")
    load_kaya(f"{ctx.scene_root_path}/Robots/Kaya")
    stage = get_stage()
    if stage is not None:
        create_desk_cluster(stage, f"{ctx.scene_root_path}/Desks", count=6)
    return ctx
