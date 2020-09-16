import numpy as np
from datetime import datetime
import time




def General_Sales():
    
    global productos
    global daily_sale
    global articles
    
        
    productos = [{"chilidog":25}, {"tostielote":35}, {"tosticeviche":60}, {"boya":18}, {"refresco":17}, {"tostada":10}, {"elote":25},{"agua":8}, {"galleta":10}, {"l_ceviche":250}, {"ml_ceviche":130}, {"fruta":25}, {"rusa":50}, {"crayon":7}, {"winis":3}, {"mamut":3}, {"paleta":3}, {"gomita":1},{"tostiqueso":20},{"extra":1},{"propina":1},{"tos_ceviche":30},{"tamal":12}]
    daily_sale = [] 
    articles = []
    
    real_sale = 0.0
        
        
    #registra ventas, articulos y cantidad de articulos
    def registrator_sales(daily_sale, articles):
        print("""\nProcedimiento para registrar las ventas y la venta total del dia correspondiente, despues de cada venta registrada aparece un espacio en blanco,\nescriba \"stop\" para terminar el registro""")
        #El siguiente mensaje tardara un segundo en aparecer
        for x in range (1,0,-1):
            time.sleep(1)
        if x==1:
                print("""\n    <<<Los productos que actualmente estan disponibles son los siguienetes, pero para registrarlo se tendra que usar la forma abreviada que\n       esta entre corchetes si es que la hay*>>>
        ----------------------------------------------------------------------------------------------------------------------------------------------------
        chilidog [chil]       #  boya            #   elote [elot] #  crayon [cray] #  litro ceviche [l_cev]         # mamut                 # propina [prop]
        tostielote [tostie]   #  refresco [refr] #   agua         #  rusa          #  medio litro ceviche [ml_cev]  # tostiqueso [tostiq]   #
        tosticeviche [tostic] #  tostada [tosta] #   fruta [frut] #  winis [wini]  #  paleta [pale]                 # exrtra/propina [extr] #   
        ----------------------------------------------------------------------------------------------------------------------------------------------------
        \n""")
        
        #el check sirve para que el programa sepa cuando detenerse al typear stop, eso mismo hace
        check = " "
        while check != "stop":
            sold_item = input("\nproducto vendido: ")
            amount_item = input("cantidad de artiulos: ")
            
            #La cantidad de items solo puede ser strings formadas por numeros
            while amount_item.isalpha():
                amount_item = input("La \"cantidad vendida\" debe ser un numero* : ") 
            
            #Si en lugar de poner un numero solo das enter, se entiende que eso equivale a 1 item
            if amount_item == "":
                amount_item = "1"
            
            
            #La cantidad de items debe ser siempre positiva
            while int(amount_item) < 1:
                print("\n   <<<Solo se admiten numeros mayores a 0, no tiene sentido agragar algo que no se pidio. Vuelva a intentarlo*>>>")
                pass
            else:
                #Esta seccion se encarga de almacenar el valor del producto y su cantidad en las listas corresponidentes
                try:
                    for element in productos:
                        for key in element:
                            if sold_item == key[:4] or sold_item == key[:6] or sold_item == key or sold_item == key[:5]:
                                n=0
                                while n < int(amount_item):
                                    articles.append(key)
                                    n += 1
                                sale = list(element.values())  
                                daily_sale += sale*int(amount_item)
                    check = input()
                except:
                    print("Hubo un problema con el producto introducido")
    
        #Registra la venta real      
        nonlocal real_sale
        real_sale = []
        real_sale.append(input("\nVenta real registrada: "))
        while real_sale[0].isalpha():
            real_sale[0] = input("La \"venta venta\" debe ser un numero* : ")
        real_sale = float(real_sale[0])
        
        
        def reducer():
            global daily_sale
            global articles
            global quanti_articles

            counter = 0
            objeto_filtered = []
            valor_filtered = []

            quanti_articles = []

            for index in range(0, len(articles)):
                if articles[index] not in objeto_filtered:
                    objeto_filtered.append(articles[index])
                    valor_filtered.append(daily_sale[index])

                else:
                    for jndex in range(0, len(objeto_filtered)):
                        if articles[index] == objeto_filtered[jndex]:
                            valor_filtered[jndex] += daily_sale[index]
            
            for x in (objeto_filtered):
                for y in (articles):
                    if y == x:
                        counter += 1
                quanti_articles.append(counter)
                counter = 0
                
            

            articles = objeto_filtered
            daily_sale = valor_filtered
        
                
            del objeto_filtered
            del valor_filtered
            try:
                print(objeto_filtered, valor_filtered)
            except:
                print("\n")
                    #imprime la venta total
            
            
                
            return articles,daily_sale, quanti_articles
        reducer()
        
        return daily_sale, articles, real_sale, quanti_articles
    
    def totals():
        global registered_sale
        registered_sale = sum(daily_sale)
        return registrator_sales

    registrator_sales(daily_sale, articles)
    totals()

    return real_sale, articles, daily_sale, quanti_articles, registered_sale


# print("venta registrada                ", registered_sale)
# print("venta real                      ", real_sale)
# print("lista reducida de articulos:    ", articles)
# print("lista reducida de venta diaria: ", daily_sale)
# print("lista de cantidad de articulos: ", quanti_articles)

