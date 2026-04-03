from tasks.base_task import TaskDescription

SORTING_TASK = TaskDescription(
    name="Sorting Task",
    goals=["pick objects", "place objects into bins", "coordinate arm motions"],
    success_criteria=["correct sorting", "stable placement"],
)
