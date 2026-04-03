from __future__ import annotations

from common import ensure_output_dir, initialize_basic_scene, add_robot_nova_carter, translate_prim

try:
    import omni.replicator.core as rep
except Exception:
    rep = None


OUTPUT_DIR = ensure_output_dir("sensor_outputs/depth_camera_example")


def build_scene():
    world = initialize_basic_scene()
    add_robot_nova_carter("/World/NovaCarter")
    translate_prim("/World/NovaCarter", (0.0, 0.0, 0.0))
    return world


def attach_depth_camera():
    if rep is None:
        raise RuntimeError("omni.replicator.core is not available in this Isaac Sim environment.")
    camera = rep.create.camera(
        position=(2.5, 2.0, 1.8),
        look_at=(0.0, 0.0, 0.6),
        clipping_range=(0.01, 50.0),
    )
    render_product = rep.create.render_product(camera, (640, 480))
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir=str(OUTPUT_DIR), distance_to_image_plane=True, depth=True, rgb=True)
    writer.attach([render_product])
    return camera, render_product, writer


def main():
    world = build_scene()
    attach_depth_camera()
    for _ in range(10):
        world.step(render=True)
    print(f"Depth-related outputs will be written to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
