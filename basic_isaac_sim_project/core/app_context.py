from utils.logging_utils import log_info, log_warn

def get_stage():
    try:
        import omni.usd  # type: ignore
        return omni.usd.get_context().get_stage()
    except Exception:
        log_warn("Isaac Sim stage is not available in this Python environment.")
        return None

def new_stage():
    try:
        import omni.usd  # type: ignore
        omni.usd.get_context().new_stage()
        log_info("Created a new stage.")
    except Exception:
        log_warn("Could not create a new stage outside Isaac Sim.")
