import io
import sys

_INPUT = """\
6
5
1 2 3
1 3 6
1 4 9
4 5 10
4
2 2 3
2 1 5
1 3 1
2 1 5
7
1 2 1000000000
2 3 1000000000
3 4 1000000000
4 5 1000000000
5 6 1000000000
6 7 1000000000
3
2 1 6
1 1 294967296
2 1 6
1
1
2 1 1
8
1 2 105
1 3 103
2 4 105
2 5 100
5 6 101
3 7 106
3 8 100
18
2 2 8
2 3 6
1 4 108
2 3 4
2 3 5
2 5 5
2 3 1
2 4 3
1 1 107
2 3 1
2 7 6
2 3 8
2 1 5
2 7 6
2 4 7
2 1 7
2 5 3
2 8 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def EulerTour(G, s):
      depth=[-1]*len(G)
      depth[s]=0
      done = [0]*len(G)
      Q = [~s, s] # 根をスタックに追加
      parent=[-1]*len(G)
      ET = []
      left,right=[-1]*len(G),[-1]*len(G)
      while Q:
          i = Q.pop()
          if i >= 0: # 行きがけの処理
              done[i] = 1
              ET.append(i)
              for a in G[i][::-1]:
                  if done[a]: continue
                  depth[a]=depth[i]+1
                  parent[a]=i
                  Q.append(~a) # 帰りがけの処理をスタックに追加
                  Q.append(a) # 行きがけの処理をスタックに追加
          else: # 帰りがけの処理
              ET.append(i)
      for i in range(len(G)*2):
        if ET[i]>=0 and left[ET[i]]==-1: left[ET[i]]=i
        if ET[~i]<0 and right[~ET[~i]]==-1: right[~ET[~i]]=len(G)*2-i-1
      return ET, left, right, depth, parent #(right-left+1)//2がその頂点を含む部分木の大きさ

  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for w,y in G[x]:
        if D[y]>D[x]+w:
          D[y]=D[x]+w
          dq.append(y)
    return D

  N=int(input())
  G1=[[] for _ in range(N)]
  G2=[[] for _ in range(N)]
  edges=[]
  for i in range(N-1):
    u,v,w=map(int,input().split())
    u-=1; v-=1
    G1[u].append((w,v))
    G1[v].append((w,u))
    G2[u].append(v)
    G2[v].append(u)
    edges.append([u,v,w])
  ET, left, right, depth, parent = EulerTour(G2,0)
  D=bfs(G1,0)
  D2=[0]*(2*N)
  for i in range(N):
      D2[left[i]]=D[i]
      D2[right[i]]=D[i]

  #LCA(最小共通祖先)ここは準備
  class LCA_Tree:
      def __init__(self, G, s):
          self.G=G
          self.s=s

          def EulerTour(G, s):
              depth=[-1]*len(G)
              depth[s]=0
              done = [0]*len(G)
              Q = [~s, s] # 根をスタックに追加
              parent=[-1]*len(G)
              ET = []
              left=[-1]*len(G)
              while Q:
                  i = Q.pop()
                  if i >= 0: # 行きがけの処理
                      done[i] = 1
                      if left[i]==-1: left[i]=len(ET)
                      ET.append(i)
                      for a in G[i][::-1]:
                          if done[a]: continue
                          depth[a]=depth[i]+1
                          parent[a]=i
                          Q.append(~a) # 帰りがけの処理をスタックに追加
                          Q.append(a) # 行きがけの処理をスタックに追加
                  else: # 帰りがけの処理
                      ET.append(parent[~i])
              return ET[:-1], left, depth, parent
          self.S,self.F,self.depth,self.parent=EulerTour(self.G,0)
          self.INF = (len(self.G), None)
          self.M = 2*len(self.G)
          self.M0 = 2**(self.M-1).bit_length()
          self.data = [self.INF]*(2*self.M0)
          for i, v in enumerate(self.S):
              self.data[self.M0-1+i] = (self.depth[v], i)
          for i in range(self.M0-2, -1, -1):
              self.data[i] = min(self.data[2*i+1], self.data[2*i+2])

      #LCAの計算 (generatorで最小値を求める)
      def LCA(self, u, v):
        def _query(a, b):
            yield self.INF
            a += self.M0; b += self.M0
            while a < b:
                if b & 1:
                    b -= 1
                    yield self.data[b-1]
                if a & 1:
                    yield self.data[a-1]
                    a += 1
                a >>= 1; b >>= 1
        fu = self.F[u]; fv = self.F[v]
        if fu > fv:
            fu, fv = fv, fu
        return self.S[min(_query(fu, fv+1))[1]]

  class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    #合計にはrを含まない
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
    #pの位置をxという値にセット
    def set(self, p, x):
        self.add(p, -self.sum(p, p+1) + x)

  bit=BIT(2*N+2)
  for i in range(2*N):
      if i==0: bit.add(i+1,D2[i])
      elif i<2*N+1: bit.add(i+1,D2[i]-D2[i-1])
  lca=LCA_Tree(G2,0)
  Q=int(input())
  for i in range(Q):
      d,u,v=map(int,input().split())
      if d==1:
          u-=1
          x,y,z=edges[u]
          if parent[x]==y: p=x
          else: p=y
          bit.add(left[p]+1,v-edges[u][2])
          bit.add(right[p]+1,edges[u][2]-v)
          edges[u][2]=v
      else:
          u-=1; v-=1
          print(bit.sum(0,left[u]+2)+bit.sum(0,left[v]+2)-2*bit.sum(0,left[lca.LCA(u,v)]+2))