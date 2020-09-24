def bestfit(blocks,b,process,p):
    allocation_array=[]
    for i in range(0,p):
        allocation_array.append(-1)
    for i in range(0,p):
        bestfit=-1
        for j in range(0,b):
            if blocks[j]>=process[i]:
                if bestfit==-1:
                    bestfit=j
                elif blocks[bestfit]>blocks[j]:
                    bestfit=j
        if bestfit!=-1:
            allocation_array[i]=bestfit
            blocks[bestfit]=blocks[bestfit]-process[i]    
    return allocation_array

            



m=input("number of blocks: ")
b=int(m)
blocks=[]
for i in range(0,b):
    k=input(f"{i+1 } block size: ")
    blocks.append(int(k))
n=input("number of process: ")
p=int(n)
process=[]
for j in range(0,p):
    k=input(f"{j+1 } process size: ")
    process.append(int(k))
assignment=[]
assignment=bestfit(blocks,b,process,p)
for i in range(0,p):
    if assignment[i]==-1:
        bl="Not Allocation_arrayated"
        print(f"Process {i+1} has block {bl}")
    else:
        print(f"Process {i+1} has block {assignment[i]+1}")

