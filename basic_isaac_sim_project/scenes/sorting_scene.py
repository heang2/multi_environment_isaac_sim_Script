from scenes.common_scene_setup import prepare_single_scene
from environments.grid_environment import load_grid_environment
from robots.manipulators import load_franka
from props.conveyors import create_conveyor
from props.basic_shapes import create_box
from core.app_context import get_stage

def build_dual_arm_sorting_scene():
    ctx = prepare_single_scene("DualArmSortingCellComplex")
    load_grid_environment(f"{ctx.scene_root_path}/Environment")
    load_franka(f"{ctx.scene_root_path}/Robots/FrankaLeft")
    load_franka(f"{ctx.scene_root_path}/Robots/FrankaRight")
    stage = get_stage()
    if stage is not None:
        create_conveyor(stage, f"{ctx.scene_root_path}/Conveyor", length=8.0)
        create_box(stage, f"{ctx.scene_root_path}/BinA", translate=(3, 2, 0.5), scale=(1, 1, 1))
        create_box(stage, f"{ctx.scene_root_path}/BinB", translate=(3, -2, 0.5), scale=(1, 1, 1))
    return ctx
