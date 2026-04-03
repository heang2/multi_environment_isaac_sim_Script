from __future__ import annotations

from common import initialize_basic_scene, add_robot_nova_carter, translate_prim, print_stage_prim_exists

LIDAR_PRIM_PATH = "/World/NovaCarter/LidarSensor"


def build_scene():
    world = initialize_basic_scene()
    add_robot_nova_carter("/World/NovaCarter")
    translate_prim("/World/NovaCarter", (0.0, 0.0, 0.0))
    return world


def attach_lidar():
    try:
        import omni.kit.commands
    except Exception as exc:
        raise RuntimeError("omni.kit.commands is not available.") from exc

    omni.kit.commands.execute(
        "IsaacSensorCreateRtxLidar",
        path=LIDAR_PRIM_PATH,
        parent="/World/NovaCarter",
        config="Example_Rotary",
        translation=(0.0, 0.0, 1.2),
        orientation=(1.0, 0.0, 0.0, 0.0),
    )
    print_stage_prim_exists(LIDAR_PRIM_PATH)


def main():
    world = build_scene()
    attach_lidar()
    for _ in range(5):
        world.step(render=True)
    print("LiDAR example scene created.")


if __name__ == "__main__":
    main()
