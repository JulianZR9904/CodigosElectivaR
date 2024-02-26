#B.4

int; opcion =  0 
#float; Largo,Altura,Ancho=0


while  opcion <5:
     def Vol_prisma(Largo,Altura,Ancho):
      print('El volumen del prisma es: ' + str(Largo*Altura*Ancho))
     
     def Vol_piramide(Base,Altura):
       print('El volumen de la piramede es: ' + str((Base*Altura)/3))
       
     def Vol_cilindro(Radio,Altura):
       print('El volumen del cilindro es: '+ str ((3.1416*(Radio*Radio))*Altura))

     def Vol_cono(RadioMayor,RadioMenor,Altura):
       print('El volumen del cono es: ' + str ((3.1416* Altura) * (RadioMayor**2 + RadioMenor**2 + RadioMenor*RadioMayor)/3))

     print()
     print('#' * 20 + 'BIENVENIDO' + '#' * 20)
     print()
     print ('Ingrese una opcion: ')
     print('1. Volumen de Prisma.')
     print('2. Volumen de Piramide.')
     print('3. Volumen de Conotruncado.')
     print('4. Volumen de Cilindro.')
     print('5. SALIR.')
     print()
     opcion= int(input ('Opcion: '))
     match opcion:
  
      case 1:
       print('Volumen de prisma')
       Vol_prisma(Largo= float(input('Ingrese el largo: ')),
       Ancho= float(input('Ingrese el ancho: ')),
       Altura= float(input('Ingrese la altura: ')))
      case 2:
       print('Volumen de piramede')
       Vol_piramide(Base= float(input('Ingrese el area de la base: ') ),
       Altura= float(input('Ingrese la altura: ')))

      case 3:
       print('Volumen de cono')
       Vol_cono(RadioMayor= float(input('Ingrese el radio Mayor: ')),
       RadioMenor= float(input('Ingrese el Radio Mneor: ')),
       Altura= float(input('Ingrese la altura: ')))
      
      case 4:
       print('Volumen de Cilindro')    
       Vol_cilindro( Radio= float(input('Ingrese el radio: ')),
                    Altura= float(input('Ingrese la altura: ')))
  

 
