from __future__ import annotations

from common import ensure_output_dir, initialize_basic_scene, add_robot_jetbot, translate_prim

try:
    import omni.replicator.core as rep
except Exception:
    rep = None


OUTPUT_DIR = ensure_output_dir("sensor_outputs/synthetic_data_writer_example")


def build_scene():
    world = initialize_basic_scene()
    add_robot_jetbot("/World/Jetbot")
    translate_prim("/World/Jetbot", (0.0, 0.0, 0.0))
    return world


def setup_writer():
    if rep is None:
        raise RuntimeError("omni.replicator.core is not available in this Isaac Sim environment.")

    camera = rep.create.camera(position=(3.5, 2.5, 2.0), look_at=(0.0, 0.0, 0.4))
    render_product = rep.create.render_product(camera, (1280, 720))

    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(
        output_dir=str(OUTPUT_DIR),
        rgb=True,
        bounding_box_2d_tight=True,
        semantic_segmentation=True,
    )
    writer.attach([render_product])
    return camera, render_product, writer


def main():
    world = build_scene()
    setup_writer()
    for _ in range(10):
        world.step(render=True)
    print(f"Synthetic data outputs will be written to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
