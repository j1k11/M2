'''
Тривалість місяця варіюється від 28 до 31 дня. 
У цій вправі ви створите програму, 
яка читає назву місяця від користувача у вигляді рядка. 
Тоді ваша програма повинна відображати кількість днів у цьому місяці.
Відобразіть «28 або 29 днів» для лютого, щоб зверталися до високосних років.

'''
# Зчитування назви місяця від користувача
month = input("Введіть назву місяця: ")

# Перевірка кількості днів у місяці і виведення результату
if month == "квітень" or month == "червень" or month == "вересень" or month == "листопад":
    days = 30
elif month == "лютий":
    days = "28 або 29"
else:
    days = 31

# Виведення результату
print(f"{month} має {days} днів.")
