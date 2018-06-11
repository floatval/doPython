"""
欧几里得求最大公约数算法
适用于分母为正的情况
算法思维如下：
gcd(a,b) = gcd(b,a mod b)
"""
#! /usr/bin/env python3
# encoding: utf-8


def gcd(m, n):
    while m % n != 0:
        oldM = m
        oldN = n
        m = oldN
        n = oldM % oldN
    return n


print(gcd(20, 10))
print(gcd(9, 5))
