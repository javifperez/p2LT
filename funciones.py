"""
Funciones complementarias del diseño de la red VoIP

Autores: Javi Fernandez y Juan Pablo Cano

"""
import numpy as np
import erlang 

#Funcion que elige un codec en funcion de un MOS
def elegir_codec(mos, codecs):
    d = codecs[:,2] - mos
    for i in range(0,len(d),1):
        if (d[i]>=1):
            d[i]=0
    codec = np.argmax(d)
    
    return codec
    
def retardo_total(Rr,J,VPS,CSI,Ralg):
    #Retardo conjunto, CODEC + paquetizacion
    Rorg = VPS + 0.1*CSI
        #Retardos buffer antijitter
    Rjitter_1 = 1.5*J
    Rjitter_2 = 2*J
    #Retardo de decodificacion
    Rdest = 0.1*VPS
    #Retardo total para cada buffer antiijtter
    Rt1 = Rorg + Ralg + Rr + Rjitter_1 + Rdest
    Rt2 = Rorg + Ralg + Rr + Rjitter_2 + Rdest
        #Calculamos el numero de paquetes almacenados en el buffer antijitter
    #en cada caso
    Npaq1 = Rjitter_1//VPS
    Npaq2 = Rjitter_2//VPS
    
    return Rorg, Ralg, Rr, Rjitter_1, Rjitter_2, Rdest, Rt1, Rt2, Npaq1, Npaq2

#Funcion que calcula la BHT
def calculo_BHT(Nc,Nl,Tpll):
    BHT=(Nc*Nl*Tpll)/60
    
    return BHT
#Funcion que calcula el BWll
def calculo_BWll(CSS,CSI,VPS):
    #Calculamos la longitud de las cabeceras
    Lcab_cRTP=20+6+4
    Lcab_RTP=20+6+20+8+12
    #Longitud total del paquete en bits (cRTP)
    Lpaq_cRTP=(Lcab_cRTP+VPS)*8
    #Longitud total del paquete en bits (RTP)
    Lpaq_RTP=(Lcab_RTP+VPS)*8
    #Calculamos el CBR (Codec Bit Rate)
    CBR=(CSS*8)/(CSI/1000)#Expresado en bps
    #Calculamos PPS
    PPS=CBR/(VPS*8)
    #Calculamos el ancho de banda de una llamada
    BWll_RTP=(Lpaq_RTP*PPS)/1000 #kbps
    BWll_cRTP=(Lpaq_cRTP*PPS)/1000 #kbps
    
    return BWll_RTP,BWll_cRTP
#Funcion que calcula el BWST
def calculo_BWST(BHT,Pb,BWll_RTP,BWll_cRTP):
    Nllamadas=erlang.extended_b_lines(BHT,Pb/100)
    BWST_RTP=Nllamadas*BWll_RTP/1000 #Mbps
    BWST_cRTP=Nllamadas*BWll_cRTP/1000 #Mbps
    
    return BWST_RTP,BWST_cRTP

#Funcion que convierte el MOS a un indice numerico
def transformaMOS(mos):
    resultado=0
    
    if(mos=="Excelente"):
        resultado=5
    elif(mos=="Bueno"):
        resultado=4
    elif(mos=="Aceptable"):
        resultado=3
    elif(mos=="Bajo"):
        resultado=2
    elif(mos=="Malo"):
        resultado=1
    
    return resultado
#Funcion que elige el retardo en funcion del parametro de entrada
def eligeRt(combobox_retardo_total):
    rt=0
    if (combobox_retardo_total=="Aceptable"):
        rt=150
    elif (combobox_retardo_total=="Moderado"):
        rt=275
    elif (combobox_retardo_total=="Inaceptable"):
        rt=400
    return rt
        
    
    
    