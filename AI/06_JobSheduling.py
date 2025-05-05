n=int(input("Enter number of jobs: "))
jobs=[]

print("Enter job id, latest time slot to complete, and profit: ")
for i in range(n):
    job_id, latest_slot,profit=input().split()
    jobs.append((job_id, int(latest_slot), int(profit)))

jobs.sort(key=lambda x:x[2], reverse=True)
max_slot=max(job[1] for job in jobs)

slots=[False]*(max_slot+1)
result=[' ']*(max_slot+1)

total_profit=0

for job_id,latest_slot,profit in jobs:
    for t in range(latest_slot,0,-1):
        if not slots[t]:
            slots[t] =True
            result[t]=job_id
            total_profit+=profit
            break

print("Sheduled Jobs: ",end=" ")
for i in range (1,max_slot+1):
    if(slots[i]):
        print(result[i],end=" ")
print(f"\nTotal Profit: {total_profit}")