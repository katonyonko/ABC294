import io
import sys

_INPUT = """\
6
3 1 1
1 2
4 1
1 4
1 4
2 2 2
6 4
10 1
5 8
9 6
4 5 10
5 4
1 6
7 4
9 8
2 2
5 6
6 7
5 3
8 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_right
  N,M,K=map(int,input().split())
  taka=[list(map(int,input().split())) for _ in range(N)]
  aoki=[list(map(int,input().split())) for _ in range(M)]
  l,r=0,1
  for _ in range(100):
    x=(l+r)/2
    tmp=sorted([sum(aoki[i])*x-aoki[i][0] for i in range(M)])
    cnt=0
    for i in range(N):
      cnt+=bisect_right(tmp,taka[i][0]-sum(taka[i])*x)
    if cnt>=K: l=x
    else: r=x
  print(l*100)