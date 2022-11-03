salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
r = 1.03

need_money = 0
for i in range (0, months):
    i = spend - salary
    spend = spend * r
    need_money += i



print(round(need_money))
