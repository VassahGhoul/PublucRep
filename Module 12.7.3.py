'''Итоговое задание  12.7.3 
 Нужный вариант нужно раскоментировать'''
 
# Ввод суммы вклада
money = int(input ("Введи сумму вклада: ")) 

#--------- исходные данные------------№
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} 

'''#---------Решение тупо в лоб -----------#
#        Формируем  список % ставок
deposit = list (per_cent.values ())             
#        Вычисляем % по вкладам 
deposit [0] = deposit [0] *money/100     
deposit [1] = deposit [1] *money/100
deposit [2] = deposit [2] *money/100
deposit [3] = deposit [3] *money/100 '''

#---------Решение умно в лоб -----------#
deposit = list(map(lambda x: x*money/100, per_cent.values ()))

'''#---------Решение по лбу-----------#
#           Формируем  список % ставок 
deposit = list (per_cent.values ())                  
#            Цикл по индексам списка, с Len
for  i in range(len(deposit)):                           
       deposit [i] = deposit [i] *money/100 '''   

# ---------------Вывод данных----------------#
print ("Полученный депозит: ", deposit)
deposit.sort()
print ("Отсортированный депозит: ", deposit)
print ("Максимальный депозит: ", max (deposit))
