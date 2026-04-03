from environments.base_environment import load_environment

def load_hospital_environment(prim_path: str = "/World/HospitalEnvironment"):
    return load_environment("hospital", prim_path)
