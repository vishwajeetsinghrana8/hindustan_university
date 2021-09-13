def tabel():
    num = int(input("Enter the value:"))
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
        
        
def func2():
    var1 = int(input("Var1:"))
    var2 = int(input("Var2:"))
    
    var3 = var1 + var2
    print("Sum:",var3)
    
def func3(var1,var2):
    var3 = var1 ** var2
    
    print("Pow:",var3)
    
def func4():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))
    
    var3 = var1 * var2
    
    return var3