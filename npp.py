def npp_formula(jobs, arrival_time, burst_time, priority):
    n = len(jobs)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_burst = list(burst_time)
    current_time = 0

    for i in range(len(jobs)):
        min_priority = float('inf')
        min_burst = float('inf')
        next_job = None

        #This will check which job should be processed first, based on their AT, BT, and P
        for i in range(len(jobs)):
            if arrival_time[i] <= current_time and remaining_burst[i] != float('inf') and priority[i] <= min_priority:
                #If it encounter a jobs with same priority, it will process a job base on the BT
                if remaining_burst[i] < min_burst:
                    min_burst = remaining_burst[i]
                    min_priority = priority[i]
                    next_job = i
                elif remaining_burst[i] > min_burst:
                    min_burst = remaining_burst[i - 1]
                    min_priority = priority[i - 1]
                    next_job = i

        #If there's no Job found it will add 1 to the current time
        if next_job is None:
            current_time += 1
            continue

        waiting_time[next_job] = current_time - arrival_time[next_job]

        current_time += burst_time[next_job]
        turnaround_time[next_job] = waiting_time[next_job] + burst_time[next_job]

        remaining_burst[next_job] = float('inf')

    return arrival_time, burst_time, priority, waiting_time, turnaround_time

def main():
    jobs = ["A", "B", "C", "D", "E"]
    arrival_time = [0, 0, 3, 5, 7]
    burst_time = [4, 2, 5, 2, 2]
    priority = [3, 2, 1, 1, 2]

    print("================================================")
    print("Welcome to the Non Preemptive Priority Simulator")
    print("================================================")
    '''
    for i in range(5):
        arrival_time.append(int(input(f"Enter arrival time for the job {jobs[i]}: ")))
        burst_time.append(int(input(f"Enter burst time for the job {jobs[i]}: ")))
        priority.append(int(input(f"Enter priority for the job {jobs[i]}: ")))
        print("")
    '''
    arrival_time, burst_time, priority, waiting_time, turnaround_time = npp_formula(jobs, arrival_time, burst_time, priority)

    print("------------------------------------------------")
    print("   Job\t|   AT\t|   BT\t|   P\t|  TAT\t|   WT")
    for i in range(len(jobs)):
        print(f"    {jobs[i]}\t|   {arrival_time[i]}\t|   {burst_time[i]}\t|   {priority[i]}\t|   {turnaround_time[i]}\t|   {waiting_time[i]}")
    print("------------------------------------------------")


main()