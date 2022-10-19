import exception as exp
def get_valueR():
    a = input('Enter rational number = ')
    return(exp.CheckInputFloat(a))

def get_valueC():
    a = input('Enter complex number part1 = ')
    b = input('Enter complex number part2 = ')
    a = exp.CheckInputFloat(a)
    b = exp.CheckInputFloat(b)
    if a!=None and b!=None:
        return complex(a,b)
    else:
        return None


def view_data(title, data):
    result="{0} = {1}".format(title,data)
    print(result)
    return result
