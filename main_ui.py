# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1317, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 0, 1241, 741))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_7 = QtWidgets.QLabel(self.page_1)
        self.label_7.setGeometry(QtCore.QRect(180, 220, 181, 16))
        self.label_7.setObjectName("label_7")
        self.line_14 = QtWidgets.QFrame(self.page_1)
        self.line_14.setGeometry(QtCore.QRect(600, 350, 431, 21))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.label_21 = QtWidgets.QLabel(self.page_1)
        self.label_21.setGeometry(QtCore.QRect(610, 410, 171, 16))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.line_25 = QtWidgets.QFrame(self.page_1)
        self.line_25.setGeometry(QtCore.QRect(1030, 390, 3, 61))
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.label_9 = QtWidgets.QLabel(self.page_1)
        self.label_9.setGeometry(QtCore.QRect(180, 310, 171, 21))
        self.label_9.setObjectName("label_9")
        self.line_11 = QtWidgets.QFrame(self.page_1)
        self.line_11.setGeometry(QtCore.QRect(710, 180, 321, 21))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_13 = QtWidgets.QFrame(self.page_1)
        self.line_13.setGeometry(QtCore.QRect(590, 190, 20, 171))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.combobox_retardo_boca_oido = QtWidgets.QComboBox(self.page_1)
        self.combobox_retardo_boca_oido.setGeometry(QtCore.QRect(790, 280, 221, 22))
        self.combobox_retardo_boca_oido.setObjectName("combobox_retardo_boca_oido")
        self.combobox_retardo_boca_oido.addItem("")
        self.combobox_retardo_boca_oido.addItem("")
        self.combobox_retardo_boca_oido.addItem("")
        self.combobox_retardo_boca_oido.addItem("")
        self.combobox_retardo_boca_oido.addItem("")
        self.label_10 = QtWidgets.QLabel(self.page_1)
        self.label_10.setGeometry(QtCore.QRect(180, 280, 171, 21))
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(420, 0, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_J = QtWidgets.QLineEdit(self.page_1)
        self.label_J.setGeometry(QtCore.QRect(790, 240, 221, 21))
        self.label_J.setObjectName("label_J")
        self.label_19 = QtWidgets.QLabel(self.page_1)
        self.label_19.setGeometry(QtCore.QRect(180, 410, 171, 16))
        self.label_19.setObjectName("label_19")
        self.line_6 = QtWidgets.QFrame(self.page_1)
        self.line_6.setGeometry(QtCore.QRect(600, 100, 61, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_13 = QtWidgets.QLabel(self.page_1)
        self.label_13.setGeometry(QtCore.QRect(620, 130, 141, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_1)
        self.label_14.setGeometry(QtCore.QRect(670, 180, 31, 16))
        self.label_14.setObjectName("label_14")
        self.line_21 = QtWidgets.QFrame(self.page_1)
        self.line_21.setGeometry(QtCore.QRect(600, 390, 3, 61))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.label_17 = QtWidgets.QLabel(self.page_1)
        self.label_17.setGeometry(QtCore.QRect(620, 280, 161, 21))
        self.label_17.setObjectName("label_17")
        self.line_12 = QtWidgets.QFrame(self.page_1)
        self.line_12.setGeometry(QtCore.QRect(600, 180, 61, 21))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_3 = QtWidgets.QFrame(self.page_1)
        self.line_3.setGeometry(QtCore.QRect(160, 100, 61, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(180, 160, 181, 16))
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(self.page_1)
        self.line_4.setGeometry(QtCore.QRect(160, 350, 381, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.page_1)
        self.label_4.setGeometry(QtCore.QRect(180, 130, 171, 16))
        self.label_4.setObjectName("label_4")
        self.line_15 = QtWidgets.QFrame(self.page_1)
        self.line_15.setGeometry(QtCore.QRect(1020, 190, 21, 171))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_20 = QtWidgets.QFrame(self.page_1)
        self.line_20.setGeometry(QtCore.QRect(540, 390, 3, 61))
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.label_18 = QtWidgets.QLabel(self.page_1)
        self.label_18.setGeometry(QtCore.QRect(230, 380, 41, 16))
        self.label_18.setObjectName("label_18")
        self.label_11 = QtWidgets.QLabel(self.page_1)
        self.label_11.setGeometry(QtCore.QRect(180, 190, 191, 16))
        self.label_11.setObjectName("label_11")
        self.combobox_MOS = QtWidgets.QComboBox(self.page_1)
        self.combobox_MOS.setGeometry(QtCore.QRect(790, 130, 221, 22))
        self.combobox_MOS.setObjectName("combobox_MOS")
        self.combobox_MOS.addItem("")
        self.combobox_MOS.addItem("")
        self.combobox_MOS.addItem("")
        self.combobox_MOS.addItem("")
        self.combobox_MOS.addItem("")
        self.label_Tpll = QtWidgets.QLineEdit(self.page_1)
        self.label_Tpll.setGeometry(QtCore.QRect(410, 190, 111, 21))
        self.label_Tpll.setObjectName("label_Tpll")
        self.line_16 = QtWidgets.QFrame(self.page_1)
        self.line_16.setGeometry(QtCore.QRect(260, 380, 281, 21))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.boton_esquema = QtWidgets.QPushButton(self.page_1)
        self.boton_esquema.setGeometry(QtCore.QRect(160, 480, 191, 28))
        self.boton_esquema.setObjectName("boton_esquema")
        self.label_Pb = QtWidgets.QLineEdit(self.page_1)
        self.label_Pb.setGeometry(QtCore.QRect(390, 410, 111, 21))
        self.label_Pb.setObjectName("label_Pb")
        self.label_15 = QtWidgets.QLabel(self.page_1)
        self.label_15.setGeometry(QtCore.QRect(620, 210, 141, 21))
        self.label_15.setObjectName("label_15")
        self.label_BWres = QtWidgets.QLineEdit(self.page_1)
        self.label_BWres.setGeometry(QtCore.QRect(410, 250, 111, 21))
        self.label_BWres.setObjectName("label_BWres")
        self.line_8 = QtWidgets.QFrame(self.page_1)
        self.line_8.setGeometry(QtCore.QRect(600, 155, 431, 31))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_18 = QtWidgets.QFrame(self.page_1)
        self.line_18.setGeometry(QtCore.QRect(160, 390, 3, 61))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_2 = QtWidgets.QFrame(self.page_1)
        self.line_2.setGeometry(QtCore.QRect(300, 100, 241, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_BWst = QtWidgets.QLineEdit(self.page_1)
        self.label_BWst.setGeometry(QtCore.QRect(900, 410, 111, 21))
        self.label_BWst.setObjectName("label_BWst")
        self.label_20 = QtWidgets.QLabel(self.page_1)
        self.label_20.setGeometry(QtCore.QRect(670, 380, 101, 16))
        self.label_20.setObjectName("label_20")
        self.label_Nc = QtWidgets.QLineEdit(self.page_1)
        self.label_Nc.setGeometry(QtCore.QRect(410, 130, 111, 21))
        self.label_Nc.setObjectName("label_Nc")
        self.label_3 = QtWidgets.QLabel(self.page_1)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.line_10 = QtWidgets.QFrame(self.page_1)
        self.line_10.setGeometry(QtCore.QRect(1020, 110, 21, 61))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_17 = QtWidgets.QFrame(self.page_1)
        self.line_17.setGeometry(QtCore.QRect(160, 380, 61, 21))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line = QtWidgets.QFrame(self.page_1)
        self.line.setGeometry(QtCore.QRect(142, 110, 41, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_Nl = QtWidgets.QLineEdit(self.page_1)
        self.label_Nl.setGeometry(QtCore.QRect(410, 160, 111, 21))
        self.label_Nl.setObjectName("label_Nl")
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 371, 31))
        self.label_2.setObjectName("label_2")
        self.combobox_retardo_total = QtWidgets.QComboBox(self.page_1)
        self.combobox_retardo_total.setGeometry(QtCore.QRect(790, 310, 221, 22))
        self.combobox_retardo_total.setObjectName("combobox_retardo_total")
        self.combobox_retardo_total.addItem("")
        self.combobox_retardo_total.addItem("")
        self.combobox_retardo_total.addItem("")
        self.label_8 = QtWidgets.QLabel(self.page_1)
        self.label_8.setGeometry(QtCore.QRect(180, 250, 221, 16))
        self.label_8.setObjectName("label_8")
        self.line_23 = QtWidgets.QFrame(self.page_1)
        self.line_23.setGeometry(QtCore.QRect(780, 380, 251, 21))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.label_6 = QtWidgets.QLabel(self.page_1)
        self.label_6.setGeometry(QtCore.QRect(240, 220, 55, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.boton_siguiente = QtWidgets.QPushButton(self.page_1)
        self.boton_siguiente.setGeometry(QtCore.QRect(940, 480, 93, 28))
        self.boton_siguiente.setObjectName("boton_siguiente")
        self.line_9 = QtWidgets.QFrame(self.page_1)
        self.line_9.setGeometry(QtCore.QRect(710, 100, 321, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_16 = QtWidgets.QLabel(self.page_1)
        self.label_16.setGeometry(QtCore.QRect(620, 240, 121, 21))
        self.label_16.setObjectName("label_16")
        self.line_5 = QtWidgets.QFrame(self.page_1)
        self.line_5.setGeometry(QtCore.QRect(530, 110, 21, 251))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_23 = QtWidgets.QLabel(self.page_1)
        self.label_23.setGeometry(QtCore.QRect(620, 310, 131, 16))
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.page_1)
        self.label_22.setGeometry(QtCore.QRect(620, 410, 231, 16))
        self.label_22.setObjectName("label_22")
        self.combobox_encap_wan = QtWidgets.QComboBox(self.page_1)
        self.combobox_encap_wan.setGeometry(QtCore.QRect(410, 310, 111, 22))
        self.combobox_encap_wan.setObjectName("combobox_encap_wan")
        self.combobox_encap_wan.addItem("")
        self.combobox_encap_wan.addItem("")
        self.combobox_encap_wan.addItem("")
        self.combobox_encap_wan.addItem("")
        self.line_19 = QtWidgets.QFrame(self.page_1)
        self.line_19.setGeometry(QtCore.QRect(160, 435, 381, 31))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.label_12 = QtWidgets.QLabel(self.page_1)
        self.label_12.setGeometry(QtCore.QRect(670, 100, 55, 16))
        self.label_12.setObjectName("label_12")
        self.line_24 = QtWidgets.QFrame(self.page_1)
        self.line_24.setGeometry(QtCore.QRect(600, 430, 431, 41))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.label_Rr = QtWidgets.QLineEdit(self.page_1)
        self.label_Rr.setGeometry(QtCore.QRect(790, 210, 221, 21))
        self.label_Rr.setObjectName("label_Rr")
        self.line_7 = QtWidgets.QFrame(self.page_1)
        self.line_7.setGeometry(QtCore.QRect(600, 110, 3, 61))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_Pll = QtWidgets.QLineEdit(self.page_1)
        self.label_Pll.setGeometry(QtCore.QRect(410, 220, 111, 21))
        self.label_Pll.setObjectName("label_Pll")
        self.combobox_tuneles = QtWidgets.QComboBox(self.page_1)
        self.combobox_tuneles.setGeometry(QtCore.QRect(410, 280, 111, 22))
        self.combobox_tuneles.setObjectName("combobox_tuneles")
        self.combobox_tuneles.addItem("")
        self.combobox_tuneles.addItem("")
        self.combobox_tuneles.addItem("")
        self.line_22 = QtWidgets.QFrame(self.page_1)
        self.line_22.setGeometry(QtCore.QRect(600, 380, 61, 21))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(250, 180, 261, 16))
        self.label_24.setObjectName("label_24")
        self.line_26 = QtWidgets.QFrame(self.page_2)
        self.line_26.setGeometry(QtCore.QRect(240, 360, 731, 20))
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.label_25 = QtWidgets.QLabel(self.page_2)
        self.label_25.setGeometry(QtCore.QRect(250, 150, 261, 16))
        self.label_25.setObjectName("label_25")
        self.label_RetardoAntijitter2 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoAntijitter2.setGeometry(QtCore.QRect(860, 240, 81, 16))
        self.label_RetardoAntijitter2.setObjectName("label_RetardoAntijitter2")
        self.label_cumple_o_no = QtWidgets.QLabel(self.page_2)
        self.label_cumple_o_no.setGeometry(QtCore.QRect(280, 430, 91, 16))
        self.label_cumple_o_no.setObjectName("label_cumple_o_no")
        self.label_26 = QtWidgets.QLabel(self.page_2)
        self.label_26.setGeometry(QtCore.QRect(250, 270, 261, 16))
        self.label_26.setObjectName("label_26")
        self.label_RetardoRed15 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoRed15.setGeometry(QtCore.QRect(640, 210, 81, 16))
        self.label_RetardoRed15.setObjectName("label_RetardoRed15")
        self.line_27 = QtWidgets.QFrame(self.page_2)
        self.line_27.setGeometry(QtCore.QRect(240, 100, 731, 20))
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.label_RetardoAlgoritmico15 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoAlgoritmico15.setGeometry(QtCore.QRect(640, 180, 81, 16))
        self.label_RetardoAlgoritmico15.setObjectName("label_RetardoAlgoritmico15")
        self.label_PaquetesBuffer2 = QtWidgets.QLabel(self.page_2)
        self.label_PaquetesBuffer2.setGeometry(QtCore.QRect(860, 330, 111, 16))
        self.label_PaquetesBuffer2.setObjectName("label_PaquetesBuffer2")
        self.line_28 = QtWidgets.QFrame(self.page_2)
        self.line_28.setGeometry(QtCore.QRect(240, 70, 731, 20))
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.page_2)
        self.line_29.setGeometry(QtCore.QRect(960, 80, 20, 401))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.label_27 = QtWidgets.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(250, 120, 71, 16))
        self.label_27.setObjectName("label_27")
        self.label_Retardodecodificacion2 = QtWidgets.QLabel(self.page_2)
        self.label_Retardodecodificacion2.setGeometry(QtCore.QRect(860, 270, 71, 16))
        self.label_Retardodecodificacion2.setObjectName("label_Retardodecodificacion2")
        self.label_RetardoAntijitter15 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoAntijitter15.setGeometry(QtCore.QRect(640, 240, 91, 16))
        self.label_RetardoAntijitter15.setObjectName("label_RetardoAntijitter15")
        self.line_30 = QtWidgets.QFrame(self.page_2)
        self.line_30.setGeometry(QtCore.QRect(230, 80, 21, 401))
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.label_28 = QtWidgets.QLabel(self.page_2)
        self.label_28.setGeometry(QtCore.QRect(250, 90, 281, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.page_2)
        self.label_29.setGeometry(QtCore.QRect(250, 210, 261, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page_2)
        self.label_30.setGeometry(QtCore.QRect(840, 120, 121, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.page_2)
        self.label_31.setGeometry(QtCore.QRect(610, 120, 121, 16))
        self.label_31.setObjectName("label_31")
        self.label_RetardoTotal2 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoTotal2.setGeometry(QtCore.QRect(860, 300, 71, 16))
        self.label_RetardoTotal2.setObjectName("label_RetardoTotal2")
        self.label_RetardoTotal15 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoTotal15.setGeometry(QtCore.QRect(640, 300, 81, 16))
        self.label_RetardoTotal15.setObjectName("label_RetardoTotal15")
        self.SiguienteR = QtWidgets.QPushButton(self.page_2)
        self.SiguienteR.setGeometry(QtCore.QRect(860, 440, 93, 28))
        self.SiguienteR.setObjectName("SiguienteR")
        self.label_RetardoAlgoritmico2 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoAlgoritmico2.setGeometry(QtCore.QRect(860, 180, 81, 16))
        self.label_RetardoAlgoritmico2.setObjectName("label_RetardoAlgoritmico2")
        self.label_RetardoRed2 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoRed2.setGeometry(QtCore.QRect(860, 210, 81, 16))
        self.label_RetardoRed2.setObjectName("label_RetardoRed2")
        self.label_tamanoAntijitter = QtWidgets.QLabel(self.page_2)
        self.label_tamanoAntijitter.setGeometry(QtCore.QRect(450, 390, 55, 16))
        self.label_tamanoAntijitter.setObjectName("label_tamanoAntijitter")
        self.label_32 = QtWidgets.QLabel(self.page_2)
        self.label_32.setGeometry(QtCore.QRect(370, 430, 161, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.page_2)
        self.label_33.setGeometry(QtCore.QRect(250, 240, 261, 16))
        self.label_33.setObjectName("label_33")
        self.label_RetardoDecodificacion15 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoDecodificacion15.setGeometry(QtCore.QRect(640, 270, 81, 16))
        self.label_RetardoDecodificacion15.setObjectName("label_RetardoDecodificacion15")
        self.label_PaquetesBuffer15 = QtWidgets.QLabel(self.page_2)
        self.label_PaquetesBuffer15.setGeometry(QtCore.QRect(640, 330, 121, 16))
        self.label_PaquetesBuffer15.setObjectName("label_PaquetesBuffer15")
        self.label_34 = QtWidgets.QLabel(self.page_2)
        self.label_34.setGeometry(QtCore.QRect(510, 390, 381, 16))
        self.label_34.setObjectName("label_34")
        self.line_31 = QtWidgets.QFrame(self.page_2)
        self.line_31.setGeometry(QtCore.QRect(240, 470, 731, 20))
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.label_RetardoConjunto15 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoConjunto15.setGeometry(QtCore.QRect(640, 150, 91, 16))
        self.label_RetardoConjunto15.setObjectName("label_RetardoConjunto15")
        self.label_35 = QtWidgets.QLabel(self.page_2)
        self.label_35.setGeometry(QtCore.QRect(250, 300, 261, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.page_2)
        self.label_36.setGeometry(QtCore.QRect(250, 330, 311, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.page_2)
        self.label_37.setGeometry(QtCore.QRect(350, 0, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.page_2)
        self.label_38.setGeometry(QtCore.QRect(250, 390, 181, 16))
        self.label_38.setObjectName("label_38")
        self.label_RetardoConjunto2 = QtWidgets.QLabel(self.page_2)
        self.label_RetardoConjunto2.setGeometry(QtCore.QRect(860, 150, 71, 16))
        self.label_RetardoConjunto2.setObjectName("label_RetardoConjunto2")
        self.label_VPS = QtWidgets.QLabel(self.page_2)
        self.label_VPS.setGeometry(QtCore.QRect(540, 90, 131, 16))
        self.label_VPS.setObjectName("label_VPS")
        self.label_47 = QtWidgets.QLabel(self.page_2)
        self.label_47.setGeometry(QtCore.QRect(590, 430, 111, 16))
        self.label_47.setObjectName("label_47")
        self.label_retardo_total = QtWidgets.QLabel(self.page_2)
        self.label_retardo_total.setGeometry(QtCore.QRect(694, 430, 91, 20))
        self.label_retardo_total.setText("")
        self.label_retardo_total.setObjectName("label_retardo_total")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_Correo = QtWidgets.QPushButton(self.page_3)
        self.pushButton_Correo.setGeometry(QtCore.QRect(260, 380, 201, 28))
        self.pushButton_Correo.setObjectName("pushButton_Correo")
        self.line_32 = QtWidgets.QFrame(self.page_3)
        self.line_32.setGeometry(QtCore.QRect(970, 90, 21, 371))
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.label_39 = QtWidgets.QLabel(self.page_3)
        self.label_39.setGeometry(QtCore.QRect(320, 10, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.line_33 = QtWidgets.QFrame(self.page_3)
        self.line_33.setGeometry(QtCore.QRect(230, 450, 751, 16))
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.pushButton_Inicio = QtWidgets.QPushButton(self.page_3)
        self.pushButton_Inicio.setGeometry(QtCore.QRect(790, 380, 93, 28))
        self.pushButton_Inicio.setObjectName("pushButton_Inicio")
        self.label_40 = QtWidgets.QLabel(self.page_3)
        self.label_40.setGeometry(QtCore.QRect(490, 140, 231, 16))
        self.label_40.setObjectName("label_40")
        self.label_BWIIRTP = QtWidgets.QLabel(self.page_3)
        self.label_BWIIRTP.setGeometry(QtCore.QRect(580, 190, 171, 16))
        self.label_BWIIRTP.setObjectName("label_BWIIRTP")
        self.label_41 = QtWidgets.QLabel(self.page_3)
        self.label_41.setGeometry(QtCore.QRect(270, 190, 55, 16))
        self.label_41.setObjectName("label_41")
        self.line_34 = QtWidgets.QFrame(self.page_3)
        self.line_34.setGeometry(QtCore.QRect(230, 120, 751, 16))
        self.line_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.label_42 = QtWidgets.QLabel(self.page_3)
        self.label_42.setGeometry(QtCore.QRect(270, 270, 55, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.page_3)
        self.label_43.setGeometry(QtCore.QRect(750, 330, 191, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_3)
        self.label_44.setGeometry(QtCore.QRect(770, 140, 201, 16))
        self.label_44.setObjectName("label_44")
        self.label_BWstCRTP = QtWidgets.QLabel(self.page_3)
        self.label_BWstCRTP.setGeometry(QtCore.QRect(820, 270, 161, 16))
        self.label_BWstCRTP.setObjectName("label_BWstCRTP")
        self.label_45 = QtWidgets.QLabel(self.page_3)
        self.label_45.setGeometry(QtCore.QRect(550, 330, 101, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.page_3)
        self.label_46.setGeometry(QtCore.QRect(240, 100, 181, 16))
        self.label_46.setObjectName("label_46")
        self.comboBox_Codecs = QtWidgets.QComboBox(self.page_3)
        self.comboBox_Codecs.setGeometry(QtCore.QRect(540, 380, 141, 22))
        self.comboBox_Codecs.setObjectName("comboBox_Codecs")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.comboBox_Codecs.addItem("")
        self.line_35 = QtWidgets.QFrame(self.page_3)
        self.line_35.setGeometry(QtCore.QRect(220, 90, 21, 371))
        self.line_35.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.label_BWstRTP = QtWidgets.QLabel(self.page_3)
        self.label_BWstRTP.setGeometry(QtCore.QRect(820, 190, 161, 16))
        self.label_BWstRTP.setObjectName("label_BWstRTP")
        self.label_BWIICRTP = QtWidgets.QLabel(self.page_3)
        self.label_BWIICRTP.setGeometry(QtCore.QRect(580, 270, 171, 16))
        self.label_BWIICRTP.setObjectName("label_BWIICRTP")
        self.line_36 = QtWidgets.QFrame(self.page_3)
        self.line_36.setGeometry(QtCore.QRect(230, 80, 751, 16))
        self.line_36.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.label_hora_cargada = QtWidgets.QLabel(self.page_3)
        self.label_hora_cargada.setGeometry(QtCore.QRect(460, 100, 221, 16))
        self.label_hora_cargada.setObjectName("label_hora_cargada")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1317, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Probabilidad de llamada (%)"))
        self.label_9.setText(_translate("MainWindow", "Encapsulación WAN"))
        self.combobox_retardo_boca_oido.setItemText(0, _translate("MainWindow", "Muy satisfecho"))
        self.combobox_retardo_boca_oido.setItemText(1, _translate("MainWindow", "Satisfecho"))
        self.combobox_retardo_boca_oido.setItemText(2, _translate("MainWindow", "Algunos usuarios insatisfechos"))
        self.combobox_retardo_boca_oido.setItemText(3, _translate("MainWindow", "Muchos usuarios insatisfechos"))
        self.combobox_retardo_boca_oido.setItemText(4, _translate("MainWindow", "Todos los usuarios insatisfechos"))
        self.label_10.setText(_translate("MainWindow", "Túneles"))
        self.label.setText(_translate("MainWindow", "Calculadora VoIP"))
        self.label_19.setText(_translate("MainWindow", "Probabilidad de bloqueo (%)"))
        self.label_13.setText(_translate("MainWindow", "Mean Opinioin Score"))
        self.label_14.setText(_translate("MainWindow", "QoS"))
        self.label_17.setText(_translate("MainWindow", "Nivel de retardo boca-oido"))
        self.label_5.setText(_translate("MainWindow", "Número de líneas por cliente"))
        self.label_4.setText(_translate("MainWindow", "Número de empresas cliente"))
        self.label_18.setText(_translate("MainWindow", "GoS"))
        self.label_11.setText(_translate("MainWindow", "Tiempo medio de llamada (min)"))
        self.combobox_MOS.setItemText(0, _translate("MainWindow", "Excelente"))
        self.combobox_MOS.setItemText(1, _translate("MainWindow", "Bueno"))
        self.combobox_MOS.setItemText(2, _translate("MainWindow", "Aceptable"))
        self.combobox_MOS.setItemText(3, _translate("MainWindow", "Bajo"))
        self.combobox_MOS.setItemText(4, _translate("MainWindow", "Malo"))
        self.boton_esquema.setText(_translate("MainWindow", "Mostrar esquema de la red"))
        self.label_15.setText(_translate("MainWindow", "Retardo de red (ms)"))
        self.label_20.setText(_translate("MainWindow", "Ancho de Banda"))
        self.label_3.setText(_translate("MainWindow", "Llamadas"))
        self.label_2.setText(_translate("MainWindow", "Introduzca los parámetros que se piden a continuación:"))
        self.combobox_retardo_total.setItemText(0, _translate("MainWindow", "Aceptable"))
        self.combobox_retardo_total.setItemText(1, _translate("MainWindow", "Moderado"))
        self.combobox_retardo_total.setItemText(2, _translate("MainWindow", "Inaceptable"))
        self.label_8.setText(_translate("MainWindow", "Ancho de banda de reserva (%)"))
        self.boton_siguiente.setText(_translate("MainWindow", "Siguiente"))
        self.label_16.setText(_translate("MainWindow", "Jitter (ms)"))
        self.label_23.setText(_translate("MainWindow", "Retardo total de VoIP"))
        self.label_22.setText(_translate("MainWindow", "Ancho de Banda con SIPTRUNK (Mbps)"))
        self.combobox_encap_wan.setItemText(0, _translate("MainWindow", "PPPoE"))
        self.combobox_encap_wan.setItemText(1, _translate("MainWindow", "PPP"))
        self.combobox_encap_wan.setItemText(2, _translate("MainWindow", "Ethernet"))
        self.combobox_encap_wan.setItemText(3, _translate("MainWindow", "Ethernet 802.1q"))
        self.label_12.setText(_translate("MainWindow", "QoE"))
        self.combobox_tuneles.setItemText(0, _translate("MainWindow", "MPLS"))
        self.combobox_tuneles.setItemText(1, _translate("MainWindow", "IPSEC"))
        self.combobox_tuneles.setItemText(2, _translate("MainWindow", "L2TP"))
        self.label_24.setText(_translate("MainWindow", "Retardo Algoritmico"))
        self.label_25.setText(_translate("MainWindow", "Retardo Conjunto, CODEC+paquetización"))
        self.label_RetardoAntijitter2.setText(_translate("MainWindow", "-"))
        self.label_cumple_o_no.setText(_translate("MainWindow", "-"))
        self.label_26.setText(_translate("MainWindow", "Retardo de decodificación en el destino"))
        self.label_RetardoRed15.setText(_translate("MainWindow", "-"))
        self.label_RetardoAlgoritmico15.setText(_translate("MainWindow", "-"))
        self.label_PaquetesBuffer2.setText(_translate("MainWindow", "-"))
        self.label_27.setText(_translate("MainWindow", "RETARDOS"))
        self.label_Retardodecodificacion2.setText(_translate("MainWindow", "-"))
        self.label_RetardoAntijitter15.setText(_translate("MainWindow", "-"))
        self.label_28.setText(_translate("MainWindow", "La VPS(Voice Payload) del CODEC elegido es: "))
        self.label_29.setText(_translate("MainWindow", "Retardo de Red"))
        self.label_30.setText(_translate("MainWindow", "Buffer Antijitter x2"))
        self.label_31.setText(_translate("MainWindow", "Buffer Antijitter x1.5"))
        self.label_RetardoTotal2.setText(_translate("MainWindow", "-"))
        self.label_RetardoTotal15.setText(_translate("MainWindow", "-"))
        self.SiguienteR.setText(_translate("MainWindow", "Siguiente"))
        self.label_RetardoAlgoritmico2.setText(_translate("MainWindow", "-"))
        self.label_RetardoRed2.setText(_translate("MainWindow", "-"))
        self.label_tamanoAntijitter.setText(_translate("MainWindow", "-"))
        self.label_32.setText(_translate("MainWindow", "las condiciones de retardo"))
        self.label_33.setText(_translate("MainWindow", "Retardo del Buffer antijitter"))
        self.label_RetardoDecodificacion15.setText(_translate("MainWindow", "-"))
        self.label_PaquetesBuffer15.setText(_translate("MainWindow", "-"))
        self.label_34.setText(_translate("MainWindow", "veces el jitter máximo para satisfacer las condiciones de retardo"))
        self.label_RetardoConjunto15.setText(_translate("MainWindow", "-"))
        self.label_35.setText(_translate("MainWindow", "Retardo Total "))
        self.label_36.setText(_translate("MainWindow", "Número de paquetes RTP almacenados en el buffer"))
        self.label_37.setText(_translate("MainWindow", "Cálculo del retardo total"))
        self.label_38.setText(_translate("MainWindow", "El buffer antijitter debe ser de:"))
        self.label_RetardoConjunto2.setText(_translate("MainWindow", "-"))
        self.label_VPS.setText(_translate("MainWindow", "-"))
        self.label_47.setText(_translate("MainWindow", "Retardo total: "))
        self.pushButton_Correo.setText(_translate("MainWindow", "Mandar el informe de resultados"))
        self.label_39.setText(_translate("MainWindow", "Cálculo del ancho de banda"))
        self.pushButton_Inicio.setText(_translate("MainWindow", "Inicio"))
        self.label_40.setText(_translate("MainWindow", "Ancho de banda de una llamada (BWII) "))
        self.label_BWIIRTP.setText(_translate("MainWindow", "-"))
        self.label_41.setText(_translate("MainWindow", "RTP"))
        self.label_42.setText(_translate("MainWindow", "CRTP"))
        self.label_43.setText(_translate("MainWindow", "Cambiar parámetros de entrada"))
        self.label_44.setText(_translate("MainWindow", "Ancho de banda SIPTRUNK (BWst)"))
        self.label_BWstCRTP.setText(_translate("MainWindow", "-"))
        self.label_45.setText(_translate("MainWindow", "Elegir otro codec"))
        self.label_46.setText(_translate("MainWindow", "Tráfico de la hora cargada:"))
        self.comboBox_Codecs.setItemText(0, _translate("MainWindow", "G711"))
        self.comboBox_Codecs.setItemText(1, _translate("MainWindow", "G729"))
        self.comboBox_Codecs.setItemText(2, _translate("MainWindow", "G723163"))
        self.comboBox_Codecs.setItemText(3, _translate("MainWindow", "G723153"))
        self.comboBox_Codecs.setItemText(4, _translate("MainWindow", "G72632"))
        self.comboBox_Codecs.setItemText(5, _translate("MainWindow", "G72624"))
        self.comboBox_Codecs.setItemText(6, _translate("MainWindow", "G728"))
        self.comboBox_Codecs.setItemText(7, _translate("MainWindow", "G722"))
        self.comboBox_Codecs.setItemText(8, _translate("MainWindow", "Codecibcmode2"))
        self.comboBox_Codecs.setItemText(9, _translate("MainWindow", "Codecibcmode3"))
        self.label_BWstRTP.setText(_translate("MainWindow", "-"))
        self.label_BWIICRTP.setText(_translate("MainWindow", "-"))
        self.label_hora_cargada.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

