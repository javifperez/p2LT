"""
Autores: Javi Fernandez y Juan Pablo Cano

"""
import funciones as funciones
import numpy as np
import webbrowser 
import smtplib
from main_ui import *

#Guardamos en vectores las propiedades de los códecs y los valores de Erlang
codecs = np.loadtxt(open("tabla_codecs.csv", "rb"), delimiter=";")
era = np.loadtxt(open("tabla_erlang.csv", "rb"), delimiter=";")
#inicializamos variables globales en el programa para usarlas posteriormente
vector_retardos = [] #vector qua guarda los retardos calculados
parametros_codec = []#vector que almacena los parametros de un codec en concreto
BWll = []#Vector de anchos de banda
BWst = []#vector de anchos de banda con calidad de servicio
cambiar_codec = 0#booleano que nos dice si tenemos que cambiar de codec
indice_codec = 0#entero que contiene el indice de un codec
Rt = 0#retardo total
bht = 0#trafico de la hora cargada
BWres = 0#porcentaje de ancho de banda de reserva


#definimos la clase que pertenece a la ventana principal
class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    #funcion que inicializa la interfaz grafica
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.mostrarPag1()
        
    #funcion que muestra la primera ventana
    def mostrarPag1(self):
        
        global cambiar_codec
        
        self.stackedWidget.setCurrentWidget(self.page_1)#mostramos la pagina 1
        
        if (cambiar_codec == 0):#si no hay que cambiar el codec activamos la casilla de selección 
                                #del codec
            self.combobox_MOS.setEnabled(1)
        
        cambiar_codec = 0
        self.boton_siguiente.clicked.connect(self.mostrarPag2)
        self.boton_esquema.clicked.connect(self.abrir_pagina)
        
    #funcion que muestra la segunda ventana   
    def mostrarPag2(self):
        
        self.valorespag1()
        self.realizarCalculos()
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.valorespag2()
        self.SiguienteR.clicked.connect(self.mostrarPag3)
        
    #funcion que muestra la tercera ventana
    def mostrarPag3(self):
        
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.valorespag3()
        self.comboBox_Codecs.activated.connect(self.combo_codec)
        self.pushButton_Inicio.clicked.connect(self.mostrarPag1)
        self.pushButton_Correo.clicked.connect(self.mandacorreo)
        
    #funcion que asigna los valores de entrada a las variables
    def valorespag1(self):
        global mos, Nc, Nl, Tpll, Pll, BWres, tuneles, encapsulado, Pb, Rr, Jitter
        global rboca_oido, retardo_total, BWst

        #Asignamos valor a las variables desde la interfez grafica
        #de tipo label
        Nc=self.label_Nc.text()#numero de empresas cliente
        Nl=self.label_Nl.text()#numero de lineas por cliente
        Tpll=self.label_Tpll.text()#tiempo medio de llamada
        Pll=self.label_Pll.text()#probabilidad de llamada
        BWres=self.label_BWres.text()#porcentaje de ancho de banda de reserva
        Pb=self.label_Pb.text()#probabilidad de bloqueo
        Rr=self.label_Rr.text()#retardo de la red
        Jitter=self.label_J.text()#jitter
        BWst=self.label_BWst.text()#ancho de banda contratado con el proveedor SIPTRUNK
        
        #Inicializamos con el string "0" las variables anteriores para
        #que no haya problema al pasarlas a int
        if(Nc==""):
            Nc="0"
            Nl="0"
            Tpll="0"
            Pll="0"
            BWres="0"
            Pb="0"
            Rr="0"
            Jitter="0"
            BWst="0"

        #tipo comboBox
        mos = self.combobox_MOS.currentText()#Mean Opinion Score
        tuneles = self.combobox_tuneles.currentText()#tipo de conmutacion en la red con el proveedor
        rboca_oido = self.combobox_retardo_boca_oido.currentText()#retardo boca a oido
        encapsulado = self.combobox_encap_wan.currentText()#tipo de encapsulado
        retardo_total = self.combobox_retardo_total.currentText()#retardo VoIP
    #funcion encargada de hacer los calculos  con los datos de entrada
    def realizarCalculos(self):
        global BWst, bht, BWll, vector_retardos, mos_numerico, indice_codec
        global parametros_codec
        
        #Segun el MOS elegido anteriormente, asignamos un valor entero que va desde el 1 al 5
        mos_numerico=funciones.transformaMOS(mos)
        
        #Si no hay que cambiar codec vemos elegimos el codec con el que vamos a trabajar
        #y le asignamos un numero
        if cambiar_codec==0: 
            indice_codec = funciones.elegir_codec(mos_numerico, codecs)
            self.comboBox_Codecs.setCurrentIndex(indice_codec)
        #Volcamos en un vector todos los parámetros sólo del codec elegido 
        parametros_codec = codecs[indice_codec,:]
        
        #Realizamos los calculos
        BWll = funciones.calculo_BWll(parametros_codec[0],parametros_codec[1],parametros_codec[3])
        bht = funciones.calculo_BHT(int(Nc),int(Nl),int(Tpll))
        BWst = funciones.calculo_BWST(bht,int(Pll),BWll[0],BWll[1])
        vector_retardos = funciones.retardo_total(int(Rr), int(Jitter), parametros_codec[4], parametros_codec[1], era[indice_codec])
   #Función que muestra los valores que aparecen en la página 2
    def valorespag2(self):
        global Rt, rboca_oido, cumple, tamano_antijitter, retardofin
        
        #Mostramos los valores de los resultados obtenidos en la función anterior
        self.label_VPS.setText(str(parametros_codec[4]))
        self.label_RetardoConjunto15.setText(str(vector_retardos[0]) + ' ms')
        self.label_RetardoConjunto2.setText(str(vector_retardos[0]) + ' ms')
        self.label_RetardoAlgoritmico15.setText(str(vector_retardos[1]) + ' ms')
        self.label_RetardoAlgoritmico2.setText(str(vector_retardos[1]) + ' ms')
        self.label_RetardoRed15.setText(str(vector_retardos[2]) + ' ms')
        self.label_RetardoRed2.setText(str(vector_retardos[2]) + ' ms')
        self.label_RetardoAntijitter15.setText(str(vector_retardos[3]) + ' ms')
        self.label_RetardoAntijitter2.setText(str(vector_retardos[4]) + ' ms')
        self.label_RetardoDecodificacion15.setText(str(vector_retardos[5]) + ' ms')
        self.label_Retardodecodificacion2.setText(str(vector_retardos[5]) + ' ms')
        self.label_RetardoTotal15.setText(str(vector_retardos[6]) + ' ms')
        self.label_RetardoTotal2.setText(str(vector_retardos[7]) + ' ms')
        self.label_PaquetesBuffer15.setText(str(vector_retardos[8]) + ' paquetes')
        self.label_PaquetesBuffer2.setText(str(vector_retardos[9]) + ' paquetes')
        #Escogemos un Rt en función del nivel de satisfacción
        Rt=funciones.eligeRt(retardo_total)
        #Vemos si los valores obtenidos cumplen o no
        if (Rt>=vector_retardos[6]):
            self.label_retardo_total.setText(str(vector_retardos[6])) 
            self.label_tamanoAntijitter.setText("x1.5")
            self.label_cumple_o_no.setText("CUMPLE")
            self.label_RetardoTotal15.setStyleSheet("background-color: lightgreen")
            self.label_RetardoTotal2.setStyleSheet("background-color: red")
        elif(Rt>=vector_retardos[7]):
            self.labelretardo_total.setText(str(vector_retardos[6]))
            self.label_tamanoAntijitter.setText("x2")
            self.label_cumple_o_no.setText("CUMPLE")
            self.label_RetardoTotal15.setStyleSheet("background-color: lightgreen")
            self.label_RetardoTotal2.setStyleSheet("background-color: red")
        elif(Rt>=vector_retardos[6] and Rt>=vector_retardos[7]):
            self.label_retardo_total.setText(str(vector_retardos[6])) 
            self.label_tamanoAntijitter.setText("x2")
            self.label_cumple_o_no.setText("CUMPLE")
            self.label_RetardoTotal15.setStyleSheet("background-color: lightgreen")
            self.label_RetardoTotal2.setStyleSheet("background-color: lightgreen")
        elif(Rt<vector_retardos[6] and Rt<vector_retardos[7]):
            self.label_retardo_total.setText(str(vector_retardos[6]))
            self.label_tamanoAntijitter.setText(" ")
            self.label_cumple_o_no.setText("NO CUMPLE")
            self.label_RetardoTotal15.setStyleSheet("background-color: red")
            self.label_RetardoTotal2.setStyleSheet("background-color: red")
        #Guardamos variables para la posterior generación del informe   
        cumple=self.label_cumple_o_no.text()
        tamano_antijitter=self.label_tamanoAntijitter.text()
        retardofin=self.label_retardo_total.text()
        
    #Fución que muestra los valores de la pagina 3 y genera el informe
    def valorespag3(self): 
        global codec_elegido, informe
        
        #guardamos codec que hemos elegido para mostrarlo en el informe
        codec_elegido= self.comboBox_Codecs.currentText()
        
        #Mostramos en la pagina 3 los resultados finales
        self.label_hora_cargada.setText(str(bht) + ' Erlangs')
        self.label_BWIIRTP.setText(str(BWll[0]) + ' Kbps')
        self.label_BWstRTP.setText(str(BWst[0]) + ' Mbps')
        self.label_BWIICRTP.setText(str(BWll[1]) + ' Kbps')
        self.label_BWstCRTP.setText(str(BWst[1]) + ' Mbps')
        
        #Generamos el informe y lo guardamos en 3 cadenas de caracteres
        inicial=("SITUACION DEFINIDA COMO ENTRADA \n\n || Numero de empresas: "+str(Nc)+
                 " || Numero de lineas por cliente: "+str(Nl)+ "\n || Tiempo medio de la llamada: "
                 +str(Tpll)+"min"+" || Probabilidd de llamada: "+str(Pll)+ "\n || Tuneles: "+
                 str(tuneles)+ " || Encapsulacion: "+str(encapsulado)+ "\n || MOS: "
                 +str(mos)+ " || Retardo de red: "+str(Rr)+ "\n || Jitter(ms): "+str(Jitter)+
                 " || Nivel de retardo boca oido: "+str(rboca_oido)+ "\n || Retardo total VoIP: "+str(retardo_total)+
                 " || Probabilidad de bloqueo: "+str(Pb)+ "\n || Ancho de banda con SIPTrunk(Mbps)"+
                 str(BWst)+"Mbps")
        
        iretardos=("\n\n     RESULTADOS DEL CALCULO DE LOS RETARDOS \n\n"+
                   " || Retardo conjunto (CODEC+paquetizacion) Jitter: 1,5: "+str(vector_retardos[0] )+"ms"
                   +" \n || Retardo conjunto (CODEC+paquetizacion) Jitter: 2: "+str(vector_retardos[0])+"ms"
                   +"\n || Retardo algoritmico: Jitter: 1,5: "+str(vector_retardos[1])+"ms"
                   +" || Retardo algoritmico: Jitter: 2: "+str(vector_retardos[1])+"ms"
                   +"\n || Retardo de Red: Jitter: 1,5: "+str(vector_retardos[2])+"ms"
                   +" || Retardo de Red: Jitter: 2: "+str(vector_retardos[2])+"ms"
                   +"\n || Retardo de buffer antijitter: Jitter: 1,5: "+str(vector_retardos[3])+"ms"
                   +"\n || Retardo de buffer antijitter: Jitter: 2: "+str(vector_retardos[4])+"ms"
                   +"\n || Retardo de decodificacion en el destino: Jitter: 1,5: "+str(vector_retardos[5])+"ms"
                   +"\n ||  Retardo de decodificacion en el destino : Jitter: 2: "+str(vector_retardos[5])+"ms"
                   +"\n || Retardo total: Jitter: 1,5: "+str(vector_retardos[6])+"ms"
                   +" || Retardo total: Jitter: 2: "+str(vector_retardos[7])+"ms"
                   +"\n || Numero de paquetes RTP almacenados en el buffer: Jitter: 1,5: "+str(vector_retardos[8])+"ms"
                   +"\n ||  Numero de paquetes RTP almacenados en el buffer: 2: "+str(vector_retardos[9])+"ms"
                   +"\n || El buffer antijitter debe ser de: "+ str(tamano_antijitter)+
                   "\n || Las condiciones de retardo: "+ str(cumple)+ "\n || Retardo total final: "+ str(retardofin)+"ms")
        
        ianchobanda=("\n\n     RESULTADOS DEL CALCULO DEL ANCHO DE BANDA Y TRAFICO \n\n"+
                     " || Ancho de banda de una llamada(BWII) RTP: "+str(BWll[0]) +"Mbps"+
                     "\n || Ancho de banda de una llamada(BWII) CRTP: "+str(BWll[1])+"Mbps"+
                     "\n || Ancho de banda SIPTrunk RTP: "+str(BWst[0])+"Mbps"+
                     " || Ancho de banda SIPTrunk RTP: "+str(BWst[1])+"Mbps"+
                     "\n || Trafico en la hora cargada: "+str(bht)+"Erlang"+
                     "\n\n    INFORME GENERADO Y ENVIADO POR SPYDER")
        #Sumamos las tres partes que componen el informe
        informe=inicial+iretardos+ianchobanda

    #Funcion que muestra el esquema de la red
    def abrir_pagina(self):
        
        webbrowser.open('https://drive.google.com/file/d/1-CvcssHM-HYK5-VbZDAIQ_0kLJb-FOpS/view')
        
    #Funcion para cambiar de codec
    def combo_codec(self):
        global indice_codec, cambiar_codec
        
        cambiar_codec = 1
        #Desactivamos la casilla para escoger el MOS
        self.combobox_MOS.setEnabled(0)
        #trabajamos ahora con el codec seleccionado en la ventana 3
        indice_codec = self.comboBox_Codecs.currentIndex()
        #Actualizamos los valores de la pagina 1 y mostramos su contenido
        self.valorespag1()
        self.mostrarPag1()
        
    #Funcion que envía por correo el informe generado en el string 
    def mandacorreo(self):
        port = 587
        smtp_server = "correo.ugr.es"
        sender_email = "jupacanolopez@correo.ugr.es"
        receiver_email = "javihijate@correo.ugr.es"
        password = "juampi65"

        message = """\
        """+informe

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.close()
        pass

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	windows = MainWindows()
	windows.show()
	app.exec_()
