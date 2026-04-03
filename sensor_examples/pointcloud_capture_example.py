from __future__ import annotations

from common import initialize_basic_scene, add_robot_nova_carter, translate_prim, print_stage_prim_exists

POINTCLOUD_SENSOR_PATH = "/World/NovaCarter/PointCloudLidar"


def build_scene():
    world = initialize_basic_scene()
    add_robot_nova_carter("/World/NovaCarter")
    translate_prim("/World/NovaCarter", (0.0, 0.0, 0.0))
    return world


def attach_pointcloud_sensor():
    try:
        import omni.kit.commands
    except Exception as exc:
        raise RuntimeError("omni.kit.commands is not available.") from exc

    omni.kit.commands.execute(
        "IsaacSensorCreateRtxLidar",
        path=POINTCLOUD_SENSOR_PATH,
        parent="/World/NovaCarter",
        config="Example_Rotary",
        translation=(0.0, 0.0, 1.3),
        orientation=(1.0, 0.0, 0.0, 0.0),
    )
    print_stage_prim_exists(POINTCLOUD_SENSOR_PATH)


def main():
    world = build_scene()
    attach_pointcloud_sensor()
    for _ in range(5):
        world.step(render=True)
    print("Point-cloud style capture setup is ready.")


if __name__ == "__main__":
    main()
