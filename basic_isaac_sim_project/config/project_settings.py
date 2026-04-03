from dataclasses import dataclass

@dataclass(frozen=True)
class ProjectSettings:
    root_prim_path: str = "/World"
    generated_root_name: str = "GeneratedScenes"
    default_units_in_meters: float = 1.0
    enable_physics: bool = True
    default_ground_plane: bool = True
    default_dome_light_intensity: float = 2500.0
    default_distant_light_intensity: float = 3000.0

DEFAULT_SETTINGS = ProjectSettings()
