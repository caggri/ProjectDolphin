import random
#Initial state of x and y
x = 0
y = 0

x_max = 10
y_max = 6
def fullX(x,y):
    x = x_max
    return x, y

def fullY(x,y):
    y = y_max
    return x, y

def emptyX(x, y):
    x = 0
    return x, y

def emptyY(x, y):
    y = 0
    return x, y

def xToY(x,y):
    amount = x + y
    if amount >=6:
        y = 6
        x = amount - 6
    elif amount < 6:
        x = 0
        y = amount
    return x, y

def yToX(x,y):
    amount = x + y
    if amount >=10:
        x = 10
        y = amount - 10
    elif amount < 10:
        x = amount
        y = 0
    return x, y

def randomStep(x,y):
    allowed = ["fullX","fullY","emptyX","emptyY","xToY","yToX"]
    if x == x_max:
        allowed.remove("fullX")
    if y == y_max:
        allowed.remove("fullY")
    if x == 0:
        allowed.remove("emptyX")
        allowed.remove("xToY")
    if y == 0:
        allowed.remove("emptyY")
        allowed.remove("yToX")
    if x == x_max and y == y_max:
        allowed = ["emptyX","emptyY"]     
    return allowed

def runSearch(x,y):
    idiot = []
    how_many_times_turned = 0
    while x != 8:
        # Get allowed functions, "to" is available function number
        functions = randomStep(x,y)
        # Select random functions from possible ones
        get_rand = random.randint(0,len(functions)-1)
        run_this = (functions[get_rand]+"(x,y)")
        how_many_times_turned += 1
        x, y = eval(run_this)
        a = str(x)
        b = str(y)
        c = a+","+b
        idiot.append(c)
        #print(x, y, "=>",end="")
    return how_many_times_turned, idiot
# Main
for i in range(0,5):
    many, idiot = runSearch(x,y)
    print("Done! ",many," times")
    print(idiot)
