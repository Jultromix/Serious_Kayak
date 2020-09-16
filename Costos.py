import time



def General_Costs():
    
    def variables_costs():
        global tiendas
        global daily_costlist
        global visited_stores
        global daily_cost
        tiendas = ["treviño","chiquilin","plasticocos","regia", "smart", "soriana", "caballero","carniceria", "sams","panaderia","molienda","oxxo"] 
        daily_costlist = []
        visited_stores = [] 
        daily_cost = 0
        return daily_costlist, visited_stores

    def registrator_costs(daily_costlist, visited_stores):
        print("""\nProcedimiento para registrar los costos y el costo total del dia correspondiente, despues de cada compra registrada aparece un espacio en blanco,\nescriba \"stop\" para terminar el registro""")
        #El siguiente mensaje tardara un segundo en aparecer
        for x in range (1,0,-1):
            time.sleep(1)
        if x==1:
                print("""\n    <<<Las tiendas que actualmente estan disponibles son las siguienetes, pero para capturar la tienda se tendra que usar la forma abreviada que esta entre corchetes*>>>
        
        Chiquilin: [chiq]   Treviño: [trev]   Smart: [smar]   Soriana: [sori]   Caballero: [caba]   Plasticocos: [plas]   Regia: [regi]   Carnicería: [carn]   SMART: [smar]   Panaderia: [pana]   Oxxo: [oxxo]\n\n""")
        
        #el check sirva para que el programa sepa cuando detenerse
        check = " "
        while check != "stop":
            store = input("\nTienda donde se compró: ")
            amount_purchases= input("Cantidad de compras: ")
            
            #La cantidad solo deben ser strings formadas por numeros
            while amount_purchases.isalpha():
                amount_purchases = input("La \"cantidad de compras\" debe ser un numero* : ") 
            
            #Si en lugar de poner un numero solo das enter, se entiende que eso equivale a 1
            if amount_purchases == "":
                amount_purchases = "1"
                

            #La cantidad de items debe ser siempre positiva
            if int(amount_purchases) < 1:
                print("\n   <<<Solo se admiten numeros mayores a 0, no tiene sentido agragar algo que no se pidio. Vuelva a intentarlo*>>>")
                pass
            elif int(amount_purchases) > 8:
                print("\n   <<<Normalmente no se hacen tantas compras>>>")
            else:
                #Esta seccion se encarga de almacenar el valor del producto y su cantidad en las listas corresponidentes
                try:
                    for element in tiendas:
                        if store == element[:4]:
                            cycles = 0
                            while cycles < int(amount_purchases):   
                                daily_costlist.append(input("Precio de compra: "))
                                visited_stores.append(element)
                                while daily_costlist[-1].isalpha():
                                    daily_costlist[-1]= input("El \"precio de compra\" debe ser un numero* : ")
                                cycles += 1
                    check = input()   
                    
                except:
                    print("Hubo un problema con el producto introducido")
                #convierte cada elemento de la lista en flotante/decimal
                for index in range(0, len(daily_costlist)):
                    daily_costlist[index] = float(daily_costlist[index])           
        
        def reducer():
            global daily_costlist
            global visited_stores
            

            objeto_filtered = []
            valor_filtered = []

            for index in range(0, len(visited_stores)):
                if visited_stores[index] not in objeto_filtered:
                    objeto_filtered.append(visited_stores[index])
                    valor_filtered.append(daily_costlist[index])

                else:
                    for jndex in range(0, len(objeto_filtered)):
                        if visited_stores[index] == objeto_filtered[jndex]:
                            valor_filtered[jndex] += daily_costlist[index]
                    
            visited_stores = objeto_filtered
            daily_costlist = valor_filtered
        
                
            del objeto_filtered
            del valor_filtered
            try:
                print(objeto_filtered, valor_filtered)
            except:
                print("\n")
            return visited_stores,daily_costlist   
        reducer()

        return daily_costlist, visited_stores
        
    def totals(daily_costlist):
        global daily_cost
        daily_cost = sum(daily_costlist)                        
        return daily_cost

    variables_costs()
    registrator_costs(daily_costlist, visited_stores)
    
    totals(daily_costlist)
    return visited_stores, daily_costlist, daily_cost
