from scenes.scene_registry import SCENE_BUILDERS

if __name__ == "__main__":
    for name, builder in SCENE_BUILDERS.items():
        print(f"Building: {name}")
        builder()
