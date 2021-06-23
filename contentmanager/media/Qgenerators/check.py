import random

f=open('check.txt','r')
line=f.readline()

print(line)

line=line.split(";")
i=0
st=line[0]
for c in st:
    if c=="$":
        r=line[i+1]
        s=st.split("$",1)
        r=r.split(',')
        rand=random.randint(int(r[0]),int(r[1]))
        s=s[0]+str(rand)+s[1]
        st=s
        i=i+1
print(st) 
    