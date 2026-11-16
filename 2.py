def fcfs(processes):
    # processes: list of [name, arrival_time, burst_time]
    order = sorted(processes, key=lambda p: (p[1], int(p[0][1:])))
    time = 0
    rows = []
    gantt = []
    for name, at, bt in order:
        if time < at:
            gantt.append(("Idle", time, at))
            time = at
        start = time
        time += bt
        ct = time
        tat = ct - at
        wt = tat - bt
        rows.append((name, at, bt, ct, tat, wt))
        gantt.append((name, start, ct))
    show_results("FCFS", rows, gantt)


def sjf_preemptive(processes):
    # Preemptive SJF / Shortest Remaining Time First
    n = len(processes)
    names = [p[0] for p in processes]
    arrival = [p[1] for p in processes]
    burst = [p[2] for p in processes]
    remaining = burst[:]
    completion = [0] * n
    time = 0
    completed = 0
    timeline = []
    while completed < n:
        ready = [i for i in range(n)
                 if arrival[i] <= time and remaining[i] > 0]
        if not ready:
            next_arrival = min(arrival[i] for i in range(n)
                               if remaining[i] > 0)
            timeline.append(("Idle", time, next_arrival))
            time = next_arrival
            continue
        idx = min(ready, key=lambda i: (remaining[i], arrival[i], i))
        if timeline and timeline[-1][0] == names[idx] and timeline[-1][2] == time:
            timeline[-1] = (names[idx], timeline[-1][1], time + 1)
        else:
            timeline.append((names[idx], time, time + 1))
        remaining[idx] -= 1
        time += 1
        if remaining[idx] == 0:
            completion[idx] = time
            completed += 1
    rows = []
    for i in range(n):
        tat = completion[i] - arrival[i]
        wt = tat - burst[i]
        rows.append((names[i], arrival[i], burst[i], completion[i], tat, wt))
    show_results("SJF (Preemptive SRTF)", rows, timeline)


def show_results(title, rows, gantt):
    print("\n" + title + " Scheduling Results")
    print("-" * 66)
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for name, at, bt, ct, tat, wt in sorted(rows, key=lambda r: int(r[0][1:])):
        print(f"{name}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
    print("-" * 66)
    print(f"Average Waiting Time : {sum(r[5] for r in rows) / len(rows):.2f}")
    print(f"Average Turnaround Time : {sum(r[4] for r in rows) / len(rows):.2f}")
    print("\nGantt Chart:")
    print(" | ".join(f"{name} ({start}-{end})" for name, start, end in gantt))


def main():
    n = int(input("Enter number of processes (at least 4): "))
    if n < 4:
        print("Please enter at least 4 processes.")
        return
    processes = []
    for i in range(n):
        print(f"\nProcess P{i + 1}")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        if at < 0 or bt <= 0:
            print("Arrival time must be >= 0 and burst time must be > 0.")
            return
        processes.append((f"P{i + 1}", at, bt))
    while True:
        print("\nMENU")
        print("1. FCFS Scheduling")
        print("2. SJF (Preemptive SRTF) Scheduling")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            fcfs(processes)
        elif choice == "2":
            sjf_preemptive(processes)
        elif choice == "3":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()