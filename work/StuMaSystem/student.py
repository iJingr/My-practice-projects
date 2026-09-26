class Student():

    # 计算学生总成绩、计算学生平均成绩、根据平均成绩判断学生等级、输出学生完整信息

    def __init__(self, name, age, m_score, c_score):
        self.name = name
        self.age = age
        self.m_score = float(m_score)
        self.c_score = float(c_score)

    def score_sum(self):
        return self.c_score + self.c_score

    def score_average(self):
        return self.score_sum() / 2

    def level_judge(self):
        if self.score_average() >= 90:
            return "A"
        elif self.score_average() >= 80:
            return "B"
        elif self.score_average() >= 70:
            return "C"
        elif self.score_average() >= 60:
            return "D"
        else:
            return "F"

    def info_print(self):
        print(
            f'姓名:{self.name} 年龄:{self.age} 数学成绩:{self.m_score:.1f} 语文成绩:{self.c_score:.1f} 总成绩:{self.score_sum():.1f} 平均成绩:{self.score_average():.1f} 评级:{self.level_judge()}')


