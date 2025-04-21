import random  # For generating random vehicle arrivals

# --- Simulation settings ---
duration = 60        # Total simulation time (in seconds)
capacity = 10        # Max size of each circular queue
arrival_prob = 0.3   # Probability of vehicle arrival per second

# --- Circular queues for NS and EW directions ---
queue_NS = [None] * capacity
queue_EW = [None] * capacity

front_NS = rear_NS = size_NS = 0
front_EW = rear_EW = size_EW = 0

# --- Statistics ---
wait_times = []
max_NS = max_EW = 0
vehicle_id = 0

# --- Simulation loop ---
for t in range(duration):
    # Vehicle arrives at NS direction
    if random.random() < arrival_prob and size_NS < capacity:
        queue_NS[rear_NS] = (vehicle_id, t)
        rear_NS = (rear_NS + 1) % capacity
        size_NS += 1
        vehicle_id += 1

    # Vehicle arrives at EW direction
    if random.random() < arrival_prob and size_EW < capacity:
        queue_EW[rear_EW] = (vehicle_id, t)
        rear_EW = (rear_EW + 1) % capacity
        size_EW += 1
        vehicle_id += 1

    # Traffic light alternates every 5 seconds
    if (t // 5) % 2 == 0 and size_NS > 0:  # Green light for NS
        v = queue_NS[front_NS]
        queue_NS[front_NS] = None
        front_NS = (front_NS + 1) % capacity
        size_NS -= 1
        wait_times.append(t - v[1])
    elif size_EW > 0:  # Green light for EW
        v = queue_EW[front_EW]
        queue_EW[front_EW] = None
        front_EW = (front_EW + 1) % capacity
        size_EW -= 1
        wait_times.append(t - v[1])

    # Track max queue lengths
    max_NS = max(max_NS, size_NS)
    max_EW = max(max_EW, size_EW)

# --- Final statistics ---
avg_wait = sum(wait_times) / len(wait_times) if wait_times else 0

print(f"Average wait time: {avg_wait:.2f} seconds")
print(f"Total vehicles processed: {len(wait_times)}")
print(f"Max queue length NS: {max_NS}")
print(f"Max queue length EW: {max_EW}")
