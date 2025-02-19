import sqlite3
import sys

import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
from login import Ui_Login
from ui_main import Ui_MainWindow
from database import DataBase
from xml_files import Read_xml
from PySide6.QtSql import QSqlDatabase, QSqlTableModel


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.checkLogin)



    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticacao = self.users.checar_usuario(self.txt_user.text().upper(), self.txt_password.text())

        if autenticacao.lower() == "Administrador" or autenticacao == "Usuário":
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro")
                msg.setText(f"Login ou senha incorreto!\n Mais {self.tentativas + 1} tentativas!")
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                self.users.encerra_conexao()

                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.model = None
        self.path = None
        self.campo = None
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_importa.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_importar))

        self.btn_cadastrar_usuario.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastrar.clicked.connect(self.inscrever_usuario)

        self.btn_abrir.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        self.btn_exel.clicked.connect(self.excel_file)

        self.table_geral()

    def inscrever_usuario(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas dirvegentes")
            msg.setText("As senhas são distintas!")
            msg.exec()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()

        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()

        db.inserir_usuario(nome, user, password, access)

        db.encerra_conexao()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str("Open Directory"),
                                                     "/home",
                                                     QFileDialog.ShowDirsOnly

                                                     | QFileDialog.DontResolveSymlinks)
        self.txt_file.setText(self.path)

    def import_xml_files(self):
        xml = Read_xml(self.txt_file.text())
        all_files = xml.all_files()

        db = DataBase()
        db.conecta()

        for file in all_files:
            notas = xml.nfe_data(file)  # Pega os dados do XML
            for nota in notas:
                try:
                    cursor = db.connection.cursor()
                    cursor.execute("""
                        INSERT INTO Notas (NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
                                           valorNfe, itemNota, cod, qntd, descricao, unidade_medida, valorProd,
                                           data_importacao, usuario, data_saida)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, nota)
                    db.connection.commit()
                except Exception as e:
                    print(f"Erro ao inserir no banco: {e}")

        db.encerra_conexao()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("Importação concluída!")
        msg.exec()

    def table_geral(self):
        self.tb_geral.setStyleSheet(u" QHeaderView{ color:black}; color:black;font-size: 15px;")

        db = QSqlDatabase.database()

        if not db.isOpen():
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("system.db")
            if not db.open():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro no Banco de Dados")
                msg.setText("Não foi possível abrir o banco de dados.")
                msg.exec()
                return

        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()

    def excel_file(self):
        cnx = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM Notas", cnx)
        result.to_excel("Resumo de notas.xlsx", sheet_name='Notas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Notas")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    '''window = MainWindow()'''
    window = Login()
    window.show()
    sys.exit(app.exec())
