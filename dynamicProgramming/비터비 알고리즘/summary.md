## 비터비 알고리즘(Viterbi algorithm)
비터비 경로를 찾기 위한 동적 계획법 알고리즘
> Viterbi Path(비터비 경로)
> 은닉 마르코프 모형 등에서 관측된 사건들의 순서를 야기한 가장 가은성 높은 은깃 상태들의 순서

> Hidden Markov Model(은닉 마르코프)
> 통계적 마르코프 모형의 하나로, 시스템이 **은닉된 상태**와 **관찰가능한 결과**은 두가지 요소로만 구성된다고 보는 모델
> **관찰 가능한 결과**를 야기하는 직접적인 원인은 관측될 수 없는 **은닉상태**들이다.
> 그 *상태들이 마르코프 과정을 통해 도출된 결과*들만이 관찰될 수 있기 때문에 은닉이라는 단어가 붙게 됐다.
>> 마르코프 연쇄와 같은 단순한 마르코프 모형에서는 상태를 관찰자가 직접적으로 볼 수 있으며, 그러므로 상태가 전이될 확류은 단순히 모수(parameter)로 표현 될 수 있다.

> 마르코프 연쇄
> 이산 시간 확률 과정이다.
> 시간에 따른 계의 상태의 변화를 나타낸다.


### 예시
모든 마을 주민이 **건강(Healthy)**하거나 **열(Fever)**이 나는 두가지 상태만 있는 마을이 있다고 하자.
이 마을에서 오직 마을 의사 만이 각자가 열이 나는지 아닌지를 판단 할 수 있다.
의사는 환자들에게 몸 상태가 어던지 질문하여 열의 유무를 진단한다.
마을 사람들은 멀쩡하다(normal), 어지럽다(dizzy)중에서 하나의 답변 만을 답할 수 있다.

> 의사는 환자들의 건강 상태가 이산적인 마르코프 연쇄를 따른다고 생각한다. **Healthy**, **Fever** 두가지 상태가 존재하지만 의사는 이를 직접적으로 관찰 할 수 없고 숨겨져 있다. ->  은닉된 상태(Healthy, Fever)
> 하루에 한번 환자는 의사에게 자신의 건강 상태에 따라 Normal, Dizzy, Cold중 한가지를 이야기 할 수 있다. -> 관찰가능한 결과(Normal, Dizzy, Cold)

관측값(Normal, Cold, Dizzy)은 은닉 상태(Healthy, Fever)와 함꼐 은닉 마르코프 모형(HMM)을 구성한다.

```python
obs = ('normal', 'cold', 'dizzy')
states = ('Healthy', 'Fever')
# start_probability - 첫 방문시 어느 상태에 있는가에 대한 의사의 생각
start_p = {'Healthy': 0.6, 'Fever': 0.4}
# 마르코프 연쇄에 따른 건강 상태의 변화
# transition_probability
trans_p = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6}
}
# 이 규칙으로 은닉 값이 관찰가능한 상태(관측값)을 결정한다.
# emission_probability - 매 하루마다 환자가 자신의 몸 상태를 어떻게 느끼는지
emit_p = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
}
```

**환자는 3일간 연속으로 의사를 방문하였고, 의사는 첫날 환자가 "멀쩡하다"고 느꼈고, 이튿날 "춥다"고 느꼈으며, 셋째 날에는 "어지럽다"고 느꼈다는 것을 알게 되었다**
**환자가 설명한 관측값에 맞는 가장 가능성 높은 건강 상태의 순서는 무엇인가?**

```python
# Helps visualize the steps of Viterbi.
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)
    
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    # 0인 시각 초기화
    for y in states:
        print(y)
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
        print(V)
        print(path)
 
    # alternative Python 2.7+ initialization syntax
    # V = [{y:(start_p[y] * emit_p[y][obs[0]]) for y in states}]
    # path = {y:[y] for y in states}
 
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)

            V[t][y] = prob
            #print("gggg", path[state] + [y])
            #print("eeee", path[state], [y])
            newpath[y] = path[state] + [y]
            print("d",newpath)
        # Don't need to remember the old paths
        path = newpath
 
    print_dptable(V)
    

    
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])

def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
print(example())
```