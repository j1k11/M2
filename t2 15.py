'''
Прийнято говорити, що один людський рік еквівалентний 7 собачим рокам.
Однак це просте перетворення не визнає, що собаки досягають дорослого 
віку приблизно через два роки. В результаті деякі люди вважають, 
що кожен з перших двох людських років краще вважати 10,5 собачими роками, 
а потім вважати кожен наступний людський рік 4 собачими роками.
Напишіть програму, яка реалізує переклад з людських років в собачі роки, 
описані в попередньому пункті. Переконайтеся,
що ваша програма працює правильно для конверсій менше двох людських років 
і для конверсій двох або більше людських років. Ваша програма повинна видавати 
відповідне повідомлення про помилку, якщо користувач вводить від'ємне число.

'''
# Зчитування віку людини від користувача
human_years = float(input("Введіть вік людини: "))

# Перевірка на від'ємне число
if human_years < 0:
    print("Введіть додатне число.")
else:
    # Розрахунок собачих років за вказаним віком людини
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 2 * 10.5 + (human_years - 2) * 4
    
    # Виведення результату
    print(f"Вік у собачих роках: {dog_years}")
