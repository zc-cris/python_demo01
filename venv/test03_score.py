
score = int(input("请输入你的成绩："))

if score > 90:
    print("优秀")
elif score > 80:
    print("良好")
elif score > 70:
    print("普通")
elif score > 60:
    print("及格")
else:
    print("重考")