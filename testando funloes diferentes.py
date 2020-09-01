from datetime import datetime


def comparar_datas(data_acomparar):
    data_atual = datetime.now()
    data_atual = data_atual.strftime('%d/%m/%Y')
    (diaA, mesA, anoA) = data_atual.split('/')
    (dia, mes, ano) = data_acomparar.split('/')
    diferenca_dia = int(diaA) - int(dia)
    diferenca_mes = int(mesA) - int(mes)
    if diferenca_mes < 0:
        print(f'O pagamento estpa atrazado: {diferenca_mes* - 1}')
    elif diferenca_dia < 0:
        print(f'O pagamento está atrazado:{diferenca_dia* - 1}')
    else:
        print(f'Faltam {diferenca_dia} dias para o pagamento.')


data_e_hora_atuais = datetime.now()
data_str = data_e_hora_atuais.strftime('%d/%m/%Y')
data_do_dia = input('digite a data: ')

print(data_str.split('/'))
