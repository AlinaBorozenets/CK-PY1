money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
r = 1.05
d = salary - spend
month = 0
while money_capital + d > spend:
    money_capital += d
    spend = spend * r
    if money_capital + d == spend:
     break
    month += 1



print(month)
