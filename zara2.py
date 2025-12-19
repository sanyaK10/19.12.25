number = input("Введіть число:")
procent = input("Введіть відсоток:")
number = float(number)
procent = float(procent)
procentomore = procent % number
print(f"Відсоток:{procentomore}")