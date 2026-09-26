# 保存学生数据到 JSON 文件、从 JSON 文件读取学生数据、JSON 数据与 Student 对象之间转换
import json
import student

FILE_PATH = 'student.json'


def upload_data(stu_info):
    data = []
    for n in stu_info:
        data.append({
            'name':n.name,
            'age':n.age,
            'm_score':n.m_score,
            'c_score':n.c_score
        })
    with open(FILE_PATH, 'w', encoding='utf-8') as up_file:
        json.dump(data, up_file, ensure_ascii=False, indent=2)



def download_data():
    with open(FILE_PATH, 'r', encoding='utf-8') as stu_json:
        stu_info = json.load(stu_json)

        stus = []
        for n in stu_info:
            stus.append(student.Student(n['name'], n['age'], n['m_score'], n['c_score']))
            # print(stus)
    return stus



