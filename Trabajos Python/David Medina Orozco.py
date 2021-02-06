def main():
    import random;
    n=int(input("NUMERO DE DEPARTAMENTOS:"));
    m=12;
    mat=[];
    vec1=[];
    for i in range (0,n):
        mat.append([0]*m);
    #endfor
    vec1=[""]*n;
    def llenar (ma,ve1,fil,col):
        for i in range (0,fil):
            ve1[i]=str(input("INGRESE NOMBRE DEPARTAMENTO:"));
            for j in range (0,col):
                mat[i][j]= round((random.random()*100000000));
            #endfor
        #endfor
        return;
    #endllenar
    def mostrar(ma,ve1,fil,col):
        for i in range(fil):
            print(ma[i]);
    def promMayorpresupuestoanual(ma,ve1,fil,col):
        for i in range(0,fil):
            acum=0;
            for j in range (0,col):
                acum=acum+ma[i][j];
            #endfor
            prom=acum/col;
            print(ve1[i],"TIENE UN PROMEDIO DE_",prom);
            if (i==0):
                mayorpresupuesto=acum;
                nombredep=ve1[i];
            else:
                if(acum>mayorpresupuesto):
                    mayorpresupuesto=acum;
                    nombredep=ve1[i];
        print("EL DEPARTAMENTO_",nombredep,"TIENE EL MAYOR PRESUPUESTO DE GASTOS ANUAL");            
        return;
        #endpromMayorpresupuestoanual  
    def mayormes(ma,ve1,fil,col):
        for j in range(0,col):
            mayorg=0;
            nombremayorg="";
            for i in range (0,fil):
                if (i==0):
                    mayorg=ma[i][j];
                    nombremayorg=ve1[i];
                else:
                    if(ma[i][j]>mayorg):
                        mayorg=ma[i][j];
                        nombremayorg=ve1[i];
            print("EN EL MES_",(j+1),"EL DEPARTAMENTO CON MAYOR PRESUPUESTO ES_",nombremayorg);            
        return;                
    llenar(mat,vec1,n,m);
    promMayorpresupuestoanual(mat,vec1,n,m);
    mayormes(mat,vec1,n,m);
    print ("PRACTICA PRESENTADA POR DAVID MEDINA OROZCO GRUPO 062");
main()        