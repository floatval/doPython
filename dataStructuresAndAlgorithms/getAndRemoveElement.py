"""
通过递归,不使用其他数据结构和list的特性
实现栈的逆序输出
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return self.items[len(self.items)-1]

def iter(s):
    """
    弹出栈底元素
    """
    result = s.pop()
    if s.isEmpty():
        return result
    else:
        last = iter(s)
        s.push(result)
        return last


s3 = Stack()
s3.push(3)
s3.push(2)
s3.push(1)
while not s3.isEmpty():
    print(iter(s3))
