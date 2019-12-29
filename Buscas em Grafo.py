# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'novainterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import Cor_Busca
import Grafoparainterface as gf
import Limpar_Estilo


class Ui_Trabalho_LMD(object):
    def setupUi(self, Trabalho_LMD):
        Trabalho_LMD.setObjectName("Trabalho_LMD")
        Trabalho_LMD.setEnabled(True)
        Trabalho_LMD.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Trabalho_LMD.sizePolicy().hasHeightForWidth())
        Trabalho_LMD.setSizePolicy(sizePolicy)
        Trabalho_LMD.setMinimumSize(QtCore.QSize(0, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons8-módulo-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Trabalho_LMD.setWindowIcon(icon)
        Trabalho_LMD.setToolTipDuration(-1)
        Trabalho_LMD.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(Trabalho_LMD)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(1000, 570, 261, 131))
        self.frame_2.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Limpar = QtWidgets.QPushButton(self.frame_2)
        self.Limpar.setGeometry(QtCore.QRect(10, 90, 111, 31))
        self.Limpar.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.Limpar.setObjectName("Limpar")
        self.Sair = QtWidgets.QPushButton(self.frame_2)
        self.Sair.setGeometry(QtCore.QRect(129, 90, 121, 31))
        self.Sair.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"")
        self.Sair.setObjectName("Sair")
        self.Busca_em_Profundidade = QtWidgets.QPushButton(self.frame_2)
        self.Busca_em_Profundidade.setGeometry(QtCore.QRect(10, 50, 241, 31))
        self.Busca_em_Profundidade.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.Busca_em_Profundidade.setObjectName("Busca_em_Profundidade")
        self.Busca_em_Largura = QtWidgets.QPushButton(self.frame_2)
        self.Busca_em_Largura.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.Busca_em_Largura.setToolTipDuration(-1)
        self.Busca_em_Largura.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.Busca_em_Largura.setObjectName("Busca_em_Largura")
        self.RioGrandedoSul = QtWidgets.QPushButton(self.centralwidget)
        self.RioGrandedoSul.setGeometry(QtCore.QRect(490, 620, 31, 31))
        self.RioGrandedoSul.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.RioGrandedoSul.setText("")
        self.RioGrandedoSul.setObjectName("RioGrandedoSul")
        self.Amazonas = QtWidgets.QPushButton(self.centralwidget)
        self.Amazonas.setGeometry(QtCore.QRect(290, 140, 31, 31))
        self.Amazonas.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Amazonas.setText("")
        self.Amazonas.setObjectName("Amazonas")
        self.Acre = QtWidgets.QPushButton(self.centralwidget)
        self.Acre.setGeometry(QtCore.QRect(170, 260, 31, 31))
        self.Acre.setSizeIncrement(QtCore.QSize(1, 1))
        self.Acre.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Acre.setText("")
        self.Acre.setFlat(False)
        self.Acre.setObjectName("Acre")
        self.Rondonia = QtWidgets.QPushButton(self.centralwidget)
        self.Rondonia.setGeometry(QtCore.QRect(330, 290, 31, 31))
        self.Rondonia.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Rondonia.setText("")
        self.Rondonia.setObjectName("Rondonia")
        self.SantaCatarina = QtWidgets.QPushButton(self.centralwidget)
        self.SantaCatarina.setGeometry(QtCore.QRect(550, 580, 31, 31))
        self.SantaCatarina.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.SantaCatarina.setText("")
        self.SantaCatarina.setObjectName("SantaCatarina")
        self.Parana = QtWidgets.QPushButton(self.centralwidget)
        self.Parana.setGeometry(QtCore.QRect(520, 530, 31, 31))
        self.Parana.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Parana.setText("")
        self.Parana.setObjectName("Parana")
        self.SaoPaulo = QtWidgets.QPushButton(self.centralwidget)
        self.SaoPaulo.setGeometry(QtCore.QRect(570, 490, 31, 31))
        self.SaoPaulo.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.SaoPaulo.setText("")
        self.SaoPaulo.setObjectName("SaoPaulo")
        self.MinasGerais = QtWidgets.QPushButton(self.centralwidget)
        self.MinasGerais.setGeometry(QtCore.QRect(650, 430, 31, 31))
        self.MinasGerais.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.MinasGerais.setText("")
        self.MinasGerais.setObjectName("MinasGerais")
        self.RiodeJaneiro = QtWidgets.QPushButton(self.centralwidget)
        self.RiodeJaneiro.setGeometry(QtCore.QRect(670, 500, 31, 31))
        self.RiodeJaneiro.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.RiodeJaneiro.setText("")
        self.RiodeJaneiro.setObjectName("RiodeJaneiro")
        self.EspiritoSanto = QtWidgets.QPushButton(self.centralwidget)
        self.EspiritoSanto.setGeometry(QtCore.QRect(710, 450, 31, 31))
        self.EspiritoSanto.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.EspiritoSanto.setText("")
        self.EspiritoSanto.setObjectName("EspiritoSanto")
        self.Bahia = QtWidgets.QPushButton(self.centralwidget)
        self.Bahia.setGeometry(QtCore.QRect(690, 310, 31, 31))
        self.Bahia.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Bahia.setText("")
        self.Bahia.setObjectName("Bahia")
        self.Sergipe = QtWidgets.QPushButton(self.centralwidget)
        self.Sergipe.setGeometry(QtCore.QRect(780, 300, 31, 31))
        self.Sergipe.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Sergipe.setText("")
        self.Sergipe.setObjectName("Sergipe")
        self.Alagoas = QtWidgets.QPushButton(self.centralwidget)
        self.Alagoas.setGeometry(QtCore.QRect(810, 270, 31, 31))
        self.Alagoas.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Alagoas.setText("")
        self.Alagoas.setObjectName("Alagoas")
        self.Ceara = QtWidgets.QPushButton(self.centralwidget)
        self.Ceara.setGeometry(QtCore.QRect(740, 180, 31, 31))
        self.Ceara.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Ceara.setText("")
        self.Ceara.setObjectName("Ceara")
        self.Pernambuco = QtWidgets.QPushButton(self.centralwidget)
        self.Pernambuco.setGeometry(QtCore.QRect(740, 250, 31, 31))
        self.Pernambuco.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Pernambuco.setText("")
        self.Pernambuco.setObjectName("Pernambuco")
        self.Paraiba = QtWidgets.QPushButton(self.centralwidget)
        self.Paraiba.setGeometry(QtCore.QRect(790, 230, 31, 31))
        self.Paraiba.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Paraiba.setText("")
        self.Paraiba.setObjectName("Paraiba")
        self.RioGrandedoNorte = QtWidgets.QPushButton(self.centralwidget)
        self.RioGrandedoNorte.setGeometry(QtCore.QRect(810, 200, 31, 31))
        self.RioGrandedoNorte.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.RioGrandedoNorte.setText("")
        self.RioGrandedoNorte.setObjectName("RioGrandedoNorte")
        self.Piaui = QtWidgets.QPushButton(self.centralwidget)
        self.Piaui.setGeometry(QtCore.QRect(680, 240, 31, 31))
        self.Piaui.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Piaui.setText("")
        self.Piaui.setObjectName("Piaui")
        self.Maranhao = QtWidgets.QPushButton(self.centralwidget)
        self.Maranhao.setGeometry(QtCore.QRect(640, 180, 31, 31))
        self.Maranhao.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Maranhao.setText("")
        self.Maranhao.setObjectName("Maranhao")
        self.Tocantins = QtWidgets.QPushButton(self.centralwidget)
        self.Tocantins.setGeometry(QtCore.QRect(590, 270, 31, 31))
        self.Tocantins.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Tocantins.setText("")
        self.Tocantins.setObjectName("Tocantins")
        self.Para = QtWidgets.QPushButton(self.centralwidget)
        self.Para.setGeometry(QtCore.QRect(500, 170, 31, 31))
        self.Para.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Para.setText("")
        self.Para.setObjectName("Para")
        self.Amapa = QtWidgets.QPushButton(self.centralwidget)
        self.Amapa.setGeometry(QtCore.QRect(520, 60, 31, 31))
        self.Amapa.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Amapa.setText("")
        self.Amapa.setObjectName("Amapa")
        self.Roraima = QtWidgets.QPushButton(self.centralwidget)
        self.Roraima.setGeometry(QtCore.QRect(350, 40, 31, 31))
        self.Roraima.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Roraima.setText("")
        self.Roraima.setObjectName("Roraima")
        self.MatoGrosso = QtWidgets.QPushButton(self.centralwidget)
        self.MatoGrosso.setGeometry(QtCore.QRect(450, 310, 31, 31))
        self.MatoGrosso.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.MatoGrosso.setText("")
        self.MatoGrosso.setObjectName("MatoGrosso")
        self.Goias = QtWidgets.QPushButton(self.centralwidget)
        self.Goias.setGeometry(QtCore.QRect(560, 370, 31, 31))
        self.Goias.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.Goias.setText("")
        self.Goias.setObjectName("Goias")
        self.MatoGrossodoSul = QtWidgets.QPushButton(self.centralwidget)
        self.MatoGrossodoSul.setGeometry(QtCore.QRect(460, 450, 31, 31))
        self.MatoGrossodoSul.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 blue, stop: 1 blue\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.MatoGrossodoSul.setText("")
        self.MatoGrossodoSul.setObjectName("MatoGrossodoSul")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(920, 0, 441, 31))
        self.label_27.setStyleSheet("font: 75 oblique 11pt \"Waree\";")
        self.label_27.setObjectName("label_27")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 871, 721))
        self.label.setStyleSheet("background-image:url(./fundodefdef.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 47, 13))
        self.label_2.setStyleSheet("background-image:url(:/newPrefix/fundo2mapa.png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 280, 21, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 31, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 330, 31, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 190, 31, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 90, 31, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 50, 31, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(670, 170, 31, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 480, 31, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(510, 560, 21, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(580, 520, 31, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(750, 460, 31, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(700, 530, 31, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(680, 420, 31, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(420, 330, 31, 17))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(570, 310, 21, 17))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(560, 410, 31, 17))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(710, 340, 31, 17))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(670, 270, 16, 17))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(810, 320, 31, 17))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(840, 290, 31, 17))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(750, 280, 21, 17))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(840, 240, 31, 17))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(840, 190, 31, 17))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(780, 170, 31, 17))
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(590, 590, 21, 17))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(520, 630, 21, 17))
        self.label_29.setObjectName("label_29")
        self.label.raise_()
        self.frame_2.raise_()
        self.RioGrandedoSul.raise_()
        self.Amazonas.raise_()
        self.Acre.raise_()
        self.Rondonia.raise_()
        self.SantaCatarina.raise_()
        self.Parana.raise_()
        self.SaoPaulo.raise_()
        self.MinasGerais.raise_()
        self.RiodeJaneiro.raise_()
        self.EspiritoSanto.raise_()
        self.Bahia.raise_()
        self.Ceara.raise_()
        self.Pernambuco.raise_()
        self.Paraiba.raise_()
        self.RioGrandedoNorte.raise_()
        self.Piaui.raise_()
        self.Maranhao.raise_()
        self.Tocantins.raise_()
        self.Para.raise_()
        self.Amapa.raise_()
        self.Roraima.raise_()
        self.MatoGrosso.raise_()
        self.Goias.raise_()
        self.MatoGrossodoSul.raise_()
        self.label_27.raise_()
        self.Alagoas.raise_()
        self.Sergipe.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        Trabalho_LMD.setCentralWidget(self.centralwidget)

        self.retranslateUi(Trabalho_LMD)
        QtCore.QMetaObject.connectSlotsByName(Trabalho_LMD)
        self.Vertice = "Ac"
        self.Acre.clicked.connect(self.Mudar1Ac)
        self.Alagoas.clicked.connect(self.Mudar1Al)
        self.Amapa.clicked.connect(self.Mudar1Ap)
        self.Amazonas.clicked.connect(self.Mudar1Am)
        self.Bahia.clicked.connect(self.Mudar1Ba)
        self.Ceara.clicked.connect(self.Mudar1Ce)
        self.EspiritoSanto.clicked.connect(self.Mudar1Es)
        self.Goias.clicked.connect(self.Mudar1Go)
        self.Maranhao.clicked.connect(self.Mudar1Ma)
        self.MatoGrosso.clicked.connect(self.Mudar1Mt)
        self.MatoGrossodoSul.clicked.connect(self.Mudar1Ms)
        self.MinasGerais.clicked.connect(self.Mudar1Mg)
        self.Para.clicked.connect(self.Mudar1Pa)
        self.Paraiba.clicked.connect(self.Mudar1Pb)
        self.Parana.clicked.connect(self.Mudar1Pr)
        self.Pernambuco.clicked.connect(self.Mudar1Pe)
        self.Piaui.clicked.connect(self.Mudar1Pi)
        self.RiodeJaneiro.clicked.connect(self.Mudar1Rj)
        self.RioGrandedoNorte.clicked.connect(self.Mudar1Rn)
        self.RioGrandedoSul.clicked.connect(self.Mudar1Rs)
        self.Rondonia.clicked.connect(self.Mudar1Ro)
        self.Roraima.clicked.connect(self.Mudar1Rr)
        self.SantaCatarina.clicked.connect(self.Mudar1Sc)
        self.SaoPaulo.clicked.connect(self.Mudar1Sp)
        self.Sergipe.clicked.connect(self.Mudar1Se)
        self.Tocantins.clicked.connect(self.Mudar1To)
        self.Limpar.clicked.connect(self.Limp)
        self.Busca_em_Largura.clicked.connect(self.Buscarl)
        self.Busca_em_Profundidade.clicked.connect(self.Buscarp)

    def Buscarl(self):
        a = gf.Busca_em_Largura(self.Vertice)
        for i in a:
            if i == "Acre":
                Cor_Busca.Mudar2Ac(self)
                QtTest.QTest.qWait(1000)
            if i == "Alagoas":
                Cor_Busca.Mudar2Al(self)
                QtTest.QTest.qWait(1000)
            if i == "Amapá":
                Cor_Busca.Mudar2Ap(self)
                QtTest.QTest.qWait(1000)
            if i == "Amazonas":
                Cor_Busca.Mudar2Am(self)
                QtTest.QTest.qWait(1000)
            if i == "Bahia":
                Cor_Busca.Mudar2Ba(self)
                QtTest.QTest.qWait(1000)
            if i == "Ceará":
                Cor_Busca.Mudar2Ce(self)
                QtTest.QTest.qWait(1000)
            if i == "Espírito Santo":
                Cor_Busca.Mudar2Es(self)
                QtTest.QTest.qWait(1000)
            if i == "Goiás":
                Cor_Busca.Mudar2Go(self)
                QtTest.QTest.qWait(1000)
            if i == "Maranhão":
                Cor_Busca.Mudar2Ma(self)
                QtTest.QTest.qWait(1000)
            if i == "Mato Grosso":
                Cor_Busca.Mudar2Mt(self)
                QtTest.QTest.qWait(1000)
            if i == "Mato Grosso do Sul":
                Cor_Busca.Mudar2Ms(self)
                QtTest.QTest.qWait(1000)
            if i == "Minas Gerais":
                Cor_Busca.Mudar2Mg(self)
                QtTest.QTest.qWait(1000)
            if i == "Pará":
                Cor_Busca.Mudar2Pa(self)
                QtTest.QTest.qWait(1000)
            if i == "Paraíba":
                Cor_Busca.Mudar2Pb(self)
                QtTest.QTest.qWait(1000)
            if i == "Paraná":
                Cor_Busca.Mudar2Pr(self)
                QtTest.QTest.qWait(1000)
            if i == "Pernambuco":
                Cor_Busca.Mudar2Pe(self)
                QtTest.QTest.qWait(1000)
            if i == "Piauí":
                Cor_Busca.Mudar2Pi(self)
                QtTest.QTest.qWait(1000)
            if i == "Rio de Janeiro":
                Cor_Busca.Mudar2Rj(self)
                QtTest.QTest.qWait(1000)
            if i == "Rio Grande do Norte":
                Cor_Busca.Mudar2Rn(self)
                QtTest.QTest.qWait(1000)
            if i == "Rio Grande do Sul":
                Cor_Busca.Mudar2Rs(self)
                QtTest.QTest.qWait(1000)
            if i == "Rondônia":
                Cor_Busca.Mudar2Ro(self)
                QtTest.QTest.qWait(1000)
            if i == "Roraima":
                Cor_Busca.Mudar2Rr(self)
                QtTest.QTest.qWait(1000)
            if i == "Santa Catarina":
                Cor_Busca.Mudar2Sc(self)
                QtTest.QTest.qWait(1000)
            if i == "São Paulo":
                Cor_Busca.Mudar2Sp(self)
                QtTest.QTest.qWait(1000)
            if i == "Sergipe":
                Cor_Busca.Mudar2Se(self)
                QtTest.QTest.qWait(1000)
            if i == "Tocantins":
                Cor_Busca.Mudar2To(self)
                QtTest.QTest.qWait(1000)
    
                
    def Buscarp(self):
        a = gf.Busca_em_Profundidade(self.Vertice)
        for i in a:
            if i == "Acre":
                Cor_Busca.Mudar2Ac(self)
                QtTest.QTest.qWait(1000)
            if i == "Alagoas":
                Cor_Busca.Mudar2Al(self)
                QtTest.QTest.qWait(1000)
            if i == "Amapá":
                Cor_Busca.Mudar2Ap(self)
                QtTest.QTest.qWait(1000)
            if i == "Amazonas":
                Cor_Busca.Mudar2Am(self)
                QtTest.QTest.qWait(1000)
            if i == "Bahia":
                Cor_Busca.Mudar2Ba(self)
                QtTest.QTest.qWait(1000)
            if i == "Ceará":
                Cor_Busca.Mudar2Ce(self)
                QtTest.QTest.qWait(1000)
            if i == "Espírito Santo":
                Cor_Busca.Mudar2Es(self)
                QtTest.QTest.qWait(1000)
            if i == "Goiás":
                Cor_Busca.Mudar2Go(self)
                QtTest.QTest.qWait(1000)
            if i == "Maranhão":
                Cor_Busca.Mudar2Ma(self)
                QtTest.QTest.qWait(1000)
            if i == "Mato Grosso":
                Cor_Busca.Mudar2Mt(self)
                QtTest.QTest.qWait(1000)
            if i == "Mato Grosso do Sul":
                Cor_Busca.Mudar2Ms(self)
                QtTest.QTest.qWait(1000)
            if i == "Minas Gerais":
                Cor_Busca.Mudar2Mg(self)
                QtTest.QTest.qWait(1000)
            if i == "Pará":
                Cor_Busca.Mudar2Pa(self)
                QtTest.QTest.qWait(1000)
            if i == "Paraíba":
                Cor_Busca.Mudar2Pb(self)
                QtTest.QTest.qWait(1000)
            if i == "Paraná":
                Cor_Busca.Mudar2Pr(self)
                QtTest.QTest.qWait(1000)
            if i == "Pernambuco":
                Cor_Busca.Mudar2Pe(self)
                QtTest.QTest.qWait(1000)
            if i == "Piauí":
                Cor_Busca.Mudar2Pi(self)
                QtTest.QTest.qWait(1000)
            if i == "Rio de Janeiro":
                Cor_Busca.Mudar2Rj(self)
                QtTest.QTest.qWait(1000)
            if i == "Rio Grande do Norte":
                Cor_Busca.Mudar2Rn(self)
                QtTest.QTest.qWait(1000)
            if i == "Rio Grande do Sul":
                Cor_Busca.Mudar2Rs(self)
                QtTest.QTest.qWait(1000)
            if i == "Rondônia":
                Cor_Busca.Mudar2Ro(self)
                QtTest.QTest.qWait(1000)
            if i == "Roraima":
                Cor_Busca.Mudar2Rr(self)
                QtTest.QTest.qWait(1000)
            if i == "Santa Catarina":
                Cor_Busca.Mudar2Sc(self)
                QtTest.QTest.qWait(1000)
            if i == "São Paulo":
                Cor_Busca.Mudar2Sp(self)
                QtTest.QTest.qWait(1000)
            if i == "Sergipe":
                Cor_Busca.Mudar2Se(self)
                QtTest.QTest.qWait(1000)
            if i == "Tocantins":
                Cor_Busca.Mudar2To(self)
                QtTest.QTest.qWait(1000)
     
    def Limp(self):
        Limpar_Estilo.Limpar(self)

    def Mudar1Ac(self):
        self.Vertice = "Acre"
        Limpar_Estilo.Limpar(self)
        self.Acre.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 red, stop: 1 red\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 red, stop: 1 red\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 red, stop: 1 red\n"
