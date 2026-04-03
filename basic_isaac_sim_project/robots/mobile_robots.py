from robots.base_robot import load_robot

def load_nova_carter(prim_path: str):
    return load_robot("nova_carter", prim_path)

def load_jetbot(prim_path: str):
    return load_robot("jetbot", prim_path)

def load_create3(prim_path: str):
    return load_robot("create3", prim_path)

def load_kaya(prim_path: str):
    return load_robot("kaya", prim_path)

def load_jackal(prim_path: str):
    return load_robot("jackal", prim_path)
