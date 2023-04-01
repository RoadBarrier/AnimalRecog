import os


def menu():  # 绘制主页菜单
    print("*************************")
    print("*    欢迎使用动物识别系统   *")
    print("*      1.查看规则库       *")
    print("*      2.新增规则         *")
    print("*      3.修改规则         *")
    print("*      4.删除规则         *")
    print("*      5.进行识别         *")
    print("*      6.退出系统         *")
    print("*在功能中输入数字0可以返回主页*")
    print("*************************")


def ReadRules(rulefile):  # 查看
    fp = open(rulefile, 'r', encoding='UTF-8')
    try:
        lines = fp.readlines()  # 全部规则
    finally:
        fp.close()
    rulelist = []

    for line in lines:  # 单条规则
        rule_line = line.split(",")  # 切割特征和结论
        condition = rule_line[0:-1]  # 除了最后一个都是特征
        result = rule_line[-1][:-1]  # 最后一个是结论，最后一个字符是\n
        condition.append(result)  # 重新组合成列表
        rulelist.append(condition)
    j = 1
    for i in rulelist:
        print(j, ":", i[0:-1], i[-1])  # 输出 j是序号
        j += 1
        if j == len(rulelist) + 1: break

    os.system('pause')


def NewRule(rulefile):  # 新规则
    fp = open(rulefile, 'r', encoding='UTF-8')
    lines = fp.readlines()  # 全部规则
    fp.close()
    print("请按格式输入规则：{条件1,条件2,条件3,条件4,...,结论}")
    new_rule = input()

    if (new_rule == '0'):
        return
    try:
        lines.append(new_rule + '\n')  # 全部规则+新规则
        fp = open(rulefile, 'w', encoding='UTF-8')
        fp.writelines(lines)
    finally:
        # print(lines)
        fp.close()
    print("添加成功")
    os.system('pause')


def ConfigRule(rulefile):  # 改规则
    fp = open(rulefile, 'r+', encoding='UTF-8')
    lines = fp.readlines()
    fp.close()
    print("请选择要修改的规则（输入规则序号）：")
    ruleno = input()  # 输入序号
    if (ruleno == '0'): return
    ruleno = int(ruleno) - 1
    print("所选规则为：", lines[ruleno])  # 展示规则
    print("请按格式输入规则：{条件1,条件2,条件3,条件4,...,结论}")
    new_rule = input()
    if (new_rule == '0'): return
    lines[ruleno] = new_rule + '\n'  # 覆盖该条规则
    fp = open(rulefile, 'w+', encoding='UTF-8')
    fp.writelines(lines)
    fp.close()
    print('修改完成')
    os.system('pause')


def DelRule(rulefile):  # 删规则
    fp = open(rulefile, 'r+', encoding='UTF-8')
    lines = fp.readlines()
    fp.close()
    print("请选择要删除的规则（输入规则序号）：")
    ruleno = input()
    if (ruleno == '0'): return
    ruleno = int(ruleno) - 1
    print("所选规则为：", lines[ruleno])
    print("注意！您确定要删除吗？(Y/N)")
    checkDel = input()  # 二次确认
    if (checkDel == 'N'):
        print("已取消删除")
    if (checkDel == 'Y'):
        print('已删除所选规则：', lines.pop(ruleno))  # pop掉该条
        fp = open(rulefile, 'w+', encoding='UTF-8')
        fp.writelines(lines)
        fp.close()

    os.system('pause')


def RegcStart(rulefile):
    fp = open(rulefile, 'r', encoding='UTF-8')
    lines = fp.readlines()
    fp.close()
    rule = []
    result = []
    for line in lines:  # 单条规则
        temp = line.split(",")  # 切割
        rule.append(temp[0:-1])  # 分开保存
        result.append(temp[-1][0:-1])
    # print(rule)
    # print(result)

    print("请按格式输入特征：{特征1,特征2,特征3,特征4,...}")
    temp = input()
    characters = temp.split(',')  # 切割成列表
    # print(characters)
    # print(temp.split(','))
    # print(characters)
    count = 0
    while 1:
        if set(characters).issuperset(set(rule[count])):  # 特征 是 规则 母集
            characters.append(result[count])  # 更新特征
            # print(characters)
        count += 1
        if count >= len(rule):  # 没了
            break
    # del characters[-1]  # 去除列表最后的空项
    if characters != temp.split(','):
        print("最后匹配到的规则结论为：", characters[-1])  # 输出最后一个项
    else:
        print("找不到匹配规则")
    print('\n\n**如果不能匹配到特定动物，请检查规则库是否含有该动物的规则，或是特征与规则字眼上的差别')

    os.system('pause')


if __name__ == '__main__':
    rulefile = 'rules.txt'
    while (1):
        menu()
        selections = input()
        if (selections == '1'): ReadRules(rulefile)
        if (selections == '2'): NewRule(rulefile)
        if (selections == '3'): ConfigRule(rulefile)
        if (selections == '4'): DelRule(rulefile)
        if (selections == '5'): RegcStart(rulefile)
        if (selections == '6'): exit()
