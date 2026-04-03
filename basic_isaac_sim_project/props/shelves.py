from props.basic_shapes import create_box

def create_shelf_block(stage, root_path: str, rows: int = 2, cols: int = 4, spacing_x: float = 2.5, spacing_y: float = 2.0):
    index = 0
    for r in range(rows):
        for c in range(cols):
            create_box(stage, f"{root_path}/Shelf_{index}", translate=(c * spacing_x, r * spacing_y, 1.0), scale=(1.5, 0.6, 2.0))
            index += 1
