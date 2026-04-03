from environments.base_environment import load_environment

def load_grid_environment(prim_path: str = "/World/GridEnvironment"):
    return load_environment("grid_room", prim_path)
