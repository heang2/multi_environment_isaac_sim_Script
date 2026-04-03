from scenes.warehouse_scene import build_warehouse_mixed_fleet_scene
from scenes.sorting_scene import build_dual_arm_sorting_scene
from scenes.hospital_scene import build_hospital_scene
from scenes.office_scene import build_office_scene
from scenes.quadruped_scene import build_quadruped_scene
from scenes.digital_twin_scene import build_digital_twin_loading_zone_scene

SCENE_BUILDERS = {
    "warehouse_mixed_fleet": build_warehouse_mixed_fleet_scene,
    "dual_arm_sorting_cell": build_dual_arm_sorting_scene,
    "hospital_inspection_and_service": build_hospital_scene,
    "office_delivery_multi_robot": build_office_scene,
    "quadruped_maze_and_ramp": build_quadruped_scene,
    "warehouse_digital_twin_loading_zone": build_digital_twin_loading_zone_scene,
}
