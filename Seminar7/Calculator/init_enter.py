def get_valueR():
    a = input('Enter rational number = ')
    return(CheckInputFloat(a))

def get_valueC():
    a = input('Enter complex number part1 = ')
    b = input('Enter complex number part2 = ')
    a = CheckInputFloat(a)
    b = CheckInputFloat(b)
    if a!=None and b!=None:
        return complex(a,b)
    else:
        return None

def CheckInputFloat(testInput):
    try:
        return float(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None

def view_data(title, data):
    result="{0} = {1}".format(title,data)
    print(result)
    return result
