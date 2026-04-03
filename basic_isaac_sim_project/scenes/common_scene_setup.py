from core.app_context import get_stage
from core.light_setup import create_dome_light, create_distant_light
from core.physics_setup import enable_physics_scene
from core.stage_manager import delete_prim_if_exists
from scenes.scene_context import SceneContext

def prepare_single_scene(scene_name: str) -> SceneContext:
    stage = get_stage()
    scene_root = f"/World/{scene_name}"
    delete_prim_if_exists(scene_root)
    enable_physics_scene()
    if stage is not None:
        create_dome_light(stage)
        create_distant_light(stage)
    return SceneContext(scene_name=scene_name, scene_root_path=scene_root)
