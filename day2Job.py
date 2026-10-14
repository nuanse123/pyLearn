# 定义分数并作判断
score = 75

if score >= 90:
    print('优秀')
elif score >= 60:
    print('及格')
else:
    print('不及格')

# for循环打印1-20
for num in range(1,21):
    print('当前是',num)
    if num % 3 == 0:
        print(num,'能被3整除')