def main(): 
    import random;
    n=int(input("INGRESE NUMEROS DE ELEMENTOS:"));
    a=[0]*n;
    def llenarvector(v,z):
        for i in range (0,z):
            v[i]=(random.randint(0,5));
        return;
    def imprimirvector(v,z):
        for i in range (0,z):
            print(v[i]," ",end =" ");
        print("    ")    
        return;
    def promediovector(v,z):
        suma=0;
        for i in range (0,z):
            suma=suma+v[i];
        prom=suma/z;
        return prom;
    def ordenarvector(v,z):
        i=0;
        temp=0;
        while i<n-1:
            j=i+1;
            while j<n:
                if v[i]> v[j]:
                    temp=v[i];
                    v[i]=v[j];
                    v[j]=temp;
                j=j+1;
            i = i+1    
        return;        
    def mayorelemento(v,z):
        i=0;
        mayor=0;
        for i in range (0,z):
            if i==0:
                mayor=v[i];
            else:
                if v[i]>mayor:
                    mayor=v[i];
        return mayor;
    def menorelemento(v,z):
        i=0;
        menor=0;
        for i in range (0,z):
            if i==0:
                menor=v[i];
            else:
                if v[i]<menor:
                    menor=v[i];
        return menor;
    def numerovector(v,z):
         acum=0;
         num=int(input("INGRESE NUMERO PARA SABER LAS VECES QUE SE NECUNTRA EN EL VECTOR:"));
         for i in range (0,z):
             if num==v[i]:
                acum=acum+1;
         if acum>0:
             print("EL NUMERO_",num,"_SE ENCUENTRA_",acum,"VECES EN EL VECTOR");
         else:
             print("EL NUMERO_",num,"_SE ENCUENTRA 0 VECES EN EL VECTOR");
         return;         
    llenarvector(a,n);
    numerovector(a,n)
    print ("vector original")
    imprimirvector(a,n);
    ordenarvector(a,n);
    print("vector ordenado")
    imprimirvector(a,n);
    promedio=promediovector(a,n);
    mayorv=mayorelemento(a,n)
    menorv=menorelemento(a,n)
    print("EL PROMEDIO ES:",promedio);
    print("EL NUMERO MAYOR ES:",mayorv);
    print("EL NUMERO MENOR:",menorv);
    print("PRACTICA PRESENTADA POR DAVID MEDINA OROZCO GRUPO 062");
main()


