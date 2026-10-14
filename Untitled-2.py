word = "подземелье"
print(word[0])
print(word[1])
print(word[-1])
print(word[-2])

print(word[0:3])
print(word[3:6])
print(word[3:])
print(word[:3])

print(len(word))

text = "  Ты ЗАШЁЛ в тёмный ЛЕС  "
print(text.lower())
print(text.strip())

print(text.replace("тёмный", "светлый"))

text2 = "гоблин гоблин дракон гоблин"
print(text2.find("гоблин"))
print(text2.count("гоблин"))

command = "взять меч"
parts = command.split()
print(parts[0])
print(parts[1])

user_input = input()
user_input = user_input.lower().strip()
words = user_input.split()
if len(words) == 0:
    print("Ты ничего не сказал.")
else:
    action = words[0]
    if action == "взять":
        print("Ты берёшь предмет.")
    elif action == "идти":
        print("Ты идёшь.")
    elif action == "осмотреть":
        print("Ты осматриваешься.")
    else:
        print("Я не понял.")