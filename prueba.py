
from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,CallbackQueryHandler, Filters

from telegram import InlineKeyboardMarkup,InlineKeyboardButton,InputMedia,InputMediaPhoto

Lista_de_Productos = [
    (0,'Bombones a Domicilio'),
    (1,'Pipas de Madera'),  
    (0,'Tacos'),
    (1,'Jarrones de Ceramica'),  
    (1,'Jarrones de Metal'), 
    (1,'Jarrones de Plastico'), 
    (1,'Jarrones de Aluminio'), 
    (1,'Jarrones de Madera'), 
    (1,'Jarrones de Barro'), 
   
    
    ]

Categorias_Productos = [
    (1,'Chucheria'),
    (2,'Artesania'),
]

'''
Codigo para enviar una lista en 3 columnas de botones


lista = []
lista2=[]
lista_final = []
contador = 0 

sobrante = 0

for i in Lista_de_Productos:
    if i[0] == 1:
        lista.append(i[1])
       


largo_lista=len(lista)

if largo_lista%3==0:
    sobrante=0


if (largo_lista-1)%3==0:
    sobrante=1
if (largo_lista-2)%3==0:
    sobrante=2



for i in lista:
        contador = contador+1
        if contador%3!=0:
            lista2.append(i)
        if contador%3==0:
            lista2.append(i)
            lista_final.append(lista2)
            lista2=[]
        if sobrante!=0 and contador==len(lista):
            lista_final.append(lista2)

print(lista_final)


'''

lista = [1,2]
lista2= [3,4]

lista3 = lista+lista2



print(lista3)