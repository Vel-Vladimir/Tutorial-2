# print(0 and "22")
# if True == 2:
#     print("Inside If")
# age = 12
# adult = True if age >= 18 else False
# print(adult)

# # Возьмем первый truly value
# var = 0 or "" or -1
# print("Var = ", var)
print(1 or 0 and 0) # 1
print((1 or 0) and 0) # 0

while True:
    int("a")
    print("Inside while loop")
    break
else:
    print("inside ELSE") # выпониться когда ни разу не выполнится цикл while или for

try:
    pass
except:
    pass
else:
    pass # выпониться когда ни разу не выполнится исключение (exception)