"""
实现逻辑门
其中涉及到了 Python 中的 MRO(method resolution order)
的理解以及　super 的用法
"""

#! /usr/bin/env python3
# encoding: utf-8


class LogicGate:
    """
    逻辑门的所有共性
    """

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        """
        获取标签
        """
        return self.label

    def getOutput(self):
        # 此处是用了继承的，作用是执行所有类型的逻辑门
        # 且所有的逻辑门类中都要有逻辑执行(performGateLogic) 函数
        self.output = self.performGateLogic()  # 此处若检查到语法错误,请忽略
        return self.output


class BinaryGate(LogicGate):
    """
    二输入一输出的门
    """

    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        """
        获取逻辑门中的引脚Ａ的输入状态
        """
        if self.pinA is None:
            return int(input("请输入逻辑门引脚A的输入（0/1）" + self.getLabel() +
                             "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        """
        获取逻辑门中的引脚Ｂ的输入状态
        """
        if self.pinB is None:
            return int(input("请输入逻辑门引脚B的输入（0/1）" + self.getLabel() +
                             "-->"))
        else:
            return self.pinB.getFrom().getOutput()


class UnaryGate(LogicGate):
    """单输入单输出的门"""

    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        """
        获取逻辑门的引脚输入
        """
        return int(input("请输入逻辑门引脚的输入(0/1)" + self.getLabel() +
                         "-->"))


class AndGate(BinaryGate):
    """
    与门
    """

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        """
        逻辑门执行
        """
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """
    或门
    """

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        """
        逻辑门执行
        """
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NorGate(UnaryGate):
    """
    非门
    """

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        """
        逻辑门执行
        """
        a = self.getPin()
        if a == 0:
            a = 1
            return a
        else:
            a = 0
            return a


class Connector:
    """
    逻辑组合门
    """

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def get_from(self):
        """
        输入门
        """
        return self.fromgate

    def get_to(self):
        """
        输出门
        """
        return self.togate

    def setNextPin(self, soruce):
        """
        接入引脚
        """
        if self.pinA is None:
            self.pinA = soruce
        else:
            if self.pinB is None:
                self.pinB = soruce
            else:
                raise RuntimeError("Error: 无空引脚")


g1 = AndGate("G-And")
print(g1.getOutput())
print(type(g1).__mro__)
g2 = OrGate("G-Or")
print(g2.getOutput())
g3 = NorGate("G-Nor")
print(g3.getOutput())
c1 = Connector(g1, g2)
print(type(c1).__mro__)
# print(c1)
# c2 = Connector(g1, g3)
# print(c2)
# c3 = Connector(g2, g3)
# print(c3)