"        );\n"
"    }")


    def Mudar1Al(self):
        self.Vertice = "Alagoas"
        Limpar_Estilo.Limpar(self)
        self.Alagoas.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Ap(self):
                self.Vertice = "Amapá"
                Limpar_Estilo.Limpar(self)
                self.Amapa.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Am(self):
                self.Vertice = "Amazonas"
                Limpar_Estilo.Limpar(self)
                self.Amazonas.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Ba(self):
                self.Vertice = "Bahia"
                Limpar_Estilo.Limpar(self)
                self.Bahia.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Ce(self):
                self.Vertice = "Ceará"
                Limpar_Estilo.Limpar(self)
                self.Ceara.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Es(self):
                self.Vertice = "Espírito Santo"
                Limpar_Estilo.Limpar(self)
                self.EspiritoSanto.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Go(self):
                self.Vertice = "Goiás"
                Limpar_Estilo.Limpar(self)
                self.Goias.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Ma(self):
                self.Vertice = "Maranhão"
                Limpar_Estilo.Limpar(self)
                self.Maranhao.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Mt(self):
                self.Vertice = "Mato Grosso"
                Limpar_Estilo.Limpar(self)
                self.MatoGrosso.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Ms(self):
                self.Vertice = "Mato Grosso do Sul"
                Limpar_Estilo.Limpar(self)
                self.MatoGrossodoSul.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Mg(self):
                self.Vertice = "Minas Gerais"
                Limpar_Estilo.Limpar(self)
                self.MinasGerais.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Pa(self):
                self.Vertice = "Pará"
                Limpar_Estilo.Limpar(self)
                self.Para.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Pb(self):
                self.Vertice = "Paraíba"
                Limpar_Estilo.Limpar(self)
                self.Paraiba.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Pr(self):
                self.Vertice = "Paraná"
                Limpar_Estilo.Limpar(self)
                self.Parana.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Pe(self):
                self.Vertice = "Pernambuco"
                Limpar_Estilo.Limpar(self)
                self.Pernambuco.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Pi(self):
                self.Vertice = "Piauí"
                Limpar_Estilo.Limpar(self)
                self.Piaui.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Rj(self):
                self.Vertice = "Rio de Janeiro"
                Limpar_Estilo.Limpar(self)
                self.RiodeJaneiro.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Rn(self):
                self.Vertice = "Rio Grande do Norte"
                Limpar_Estilo.Limpar(self)
                self.RioGrandedoNorte.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Rs(self):
                self.Vertice = "Rio Grande do Sul"
                Limpar_Estilo.Limpar(self)
                self.RioGrandedoSul.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Ro(self):
                self.Vertice = "Rondônia"
                Limpar_Estilo.Limpar(self)
                self.Rondonia.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Rr(self):
                self.Vertice = "Roraima"
                Limpar_Estilo.Limpar(self)
                self.Roraima.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Sc(self):
                self.Vertice = "Santa Catarina"
                Limpar_Estilo.Limpar(self)
                self.SantaCatarina.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Sp(self):
                self.Vertice = "São Paulo"
                Limpar_Estilo.Limpar(self)
                self.SaoPaulo.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1Se(self):
                self.Vertice = "Sergipe"
                Limpar_Estilo.Limpar(self)
                self.Sergipe.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def Mudar1To(self):
                self.Vertice = "Tocantins"
                Limpar_Estilo.Limpar(self)
                self.Tocantins.setStyleSheet("QPushButton {\n"
        "    color: #333;\n"
        "    border: 2px solid #555;\n"
        "    border-radius: 15px;\n"
        "    border-style: outset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    padding: 5px;\n"
        "    }\n"
        "\n"
        "QPushButton:hover {\n"
        "    background: qradialgradient(\n"
        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-style: inset;\n"
        "    background: qradialgradient(\n"
        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
        "        radius: 1.35, stop: 0 red, stop: 1 red\n"
        "        );\n"
        "    }")

    def retranslateUi(self, Trabalho_LMD):
        _translate = QtCore.QCoreApplication.translate
        Trabalho_LMD.setWindowTitle(_translate("Trabalho_LMD", "MainWindow"))
        self.Limpar.setText(_translate("Trabalho_LMD", "Limpar"))
        self.Sair.setText(_translate("Trabalho_LMD", "Sair"))
        self.Busca_em_Profundidade.setText(_translate("Trabalho_LMD", "Busca em Profundidade"))
        self.Busca_em_Largura.setText(_translate("Trabalho_LMD", "Busca em Largura"))
        self.label_27.setText(_translate("Trabalho_LMD", "Victor Gabriel Castão da Cruz - 11911ECP004"))
        self.label_3.setText(_translate("Trabalho_LMD", "AC"))
        self.label_4.setText(_translate("Trabalho_LMD", "AM"))
        self.label_5.setText(_translate("Trabalho_LMD", "RO"))
        self.label_6.setText(_translate("Trabalho_LMD", "PA"))
        self.label_7.setText(_translate("Trabalho_LMD", "RR"))
        self.label_8.setText(_translate("Trabalho_LMD", "AP"))
        self.label_9.setText(_translate("Trabalho_LMD", "MA"))
        self.label_10.setText(_translate("Trabalho_LMD", "MS"))
        self.label_11.setText(_translate("Trabalho_LMD", "PR"))
        self.label_12.setText(_translate("Trabalho_LMD", "SP"))
        self.label_13.setText(_translate("Trabalho_LMD", "ES"))
        self.label_14.setText(_translate("Trabalho_LMD", "RJ"))
        self.label_15.setText(_translate("Trabalho_LMD", "MG"))
        self.label_16.setText(_translate("Trabalho_LMD", "MT"))
        self.label_17.setText(_translate("Trabalho_LMD", "TO"))
        self.label_18.setText(_translate("Trabalho_LMD", "GO"))
        self.label_19.setText(_translate("Trabalho_LMD", "BA"))
        self.label_20.setText(_translate("Trabalho_LMD", "PI"))
        self.label_21.setText(_translate("Trabalho_LMD", "SE"))
        self.label_22.setText(_translate("Trabalho_LMD", "AL"))
        self.label_23.setText(_translate("Trabalho_LMD", "PE"))
        self.label_24.setText(_translate("Trabalho_LMD", "PB"))
        self.label_25.setText(_translate("Trabalho_LMD", "RN"))
        self.label_26.setText(_translate("Trabalho_LMD", "CE"))
        self.label_28.setText(_translate("Trabalho_LMD", "SC"))
        self.label_29.setText(_translate("Trabalho_LMD", "RS"))
        self.Sair.clicked.connect(sys.exit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Trabalho_LMD = QtWidgets.QMainWindow()
    ui = Ui_Trabalho_LMD()
    ui.setupUi(Trabalho_LMD)
    Trabalho_LMD.show()
    sys.exit(app.exec_())

