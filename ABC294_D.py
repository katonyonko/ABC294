import io
import sys

_INPUT = """\
6
4 10
1
1
3
2 1
1
2 3
3
1
2 2
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop, heappush
  N,Q=map(int,input().split())
  called=[0]*N
  visited=[0]*N
  nxt_call=0
  h=[]
  for i in range(Q):
    event=input().split()
    if event[0]=='1':
      called[nxt_call]=1
      heappush(h,nxt_call)
      while nxt_call<N and called[nxt_call]==1: nxt_call+=1
    elif event[0]=='2':
      visited[int(event[1])-1]=1
    else:
      while True:
        x=heappop(h)
        if visited[x]==0:
          heappush(h,x)
          print(x+1)
          break