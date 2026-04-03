from scenes.common_scene_setup import prepare_single_scene
from environments.hospital_environment import load_hospital_environment
from robots.mobile_robots import load_nova_carter
from robots.quadrupeds import load_spot
from props.hospital_items import create_bed_cluster
from core.app_context import get_stage

def build_hospital_scene():
    ctx = prepare_single_scene("HospitalInspectionAndServiceComplex")
    load_hospital_environment(f"{ctx.scene_root_path}/Environment")
    load_nova_carter(f"{ctx.scene_root_path}/Robots/NovaCarter")
    load_spot(f"{ctx.scene_root_path}/Robots/Spot")
    stage = get_stage()
    if stage is not None:
        create_bed_cluster(stage, f"{ctx.scene_root_path}/Beds", count=4)
    return ctx
