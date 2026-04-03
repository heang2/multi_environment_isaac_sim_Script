from robots.base_robot import load_robot

def load_spot(prim_path: str):
    return load_robot("spot", prim_path)

def load_go2(prim_path: str):
    return load_robot("go2", prim_path)
