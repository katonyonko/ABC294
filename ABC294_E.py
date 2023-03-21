import io
import sys

_INPUT = """\
6
8 4 3
1 2
3 2
2 3
3 1
1 4
2 1
3 3
10000000000 1 1
1 10000000000
1 10000000000
1000 4 7
19 79
33 463
19 178
33 280
19 255
33 92
34 25
19 96
12 11
19 490
33 31
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  L,N1,N2=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(N1)]
  B=[list(map(int,input().split())) for _ in range(N2)]
  ans=0
  n1,n2=0,0
  amari=[0,0]
  while n1<N1 or n2<N2:
    if amari[1]==0:
      if A[n1][0]==B[n2][0]: ans+=min(A[n1][1],B[n2][1])
      if A[n1][1]-B[n2][1]>0: amari=[A[n1][0],A[n1][1]-B[n2][1]]
      else: amari=[B[n2][0],A[n1][1]-B[n2][1]]
      n1+=1;n2+=1
    elif amari[1]>0:
      if amari[0]==B[n2][0]: ans+=min(amari[1],B[n2][1])
      if amari[1]>B[n2][1]: amari=[amari[0],amari[1]-B[n2][1]]
      else: amari=[B[n2][0],amari[1]-B[n2][1]]
      n2+=1
    else:
      if amari[0]==A[n1][0]: ans+=min(-amari[1],A[n1][1])
      if -amari[1]>A[n1][1]: amari=[amari[0],amari[1]+A[n1][1]]
      else: amari=[A[n1][0],amari[1]+A[n1][1]]
      n1+=1
  print(ans)