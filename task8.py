money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
grow = 1.05
delta = salary - spend
month = 0
while money_capital + delta >= spend:
    money_capital += delta
    spend = spend * grow

    month += 1


print(month)
