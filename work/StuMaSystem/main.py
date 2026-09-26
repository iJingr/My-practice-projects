# 程序启动、用户交互、程序启动时加载学生数据、调用学生管理模块完成对应功能
import manager
import student
import file_utils



if __name__ == '__main__':

    stu_info = file_utils.download_data()
    stus = manager.Manager(stu_info)

    print(f'\t|学生成绩管理系统|\t')
    print('________________________')
    print(' |\t1、查询学生信息\t   |')
    print(' |\t2、修改学生信息\t   |')
    print(' |\t3、添加学生\t       |')
    print(' |\t4、删除学生\t       |')
    print(' |\t5、查看所有学生信息  |')
    print(' |\t6、退出\t\t       |')

    choose = int(input("请用数字表示您想进行的操作："))
    while choose != 6:
        # 查询
        if choose == 1:
            count = 0
            name = input('请输入您想查询的学生姓名：')
            for n in stu_info:
                count += 1
                if name == n.name:
                    print('请稍等...')
                    stus.index(name)
                    break
            if count == len(stu_info):
                print('没有这名学生的信息')
            choose = int(input("请用数字表示您想进行的操作："))

        # 修改
        elif choose == 2:
            info = input('请输入您想要修改的信息（姓名/年龄/数学成绩/语文成绩）：')
            if info in ("姓名", "年龄", "数学成绩", "语文成绩"):
                if info == '姓名':
                    info_01 = input('您想更改谁的姓名：')
                    for i in stu_info:
                        if info_01 == i.name:
                            info_02 = input('请输入更改后的名字：')
                            stus.update_name(info_01, info_02)
                            break
                    else:
                        print("查无此人！")

                elif info == '年龄':
                    info_01 = input('您想更改谁的年龄：')
                    for i in stu_info:
                        if info_01 == i.name:
                            info_02 = input('请输入更改后的年龄：')
                            stus.update_age(info_01, info_02)
                            break
                    else:
                        print("查无此人！")

                elif info == '数学成绩':
                    info_01 = input('您想更改谁的数学成绩：')
                    for i in stu_info:
                        if info_01 == i.name:
                            try:
                                info_02 = float(input('请输入更改后的数学成绩：'))
                                stus.update_m_score(info_01, info_02)
                                break
                            except ValueError as e:
                                print(f'输入有误：{e}')
                                break
                    else:
                        print("查无此人！")

                elif info == '语文成绩':
                    info_01 = input('您想更改谁的语文成绩：')
                    for i in stu_info:
                        if info_01 == i.name:
                            try:
                                info_02 = float(input('请输入更改后的语文成绩：'))
                                stus.update_c_score(info_01, info_02)
                                break
                            except ValueError as e:
                                print(f'输入有误：{e}')
                                break
                    else:
                        print("查无此人！")
            else:
                print('该项目不属于修改项!')
            choose = int(input("请用数字表示您想进行的操作："))

        # 添加
        elif choose == 3:
            name = input('您想添加的学生姓名：')
            age = int(input('您想添加的学生年龄：'))
            m_score = float(input('您想添加的学生数学分数：'))
            c_score = float(input('您想添加的学生语文分数：'))
            # 通过Student类创建新的学生对象，将对象的方式传入参数给Manager类
            stus.add(student.Student(name, age, m_score, c_score))
            # stus.add(name, age, m_score, c_score)
            choose = int(input("请用数字表示您想进行的操作："))

        # 删除
        elif choose == 4:
            name = input('请输入您要删除的学生：')
            stus.delete_info(name)
            choose = int(input("请用数字表示您想进行的操作："))

        # 查看所有学生信息
        elif choose == 5:
            for n in stu_info:
                student.Student.info_print(n)
            choose = int(input("请用数字表示您想进行的操作："))


