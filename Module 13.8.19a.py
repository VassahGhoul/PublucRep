# Модуль 13.8.19a Практика

'''------Блок констант и начальных значений-------'''
suma =None
tax = 0.1
age = list()
price = list()
count_tic = int(input("Скока билетов берешь? "))

'''------Блок ввода данных о возрасте человеков-----'''
for i in range (count_tic):
    print ("Введи возраст ", i+1, " человека")
    age.append(int(input()))
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
