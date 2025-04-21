# Class representing a fixed-size circular array queue
class CircularArrayQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity       # Underlying array for storing tasks
        self.capacity = capacity             # Maximum size of the queue
        self.front = self.rear = -1          # Front and rear pointers

    def is_empty(self):
        return self.front == -1              # Queue is empty when front is -1

    def is_full(self):
        # Queue is full when the next rear position equals front (circularly)
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, task):
        if self.is_full():
            raise OverflowError("Queue is full")  # Prevent enqueue if full
        if self.is_empty():
            self.front = 0                        # Set front at first insertion
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = task              # Insert task at rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")    # Prevent dequeue if empty
        task = self.queue[self.front]             # Get task at front
        if self.front == self.rear:
            # Only one task in the queue — reset to empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return task                                # Return dequeued task


# Round-Robin scheduler function
def round_robin_scheduler(queue, time_slice):
    while not queue.is_empty():
        task = queue.dequeue()                      # Get next task
        print(f"Running task: {task['name']}")
        task['time'] -= time_slice                  # Deduct quantum from task time

        if task['time'] > 0:
            # Task not finished — re-enqueue for next round
            print(f"Re-enqueuing task: {task['name']} with {task['time']} units left")
            queue.enqueue(task)


# Example tasks
tasks = [
    {'name': 'T1', 'time': 10},
    {'name': 'T2', 'time': 4},
    {'name': 'T3', 'time': 6}
]

# Create queue and enqueue tasks
queue = CircularArrayQueue(5)
for task in tasks:
    queue.enqueue(task)

# Start round-robin scheduling with a 3-unit time slice
round_robin_scheduler(queue, time_slice=3)