#encoding: utf-8
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


"""
La info de lifestore_file:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
"""
Login credenciales:
usuario: Elena Contrase;a:Saavedra
"""

#def login():
usuarioAccedio = False
intentos = 0

mensaje_bienvenida = 'Bienvenido!\nAccede con tu nombre de usuario y contrasena'
print(mensaje_bienvenida)

  #intentos de acceder al sistema
while not usuarioAccedio:
      # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    contras = input('Contrasena: ')
    intentos += 1
      #Reviso si el par coincide
    if usuario == 'elena' and contras == 'saavedra':
        usuarioAccedio = True
        print('EXCELENTE DIA!')
    else:
        print('Tienes', 3 - intentos, 'intentos restantes')
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'elena':
            print('CONTRASENA EQUIVOCADA')
        else:
            print(f'USUARIO: "{usuario}" NO REGISTRADO')        
    if intentos == 3:
        exit()
print('Acceso autorizado')



#def menu():
    #login()
    #while True:
     #   print('Que operacion desea hacer:')
     #  print('\t1. Realizar el punto 1')
     #   print('\t2. Realizar el punto 2')
     #   print('\t0. Salir')
     #   seleccion = input('> ')
     #   if seleccion == '1':
     #       continue
     #   elif seleccion == '2':
     #       punto2()
     #       print('\n')
      #  elif seleccion == '0':
       #     exit()
       # else:
        #    print('Opcion invalida!')
#menu()


#---------------1.ventas mensuales con cantidad de ventas efectuadas-------------------------------------------

def ventasmensuales():
  id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
  # Para categorizar usamos un diccionario
  categorizacion_meses = {}

  for par in id_fecha:
      # Tengo ID y Mes
      id = par[0]
      _, mes, _ = par[1].split('/')
      # Si el mes aun no existe como llave, la creamos
      if mes not in categorizacion_meses.keys():
          categorizacion_meses[mes] = []
      categorizacion_meses[mes].append(id)

  for key in categorizacion_meses.keys():
      lista_mes = categorizacion_meses[key]
      suma_venta = 0
      for id_venta in lista_mes:
          indice = id_venta - 1
          info_venta = lifestore_sales[indice]
          id_product = info_venta[1]
          precio = lifestore_products[id_product-1][2]
          suma_venta += precio
      print(key, suma_venta, f'ventas totales: {len(lista_mes)}')
ventasmensuales()
      



        
#------------------ RESEÑA DE promedio por producto------------:
def resenapromedio():
  import math
  from sympy import multiplicity
  from lifestore_file import lifestore_products, lifestore_sales

  # De las ventas obtenemos el id_product y rese;a, no necesitamos el restode info
  # tampoco filtramos si fue o no devolucion, nos sigue interesando esa rese;a.
  id_reviews_not_separated = [[sale[1], sale[2]] for sale in lifestore_sales]

  id_reviews_count = {}

  for par in id_reviews_not_separated:
      # Tengo ID y review
      id = par[0]
      review = par[1]
      # Si el id del producto aun no existe como llave, la creamos para tener
      # un lugar donde guardar la review (una lista vacia)
      if id not in id_reviews_count.keys():
          id_reviews_count[id] = []
      # En el diccionario, dentro agregamos la review al producto correspondiente
      id_reviews_count[id].append(review)

  # print(id_reviews_count)

  # Encontrar el promedio de review de cada producto:
  for id_product in id_reviews_count.keys():
      lista_reviews = id_reviews_count[id_product]
      promedio = sum(lista_reviews) / len(lista_reviews)
      # Arreglo promedio a 2 decimales
      decimales = 2
      multiplicador = 10 ** decimales
      promedio = math.ceil(promedio * multiplicador) / multiplicador
      print(f'Producto {id_product} resena promedio de: {promedio}')
resenapromedio ()

 

#--------reseña promedio por categoria, ventas realizadas e ingreso total-------
    # se puede hacer una operacion distinta con la variable promedio, podria
    # guardarse en una lista previamente definida po
# Diccionario de reviews por id
def ventascateg():
  prods_reviews = {}
  for sale in lifestore_sales:
      prod_id = sale[1]
      review = sale[2]
      if prod_id not in prods_reviews.keys():
          prods_reviews[prod_id] = []
      prods_reviews[prod_id].append(review)

  # Diccionario de ids por categoria
  cat_prods = {}
  for prod in lifestore_products:
      prod_id = prod[0]
      cat = prod[3]
      if cat not in cat_prods.keys():
          cat_prods[cat] = []
      cat_prods[cat].append(prod_id)
    
  # Ventas por categorias
  cat_ventas = {}
  for cat in cat_prods.keys():
      # La lista de productos de la categoria
      prods_list = cat_prods[cat]
      # print(cat, prods_list)
      # Defino que quiero calcular
      reviews_cat = []
      ganancias = 0
      ventas = 0

  # Por cada producto de esa categoria
      for prod_id in prods_list:
          # Obtengo las reviews, precio y cantidad de ventas del producto
          if prod_id not in prods_reviews.keys():
              continue
          reviews = prods_reviews[prod_id]
          precio = lifestore_products[prod_id-1][2]
          total_sales = len(reviews)
          # Guardo las ganancias y total de ventas en los datos de la categoria
          ganancias += precio * total_sales
          ventas += total_sales
          reviews_cat += reviews

      # Calculo la review promedio de la categoria
      rev_prom_cat = sum(reviews_cat) / len(reviews_cat)
      # Guardo todo en mi diccionario
      cat_ventas[cat] = {'Resenas_promedio': rev_prom_cat,
                        'Ingreso total $': ganancias,
                        'Ventas realizadas': ventas}

  # f'string'

  for key in cat_ventas.keys():
      print(key)
      for llave, valor in cat_ventas[key].items():
          print(f'\t {llave}: {valor}')
ventascateg()
