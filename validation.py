
def validation_cpf(cpf):
    if len(cpf)<11:
        return  "FALTA ALGUN DIGITO !!"
    try:
        cpf = list(cpf.replace('.', '').strip())
        fist_result, next_result = 0, 0
        DIGIT = cpf[-2:]
        for x in range(9):
            fist_result += int(cpf[x]) * (10 - x)
        fist_result = ((fist_result * 10) % 11)
        cpf.append(str(fist_result))
        for j in range(10):
            next_result += int(cpf[j]) * (11 - j)
        next_result = ((next_result * 10) % 11)
        if list(f'{fist_result}{next_result}') == DIGIT:
            return True
        else:
            return False
    except ValueError:
        return "LETRAS CARACTER E SPAÇO NÃO SÃO ENTRADAS VALIDAS !!!"

