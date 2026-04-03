from environments.base_environment import load_environment

def load_office_environment(prim_path: str = "/World/OfficeEnvironment"):
    return load_environment("office", prim_path)
