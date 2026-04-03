from utils.logging_utils import log_info, log_warn

def enable_physics_scene(scene_path: str = "/World/physicsScene") -> None:
    try:
        from pxr import UsdPhysics
        import omni.usd  # type: ignore
        stage = omni.usd.get_context().get_stage()
        UsdPhysics.Scene.Define(stage, scene_path)
        log_info(f"Physics scene created at {scene_path}")
    except Exception:
        log_warn("Physics scene creation skipped.")
