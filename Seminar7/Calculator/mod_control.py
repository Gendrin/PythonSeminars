import init_enter as mint
import model_sum as msum

def Operation(code_op):
    if code_op == 11:
        resultsum = msum.sum(mint.get_valueR(),mint.get_valueR())# Меню 1-1 +
        mint.view_data("Результат сложения рациональных",resultsum)
    elif code_op ==21:
        resultsum = msum.sum(mint.get_valueC(), mint.get_valueC())  # Меню 1-1 +
        mint.view_data("Результат сложения комплексных чисел", resultsum)

