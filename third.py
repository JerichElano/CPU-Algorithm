def calculate_turnaround_waiting_time(jobs, arrival_times, burst_times): #this function is for FCFS algorithm
    n = len(jobs)
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n

    completion_times[0] = burst_times[0]
    for i in range(1, n):
        if arrival_times[i] > completion_times[i - 1]:
            completion_times[i] = arrival_times[i] + burst_times[i]
        else:
            completion_times[i] = completion_times[i - 1] + burst_times[i]

    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    return turnaround_times, waiting_times

def sjf_solver(jobs, arrival_times, burst_times):
    n = len(jobs)

    # Initialize lists for waiting times and turnaround times
    waiting_times = [0] * n
    turnaround_times = [0] * n

    #Create a copy of burst times to track remaining time
    remaining_time = list(burst_times)

    #Initialize the current time
    current_time = 0

    #Iterate through all processes
    for _ in range(n):
        #Initialize variables to find the next job
        min_remaining_time = float('inf')
        next_job = None

        #Find the next job to execute
        for i in range(n):
            if arrival_times[i] <= current_time and remaining_time[i] < min_remaining_time:
                min_remaining_time = remaining_time[i]
                next_job = i

        #If no job is found, move to the next time unit
        if next_job is None:
            current_time += 1
            continue
        #Calculate waiting time for the selected job
        waiting_times[next_job] = current_time - arrival_times[next_job]

        #Update current time and turnaround time for the selected job
        current_time += burst_times[next_job]
        turnaround_times[next_job] = waiting_times[next_job] + burst_times[next_job]

        #Mark the job as completed by setting remaining time to infinity
        remaining_time[next_job] = float('inf')

    return jobs, arrival_times, burst_times, waiting_times, turnaround_times

def ordinal_suffixes(j): #for ordinal suffixes 
    ordinal_suffixes = ['st', 'nd', 'rd'] + ['th'] * j
    ordinality = []
    for i in range(j+1): #it starts with "0th" so we need to add 1 to j
        if i % 10 in (1, 2, 3) and not i in (11, 12, 13):
            ordinality.append(f"{i}{ordinal_suffixes[i % 10 - 1]}")
        elif i in (11, 12, 13):
            ordinality.append(f"{i}{ordinal_suffixes[3]}")
        else:
            ordinality.append(f"{i}{ordinal_suffixes[3]}")

    return ordinality

def main():
    jobs = []
    arrival_times = []
    burst_times = []
    tupol = []
    print("=====================================================")
    print("Welcome to the Process Scheduling Simulator")
    print("=====================================================")
    
    valid = False
    while valid == False:
        process = input("What process scheduling algorithm would you like to use? (FCFS, SJF, RR): ")
        process = process.upper()
        if process in ["FCFS", "SJF", "RR"]:
            valid = True
        else:
            print("Invalid input, please try again.")

    print("=====================================================")        

    j = int(input("Enter number of processes: ")) #Improve this part by adding a try and except
    ordinal = ordinal_suffixes(j)

    if process == "FCFS":
        for i in range(j):
            job = input(f"Enter {ordinal[i+1]} job name: ")
            arrival = int(input(f"Enter arrival time for the job {job}: "))
            burst = int(input(f"Enter burst time for the job {job}: "))
            tupol.append((job, arrival, burst))
            
        tupol.sort(key = lambda x: x[1]) #for sorting our array "tupol"

        jobs = [t[0] for t in tupol] #this sellect items from the tuple and put it inside an array
        arrival_times = [t[1] for t in tupol]
        burst_times = [t[2] for t in tupol]

        turnaround_times, waiting_times = calculate_turnaround_waiting_time(jobs, arrival_times, burst_times)

    elif process == "SJF":
        for i in range(j):
            jobs.append(input(f"Enter {ordinal[i+1]} job name: "))
            arrival_times.append(int(input(f"Enter arrival time for the job {jobs[-1]}: ")))
            burst_times.append(int(input(f"Enter burst time for the job {jobs[-1]}: ")))

        jobs, arrival_times, burst_times, waiting_times, turnaround_times = sjf_solver(jobs, arrival_times, burst_times)

    print("\n   Job\t|   AT\t|   BT\t|  TAT\t|   WT")
    for i in range(j):
        print(f"    {jobs[i]}\t|   {arrival_times[i]}\t|   {burst_times[i]}\t|   {turnaround_times[i]}\t|   {waiting_times[i]}")


main()