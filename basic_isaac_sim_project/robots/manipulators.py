from robots.base_robot import load_robot

def load_franka(prim_path: str):
    return load_robot("franka", prim_path)
