#coding:utf-8

import mysql.connector
from colorama import Fore
from prettytable import PrettyTable
from check_categroy import check_cate_func

conn = mysql.connector.connect(user='root', password='root', database='yunnan')
cursor = conn.cursor()
conn.commit()
cursor.execute('select 问题序号, 网管名称, 解决方案分类, 解决方案问题细分 from question_categ_123 where `解决方案问题细分` !=""')
values = cursor.fetchall()

dict1 = {"室分工程": "室分工程-工程建设"}

dict2 = {"室分新建": "室分新建-需重新规划"}

dict3 = {
"室分整改":[
"室分整改-待输出方案或待审核（未出整改图纸）",
"室分整改-待输出方案或待审核（未提供原图纸，无法提供方案）",
"室分整改-已出方案待实施（20个天线以下）",
"室分整改-已出方案待确认（20个天线以上）",
"室分整改-施工与设计不符",
"室分整改-物业问题",
"室分整改-新增信源",
"室分整改-其他（需整改队介入进行排查）",
"室分整改-已出方案已实施（20个天线以下）",
"室分整改-已出方案已实施（20个天线以上）"
]
}

dict4 = {
"维护处理":[
"维护处理-物业协调困难未进行排查",
"维护处理-电梯内有天线",
"维护处理-电梯内无天线",
"维护处理-地埋线、密封吊顶等封闭处无法排查",
"维护处理-RRU故障或RRU数据未配置",
"维护处理-RRU未接入天馈系统、驻波等需要代维处理的问题点",
"维护处理-无源器件更换（可自行处理）",
"维护处理-未排查出问题（需要进一步排查）"
]
}

dict5 = {
"优化处理":[
"优化处理-用户少",
"优化处理-参数调整",
"优化处理-天馈调整",
"优化处理-外泄严重"
]
}

dict6 = {"其它": "其它-未归类"}
list1 = [dict1, dict2, dict3, dict3, dict4, dict5, dict6]

table = PrettyTable(["问题序号", "网管名称", "解决方案分类", "解决方案问题细分"])
check_fault_row = []

def main(list_table):
    for i in list_table:
        tmp1, tmp2 = [], []
        if check_cate_func(list1, i[2]) == False:  # check_cate_func(values[0][2])  返回列表-字典
            check_fault_row.append(tuple(
                [Fore.GREEN + i[0] + Fore.RESET, Fore.GREEN + i[1] + Fore.RESET, Fore.RED + i[2] + Fore.RESET,
                 Fore.RED + i[3] + Fore.RESET]))
            continue
        else:
            tmp1.append(check_cate_func(list1, i[2]))
            if i[3] not in tmp1[0]:  # 核查二级分类是否在字典三级分类中
                check_fault_row.append(tuple(
                    [Fore.GREEN + i[0] + Fore.RESET, Fore.GREEN + i[1] + Fore.RESET, Fore.GREEN + i[2] + Fore.RESET,
                     Fore.RED + i[3] + Fore.RESET]))

    for i in check_fault_row:
        table.add_row([x for x in i])

    print(table)

if __name__ == '__main__':
    main(values)

cursor.close()
conn.close()