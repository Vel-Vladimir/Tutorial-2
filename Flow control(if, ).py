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


while var == -1:
    print("Inside while loop")
    var = 0
    # break
else:
    print("inside ELSE in while loop") # не выпониться когда внутри  цикла while или for сработал break

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
