class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, data):
        prev_node = self.tail.prev
        new_node = Node(data)
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def selectNode(self, num):
        node = self.head.next
        cnt = 0
        while cnt < num:
            node = node.next
            cnt += 1
        return node

    def deleteNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        if next_node.data == -2:
            return [node, prev_node]
        else:
            return [node, next_node]

    def upNode(self, node, num):
        if node.data <= num:
            return self.head.next

        cnt = 0
        while cnt < num:
            node = node.prev
            cnt += 1

            if node.data == -1:
                node = node.next
                break
        return node

    def downNode(self, node, num, n):
        if node.data + num >= n:
            return self.tail.prev

        cnt = 0
        while cnt < num:
            node = node.next
            cnt += 1

            if node.data == -2:
                node = node.prev
                break
        return node

    def restoreNode(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = node
        next_node.prev = node


def solution(n, k, cmd):
    ans = ["O"] * n
    ll = LinkedList()
    for i in range(n):
        ll.insertNode(i)

    now = ll.selectNode(k)
    deleted = []
    move = 0
    for s in cmd:
        if len(s) > 1:
            c, num = s.split(" ")
            num = int(num)

            if c == "U":
                move -= num
            else:
                move += num

        else:
            if move < 0:
                now = ll.upNode(now, -move)
            elif move > 0:
                now = ll.downNode(now, move, n)
            move = 0

            if s == "C":
                del_node, now = ll.deleteNode(now)
                deleted.append(del_node)
            elif s == "Z":
                node = deleted.pop()
                ll.restoreNode(node)

    for node in deleted:
        ans[node.data] = "X"
    return "".join(ans)

