from tasks.base_task import TaskDescription

HOSPITAL_INSPECTION_TASK = TaskDescription(
    name="Hospital Inspection",
    goals=["visit checkpoints", "avoid clutter", "cover service corridor"],
    success_criteria=["all checkpoints visited", "no collisions"],
)
