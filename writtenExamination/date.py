#!/usr/bin/env python3
# encoding: utf-8


def returnDate(year, month, date):
    # 返回订单过期时间
    bigMonth = [1, 3, 5, 7, 8, 10, 12]  # 31天的月份
    if year % 4 == 0:  # 闰年情况
        if month == 1 and (date >= 29):  # 处理订单起始于1月的特殊情况
            month += 1
            date = 29
        elif date == 1 and (month == 2):  # 处理订单起始于2月1号的特殊情况
            month += 1
            date = 1
        elif date == 1 and (month not in bigMonth):  # 排除31天的月份
            month += 1
        elif date == 1 and (month in bigMonth):  # 31天的情况
            date = 31
        else:
            month += 1
        return year, month, date
    else:  # 非闰年情况
        if month == 1 and (date >= 29):  # 处理订单起始于1月的特殊情况
            month += 1
            date = 28
        elif date == 1 and (month == 2):  # 处理订单起始于2月1号的特殊情况
            month += 1
            date = 1
        elif date == 1 and (month not in bigMonth):  # 排除31天的月份
            month += 1
        elif date == 1 and (month in bigMonth):  # 31天的情况
            month += 1
            date = 31
        else:
            month += 1
        return year, month, date


if __name__ == '__main__':
    print(returnDate(2016, 10, 10))
    print(returnDate(2016, 3, 4))
    print(returnDate(2016, 3, 1))
    print(returnDate(2017, 1, 30))
    print(returnDate(2017, 2, 1))
