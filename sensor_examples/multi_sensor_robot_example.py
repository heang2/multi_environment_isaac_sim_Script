from __future__ import annotations

from common import initialize_basic_scene, add_robot_nova_carter, translate_prim, print_stage_prim_exists

RGB_CAMERA_PATH = "/World/NovaCarter/FrontCamera"
LIDAR_PATH = "/World/NovaCarter/FrontLidar"
IMU_PATH = "/World/NovaCarter/BodyIMU"


def build_scene():
    world = initialize_basic_scene()
    add_robot_nova_carter("/World/NovaCarter")
    translate_prim("/World/NovaCarter", (0.0, 0.0, 0.0))
    return world


def attach_rgb_camera():
    try:
        import omni.kit.commands
    except Exception as exc:
        raise RuntimeError("omni.kit.commands is not available.") from exc

    omni.kit.commands.execute(
        "IsaacSensorCreateCamera",
        path=RGB_CAMERA_PATH,
        parent="/World/NovaCarter",
        translation=(0.25, 0.0, 1.1),
        orientation=(1.0, 0.0, 0.0, 0.0),
    )
    print_stage_prim_exists(RGB_CAMERA_PATH)


def attach_lidar():
    import omni.kit.commands
    omni.kit.commands.execute(
        "IsaacSensorCreateRtxLidar",
        path=LIDAR_PATH,
        parent="/World/NovaCarter",
        config="Example_Rotary",
        translation=(0.15, 0.0, 1.15),
        orientation=(1.0, 0.0, 0.0, 0.0),
    )
    print_stage_prim_exists(LIDAR_PATH)


def attach_imu():
    import omni.kit.commands
    omni.kit.commands.execute(
        "IsaacSensorCreateImuSensor",
        path=IMU_PATH,
        parent="/World/NovaCarter",
        translation=(0.0, 0.0, 0.8),
        orientation=(1.0, 0.0, 0.0, 0.0),
    )
    print_stage_prim_exists(IMU_PATH)


def main():
    world = build_scene()
    attach_rgb_camera()
    attach_lidar()
    attach_imu()
    for _ in range(5):
        world.step(render=True)
    print("Multi-sensor robot example scene is ready.")


if __name__ == "__main__":
    main()
