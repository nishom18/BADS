from datetime import datetime, timedelta
import heapq

class Task:
    """Represents a task with a name, priority, and deadline."""
    def __init__(self, name: str, priority: int, deadline: datetime):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __lt__(self, other):
        """Comparison for priority queue based on priority and deadline."""
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority > other.priority # Higher priority first

    def __repr__(self):
        return f"{self.name} (Priority: {self.priority}, Deadline: {self.deadline.strftime('%H:%M:%S')})"


class TaskScheduler:
    """Manages and executes tasks efficiently."""
    def __init__(self):
        self.task_queue = []

    def add_task(self, task: Task):
        heapq.heappush(self.task_queue, task)
        print(f"✅ Task added: {task}")

    def execute_tasks(self):
        print("\n🕒 Executing tasks by priority and deadline...\n")
        while self.task_queue:
            task = heapq.heappop(self.task_queue)
            print(f"🚀 Executing: {task}")
        print("\n🎯 All tasks completed successfully!")


if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Add some demo tasks
    scheduler.add_task(Task("Fix login bug", 5, datetime.now() + timedelta(hours=2)))
    scheduler.add_task(Task("Database backup", 2, datetime.now() + timedelta(hours=5)))
    scheduler.add_task(Task("Implement new feature", 4, datetime.now() + timedelta(hours=3)))
    scheduler.add_task(Task("Write documentation", 3, datetime.now() + timedelta(hours=4)))

    scheduler.execute_tasks()
