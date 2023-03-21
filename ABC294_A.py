import io
import sys

_INPUT = """\
6
5
1 2 3 5 6
5
2 2 2 3 3
10
22 3 17 8 30 15 12 14 11 17
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  print(*[A[i] for i in range(N) if A[i]%2==0])