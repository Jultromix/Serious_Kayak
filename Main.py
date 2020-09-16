from datetime import datetime
import numpy as np
import sqlite3
import time
import os

from MyTime import General_Time  #retorna string
from Costos import General_Costs #retorna tupla 
from Ventas import General_Sales #retorna tupla

"""Basicamente aqui se importan tres procedimientos y sus resultados se guardan en variables, que pronto pasaran su informacion 
a una base de datos"""
check = ""
while check != "stop":
    cost = General_Costs()
    sale = General_Sales()

    #----Variables reasignadas con valor de las funciones---#
                                                            #
    #    fecha                                              #
    final_date = General_Time()                             #
                                                            #
        #costo                                              #
    visited_stores = cost[0]                #lista          #
    daily_costlist = cost[1]                #lista          #
    daily_cost = cost[2]                                    #
                                                            #
        #venta                                              #
    real_sale = sale[0]                                     #
    articles = sale[1]                      #lista          #
    daily_sale = sale[2]                    #lista          #
    quanti_articles = sale[3]               #lista          #
    registered_sale = sale[4]                               #
    quanti_total = sum(quanti_articles)                     #
    utility = real_sale - daily_cost                        #
    dia = input("nombre del dia: ")                         #
                                                            # 
    #########################################################

    """lo siguiente es tener formatos de listas con orden especifico en el cual vaciar los valores, esto no
    es necesario en las listas de "articles" y visited_stores. De hecho intenta crear una lista con listas
    dentro, la intencion es tener mini listas con objeto, cantidad, valor en caso de ventas y objeto, valor 
    para el costo  """
    # cada lista en item consta de nombre_item/cantidad/venta/%cantidad/%venta
    item = [["chilidog",0,0,0,0],["tostielote",0,0,0,0],["tosticeviche",0,0,0,0],["boya",0,0,0,0], ["refresco",0,0,0,0],["tostada",0,0,0,0],["elote",0,0,0,0],["agua",0,0,0,0],["galleta",0,0,0,0],["l_ceviche",0,0,0,0],["ml_ceviche",0,0,0,0],["fruta",0,0,0,0],["rusa",0,0,0,0],["crayon",0,0,0,0],["winis",0,0,0,0],["mamut",0,0,0,0],["paleta",0,0,0,0],["gomita",0,0,0,0],["tostiqueso",0,0,0,0],["extra",0,0,0,0],["propina",0,0,0,0],["tos_ceviche",0,0,0,0],["tamal",0,0,0,0]]


    for element in articles:
        for lista in item:
            if element == lista[0] :  
                if element == "extra" or element == "propina":
                    jndex = articles.index(element)
                    lista[2] = daily_sale[jndex]
                    lista[4] = round((daily_sale[jndex]/registered_sale)*100, 3)
                else:
                    jndex = articles.index(element)
                    lista[1] = quanti_articles[jndex]
                    lista[2] = daily_sale[jndex]
                    lista[3] = round((quanti_articles[jndex]/quanti_total)*100, 3)
                    lista[4] = round((daily_sale[jndex]/registered_sale)*100, 3)

    stores = [["treviño",0],["chiquilin",0],["plasticocos",0], ["regia",0],["smart",0],["soriana",0],["caballero",0],["carniceria",0],["sams",0],["panaderia",0], ["molienda",0],["oxxo",0]]

    for store in visited_stores:
        for lista in stores:
            if store == lista[0]:  
                kindex = visited_stores.index(store)
                lista[1] = daily_costlist[kindex]



    ####Conexion con la base de datos#############
    conn = sqlite3.connect("kayak_database.db")   
    #Objeto cursor
    cursor = conn.cursor()

    #Tabla General_Info
    parameters = (final_date,dia, registered_sale, real_sale, daily_cost, utility)
    cursor.execute("INSERT INTO General_Info (Fecha, dia, Venta_diaria_registrada, Venta_diaria_real, Costo_diario, Utilidad_diaria) VALUES (?, ?, ?, ?, ?, ?)", parameters)
    print("Información anexada!")
    conn.commit()
        

    #Tabla Producto_cantidad
    parameters_amount = (item[0][1], item[3][1],item[1][1],item[2][1],item[4][1],item[5][1],item[6][1],item[7][1],item[8][1],item[9][1],item[10][1],item[11][1],item[12][1],item[13][1],item[14][1],item[15][1],item[16][1],item[17][1],item[18][1],item[21][1],item[22][1])
    cursor.execute("INSERT INTO Producto_cantidad (Chilidog, Boya, Tostielote, Tosticeviche, Refresco, Tostada, Elote, Agua, Galleta, Litro_ceviche, Medio_Litro_ceviche, Fruta, Rusa, Crayon, Winis, Mamut, Paleta, Gomita, Tostiqueso, Tostada_cev, Tamal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ?, ?)", parameters_amount)
    print("Información anexada!")
    conn.commit()
        

    #Tabla Producto_venta
    parameters_sale = (item[0][2], item[3][2],item[1][2],item[2][2],item[4][2],item[5][2],item[6][2],item[7][2],item[8][2],item[9][2],item[10][2],item[11][2],item[12][2],item[13][2],item[14][2],item[15][2],item[16][2],item[17][2], item[18][2], item[19][2], item[20][2],item[21][2], item[22][2])
    cursor.execute("INSERT INTO Producto_venta (Chilidog, Boya, Tostielote, Tosticeviche, Refresco, Tostada, Elote, Agua, Galleta, Litro_ceviche, Medio_Litro_ceviche, Fruta, Rusa, Crayon, Winis, Mamut, Paleta, Gomita, Tostiqueso, Extra, Propina, Tostada_cev, Tamal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ?, ?, ?, ?)", parameters_sale)
    print("Información anexada!")
    conn.commit()
        

    #Tabla Prod_quantporcento 
    parameters_peramount = (item[0][3], item[3][3],item[1][3],item[2][3],item[4][3],item[5][3],item[6][3],item[7][3],item[8][3],item[9][3],item[10][3],item[11][3],item[12][3],item[13][3],item[14][3],item[15][3],item[16][3],item[17][3], item[18][3],item[21][3], item[22][3])
    cursor.execute("INSERT INTO Prod_quantporcento (Chilidog, Boya, Tostielote, Tosticeviche, Refresco, Tostada, Elote, Agua, Galleta, Litro_ceviche, Medio_Litro_ceviche, Fruta, Rusa, Crayon, Winis, Mamut, Paleta, Gomita, Tostiqueso, Tostada_cev, Tamal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ?, ?)", parameters_peramount)
    print("Información anexada!")
    conn.commit()
        

    #Tabla Prod_ventaporcento
    parameters_persale = (item[0][4], item[3][4],item[1][4],item[2][4],item[4][4],item[5][4],item[6][4],item[7][4],item[8][4],item[9][4],item[10][4],item[11][4],item[12][4],item[13][4],item[14][4],item[15][4],item[16][4],item[17][4], item[18][4],item[19][4], item[20][4],item[21][4],item[22][4])
    cursor.execute("INSERT INTO Prod_ventaporcento (Chilidog, Boya, Tostielote, Tosticeviche, Refresco, Tostada, Elote, Agua, Galleta, Litro_ceviche, Medio_Litro_ceviche, Fruta, Rusa, Crayon, Winis, Mamut, Paleta, Gomita, Tostiqueso, Extra, Propina, Tostada_cev, Tamal) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", parameters_persale)
    print("Información anexada!")
    conn.commit()
        



    #Tabla Costos_tiendas
    parameters_cost = (stores[0][1],stores[1][1],stores[2][1],stores[3][1], stores[4][1],stores[5][1],stores[6][1],stores[7][1],stores[8][1],stores[9][1],stores[10][1],stores[11][1])
    cursor.execute("INSERT INTO Costos_tiendas (Treviño, Chiquilin, Plasticocos, Regia, SMART, Soriana, Caballero, Carniceria, SAMS, Panaderia, Molienda, Oxxo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", parameters_cost)
    print("Información anexada!")
    conn.commit()
    conn.close()

    check = input("")




"""Otra cosa que es necesario hacer es los objetos que se compran, el costo que tienen y la utilidad sobre ellos
ademas no estoy seguro si hacer un analisis estadistico de compra de mercancias"""