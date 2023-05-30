from PIL import Image
d = {1: "1.jpg", 2: "2.jpg", 3: "3.jpg", 4: "4.jpg", 5: "a.jpg"}

print("1 - С Днем Розетки"
      " 2 - С Днем ПТСР"
      " 3 - С Днем губки для посуды"
      " 4 - День рождения"
      " 5 - День котлет")
q = int(input("Для получения открытки введите число - номер праздника : "))

filename = d[q]
with Image.open(filename) as img:
    img.load()

img.show()