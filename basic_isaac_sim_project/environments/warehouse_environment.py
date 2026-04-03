from environments.base_environment import load_environment

def load_warehouse_environment(prim_path: str = "/World/WarehouseEnvironment"):
    return load_environment("simple_warehouse", prim_path)
