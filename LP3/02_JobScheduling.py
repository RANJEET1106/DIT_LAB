# Job Sequencing with Deadline - Simple Version

# jobs = [
#     ("J1", 2, 60),
#     ("J2", 1, 100),
#     ("J3", 3, 20),
#     ("J4", 2, 40),
#     ("J5", 1, 20)
# ]

# jobs = [
#     ("J1", 2, 100),
#     ("J2", 1, 19),
#     ("J3", 2, 27),
#     ("J4", 1, 25),
#     ("J5", 3, 15)
# ]

def JobSchedule(jobs):
    # Step 1: Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create slots (all initially empty)
    slots = [None] * (max_deadline + 1)

    profit = 0
    result = []

    # Step 2: Assign jobs greedily
    for job in jobs:
        job_id, deadline, job_profit = job

        # Find a free slot from deadline backwards
        for time in range(deadline, 0, -1):
            if slots[time] is None:
                slots[time] = job_id
                profit += job_profit
                result.append(job_id)
                break
    return result,profit
n = int(input("Enter number of jobs: "))

jobs = []
for i in range(n):
    job_id = input(f"Enter Job ID {i+1} (e.g., J1): ")
    deadline = int(input(f"Enter deadline for {job_id}: "))
    profit = int(input(f"Enter profit for {job_id}: "))
    jobs.append((job_id, deadline, profit))

result, profit = JobSchedule(jobs)
print("Order of jobs done:", result)
print("Total Profit:", profit)
