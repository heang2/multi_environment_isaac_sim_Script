from utils.logging_utils import log_info

def load_forklift_placeholder(prim_path: str):
    log_info(f"Forklift placeholder requested at {prim_path}. Replace with project-specific forklift USD if needed.")
    return prim_path
