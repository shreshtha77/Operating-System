#sjf non preemptive
def sjf_non_preemptive(processes):
    n = len(processes)
    # Sort processes by their arrival time and burst time
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))

    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0

    print("Non-Preemptive SJF Scheduling:")
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        waiting_time = max(0, current_time - process['arrival_time'])
        turnaround_time = waiting_time + process['burst_time']
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        print(f"{process['id']}\t\t{process['arrival_time']}\t\t{process['burst_time']}\t\t{waiting_time}\t\t{turnaround_time}")
        current_time += process['burst_time']

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

# Example usage:
if __name__ == "__main__":
    processes = [
        {'id': 1, 'arrival_time': 0, 'burst_time': 6},
        {'id': 2, 'arrival_time': 2, 'burst_time': 8},
        {'id': 3, 'arrival_time': 3, 'burst_time': 7},
        {'id': 4, 'arrival_time': 4, 'burst_time': 3}
    ]

    sjf_non_preemptive(processes)
