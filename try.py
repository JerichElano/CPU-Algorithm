def sjf_algorithm(processes, arrival_time, burst_time):
    # Get the number of processes
    n = len(processes)

    # Initialize lists for waiting time and turnaround time
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Create a copy of burst time to track remaining time
    remaining_time = list(burst_time)

    # Initialize the current time
    current_time = 0

    # Iterate through all processes
    for _ in range(n):
        # Initialize variables to find the next job
        min_remaining_time = float('inf')
        next_job = None

        # Find the next job to execute
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] < min_remaining_time:
                min_remaining_time = remaining_time[i]
                next_job = i

        # If no job is found, move to the next time unit
        if next_job is None:
            current_time += 1
            continue

        # Calculate waiting time for the selected job
        waiting_time[next_job] = current_time - arrival_time[next_job]

        # Update current time and turnaround time for the selected job
        current_time += burst_time[next_job]
        turnaround_time[next_job] = waiting_time[next_job] + burst_time[next_job]

        # Mark the job as completed by setting remaining time to infinity
        remaining_time[next_job] = float('inf')

    # Print the results in a tabular format
    print("Process\tArrival Time\tBurst Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Initialize lists for processes, arrival times, and burst times
processes = []
arrival_time = []
burst_time = []

# Gather user input for the SJF algorithm
print("Shortest Job First Algorithm")
user_input = int(input("Enter the number of processes: "))

for i in range(user_input):
    process_name = input(f"Enter the name of process {i + 1}: ")
    processes.append(process_name)

    process_arrival_time = int(input(f"Enter the arrival time for {process_name}: "))
    arrival_time.append(process_arrival_time)

    process_burst_time = int(input(f"Enter the burst time for {process_name}: "))
    burst_time.append(process_burst_time)

# Execute the SJF algorithm with user-provided input
sjf_algorithm(processes, arrival_time, burst_time)