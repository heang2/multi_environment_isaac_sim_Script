from tasks.base_task import TaskDescription

WAREHOUSE_NAV_TASK = TaskDescription(
    name="Warehouse Navigation",
    goals=["move through aisles", "avoid static obstacles", "reach loading zone"],
    success_criteria=["no collisions", "target zone reached"],
)
