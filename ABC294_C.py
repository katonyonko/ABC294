import io
import sys

_INPUT = """\
6
4 3
3 14 15 92
6 53 58
4 4
1 2 3 4
100 200 300 400
8 12
3 4 10 15 17 18 22 30
5 7 11 13 14 16 19 21 23 24 27 28
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  C=sorted(A+B)
  ans={C[i]:i+1 for i in range(N+M)}
  print(*[ans[A[i]] for i in range(N)])
  print(*[ans[B[i]] for i in range(M)])