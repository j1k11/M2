'''
Напишіть програму, яка починається з читання номіналу банкноти у користувача. 
Потім ваша програма повинна відобразити ім'я фізичної особи, 
яке фігурує на банкноті введеної суми. 
Відповідне повідомлення про помилку має відображатися, 
якщо такої банкноти немає.


'''
# Словник, що містить номінали банкнот та відповідні імена фізичних осіб
banknote_names = {
    1: "Леся Українка",
    2: "Іван Франко",
    5: "Тарас Шевченко",
    10: "Михайло Грушевський",
    20: "Григорій Сковорода",
    50: "Володимир Великий",
    100: "Богдан Хмельницький"
}

# Зчитування номіналу банкноти від користувача
nominal = int(input("Введіть номінал банкноти: "))

# Перевірка, чи існує введений номінал у словнику
if nominal in banknote_names:
    person_name = banknote_names[nominal]
    print(f"На банкноті номіналом {nominal} гривень зображено: {person_name}.")
else:
    print("Помилка: Немає банкноти з таким номіналом.")
