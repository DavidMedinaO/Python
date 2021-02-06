def main():
    import random


    def palabra_aleatoria():
        with open("words.txt", "r") as f:
            data = f.readlines()

        n = random.randint(0, len(data)-1)
        return data[n]


    def dibujar_ahorcado(partes):
        print("{:_^10}".format(""))
        print("{:>10}".format("|"))

        if partes == 1:
            print("{:>11}".format("(_)"))
            
        elif partes == 2:
            print("{:>11}".format("(_)"))
            print("{:>10}".format("|"))
            print("{:>10}".format("|"))
            print("{:>10}".format("|"))
        elif partes == 3:
            print("{:>11}".format("(_)"))
            print("{:>10}".format("|"))
            print("{:>10}".format("/|"))
            print("{:>10}".format("|"))
        elif partes == 4:
            print("{:>11}".format("(_)"))
            print("{:>10}".format("|"))
            print("{:>11}".format("/|\\"))
            print("{:>10}".format("|"))
        elif partes == 5:
            print("{:>11}".format("(_)"))
            print("{:>10}".format("|"))
            print("{:>11}".format("/|\\"))
            print("{:>10}".format("|"))
            print("{:>10}".format("/ "))
        elif partes == 6:
            print("{:>11}".format("(_)"))
            print("{:>10}".format("|"))
            print("{:>11}".format("/|\\"))
            print("{:>10}".format("|"))
            print("{:>11}".format("/ \\"))

        print("\n")
        
        
    def mostrar(Vec):
        i=0
        tablero="TABLERO: "
        while i < len(Vec):
            tablero= tablero + Vec[i]
            i=i+1 
        print(tablero)
        print("LA PALABRA CONTIENE: ", len(Vec), " LETRAS")
        
    def gano(Vec):
        i=0
        win= "true"
        while i < len(Vec):
            if Vec[i] == " _ ":
                win= "false"
            i=i+1 
        return win
       


    
    cont=-1
    juego = "true"
    
    while juego == "true" :
        if cont == -1:
            print("---------------------------NUEVA PARTIDA-----------------------")
            cont =0
            palabra = palabra_aleatoria()
            VecL=[" _ "]*(len(palabra)-1);
            mostrar(VecL)
            
        letra =str(input("INGRESE LA LETRA:"));
        i=0
        acerto = "false"
        print("")
        while i < len(palabra):
            if(letra.lower() == palabra[i].lower()):
                VecL[i]= letra
                acerto= "true"
            i=i+1
            
        if acerto == "false":
            print("LETRA NO EXISTENTE")
            cont= cont + 1
            dibujar_ahorcado(cont)
            print("---------------------------------")
            if cont== 6:
                print("-----------JUEGO TERMINADO - PERDISTE------------")
                jugar =str(input("VOLVER A JUGAR? S/N: "));
                if jugar.lower() == "N".lower():
                    juego= "false"
                    print("---------------GRACIAS POR JUGAR-------------")
                else:
                    cont= -1
        else:
            print("BIEN HECHO!!!")
            mostrar(VecL)
            print("-------------------------------")
                            
        Gano = gano(VecL)
        if Gano == "true":
            print("----------FELICITACIONES GANASTE-------------")
            jugar =str(input("VOLVER A JUGAR? S/N: "));
            if jugar.lower() == "N".lower():
                juego= "false"
                print("--------------GRACIAS POR JUGAR--------------")
            else:
                cont= -1
         
        
    
main()    
