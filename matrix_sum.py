arr1 = [[1,2,3],[2,3,4],[100,101,12]]
arr2 = [[3,4,5],[5,6,7],[42,32,51]]



def solution(arr1, arr2):

    # 일단 여기서는 행렬 각 요소의 합을 구한다. 다만 그 정답은 각각 모두 리스트에 쌓여있다.
    each_listed_answer = []
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            each_listed_answer.append([arr1[i][j]+arr2[i][j]])

    # 여기서 이중리스트를 푼다.
    each_listed_answer = sum(each_listed_answer,[])

    # arr의 이중리스트 갯수만큼의 리스트를 만들고, 넣어준다. 다만 pop을 썼기에, 리스트의 순서도, 리스트 내의 순서도 모두 역방향이다.
    reversed_answer = []
    for k in range(len(arr1)):
        line = []
        for p in range(len(arr2[0])):
            line.append(each_listed_answer.pop(-1))
        reversed_answer.append(line)
    reversed_answer = reversed_answer[::-1]

    # 역방향인 reversed_answer를 모두 정방향으로 돌려줬다.
    final_answer = []
    for q in range(len(arr1)):
        final_answer.append(reversed_answer[q][::-1])

    return final_answer

# 일단 답을 내기는 했는 O(n**2)이므로 더 좋은 해결방안을 찾고 싶다.
print(solution(arr1,arr2))


# 근디 생각해보니 행렬 각 요소에 행렬 정보를 추가해주면 어떨까. 딕셔너리 key로는 행렬의 값을, value로는 자리 값을 다는 것이다.



