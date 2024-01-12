def npp_formula(jobs, arrival_time, burst_time, priority):
    n = len(jobs)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    remaining_priority = list(priority)
    current_time = 0
    min_burst = float('inf')

    for i in range(len(jobs)):
        min_priority = float('inf')
        next_job = None

        #This will check which job should be processed first, based on their AT, BT, and P
        for i in range(len(jobs)):
            if arrival_time[i] <= current_time and remaining_priority[i] <= min_priority:
                #If it encounter a jobs with same priority, it will process a job base on the BT
                if burst_time[i] > min_burst and remaining_priority[i] == min_priority:
                    continue
                min_burst = burst_time[i]
                min_priority = remaining_priority[i]
                next_job = i
                print(f"Job: {jobs[next_job]}{next_job}")
        print(f"Time: {current_time}")
        #If there's no Job found it will add 1 to the current time
        if next_job is None:
            current_time += 1
            continue

        waiting_time[next_job] = current_time - arrival_time[next_job]

        current_time += burst_time[next_job]
        turnaround_time[next_job] = waiting_time[next_job] + burst_time[next_job]

        remaining_priority[next_job] = float('inf')

        print(" ")

    return arrival_time, burst_time, priority, waiting_time, turnaround_time

def main():
    '''
    jobs = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    arrival_time = [0, 0, 12, 22, 7, 27, 17, 3, 32]
    burst_time = [8, 6, 7, 6, 4, 3, 7, 6, 4]
    priority = [5, 5, 3, 1, 1, 3, 2, 4, 1]
    
    jobs = ["A", "B", "C", "D", "E", "F", "G", "H"]
    arrival_time = [8, 3, 14, 0, 17, 5, 12, 0]
    burst_time = [8, 6, 9, 5, 8, 5, 8, 7]
    priority = [2, 3, 1, 4, 1, 3, 2, 4]
    '''
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
