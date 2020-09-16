
def doc_modifier(file = input("Nombre del documento: ")):
    try:
        open(file)
        
        print("""Seleccione el numero del procedimiento a realizar
        Leer documento [1]     Leer y Escribir Documento [2]     Cerrar [3]""")
        while True:
            procedure = input("\nProcedimiento: ")

            if procedure == "1":
                document = open(file, "r")
                print(document.read())
                    
            elif procedure == "2":
                document = open(file, "a+") #append and read
                document.seek(0)
                print(" <<<texto previo: \"{} \">>>".format(document.read()))
                document.write(" "+input("Inserte texto: "))
                #print(document.read())
                
            elif procedure == "3":
                print("Accion terminada")
                document.close
                break
        
            else:
                print("El proceidmiento no existe")
                document.close()
                break
    except:
        print("El documento {0} no fue encontrado".format(file))

#Extra para analisis de datos: mathematical statistic functions, python documentation
#Kayak's_Info.txt
doc_modifier()
