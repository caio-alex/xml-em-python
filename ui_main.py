# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 361)
        MainWindow.setStyleSheet(u"background-color: #F8F9FA;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"background-color: #0056b3;\n"
"padding:5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"\n"
"QPushButton{\n"
"color: #fff;\n"
"background-color: #008cdd;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#0086b3;\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 30))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #008cdd;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#0086b3;\n"
"}")

        self.verticalLayout.addWidget(self.btn_tables)

        self.btn_importa = QPushButton(self.frame)
        self.btn_importa.setObjectName(u"btn_importa")
        self.btn_importa.setMinimumSize(QSize(0, 30))
        self.btn_importa.setFont(font)
        self.btn_importa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_importa.setStyleSheet(u"QPushButton{\n"
"color: #fff;\n"
"background-color: #008cdd;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#0086b3;\n"
"}")

        self.verticalLayout.addWidget(self.btn_importa)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"background-color:#F8F9FA;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pages = QStackedWidget(self.frame_2)
        self.pages.setObjectName(u"pages")
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_4 = QVBoxLayout(self.pg_table)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_exel = QPushButton(self.pg_table)
        self.btn_exel.setObjectName(u"btn_exel")

        self.verticalLayout_4.addWidget(self.btn_exel)

        self.tb_geral = QTableView(self.pg_table)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_4.addWidget(self.tb_geral)

        self.pages.addWidget(self.pg_table)
        self.pg_importar = QWidget()
        self.pg_importar.setObjectName(u"pg_importar")
        self.verticalLayout_8 = QVBoxLayout(self.pg_importar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.pg_importar)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setStyleSheet(u"color: #0056b3;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txt_file = QLineEdit(self.pg_importar)
        self.txt_file.setObjectName(u"txt_file")
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_file.setFont(font1)
        self.txt_file.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius: None;\n"
"background-color:rgba(0,0,0,0.2);")

        self.horizontalLayout_12.addWidget(self.txt_file)

        self.btn_abrir = QPushButton(self.pg_importar)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_12.addWidget(self.btn_abrir)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.pg_importar)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.label_4)

        self.btn_import = QPushButton(self.pg_importar)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color:#fff;\n"
"	justify-content:center;\n"
"	background-color:#0056b3;\n"
"	padding:10px;\n"
"	transform: 2s;\n"
"	border-radius:10px;\n"
"	border: solid 2px #fff;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#008cdd;\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_import)

        self.label_5 = QLabel(self.pg_importar)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_13.addWidget(self.label_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.pages.addWidget(self.pg_importar)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pages.addWidget(self.pg_sobre)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color: #0056b3;\n"
"font: 75 16pt \"Verdana\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.label_7.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        font4 = QFont()
        font4.setPointSize(12)
        self.txt_nome.setFont(font4)
        self.txt_nome.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius: None;\n"
"background-color:rgba(0,0,0,0.2);\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_nome)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_8.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setFont(font4)
        self.txt_senha.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius: None;\n"
"background-color:rgba(0,0,0,0.2);")

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setFont(font4)
        self.txt_senha_2.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius: None;\n"
"background-color:rgba(0,0,0,0.2);")

        self.horizontalLayout_8.addWidget(self.txt_senha_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, -1, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_10)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setFont(font4)
        self.txt_usuario.setStyleSheet(u"border-bottom:2px solid black;\n"
"border-radius: None;\n"
"background-color:rgba(0,0,0,0.2);")

        self.horizontalLayout_9.addWidget(self.txt_usuario)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setFont(font4)
        self.cb_perfil.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setFont(font5)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color:#fff;\n"
"	justify-content:center;\n"
"	background-color:#0056b3;\n"
"	padding:10px;\n"
"	transform: 2s;\n"
"	border-radius:10px;\n"
"	border: solid 2px #fff;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#008cdd;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.pages.addWidget(self.pg_cadastro)

        self.verticalLayout_3.addWidget(self.pages)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_cadastrar_usuario = QPushButton(self.frame_2)
        self.btn_cadastrar_usuario.setObjectName(u"btn_cadastrar_usuario")
        self.btn_cadastrar_usuario.setFont(font5)
        self.btn_cadastrar_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"	color:#fff;\n"
"	justify-content:center;\n"
"	background-color:#ff7f00;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#ffae42;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_cadastrar_usuario)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Tabelas", None))
        self.btn_importa.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_exel.setText(QCoreApplication.translate("MainWindow", u"Gerar Exel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Importar Dados</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o arquivo .xml", None))
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_4.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><span style=\" font-size:16pt; font-weight:600; color:#0056b3;\">Leitor de arquivo xml</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0056b3;\">com </span><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">Python</span></p><p align=\"center\"><span style=\" font-size:11pt; color:#0056b3;\"><br/></span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Confirmar senha:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.btn_cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
    # retranslateUi

