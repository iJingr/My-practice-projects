# student_info = [
#     {'姓名':'小明', '年龄':17, '数学分数':80.5, '语文分数':90.0},
#     {'姓名':'小王', '年龄':17, '数学分数':91.5, '语文分数':83.5},
#     {'姓名':'小福', '年龄':17, '数学分数':92.5, '语文分数':75.0}
#     ]
#
# for i in student_info:
#     sum = 0
#     for j in i:
#         print(type(i.get(j)))
#         print(i.get(j))
#     #     if type(j) == float:
#     #         print()
#     #
#     #
#     # print()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = {}
for i in strs:
    sorted_i = ''.join(sorted(i))
    if sorted_i not in d:
        d[sorted_i] = []
    d[sorted_i].append(i)
print(list(d.values()))
print(type(d.values()))



