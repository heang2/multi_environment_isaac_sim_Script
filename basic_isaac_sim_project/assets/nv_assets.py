from typing import List, Optional
from utils.logging_utils import log_info, log_warn

def get_assets_root_path() -> Optional[str]:
    try:
        from omni.isaac.core.utils.nucleus import get_assets_root_path as _get_assets_root_path  # type: ignore
        return _get_assets_root_path()
    except Exception:
        log_warn("Could not resolve NVIDIA assets root path.")
        return None

def add_reference_to_stage(usd_path: str, prim_path: str) -> None:
    try:
        from omni.isaac.core.utils.stage import add_reference_to_stage as _add_reference_to_stage  # type: ignore
        _add_reference_to_stage(usd_path=usd_path, prim_path=prim_path)
        log_info(f"Referenced asset: {usd_path} -> {prim_path}")
    except Exception:
        log_warn(f"Could not add reference: {usd_path} -> {prim_path}")

def candidate_usd_paths(relative_paths: List[str]) -> List[str]:
    root = get_assets_root_path()
    if root is None:
        return []
    return [f"{root}/{p}" for p in relative_paths]
