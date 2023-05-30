from PIL import Image
d = {1: "1.jpg", 2: "2.jpg", 3: "3.jpg", 4: "4.jpg", 5: "a.jpg"}

print("1 - Новый год"
      " 2 - 23 февраля"
      " 3 - 8 марта"
      " 4 - День рождения"
      " 5 - День раковины")
q = int(input("Для получения открытки введите число - номер праздника : "))

filename = d[q]
with Image.open(filename) as img:
    img.load()

img.show()