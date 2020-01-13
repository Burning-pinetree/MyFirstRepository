Money = 100
SaveMoney = 0
GetMoney = 0
while 1:
    Action = int(input("请输入您要选择的操作：查询余额请按0，存钱请按1，取钱请按2，退出请按3"))
    if Action == 0:
        print("您目前的余额为%d:" % Money)
    elif Action == 1:
        SaveMoney = int(input("请输入要存钱的数目并存钱:"))
        Money += SaveMoney
        print("您目前的余额为%d:" % Money)
    elif Action == 2:
        GetMoney = int(input("请输入要取出钱的数目并取钱:"))
        Money -= GetMoney
        print("您目前的余额为%d:" % Money)
    else:
        break
