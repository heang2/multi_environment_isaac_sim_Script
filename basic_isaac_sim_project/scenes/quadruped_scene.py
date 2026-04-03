from scenes.common_scene_setup import prepare_single_scene
from environments.grid_environment import load_grid_environment
from robots.quadrupeds import load_spot, load_go2
from props.barriers import create_barrier_line
from props.terrain_obstacles import create_ramp, create_platform
from core.app_context import get_stage

def build_quadruped_scene():
    ctx = prepare_single_scene("QuadrupedMazeAndRampChallenge")
    load_grid_environment(f"{ctx.scene_root_path}/Environment")
    load_spot(f"{ctx.scene_root_path}/Robots/Spot")
    load_go2(f"{ctx.scene_root_path}/Robots/Go2")
    stage = get_stage()
    if stage is not None:
        create_barrier_line(stage, f"{ctx.scene_root_path}/MazeWalls", count=8, spacing=1.5)
        create_ramp(stage, f"{ctx.scene_root_path}/Ramp")
        create_platform(stage, f"{ctx.scene_root_path}/Platform", translate=(5, 0, 0.8))
    return ctx
