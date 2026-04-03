from __future__ import annotations

from common import ensure_output_dir, initialize_basic_scene, add_robot_jetbot, translate_prim

try:
    import omni.replicator.core as rep
except Exception:
    rep = None

try:
    from isaacsim.core.utils.semantics import add_update_semantics
except Exception:
    add_update_semantics = None


OUTPUT_DIR = ensure_output_dir("sensor_outputs/semantic_segmentation_example")


def build_scene():
    world = initialize_basic_scene()
    add_robot_jetbot("/World/Jetbot")
    translate_prim("/World/Jetbot", (0.0, 0.0, 0.0))
    return world


def assign_semantics():
    if add_update_semantics is None:
        print("Semantic utility API is unavailable in this environment.")
        return
    add_update_semantics("/World/Jetbot", "robot")
    add_update_semantics("/World/Environment", "environment")


def attach_segmentation_camera():
    if rep is None:
        raise RuntimeError("omni.replicator.core is not available in this Isaac Sim environment.")
    camera = rep.create.camera(position=(3.0, 2.0, 2.2), look_at=(0.0, 0.0, 0.5))
    render_product = rep.create.render_product(camera, (1024, 768))
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir=str(OUTPUT_DIR), rgb=True, semantic_segmentation=True)
    writer.attach([render_product])
    return camera, render_product, writer


def main():
    world = build_scene()
    assign_semantics()
    attach_segmentation_camera()
    for _ in range(10):
        world.step(render=True)
    print(f"Semantic outputs will be written to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
