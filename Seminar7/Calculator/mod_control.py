import init_enter as mint
import model_sum as msum
import model_sub as msub
import model_mult as mmult
import model_div as mdiv

def Operation(code_op):
    a,b=0,0
    infString=''
    if code_op == '11' or code_op == '12' or code_op == '13' or code_op == '15'\
            or code_op == '31' or code_op == '32' or code_op == '33':
        a, b = mint.get_valueR(), mint.get_valueR()
    if code_op == '16':
        a = mint.get_valueR()
    if code_op == '21' or code_op == '22' or code_op == '23' or code_op == '24':
            a, b = mint.get_valueC(), mint.get_valueC()


    if code_op == '11':
        resultsum = msum.sum(a,b)# Меню 1-1 +
        infString='Результат сложения рациональных чисел a -> '+str(a)+' и b -> '+str(b)
        # Пишем в лог
        mint.view_data(infString, resultsum)
    elif code_op =='21':
        resultsum = msum.sum(a, b)  # Меню 2-1 +
        infString = 'Результат сложения комплексных чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op =='12':
        resultsum = msub.sub(a, b)  # Меню 1-2 +
        infString = 'Результат вычитания рациональных чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op =='22':
        resultsum = msub.sub(a, b)  # Меню 2-2 +
        infString = 'Результат вычитания комплексных чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '13':
        resultsum = mmult.mult(a, b)  # Меню 1-3 +
        infString = 'Результат умножения рациональных чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '23':
        resultsum = mmult.mult(a, b)  # Меню 2-3 +
        infString = 'Результат умножения комплексных чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '24':
        resultsum = mdiv.div(a, b)  # Меню 2- 4 +
        infString = 'Результат деления комплексных чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '31':
        resultsum = mdiv.div(a, b)  # Меню 1 3 1 +
        infString = 'Результат деления рациональных чисел чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '32':
        resultsum = mdiv.IntDiv(a, b)  # Меню 1 3 2 +
        infString = 'Результат целочисленного деления рациональных чисел чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '33':
        resultsum = mdiv.RemDiv(a, b)  # Меню 1 3 3 +
        infString = 'Результат остатка деления рациональных чисел чисел a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '15':
        resultsum = mmult.dpow(a, b)  # Меню 1 5 +
        infString = 'Результат возведения в степень рационального числа a -> ' + str(a) + ' и b -> ' + str(b)

        mint.view_data(infString, resultsum)
    elif code_op == '16':
        resultsum = mmult.dsqrt(a)  # Меню 1 5 +
        infString = 'езультат вычисления корня рационального числа a -> ' + str(a)

        mint.view_data(infString, resultsum)