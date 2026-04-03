from assets.asset_loader import load_first_available
from assets.asset_registry import get_asset_candidates

def load_robot(alias: str, prim_path: str):
    return load_first_available(get_asset_candidates(alias), prim_path)
