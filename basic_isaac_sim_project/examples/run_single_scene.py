from scenes.scene_registry import SCENE_BUILDERS

SCENE_KEY = "warehouse_mixed_fleet"

if __name__ == "__main__":
    builder = SCENE_BUILDERS[SCENE_KEY]
    builder()
    print(f"Built scene: {SCENE_KEY}")
