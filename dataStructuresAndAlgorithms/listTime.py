"""
理解常见的列表生成方式之间
的运行时间的差别（时间复杂度）
3 和 4 的时间复杂度不会计算
原谅我这个学渣……
"""
#! /usr/bin/env python3
# encoding: utf-8

from timeit import Timer


def test1():
    """
    串联方式生成列表
    时间复杂度为O(k)
    k为数据数量
    """
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    """
    append方法生成列表
    时间复杂度为O(1)
    """
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    """
    列表解析生成列表
    """
    l = [i for i in range(1000)]


def test4():
    """
    通过列表结构体来生成列表
    """
    l = list(range(1000))


# 运行时间测试
t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("concat ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("concat ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("concat ", t4.timeit(number=1000), "milliseconds")
