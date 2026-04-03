from __future__ import annotations

from common import initialize_basic_scene, add_robot_jetbot, translate_prim, print_stage_prim_exists

IMU_PRIM_PATH = "/World/Jetbot/IMUSensor"


def build_scene():
    world = initialize_basic_scene()
    add_robot_jetbot("/World/Jetbot")
    translate_prim("/World/Jetbot", (0.0, 0.0, 0.0))
    return world


def attach_imu():
    try:
        import omni.kit.commands
    except Exception as exc:
        raise RuntimeError("omni.kit.commands is not available.") from exc

    omni.kit.commands.execute(
        "IsaacSensorCreateImuSensor",
        path=IMU_PRIM_PATH,
        parent="/World/Jetbot",
        translation=(0.0, 0.0, 0.15),
        orientation=(1.0, 0.0, 0.0, 0.0),
    )
    print_stage_prim_exists(IMU_PRIM_PATH)


def main():
    world = build_scene()
    attach_imu()
    for _ in range(5):
        world.step(render=True)
    print("IMU example scene created.")


if __name__ == "__main__":
    main()
