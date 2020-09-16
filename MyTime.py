from datetime import datetime

#revisa si el dia insertado es valido
def General_Time():
    def day_checker(time_data):
        
        time_data.append(input("día: "))
        while time_data[0].isalpha():
            time_data[0] = input("El dia debe ser un numero* : ") 

        while int(time_data[0]) < 1 or int(time_data[0]) > 31:
            print("\nEl día seleccionado esta fuera de rango; vuelva a ingresarlo")
            time_data[0]= int(input("dia :"))
        return time_data

    #revisa si el mes insertado es valido
    def month_checker(time_data):
        
        time_data.append(input("mes: "))
        while time_data[1].isalpha():
            time_data[1] = input("El mes debe ser un numero* : ") 

        while int(time_data[1]) < 1 or int(time_data[1]) > 31:
            print("\nEl mes seleccionado esta fuera de rango; vuelva a ingresarlo")
            time_data[1]= int(input("mes :"))
        return time_data

    #revisa si el año insertado es valido
    def year_checker(time_data):
        
        time_data.append(input("año: "))
        while time_data[2].isalpha():
            time_data[2] = input("El año debe ser un numero* : ") 

        while int(time_data[2]) < 1:
            print("\nEl año seleccionado esta fuera de rango; vuelva a ingresarlo")
            time_data[1]= int(input("año :"))
        return time_data
    
    #indica la fecha
    def my_time():
        global final_date
        answer = input("¿El registro es actual? [si][no]\n")
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        #Aqui preguntamos la modalidad
        if answer == "no":
        
            #Feacha manual
            print("\nIngresa el dia, mes y año expresado en numeros.")
            time_data = []

            #Registro de datos
            day_checker(time_data)
            month_checker(time_data)
            year_checker(time_data)
                        
            for mes in range(0, len(meses)+1):
                if int(time_data[1]) == mes:
                    real_month =  (meses[mes-1])
            
            final_date = "{} / {} / {}".format(time_data[0], real_month , time_data[2])
            return final_date
            
        elif answer == "si":
        #Fecha automatica actual
            dt = datetime.now()
            for mes in range(0, len(meses)-1):
                if dt.month == mes:
                    real_month =  (meses[mes-1])
            final_date = "{} / {} / {}".format(dt.day,real_month , dt.year)
            return final_date
        #Si la respuesta no es valida:
        else:
            print("Respuesta no valida")
    my_time()
    return final_date






