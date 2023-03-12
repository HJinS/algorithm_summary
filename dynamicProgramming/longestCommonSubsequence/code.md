## 동적 계획법을 위한 풀이 코드

### LCS길이 계산

수열 $X[1\dots m]$, $Y[1\dots n]$를 입력 받아 모든 $1 \leq i \leq m$와 $1 \leq j \leq n$에 대해 $X[1\dots i]$와 $Y[1\dots j]$사이의 값에 대해 LCS를 연산하고, C[i, j]에 저장한다.
C[m, n]는 X, Y에 대한 LCS값을 가지게 된다.

```python
from typing import List

input_x = ['X', 'M', 'J', 'Y', 'A', 'U', 'z']
input_y = ['M','Z','J','A','W','X','U']
m = len(x)
n = len(y)
c: List[List] = [[0 for i in range(n)] for j in range(m)]
def lcs_length(x: List, y: List):
    for i in range(m):
        c[i][0] = 0
    for j in range(n):
        c[0][j] = 0
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[m-1][n-1]
```

### 하나의 LCS 읽어들이기

**백트래킹**을 이용하여 표를 연산한다.

1. 접두사의 마지막 문자들이 같을 경우
   - 그들(접두사의 마지막 문자들)은 한 LCS에 존재해야 한다.
2. 그렇지 않는 경우
   - %x_i%와 $y_j$쌍에서 무엇이 가장 큰 LCS를 갖는지 판단하고, 같은 선택을 다시 한다.
   - 같은 길이를 갖는다면 하나를 선택하면 된다.

```python
from typing import List

def backtrack(c: List[List], x: List, y: List, i: int, j: int):
    if i == 0 or j == 0:
        return ""
    if x[i] == y[j]:
        return backtrack(c, x, y, i-1, j-1) + x[i]
    if c[i][j-1] > c[i-1][j]:
        return backtrack(c, x, y, i, j-1)
    return backtrack(c, x, y, i-1, j)
```

### 모든 LCS 읽어들이기

$x_i$와 $y_j$가 같은 길이의 결과를 반환한다면, 결과적으로 나오는 부분수열을 둘 다에서 읽어들인다.
두 문자열이 미슷하면 거으 ㅣ모든 단계에서 가지를 뻗어 나갈 수 있으므로, 이 함수는 다항함수가 아님에 유의
C를 **백트레킹**하기에 완선된 C가 필요하다(길이 정보)

```python
from typing import List
def backtrack_all(c: List[List], x: List, y: List, i: int, j: int) -> set:
    if i == 0 or j ==0:
        return {""}   
    if x[i] == y[j]:
        return {z + x[i] for z in backtrack_all(c, x, y, i-1, j-1)}
    r = set()
    if c[i][j-1] >= c[i-1][j]:
        r = r | backtrack_all(c, x, y, i, j-1)
    if c[i-1][j] >= c[i][j-1]:
        r = r | backtrack_all(c, x, y, i-1, j)
    return r
```

### diff 출력하기

C를 백트래킹하여 두 수열간의 diff를 출력한다.
C를 **백트레킹**하기에 완선된 C가 필요하다(길이 정보)

> 아래의 코드에서 $\geq$와 $<$를 $>$와 $\leq$로 바꾸면 결과가 달라짐에 주의 할 것

```python
from typing import List

def print_diff(c: List[List], x: list, y: List, i: int, j: int) -> None:
   if i >= 0 and j >= 0 and x[i] == y[j]:
      print_diff(c, x, y, i-1, j-1)
      print("  " + x[i])
   elif j > 0 and (i == 0 or c[i][j-1] >= c[i-1][j]):
      print_diff(c, x, y, i, j-1)
      print("+ " + y[j])
   elif i >= 0 and (j == 0 or c[i][j-1] < c[i-1][j]):
      print_diff(c, x, y, i-1, j)
      print("- " + x[i])
   else:
      print("")

```

### 최적화
대부분의 실제 세계의 사례에서는, 특히 diff 패치들에서, 파일의 시작과 끝은 거의 바뀌지 않고, 동시에 변하는 것 또한 일어나지 않는다.
몇개의 항목만이 수열의 중간에서 변했다면 시작과 끝은 제거해도 된다.

```python
from typing import List

input_x = ['X', 'M', 'J', 'Y', 'A', 'U', 'z']
input_y = ['M','Z','J','A','W','X','U']
m = len(input_x)
n = len(input_y)
def lcs(x: List, y: List):
    start = 0
    m_end = m-1
    n_end = n-1
    
    while start <= m_end and start <= n_end and x[start] == y[start]:
        start += 1
        
    while start <= m_end and start <= n_end and x[m_end] == y[n_end]:
        m_end -= 1
        n_end -= 1

    # 차이가 있는 부분만 돌기 위해
    # while 특성 상 조건 확인 -> 코드 수행 이기 때문에 start-1, end+1로 범위 조정 필요
    c: List[List] = [[0 for i in range(start-1, n_end+2)] for j in range(start-1, m_end+2)]

    index_diff_x = m - (m_end + 2 - (start - 1))
    index_diff_y = n - (n_end + 2 - (start - 1))
    
    for i in range(start, m_end+1):
        for j in range(start, n_end+1):
            if x[i] == y[j]:
                c[i-index_diff_x][j-index_diff_y] = c[i-1-index_diff_x][j-1-index_diff_y] + 1
            else:
                c[i-index_diff_x][j-index_diff_y] = max(c[i-index_diff_x][j-1-index_diff_y], c[i-1-index_diff_x][j-index_diff_y])
    return c[m-1-index_diff_x][n-1-index_diff_y]
```