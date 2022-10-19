import init_enter as mint
import model_sum as msum
import model_sub as msub
import model_mult as mmult
import model_div as mdiv
def Operation(code_op):
    if code_op == '11':
        resultsum = msum.sum(mint.get_valueR(),mint.get_valueR())# Меню 1-1 +
        mint.view_data("Результат сложения рациональных",resultsum)
    elif code_op =='21':
        resultsum = msum.sum(mint.get_valueC(), mint.get_valueC())  # Меню 2-1 +
        mint.view_data("Результат сложения комплексных чисел", resultsum)
    elif code_op =='12':
        resultsum = msub.sub(mint.get_valueR(), mint.get_valueR())  # Меню 1-2 +
        mint.view_data("Результат вычитания рациональных чисел", resultsum)
    elif code_op =='22':
        resultsum = msub.sub(mint.get_valueC(), mint.get_valueC())  # Меню 2-2 +
        mint.view_data("Результат вычитания комплексных чисел", resultsum)
    elif code_op == '13':
        resultsum = mmult.mult(mint.get_valueR(), mint.get_valueR())  # Меню 1-3 +
        mint.view_data("Результат умножения рациональных чисел", resultsum)
    elif code_op == '23':
        resultsum = mmult.mult(mint.get_valueC(), mint.get_valueC())  # Меню 2-3 +
        mint.view_data("Результат умножения комплексных чисел", resultsum)
    elif code_op == '24':
        resultsum = mdiv.div(mint.get_valueC(), mint.get_valueC())  # Меню 2- 4 +
        mint.view_data("Результат деления комплексных чисел", resultsum)
    elif code_op == '31':
        resultsum = mdiv.div(mint.get_valueR(), mint.get_valueR())  # Меню 1 3 1 +
        mint.view_data("Результат деления рациональных чисел чисел", resultsum)
    elif code_op == '32':
        resultsum = mdiv.IntDiv(mint.get_valueR(), mint.get_valueR())  # Меню 1 3 2 +
        mint.view_data("Результат целочисленного деления рациональных чисел чисел", resultsum)
    elif code_op == '33':
        resultsum = mdiv.RemDiv(mint.get_valueR(), mint.get_valueR())  # Меню 1 3 3 +
        mint.view_data("Результат остатка деления рациональных чисел чисел", resultsum)
    elif code_op == '15':
        resultsum = mmult.dpow(mint.get_valueR(), mint.get_valueR())  # Меню 1 5 +
        mint.view_data("Результат возведения в степень рационального числа", resultsum)
    elif code_op == '16':
        resultsum = mmult.dsqrt(mint.get_valueR())  # Меню 1 5 +
        mint.view_data("Результат вычисления корня рационального числа", resultsum)