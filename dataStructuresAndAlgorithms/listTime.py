"""
理解常见的列表生成方式之间
的运行时间的差别（时间复杂度）

总结在以下所有情况中，在最优时间复杂度下
执行速度最快的是list(range(1000))
其次是l = [i for i in range(1000)]

ps: 在数据量较小时比如1k执行速度最快的是
    append = l.append

    for i in range(1000):
        append(i)
"""


#! /usr/bin/env python3
# encoding: utf-8

from timeit import Timer
import dis


def test1():
    """
    串联方式生成列表
    时间复杂度为O(n)
    n为数据数量
    这个可以理解为单链表的添加(通过指针)
    （python内部list的实现是PyObject **ob_item）
    假设空间足够，每次在首部添加了内容之后，添加内容之前的所有
    元素都有后移, 故效率不高
    """
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    """
    append方法生成列表
    时间复杂度为O(1)
    参照1中的信息，不过此处是从尾部直接添加
    不涉及元素的移动。故而时间复杂度为O(1)
    """
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    """
    列表解析生成列表
    时间复杂度是O(1)
    较第二种情况，此处少了一步寻址故虽然时间复杂度
    一样，单效率要较第二种情况好(参照最后的情况)
    """
    l = [i for i in range(1000)]


def test4():
    """
    通过列表结构体来生成列表
    时间复杂度是O(1)
    较第三种情况此种情况少了一次迭代
    故时间复杂度同上，但效率较高
    """
    l = list(range(1000))


def test5():
    """
    时间复杂度为O(n)
    数据量小的速度最快(测试数据为1k)
    数据量大的话速度不行(测试数据为10K)
    """
    l = []
    append = l.append

    for i in range(1000):
        append(i)


def test6():
    """
    时间复杂度同样为O(1)
    其余涉及科班内容
    本学渣不懂
    """
    l = []
    append = l.append
    any(map(append, range(1000)))


# 运行时间测试
t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("concat ", t2.timeit(number=10000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("concat ", t3.timeit(number=10000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("concat ", t4.timeit(number=10000), "milliseconds")
t5 = Timer("test5()", "from __main__ import test5")
print("concat ", t5.timeit(number=10000), "milliseconds")
t6 = Timer("test6()", "from __main__ import test6")
print("concat ", t6.timeit(number=1000), "milliseconds")


# 可以参照以下方式来通过把python反汇编为字节码来观察每种方式的区别
# dis模块可以参照官方文档，如果官方文档读起来吃力的话，可以参照
# https://www.rddoc.com/doc/Python/3.6.0/zh/library/dis/
# 截止到2018.06.19 该文档为3.6.0版

# print(dis.dis(test1))
# print(dis.dis(test2))
# print(dis.dis(test3))
# print(dis.dis(test4))
# print(dis.dis(test5))
# print(dis.dis(test6))
