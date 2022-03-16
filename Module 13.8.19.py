# Модуль 13.8.19 Практика

'''------Блок констант и начальных значений-------'''
count_tic = int(input("Скока билетов берешь? "))
suma =0
price = list()

'''------Блок ввода данных о возресте человеков-----'''
age = [int(input("Возраст человека: ")) for i in range (count_tic)]

'''------Блок ввода данных о билетах человеков-----'''
for i in range (count_tic):
    if age [i]< 18:  price.append(0) 
    elif 18 <= age [i] <= 25:  price.append(990) 
    else:  price.append(1390)
    suma = sum(price)

'''------Блок вывода данных стоимости билетов человеков-----'''
if count_tic > 3:
    print("Сумма к оплате с учетом скидки 10%: ", suma*0.9)
else:
    print("Сумма к оплате без скидки 10%: ", suma)

'''print (age)
print (price)'''
