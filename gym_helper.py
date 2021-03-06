from PyQt5 import uic, QtWidgets
import mysql.connector
from datetime import datetime

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Manteigaderretida76',
    database='registro_de_alunos'
)


def mostrando_segunda_tela():
    tela_principal.close()
    tela_adicao.show()


def mostrando_primeira_tela():
    tela_adicao.close()
    tela_principal.show()


def mostrando_tela_de_amostragem():
    tela_principal.close()
    tela_de_amostragem.show()


def mostrar_tela_de_atualizacao():
    tela_principal.close()
    tela_de_atualizacao.show()


def mostrar_tela_de_remocao():
    tela_principal.close()
    tela_de_remocao.show()


def mostrar_tela_de_devedores():
    tela_principal.close()
    tela_de_devedores.show()


def retornar_menu_ad():
    tela_adicao.close()
    tela_principal.show()


def retornar_menu_lista():
    tela_de_amostragem.close()
    tela_principal.show()


def retornar_menu_atualizar():
    tela_de_atualizacao.close()
    tela_principal.show()


def retornar_menu_remo():
    tela_de_remocao.close()
    tela_principal.show()


def retornar_devedore():
    tela_de_devedores.close()
    tela_principal.show()


def atualizar_dados():
    # salvando informações
    linha_id = int(tela_de_atualizacao.lineEdit.text())
    linha_peso = float(tela_de_atualizacao.lineEdit_2.text())
    linha_idade = str(tela_de_atualizacao.lineEdit_3.text())
    # atualizando informações
    cursor = banco.cursor()
    comando_sql1 = 'select * from alunos;'
    cursor.execute(comando_sql1)
    dados_lidos = cursor.fetchall()
    for r in range(len(dados_lidos)):
        if linha_id == int(dados_lidos[r][0]):
            comando_sql2 = f'UPDATE alunos SET peso = {linha_peso} WHERE peso = {float(dados_lidos[r][2])};'
            comando_sql3 = f'UPDATE alunos SET idade = {linha_idade} WHERE idade = {float(dados_lidos[r][3])};'
            cursor.execute(comando_sql2)
            cursor.execute(comando_sql3)
            banco.commit()
            pass

    retornar_menu_atualizar()


def remover_dados():
    linha_id = tela_de_remocao.lineEdit_5.text()
    cursor = banco.cursor()
    comando_sql = f'DELETE from alunos WHERE id = {int(linha_id)};'
    cursor.execute(comando_sql)
    banco.commit()
    retornar_menu_remo()


def adicionando_informacoes():
    # salvando informações
    linha_nome = str(tela_adicao.lineEdit.text())
    linha_peso = str(tela_adicao.lineEdit_2.text())
    linha_idade = str(tela_adicao.lineEdit_3.text())
    linha_tel = str(tela_adicao.linetelefonead.text())
    linha_datapd = str(tela_adicao.linedatapgad.text())
    box_informacoes = str(tela_adicao.textboxad.text())
    # salvando o banco
    cursor = banco.cursor()
    comando_sql = "INSERT INTO alunos (nome, peso, idade, telefone, informacoes, datapg) VALUES (%s,%s,%s,%s,%s,%s);"
    dados = (linha_nome.title(), linha_peso, linha_idade, linha_tel, box_informacoes, linha_datapd)
    cursor.execute(comando_sql, dados)
    banco.commit()
    retornar_menu_ad()


def mostrando_os_devedores():
    data_atual = datetime.now()
    dia_atual = data_atual.strftime('%d')
    mostrar_tela_de_devedores()
    cursor = banco.cursor()
    comando_sql = f'select * from alunos WHERE Day(datapg) > {dia_atual};'
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    tela_de_devedores.tableWidget.setRowCount(len(dados_lidos))
    tela_de_devedores.tableWidget.setColumnCount(7)
    for i in range(len(dados_lidos)):
        for j in range(7):
            tela_de_devedores.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def mostrando_os_dados():
    mostrando_tela_de_amostragem()
    cursor = banco.cursor()
    comando_sql = 'select * from alunos;'
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    tela_de_amostragem.tableWidget.setRowCount(len(dados_lidos))
    tela_de_amostragem.tableWidget.setColumnCount(7)
    for i in range(len(dados_lidos)):
        for j in range(7):
            tela_de_amostragem.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app = QtWidgets.QApplication([])
tela_principal = uic.loadUi("tela_de_entrada.ui")
tela_adicao = uic.loadUi("tela_de_adicao.ui")
tela_de_amostragem = uic.loadUi('tela_de_amostragem.ui')
tela_de_atualizacao = uic.loadUi('tela_de_atualizacao.ui')
tela_de_remocao = uic.loadUi('tela_de_remocao.ui')
tela_de_devedores = uic.loadUi('tela_de_pagamento.ui')
# tela principal
tela_principal.pushButton.clicked.connect(mostrando_segunda_tela)
tela_principal.pushButton_2.clicked.connect(mostrando_os_dados)
tela_principal.pushButton_3.clicked.connect(mostrar_tela_de_remocao)
tela_principal.pushButton_4.clicked.connect(mostrar_tela_de_atualizacao)
tela_principal.pushButton_5.clicked.connect(mostrando_os_devedores)
# tela de adição
tela_adicao.pushButton_2.clicked.connect(adicionando_informacoes)
tela_adicao.pushButton_3.clicked.connect(retornar_menu_ad)
# tela de amostragem
tela_de_amostragem.pushButton_4.clicked.connect(retornar_menu_lista)
# tela de atualização
tela_de_atualizacao.pushButton_3.clicked.connect(retornar_menu_atualizar)
tela_de_atualizacao.pushButton_2.clicked.connect(atualizar_dados)
# tela de remocao
tela_de_remocao.pushButton_4.clicked.connect(retornar_menu_remo)
tela_de_remocao.pushButton_5.clicked.connect(remover_dados)
# tela de devedores
tela_de_devedores.pushButton_4.clicked.connect(retornar_devedore)
tela_principal.show()
app.exec()

'''
lembrete:
criação de tabelas mysql
create table alunos (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100),
    informacoes VARCHAR(3000),
    telefone INT,
    PRIMARY KEY (id)
);
'''
'''
mexendo com datas:
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime(‘%d/%m/%Y’)

print(data_e_hora_em_texto)
'''
