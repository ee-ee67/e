def bankers(allocation, maximum, available):
    n, m = len(allocation), len(available)
    need = [[maximum[i][j] - allocation[i][j] for j in range(m)]
            for i in range(n)]
    work = available[:]
    finish = [False] * n
    sequence = []

    print("Need Matrix:")
    for row in need:
        print(row)

    while len(sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + allocation[i][j] for j in range(m)]
                finish[i] = True
                sequence.append(i)
                found = True
        if not found:
            break

    if all(finish):
        print("System is in a SAFE state.")
        print("Safe sequence:", " -> ".join("P" + str(i) for i in sequence))
    else:
        print("System is in an UNSAFE state.")


if __name__ == "__main__":
    allocation = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
    maximum = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
    available = [3,3,2]
    bankers(allocation, maximum, available)