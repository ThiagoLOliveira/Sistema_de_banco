# Conta para verificar os digitos
def validaCpf(cpf):
    def Digitos(cpf, baseCalc):
        # baseCalc so pode ser 10 para o primerio dig e 11 para o segundo dig
        n = baseCalc
        base = 0
        for dig in cpf:
            ac = int(dig) * n
            base = base + ac
            n -= 1
        digito = (base * 10) % 11
        if digito > 10:
            cpf.append(str(0))
        else:
            cpf.append(str(digito))

    def VerificaCpf(cpfEnviado, cpfVerificado):
        cpf1 = []
        cpf2 = []
        for i in cpfEnviado:
            cpf1.append(i)
        for n in cpfVerificado:
            cpf2.append(n)
        if cpf1 == cpf2:
            return True
        else:
            return False

    def verificar_digitos_iguais(cpf):
        # Verifique se a lista de dígitos do CPF é diferente de 11 valores.
        if len(cpf) != 11:
            return True

        # Compare cada dígito com o dígito anterior.
        for i in range(1, len(cpf)):
            if cpf[i] != cpf[i - 1]:
                return False

        # Se nenhum dígito diferente for encontrado, todos são iguais.
        return True

    try:
        listaCpf = []
        for dig in cpf:
            listaCpf.append(dig)
        if verificar_digitos_iguais(listaCpf):
            print('Digite um CPF valido')
            return False
        else:
            cpfDig = listaCpf[:9]
            Digitos(cpfDig, 10)  # Primeiro Digito
            Digitos(cpfDig, 11)  # Segundo Digito
            return VerificaCpf(listaCpf, cpfDig) # Retorna o resultado da verificação
    except ValueError:
        print('Digite apenas números, sem "." ou "-"')
        return False
    except:
        return False