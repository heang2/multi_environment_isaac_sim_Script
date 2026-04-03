from typing import Iterable, Optional
from assets.nv_assets import add_reference_to_stage
from utils.logging_utils import log_warn

def load_first_available(candidates: Iterable[str], prim_path: str) -> Optional[str]:
    for usd_path in candidates:
        try:
            add_reference_to_stage(usd_path, prim_path)
            return usd_path
        except Exception:
            continue
    log_warn(f"No candidate asset could be loaded for {prim_path}")
    return None
