# 어떻게 해야 반복되는 글자들끼리 묶을 수 있을까?
# output => asdfa
input_str = 'asdfaasdfaasdfaasdfa'

def solutions(input_str):

    # 일단 부여받은 len(str)의 약수들을 모두 구해봤다.
    div = []
    for i in range(1, len(input_str) + 1):
        if len(input_str) % i == 0:
            div.append(i)

    # 그리고 나서는 각 약수들까지를 슬라이싱을 해서 패턴이 될만한 str들을 모았다.
    sliced = []
    for j in div:
        sliced.append(input_str[0:j])

    # 약수들과 각 부품들을 딕셔너리로 묶었다. 이때, key와 value의 곱은 len(input_str)이 되게 묶었다.
    dic = dict(zip(div[::-1], sliced))

    # key와 value의 곱이 input_str와 같은 경우를 찾아, 그 value를 반환했다.
    for k,p in dic.items():
        if k*p == input_str:
            return p
print(solutions(input_str))

