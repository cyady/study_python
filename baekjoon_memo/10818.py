N=int(input())
mylist=list(map(int, input().split()))
rlist=list(mylist[0:N])
MIN = min(rlist)
MAX = max(rlist)
# print(mylist, rlist)
print(MIN, MAX)
