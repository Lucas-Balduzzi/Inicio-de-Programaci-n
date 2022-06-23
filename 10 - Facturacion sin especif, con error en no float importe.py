print('"Facturación Empresa"')
continuar = 'y'
select_uno = '1'
select_dos = '2'
clientes_totales = 0
cliente_registrado = 'y'
comision_caja_interior = 0
comision_caja_exterior = 0
print('"Menu de Opciones: "')
while continuar == 'y':
    while continuar == 'y':
        print('\n-Seleccione caja a operar: ')
        print('1 - para Caja -Local')
        print('2 - para Caja -Vereda')
        selection = input('\n-Indique la opción deseada: ')
        menu = selection
        if selection == select_uno or select_dos:
            if selection == select_uno:
                while continuar == 'y':
                    while continuar == 'y':
                        print("\n'Caja 1 Local: '")
                        print("'Cafetería, Sandwiches, Bebidas Frías'\n")
                        cliente_si_no =(input('''Es Cliente Registrado?
Ingrese Y(yes, sí), de ser correcto: '''))
                        importe = input('\n-Ingrese Importe: ')
                        total = float(importe)
                        descuento =(total)*(0.03)
                        print("___________________________________________")
                        if (cliente_si_no == cliente_registrado):
                            print('Total con descuento cliente = '+ str(total - descuento))
                            clientes_totales = clientes_totales + 1
                            if float(importe) > int(500):
                                comision_caja_interior = comision_caja_interior + float(importe)*float(0.01)
                        else :print('Total = '+str(total))
                        if float(importe) > int(500):
                                comision_caja_interior = comision_caja_interior + float(importe)*float(0.01)
                        
                        print("___________________________________________")
                        continuar = input('-Desea realizar otra compra?: ')
                    continuar = input('\n-Continuar con facturación caja actual?: ')
            elif selection == select_dos:
                while continuar == 'y':
                    while continuar == 'y':
                        print("\n'Caja 2 Vereda: '")
                        print("'Golosinas, Cigarrillos, Otros'\n")
                        cliente_si_no =(input('''Es Cliente Registrado?
Ingrese Y(yes, sí), de ser correcto: '''))     
                        importe = input('\n-Ingrese Importe: ')
                        total = float(importe) 
                        descuento =(total)*(0.03)
                        comision_caja_exterior = comision_caja_exterior + float(importe)*(0.005)
                        print("___________________________________________")
                        if  (cliente_si_no == cliente_registrado):
                            print('Total con descuento cliente = '+ str(total - descuento))
                            clientes_totales = clientes_totales + 1
                        else :print('Total = '+str(total))
                        print("___________________________________________")
                        continuar = input('-Desea realizar otra compra?: ')
                    continuar = input('\n-Continuar con facturación caja actual?: ')
        continuar = input('\n-Volver a selección de Caja y Sector?: ')
        print("___________________________________________")
    continuar = input("-Desea continuar con el programa?: ")
    print("\n___________________________________________")
    print('Clientes Totales Atendidos al día de Hoy: ' + str(clientes_totales))
    if comision_caja_interior > 0 :
        print('Comisiones por Ventas Caja 1 Interior = '+ str(comision_caja_interior))
    elif comision_caja_exterior > 0 :
        print('\nComisiones por Ventas Caja 2 Exterior = '+ str(comision_caja_exterior))
    else: print('\nNo hubo comisiones.')
    print("__________________________________________________________________")

