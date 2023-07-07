
#Librerias necesarias para el scraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

#Librerias necesarias para crear el cvs
import pandas as pd 
import os
import numpy

#Primer enlace de MercadoLibre a revisar
link_mercadolibre = "https://listado.mercadolibre.com.co/computadores#D[A:computadores]"

#Configuraciones de Google Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#Chrome Driver
driver = webdriver.Chrome(executable_path=r"FOLDER/chromedriver.exe")

#Obtener Página Web
driver.get(link_mercadolibre)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

#Arrays para guardar todos los datos
vector = []
titulo = []
precio = []
cuota = []
envio = []
descuento = []
recomendado = []
link = []
tiendas = []

i=0

#Función para obtener el titulo de la publicación
def buscarTitulo():

    #Ciclo en el cual se itera sobre un div con clase ui-search-result__content-wrapper en MercadoLibre.
    #Funciona con la misma lógica para las otras funciones.
    for a in soup.findAll('div',attrs={'class':'ui-search-result__content-wrapper'}):
        
        #Dentro de esta clase se busca el h2 con clase ui-search-item__title y se obtiene el texto de este,
        #que en este caso es el titulo. 
        aux=a.find('h2', attrs={'class':'ui-search-item__title'}).text
        
        #Se agrega ese titulo al array titulo
        titulo.append(aux)

        #Al finalizar el ciclo, regresa el array.
    return titulo

#Función para obtener el precio de la publicación
def buscarPrecio():

    for a in soup.findAll('div',attrs={'class':'ui-search-result__content-wrapper'}):
        #Obtener Nombre del Producto
        aux=a.find('span', attrs={'class':'price-tag-fraction'}).text.replace('.','')
        precio.append(aux)
    return precio

#Función para obtener la cuota de la publicación
def buscarCuota():

    for a in soup.findAll('div',attrs={'class':'ui-search-price ui-search-price--size-x-tiny ui-search-color--BLACK'}):

        aux=a.find('span', attrs={'class':'price-tag-fraction'}).text.replace('.','')
        cuota.append(aux)
    
    return cuota

#Función para obtener el tipo de envio de la publicación
def buscarEnvio():

    for a in soup.findAll('div',attrs={'class':'ui-search-item__group__element ui-search-item__group__element--shipping'}):

        try:
            
            aux=a.find('p', attrs={'class':'ui-search-item__shipping ui-search-item__shipping--free'}).text
            envio.append(aux)
            
        except:

            aux=""
            envio.append(aux)
        
    return envio

#Función para obtener el descuento de la publicación si lo tiene
def buscarDescuento():
    
    for a in soup.findAll('span',attrs={'class':'ui-search-price__second-line__label'}):

        #Se usa un try except debido a que si no encuentra un decuento, arrojara un error, y este es capturado
        #para que no se rompa el programa
        try:
            #Si lo encuentra, se guarda en el array descuento.
            aux=a.find('span', attrs={'class':'ui-search-price__discount'}).text
            descuento.append(aux)
        except:
            #Si no, se inserta un espacio en blanco en el array descuento.
            aux=""
            descuento.append(aux)
    
    return descuento

#Función para saber si un producto es recomendado o no de la publicación
def buscarRecomendado():
    #ui-search-price__second-line__label
    for a in soup.findAll('div',attrs={'class':'ui-search-result__content-wrapper'}):

        try:
            aux=a.find('label', attrs={'class':'ui-search-styled-label ui-search-item__highlight-label__text'}).text
            
            #Si el texto traido es RECOMENDADO, lo guarda
            if aux=="RECOMENDADO":
                recomendado.append(aux)

        except:
            #Si no, guarda un espacio en blanco.
            aux=""
            recomendado.append(aux)
            
    
    return recomendado

#Función para traer el link de la publicación
def buscarLink():
    #ui-search-price__second-line__label
    for a in soup.findAll('div',attrs={'class':'ui-search-result__content-wrapper'}):

        aux=a.find('a',href = True,attrs={'class':'ui-search-item__group__element ui-search-link'})['href']
        link.append(aux)

    return link

#Función saber si el producto lo vende una tienda oficial y cual
def buscarTiendaOficial():
    
    for a in soup.findAll('div',attrs={'class':'ui-search-item__group ui-search-item__group--title'}):

        try:
            aux=a.find('p', attrs={'class':'ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY'}).text
            tiendas.append(aux)
        except:
            aux2=""
            tiendas.append(aux2)

    return tiendas

#Se ejecutan todos los métodos.
buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre2 = "https://listado.mercadolibre.com.co/computadores_Desde_51_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre2)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre3 = "https://listado.mercadolibre.com.co/computadores_Desde_101_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre3)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre4 = "https://listado.mercadolibre.com.co/computadores_Desde_151_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre4)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre5 = "https://listado.mercadolibre.com.co/computadores_Desde_201_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre5)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre6 = "https://listado.mercadolibre.com.co/computadores_Desde_251_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre6)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre7 = "https://listado.mercadolibre.com.co/computadores_Desde_301_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre7)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre8 = "https://listado.mercadolibre.com.co/computadores_Desde_351_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre8)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre9 = "https://listado.mercadolibre.com.co/computadores_Desde_401_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre9)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre10 = "https://listado.mercadolibre.com.co/computadores_Desde_451_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre10)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

#------------------------------------------------------------------------------------------------------------
link_mercadolibre11 = "https://listado.mercadolibre.com.co/computadores_Desde_501_NoIndex_True"
#Obtener Página Web
driver.get(link_mercadolibre11)

#Obtener Contenido
content = driver.page_source

#Analizar Código Fuente de la Página Web
soup = bs(content,"html.parser")

buscarTiendaOficial()
buscarLink()
buscarRecomendado()
buscarDescuento()
buscarTitulo()
buscarPrecio()
buscarCuota()
buscarEnvio()

print("Recomendado")
print(numpy.size(recomendado))
print("Descuento")
print(numpy.size(descuento))
print("Titulo")
print(numpy.size(titulo))
print("Precio")
print(numpy.size(precio))
print("Cuota")
print(numpy.size(cuota))
print("Envio")
print(numpy.size(envio))
print("Link")
print(numpy.size(link))
print("Tiendas")
print(numpy.size(tiendas))

#Se cargan los datos organizados de los arrays en otro array para guardarlos en un cvs.
for x in cuota:
    vector.append({'Titulo':titulo[i], 'Precio':precio[i],'Tipo_Envio':envio[i], 'Cuota':cuota[i],'Descuento':descuento[i], 'Es_recomendado':recomendado[i],'Tienda_Oficial':tiendas[i], 'Link_Publicación':link[i]})#'Link':link
    #Se usa par aiterar en los diferentes arrays.
    i=i+1

#Try para obtener error si algo sale mal, de lo contrario mensaje todo salio bien.
try:
  os.chdir(r'D:\Universidad\10 Semestre\Mineria de datos\Prueba Script') #####Ruta de guardado del csv
  convertirExcel = pd.DataFrame(vector)
  convertirExcel.to_excel('Datos_MercadoLibre.xlsx',index=False)
  print("Documento csv generado correctamente")

except:
  print("Error ! Verifique la ruta de guardado del archivo csv")

driver.quit()