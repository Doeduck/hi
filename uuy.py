height = float(input("請輸入您的身高（公尺）: "))
weight = float(input("請輸入您的體重（公斤）: "))
height = height/100
if height <= 0 or weight <= 0:
    print("身高和體重必須是正數。")
bmi = weight / (height ** 2)
print(f"您的 BMI 是: {bmi:.3f}")
# 判斷 BMI 範圍 (參考台灣衛福部標準)
if bmi < 18.5:
    print("體重過輕")
elif 18.5 <= bmi < 24:
    print("健康體重")
elif 24 <= bmi < 27:
    print("過重")
elif 27 <= bmi < 30:
    print("輕度肥胖")
elif 30 <= bmi < 35:
    print("中度肥胖")
else:
    print("重度肥胖")