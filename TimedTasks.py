import datetime
import time

# 获取当天日期作为初始的开始执行日期
exeDate = (datetime.datetime.now()).strftime('%Y-%m-%d')

# 设置程序最早执行时间/最晚执行时间，程序每天会在这个时间范围内开始运行一次
# 最早执行时间
startTIme = datetime.time(0, 5)
# 最晚执行时间
endTime = datetime.time(22, 20)

dividingLineStr = '================================='

while True:
    # 获取当前时间
    currentTime = datetime.datetime.now().time()
    # 获取当前日期
    currentDate = (datetime.datetime.now()).strftime('%Y-%m-%d')

    print('当前时间为 ' + currentDate + ' ' + str(currentTime))
    print('计划任务将在 ' + exeDate + ' ' + str(startTIme) + '至' + str(endTime) + ' 之间运行执行')
    print(dividingLineStr)

    if (exeDate <= currentDate) and (startTIme <= currentTime <= endTime):
        # 下述位置填入你需要执行的代码

        # 上述位置填入你需要执行的代码

        print('计划任务成功执行')
        print(dividingLineStr)
        # 成功执行一次之后执行日期改为下一天
        exeDate = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    else:
        # 轮询可以自行调整，推荐不超过（endTime-startTIme）
        time.sleep(20)
