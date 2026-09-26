# 添加学生、删除学生、修改学生成绩、查询学生信息、查看所有学生信息，使用列表保存 Student 对象，通过对象方法完成学生信息处理，修改学生信息后同步保存数据
import student
import file_utils

class Manager:

    def __init__(self, students):
        self.stus = students


    def index(self, name):
        for n in self.stus:
            if name == n.name:
                n.info_print()

    def add(self, stu):
        self.stus.append(stu)
        count = 0
        for n in self.stus:
            if stu.name == n.name:
                print('学生信息添加成功')
                break
            count += 1
            file_utils.upload_data(self.stus)
            if count == int(len(self.stus)):
                print('学生信息添加失败')

    def update_name(self, info_01, info_02):
        for n in self.stus:
            if info_01 == n.name:
                n.name = info_02
                file_utils.upload_data(self.stus)

    def update_age(self, info_01, info_02):
        for n in self.stus:
            if info_01 == n.name:
                try:
                    n['age'] = int(info_02)
                    file_utils.upload_data(self.stus)
                except ValueError:
                    print("年龄需要输入整数")

    def update_m_score(self, info_01, info_02):
        for n in self.stus:
            if info_01 == n['name']:
                if info_02 < 0 or info_02 > 100:
                    raise ValueError('分数不能大于100或者小于0')
                n['m_score'] = info_02
                file_utils.upload_data(self.stus)

    def update_c_score(self, info_01, info_02):
        for n in self.stus:
            if info_01 == n['name']:
                if info_02 < 0 or info_02 > 100:
                    raise ValueError('分数不能大于100或者小于0')
                n['c_score'] = info_02
                file_utils.upload_data(self.stus)


    def delete_info(self, info):
        for n in range(len(self.stus)):
            if info == self.stus[n].name:
                del self.stus[n]
                file_utils.upload_data(self.stus)




