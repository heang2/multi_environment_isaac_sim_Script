from __future__ import annotations

from common import ensure_output_dir, initialize_basic_scene, add_robot_jetbot, translate_prim

OUTPUT_DIR = ensure_output_dir("sensor_outputs/occupancy_map_export_example")


def build_scene():
    world = initialize_basic_scene()
    add_robot_jetbot("/World/Jetbot")
    translate_prim("/World/Jetbot", (0.0, 0.0, 0.0))
    return world


def prepare_occupancy_workflow():
    print("Preparing occupancy map export workflow...")
    print(f"Target output directory: {OUTPUT_DIR.resolve()}")
    print("Add your map generation and export API calls here for your Isaac Sim version.")


def main():
    world = build_scene()
    prepare_occupancy_workflow()
    for _ in range(3):
        world.step(render=True)
    print("Occupancy map scaffold scene is ready.")


if __name__ == "__main__":
    main()
