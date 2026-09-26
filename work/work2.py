'''
1、类与对象应用-设计Student学生类：
    属性：姓名（字符串类型）、年龄（整数类型）、数学成绩（浮点类型）以及语文成绩（浮点类型）
2、方法封装：
    方法：计算学生总成绩、计算学生平均成绩、根据平均成绩判断学生等级、输出学生完整信息
    等级评定与作业一相同
    要求将原本直接操作学生数据的代码封装到类的方法中，提高代码复用性和可维护性。
3、对象集合管理：
    使用列表保存多个学生对象，实现对学生信息的统一管理。
    创建学生对象列表，通过索引访问指定学生对象
    修改某一位学生的成绩信息，修改后重新计算该学生的总成绩、平均成绩以及成绩等级，输出更新后的学生信息

'''
# from tkinter.font import names


class Student:
    def __init__(self, name, age, m_score, c_score):
        self.name = name
        self.age = age
        self.m_score = m_score
        self.c_score = c_score

    def score_sum(self):
        sum = self.m_score + self.c_score
        return sum

    def score_average(self):
        ave = self.score_sum() / 2
        return ave


    def level_judge(self):
        if self.score_average() > 90:
            level = 'A'
            return level
        elif self.score_average() > 80 and self.score_average() < 89:
            level = 'B'
            return level
        elif self.score_average() > 70 and self.score_average() < 79:
            level = 'C'
            return level
        elif self.score_average() > 60 and self.score_average() < 69:
            level = 'D'
            return level
        else:
            level = 'F'
            return level

    def print_this(self):
        print(f'姓名:{self.name} 年龄:{self.age} 数学成绩:{self.m_score} 语文成绩:{self.c_score} 总成绩:{self.score_sum():.1f} 平均成绩:{self.score_average():.1f} 评级:{self.level_judge()}')

if __name__ == '__main__':
    stu_info = [
        Student('小张', 21, 56.9, 78.3),
        Student('小虎', 22, 66.6, 78.8),
        Student('小白', 21, 89.9, 93.2)
    ]

    for stu in stu_info:
        stu.print_this()

    name = input("输入需要修改的学生姓名(小张/小白/小虎)：")
    for s in stu_info:
        if s.name == name:
            info = input("输入需要修改的信息(年龄/数学成绩/语文成绩)：")
            for i in info:
                if i == "数":
                    new_m_score = float(input("请输入修改后的分数："))
                    s.m_score = new_m_score
                elif i == "语":
                    new_c_score = type(input("请输入修改后的分数："))
                    new_c_score = float(input("请输入修改后的分数："))
                    s.c_score = new_c_score
                elif i == "年":
                    new_age = int(input("请输入修改后的年龄："))
                    s.age = new_age
            s.print_this()
            break
        else:
            continue

