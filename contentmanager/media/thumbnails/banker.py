def comparefunc(need, work):
    for i in range(0, len(need)):
        if need[i] > work[i]:
            return False
    return True


def CheckFinished(finished):
    for i in range(0, len(finished)):
        if finished[i] == False:
            return True
    return False


print("<---------Resources--------->")
m = 0
m = int(input('enter number of resources:'))
totalresources = []
for i in range(0, m):
    r = int(input(f'enter number of instances for {i}:'))
    totalresources.append(r)
print("<---------Processes--------->")
n = 0
n = int(input('enter number of processes:'))
allocations = []
Max = []
Needs = []
Finished = []
for i in range(0, n):
    allocation = []
    for j in range(0, m):
        a = int(input(
            f'enter number of allocated instances of {j} resource for {i} process:'))
        allocation.append(a)
    allocations.append(allocation)
    Finished.append(False)

for i in range(0, n):
    M = []
    for j in range(0, m):
        a = int(input(
            f'enter number of maximum instances of {j} resource for {i} process:'))
        M.append(a)
    Max.append(M)

for i in range(0, n):
    Need = []
    for j in range(0, m):
        n = Max[i][j]-allocations[i][j]
        Need.append(n)
    Needs.append(Need)
available = []
for i in range(0, m):
    unused = 0
    used = 0
    for j in range(0, len(allocations)):
        used = used+allocations[j][i]
        print(used)
    unused = totalresources[i]-used
    available.append(unused)
work = available[:]
print('allocation', allocations)
print('needs', Needs)
print('work', work)
while CheckFinished(Finished):
    for i in range(0, len(allocations)):
        if comparefunc(Needs[i], work) and Finished[i] == False:
            used = Max[i]
            print(f'selected process {i}')
            for j in range(0, len(work)):
                work[j] = work[j]+allocations[i][j]
            Finished[i] = True
