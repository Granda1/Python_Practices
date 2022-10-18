from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = ListNode(data)

node1 = ListNode(1)
node2 = ListNode(3)
node1.next = node2
head = node1


add(3)
add(1)

# node = head
# while node.next: #node.next =None이 아닐 경우. 즉, node의 next가 있는 경우 실행
#     print(node.data)
#     node=node.next #node의 next가 없을 때까지 반복
# print(node.data)






def isPalindrome(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.data)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

print(isPalindrome(head))













