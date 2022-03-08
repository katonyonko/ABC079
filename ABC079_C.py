from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="079"
#問題
problem="c"

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
  X=list(input())
  X=[int(X[i]) for i in range(4)]
  A,B,C,D=X
  for i in range(2):
    for j in range(2):
      for k in range(2):
        tmp=A
        if i==0: tmp+=B
        else: tmp-=B
        if j==0: tmp+=C
        else: tmp-=C
        if k==0: tmp+=D
        else: tmp-=D
        if tmp==7:
          ans=(i,j,k)
  s=['+','-']
  print(A,s[ans[0]],B,s[ans[1]],C,s[ans[2]],D,'=7',sep='')
  """ここから上にコードを記述"""

  print(test_case[__+1])