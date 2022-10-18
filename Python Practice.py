x = [1, 2, 3, 4]


# output = [24,12,8,6]
# Product_of_Array_Except_Self
def solution(x):
    final = []
    input0 = x.copy()
    for i in range(len(input0)):
        locals()['input%d' % i] = input0.copy()

    for j in range(len(input0)):
        del locals()['input%d' % j][j]

    for k in range(len(input0) + 1):
        final.append(eval('*'.join([str(n) for n in locals()['input%d' % k]])))
    return final


print(solution(x))

'''
일단 함수에 들어갈 리스트를 요소의 개수만큼 복사하여 다른 변수들로 지정한다.
그리고 나서 요소의 개수만큼 각 index에 del을 진행한다. 
del을 하고 남은 리스트를 eval함수를 이용해서 내부 곱을 구한다.
구한 곱들을 final에 append한다.
'''
