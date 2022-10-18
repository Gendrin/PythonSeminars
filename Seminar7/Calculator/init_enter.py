
def get_valueR():
    a = input('Enter rational number = ')
    if a.isdigit:
        return int(a)
    else:
        a = None
    return a

def get_valueC():
    a = input('Enter complex number part1 = ')
    b = input('Enter complex number part2 = ')
    if a.isdigit and b.isdigit:
        return complex(int(a),int(b))
    else:
        a = None
    return a

def view_data(title, data):
    print(f'{title} = {data}')