# print(0 and "22")
# if True == 2:
#     print("Inside If")
# age = 12
# adult = True if age >= 18 else False
# print(adult)

# # Возьмем первый truly value
var = 0 or "" or -1
print("Var = ", var)
print(1 or 0 and 0) # 1
print((1 or 0) and 0) # 0

while True:
    print("Inside while loop")
    break
else:
    print("inside ELSE in while loop") # выпониться когда ни разу не выполнится цикл while или for

try:
    raise ValueError
except:
    print("Exception")
    # raise ValueError
else:
    print("else in try") # выпониться если не было исключения (exception)
finally:
    print("File closed 1") # выпониться всегда

print("File closed 2")
