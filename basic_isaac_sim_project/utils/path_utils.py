from pathlib import Path

def join_prim_path(*parts: str) -> str:
    cleaned = [p.strip("/") for p in parts if p]
    return "/" + "/".join(cleaned)

def ensure_directory(path: str) -> Path:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target
