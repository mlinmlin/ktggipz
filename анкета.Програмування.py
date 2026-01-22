


#Знаходимо ім'я
name = input("Ваше ім'я: ")
surname = input("Ваша фамілія: ")
age = input("Ваш вік: ")
 
country = input("Ваша країна: ")

city = input("Ваше місто: ")

has_profession = input("Ви працюєте?: ")
if  has_profession =="Так":
    profession =input("Ким саме? ")
else:
    print("Зрозуміло")
    
hobby = input("Ваші хобі: ")

book = input("Ваша улюблена книга: ")

eyes = input("Ваш колір очей: ")

film = input("Ваш улюблений фільм: ")
 
dish = input("Ваша улюблена страва: ")

height = input("Ваш зріст: ")

colour = input("Ваш улюблений колір")

pets = input("Чи є у вас домашні улюбленці")

print("\n--- Анкета ---")
print(f"Ім'я: {name}")
print(f"Ваша фамілія: {surname}")
print(f"Ваше хобі: {hobby}")
print(f"Ваша улюблена книга: {book}")
print(f"Очі: {eyes}")
print(f"Ваш улюблений фільм: {film}")
print(f"Ваша улюблена страва: {dish}")
print(f"Ваш зріст: {height}")
print(f"Ваш улюблений колір: {colour}")
print(f"Ваші домашні улюбленці: {pets}")
print(f"Вік: {age}")
print(f"Місто: {city}")
if country =="УкраЇна":
        print("Ви українець")
else:
    print("Ви іноземець")

if has_profession == "Так":
   print(profession)
else:
    print("Ви безробітні")
