int; opcion = 0

while opcion <4 :
  
   print()
   print('#' * 20 + 'BIENVENIDO' + '#' * 20)
   print()
   print ('Ingrese una opcion: ')
   print('1. Robot Cilindrico.')
   print('2. Robot Carteciano.')
   print('3. Robot Esferico o Polar.')
   print('4. SALIR.')
   print()

   opcion= int(input ('Opcion: '))
   match opcion:
      
      case 1:
         print('El robot cilindrico tine 2 articulaciones de tipo prismatica una para la altura y una para el movimiento de radio. En su base tiene 1 articulacion rotacional, es un robot R P P')
      case 2:
         print('El robot carteciano tiene 3 articulaciones prismaticas, es un robot tipo P P P') 
      case 3:
        print('El robot Esferico tiene 2 articulaciones rotacionales y 1 articulacion prismatica, es un robot R R P')   