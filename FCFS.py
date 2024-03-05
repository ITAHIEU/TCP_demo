def main():
    n = int(input("Enter number of processes: "))
    pid = [0] * n
    arrival_time = [0] * n
    burst_time = [0] * n
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    avg_waiting_time = 0
    avg_turnaround_time = 0
    #giai thích: tạo mảng toàn số 0 chứa độ dài n
    
    for i in range(n):
        print("Enter arrival time for process", i + 1, ": ", end="")
        arrival_time[i] = int(input())
        print("Enter burst time for process", i + 1, ": ", end="")
        burst_time[i] = int(input())
        pid[i] = i + 1

    for i in range(n):
        for j in range(n - (i + 1)):
            if arrival_time[j] > arrival_time[j + 1]:
                arrival_time[j], arrival_time[j + 1] = arrival_time[j + 1], arrival_time[j]
                burst_time[j], burst_time[j + 1] = burst_time[j + 1], burst_time[j]
                pid[j], pid[j + 1] = pid[j + 1], pid[j]

    for i in range(n):
        if i == 0:
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            if arrival_time[i] > completion_time[i - 1]:
                completion_time[i] = arrival_time[i] + burst_time[i]
            else:
                completion_time[i] = completion_time[i - 1] + burst_time[i]

        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        avg_waiting_time += waiting_time[i]
        avg_turnaround_time += turnaround_time[i]

    print("\nPID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(pid[i], "\t", arrival_time[i], "\t", burst_time[i], "\t", completion_time[i], "\t", turnaround_time[i], "\t", waiting_time[i])

    print("\nAverage waiting time:", avg_waiting_time / n)
    print("Average turnaround time:", avg_turnaround_time / n)


if __name__ == "__main__":
    main()
