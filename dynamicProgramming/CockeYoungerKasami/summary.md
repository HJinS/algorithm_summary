## CockeYoungerKasami(CYK) 알고리즘

특정한 **문자열**에 대해, 그 문자열이 **문맥 자유 문법**에 속하는지를 판다하고, 어던 방식으로 생성되는지를 판단하는 파싱 알고리즘

> 문맥 자유 문법
> Context-free grammar **형식문법**의 한 종류로, 생성 규칙이 다음과 같은 문법을 의미한다.
> $V \rightarrow \omega$
> $V$: 비말단(비종결자) 기호
> $\omega$: 비말단과, 말단 기호들로 구성된 문자열
> 생성 규칙의 좌측에는 단 하나의 비말단 기호만 관계한다.
>
>> 문맥 자유 문법 G는 $G = (V, \sum, R, S)$의 순서쌍으로 정의된다.
>> $V$: **비말단 기호**의 유한집합 -> {S, NP, VP, PP, Noun, Verb ...}
>> $\sum$: **말단 기호**의 유한집합, $V$와는 서로소이다. -> {I, am, he, go, school, literally...}
>>
>>> 말단 기호는 이름 그대로, 문법 규칙에서 화살표 왼쪽에 올 수 없다.($V \rightarrow eat$로 변환은 가능하지만 반대는 안된다.)
>>>
>>
>> $R$: $V$에서 $(V \cup \sum)^*$로 연결되는 **문법규칙**의 유한집합이다.
>> $S$: $V$의 원소, **시작 기호**를 가리킨다.
>>

- 기존적으로 CYK알고리즘에서는 *촘스키 정규 형식*으로 표현된 *문맥 자유 문법*을 사용하지만, 모든 *문맥 자유 문법*은 *촘스키 정규 형식*으로 변환이 가능하기 때문에 CYK 알고리즘을 사용 할 수 있다.
- 문자열의 길이가 n일때 CYK알고리즘은 $\theta(n^3)$의 시간복잡도를 가진다.
  - 현재 모든 문맥 자유 분법을 파싱 할 수있는 가장 효율적인 알고리즘이다.
  - CYK 알고리즘보다 효율적으로 동작하는 몇몇 알고리즘이 있지만, 그 알고리즘은 특정한 문법의 경우에만 사용이 가능하다.

### Chomsky Normal Form(촘스키 정규형)

일반 CFG에서는 화살표 오른쪽에 여러 개의 비말단 기호와 말단 기호들이  들어갈 수 있다.
예시 $VP \rightarrow NP have ADV PP$
하지만 *Chomsky Normal From*에서는 오직 두가지 유형의 문법 규칙만 갖는다.

- 화살표 오른쪽에 오직 두개의 *nonterminals*
- 화살표 오른쪽에 오직 하나의 *terminal*

```python

# Python implementation for the
# CYK Algorithm
 
# Non-terminal symbols
non_terminals = ["NP", "Nom", "Det", "AP",
                  "Adv", "A"]
terminals = ["book", "orange", "man",
             "tall", "heavy",
             "very", "muscular"]
 
# Rules of the grammar
R = {
     "NP": [["Det", "Nom"]],
     "Nom": [["AP", "Nom"], ["book"],
             ["orange"], ["man"]],
     "AP": [["Adv", "A"], ["heavy"],
            ["orange"], ["tall"]],
     "Det": [["a"]],
     "Adv": [["very"], ["extremely"]],
     "A": [["heavy"], ["orange"], ["tall"],
           ["muscular"]]
    }
 
# Function to perform the CYK Algorithm
# w - input string
def cykParse(w):
    n = len(w)

    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
  
    # Filling in the table
    # 전체 iteration
    # 상향식 파싱 - 입력 문장으로부터 문법 기호 S 방향으로 진행
    for j in range(0, n):
        # Iterate over the rules
        # lhs - left-hand side
        # 문법 규칙의 rhs를 lhs로 대체하는 과정의 반복
        for lhs, rule in R.items():
            # rhs - right-hand side
            for rhs in rule:
                # If a terminal is found
                # terminal - 말단 기호
                # rhs가 w의 어디에 있는지
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)
        # 파싱 위치부터 0까지 내려감
        for i in range(j, -1, -1):  
            # Iterate over the range i to j + 1
            # 다시 그 위치에서 파싱 위치로 올라감
            for k in range(i, j + 1):  
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:   
                        # If a terminal is found
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
    # If word can be formed by rules of given grammar
    if len(T[0][n-1]) != 0:
        print("True")
    else:
        print("False") 

    # Driver Code
# Given string
w = "a very heavy orange book".split()
 
# Function Call
cykParse(w)
```
