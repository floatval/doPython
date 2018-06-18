#! /usr/bin/env python3
# encoding: utf-8


import csv
import json
import copy
import collections


RESULT = collections.OrderedDict()
CIVILIZATION = collections.OrderedDict()


def get_row_count():
    """
    获得cvs文件的行数
    """
    with open('history.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        row_count = sum(1 for row in csvreader)
        return row_count


def get_local_num():
    """获得地区的代码"""
    i = 0
    country_code = []
    num_list = []
    with open('history.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for count in range(get_row_count()):
            row = next(csv_reader)
            space = row.count('')
            if space == 0:
                RESULT[row[0]] = ''
                continue
            if i == 0 and space == 1:
                country_code.append(row[1])
                i += 1  # 不同计数对应不同地区
            elif space == 1:
                country_code.append(row[1])
                i += 1
            num_list = range(1, i)
        return num_list, country_code


def get_local_civ(num_list, country_code):
    """获得地区的文明成就"""
    # 初始化所需数据结构，及标识
    local_num = 0
    civ_arch = []
    country = ''
    origin = []
    # serializers_dict = []

    with open('history.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for count in range(get_row_count()):
            row = next(csv_reader)
            if row[0] != '':
                for civ in row:
                    origin.append(civ)
                civ_type = copy.deepcopy(row[0])
                CIVILIZATION[row[1]] = row[2:]
            space = row.count('')

            # 获取地区, 每次地区变化时清空上次保存的内容
            if row[1] != '' and row[0] == '':
                saveVar = copy.deepcopy(civ_arch)
                CIVILIZATION[country_code[local_num - 1]] = saveVar
                if row[1] != country and row[1] != '':
                    civ_arch.clear()
                    local_num += 1  # 切换地区代码
                    country = row[1]  # 获取地区名称，并保存

            # 获得各地区的文明成就
            if space == 1 and row[0] == '':
                for arch in row:
                    if arch != '' and arch != row[1]:
                        civ_arch.append(arch)
                    CIVILIZATION[country_code[local_num - 1]] = civ_arch
            elif space == 2 and row[0] == '':
                for arch in row:
                    if arch != '' and arch != row[1]:
                        civ_arch.append(arch)
                    CIVILIZATION[country_code[local_num - 1]] = civ_arch
            elif space == 3 and row[0] == '':
                for arch in row:
                    if arch != '' and arch != row[1]:
                        civ_arch.append(arch)
                    # saveVar = copy.deepcopy(civ_arch)
                    # print(saveVar)
                CIVILIZATION[country_code[local_num - 1]] = civ_arch
                RESULT[civ_type] = CIVILIZATION
    # serializers_dict.append(CIVILIZATION)
    return RESULT


# def find(key):
#     """实现查找功能"""
#     with open('test.json', 'r') as f:
#         dic = json.load(f)
    # print(dic)
    # print(dic.get('非洲'))


# find('a')

if __name__ == '__main__':
    with open('test.json', "w") as json_file:
        num_list, country_code = get_local_num()
        data = get_local_civ(num_list, country_code)
        json.dump(data, json_file, ensure_ascii=False)
