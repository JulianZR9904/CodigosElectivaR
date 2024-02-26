# Entrada de datos

color=input('ingrese un color:')

match color:
    case'verde':
        print('el color es verde')
    case 'rojo':
        print('el color es rojo') 
    case 'azul':
        print('el color es azul')       
    case _: 
        print('no es el color correct')   