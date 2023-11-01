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
    j = int(input("Enter number of processes: "))
    ordinal = ordinal_suffixes(j)


    for i in range(j):
        job = input(f"Enter {ordinal[i+1]} job name: ")
        arrival = int(input(f"Enter arrival time for the job {job}: "))
        burst = int(input(f"Enter burst time for {job}: "))
        tupol.append((job, arrival, burst))

    tupol.sort(key = lambda x: x[1]) #for sorting our array "tupol"
    print(tupol)

    jobs = [t[0] for t in tupol] #this sellect items from the tuple and put it inside an array
    arrival_times = [t[1] for t in tupol]
    burst_times = [t[2] for t in tupol]

    print(arrival_times)
    print(burst_times)

    turnaround_times, waiting_times = calculate_turnaround_waiting_time(jobs, arrival_times, burst_times)

    print("\nJob\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time")
    for i in range(j):
        print(f"{jobs[i]}\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")


main()