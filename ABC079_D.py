from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="079"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  #dijkstra
  from heapq import heappop,heappush
  def Dijkstra(G,s):
    done=[False]*len(G)
    inf=10**20
    C=[inf]*len(G)
    C[s]=0
    h=[]
    heappush(h,(0,s))
    while h:
      x,y=heappop(h)
      if done[y]:
        continue
      done[y]=True
      for v in G[y]:
        if C[v[1]]>C[y]+v[0]:
          C[v[1]]=C[y]+v[0]
          heappush(h,(C[v[1]],v[1]))
    return C
  H,W=map(int,input().split())
  C=[list(map(int,input().split())) for _ in range(10)]
  G=[[(C[j][i],j) for j in range(10)] for i in range(10)]
  distance=Dijkstra(G,1)
  ans=0
  for i in range(H):
    a=list(map(int,input().split()))
    for j in range(W):
      if a[j]!=-1:
        ans+=distance[a[j]]
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])