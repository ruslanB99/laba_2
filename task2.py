salary=5000
spend=6000
increase=0.03
months=10
money_capital=0
i=0
while i <= months-1:
    money_capital += spend - salary
    spend *= 1.03
    i += 1
    money_capital_=round(money_capital,2)
print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", money_capital_)