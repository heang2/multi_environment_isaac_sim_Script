from config.asset_aliases import ASSET_ALIASES
from assets.nv_assets import candidate_usd_paths

def get_asset_candidates(alias: str):
    return candidate_usd_paths(ASSET_ALIASES.get(alias, []))
