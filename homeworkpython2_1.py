income = []
outcome = []
Balance = {}
FinalBalance = 0
for day in range(7):
    income = int(input("星期%d的收入：" %day))
    outcome = int(input("星期%d的支出："%day))
    print("星期%d的收入和支出分别是%d,%d" %(day,income,outcome))
    Balance[day] = income - outcome
    print("星期%d的结余是：%d" %(day, Balance[day]))
    FinalBalance += Balance[day]
print("最后的结余是%d" % FinalBalance)