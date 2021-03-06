from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler, 
    Filters,
    PicklePersistence)

from telegram import( 
PhotoSize,
ChatAction,
Bot,
ReplyKeyboardMarkup,
InlineKeyboardMarkup,
InlineKeyboardButton,
InputMedia,
InputMediaPhoto
)

import os

#VARIABLES QUE VOY A UTILIZAR
TOKEN_BOT = "1789009907:AAHq9GBmVkfBqkcGFbevw8iLuiB3SLMed_k"

bot = Bot(token=TOKEN_BOT)

ESPERANDO_QUE_ELIJA_CATEGORIA = 0
ESPERANDO_QUE_ELIJA_PRODUCTO = 1
ESPERANDO_QUE_SELECCIONE_VOLVER = 2


#VARIABLES QUE VOY A UTILIZAR (END)




Lista_de_Productos = [
    (0,0,'Bombones a Domicilio',"Los Mejores Bombones del mundo, Corre que te los pierdes!"),
    (1,1,'Pipas de Madera',"Las mejores pipas de cuba, Partete el rostro con glamour!"),  
    (2,0,'Tacos',"Un bocado y para mexico de cabeza! "),
    (3,1,'Jarrones de Ceramica',"Pa que adornes el gaito!"),
    (4,2,'Collares para Mascotas',"Para que los tengas controlados y no se escapenjjj!"),
    (5,2,'Cereal para perros',"Alimenta a tu perrito como dios manda!"),
    (6,3,'Telefonos Celulares',"Los mejores al mejor precio!"),
    (7,3,'Laptops a domicilio',"Pa que juegues dota con calidad xd!"),
    ]


Categorias_Productos = [
    (0,'Comida🍏🍖🌮'),
    (1,'Artesania🔨🔧'),
    (2,'Mascotas🐶🐱'),
    (3,'Tecnologia📱💻'),
]




lista_estados_del_handler_categorias=[]


lista_estados_del_handler_productos =[]


def Enviar_Imagenes(update,context,id) -> bool:
    

    directorio_general = 'imgs/'
    directorio_objetivo=''
    imagenes=[]

    with os.scandir(directorio_general) as ficheros:
              
        for i in ficheros:                  
            if(i.is_dir() and i.name == str(id)):                 
                directorio_objetivo=directorio_general+i.name

     
    if directorio_objetivo!= '':
        imagenes=os.listdir(directorio_objetivo)

        
        update.callback_query.message.chat.send_action(action=ChatAction.UPLOAD_PHOTO,timeout=None)
        for i in imagenes:
            foto = open(directorio_objetivo+'/'+i,'rb')
            bot.send_photo(
            chat_id=update.callback_query.message.chat.id,
            photo=foto    
        )
        return True
    else:
        return False
                
    
def start(update,context)-> int:


    #Cargando los botones de las categoria en columnas de a 2
    lista_botones_categorias = []
    contador=0
    lista=[]

    for i in Categorias_Productos:
        contador = contador+1
        if contador%2==0:
            lista.append(InlineKeyboardButton(text=i[1],callback_data= i[0]))
            lista_botones_categorias.append(lista)
            lista=[]
        if contador%2!=0:
            lista.append(InlineKeyboardButton(text=i[1],callback_data= i[0]))
        if contador%2!=0 and contador == len(Categorias_Productos):
            lista_botones_categorias.append(lista)

    


    if update.message:

        update.message.reply_text(
            text='Bienvenido a nuestra tienda🥰 \nElija una categoria para ver los productos que tenemos en oferta:',
            reply_markup= InlineKeyboardMarkup(lista_botones_categorias),
        )

        return ESPERANDO_QUE_ELIJA_CATEGORIA
    else:
        query = update.callback_query
        query.answer()

        query.edit_message_text(
                text='BIENVENIDO A ESTA HUMILDE TIENDA:',
                reply_markup= InlineKeyboardMarkup(lista_botones_categorias)
            )
        return ESPERANDO_QUE_ELIJA_CATEGORIA



def ListarProductos(update,context)-> int:
    query = update.callback_query
    query.answer()

  
    lista_productos_de_categoria_seleccionada=[]
    
    #Capturando  la categoria seleccionada
    id_categoria = int(query.data)
    categoria= None

    for i in Categorias_Productos:
        if i[0] == id_categoria:
            categoria=i

 
    #Cargando en nuestra lista de productos, los productos que pertenecen a la categoria seleccionada
    for i in Lista_de_Productos:
    
        if i[1] == id_categoria:
            lista_productos_de_categoria_seleccionada.append(
                [InlineKeyboardButton(text=i[2],callback_data= i[0])]
            )


    #Cargando en nuestra lista de productos el boton de volver al menu principal 
    boton1 = InlineKeyboardButton(
        text='👈 Volver',
        callback_data= 'Volver_Al_start')

    lista_productos_de_categoria_seleccionada.append([boton1])

   
    query.edit_message_text(
        text='Estas son las ofertas en la rama '+categoria[1]+':',
        reply_markup= InlineKeyboardMarkup(lista_productos_de_categoria_seleccionada)
    )
            
    return ESPERANDO_QUE_ELIJA_PRODUCTO



def Detallar_Producto_Seleccionado(update,context)-> int:
    query = update.callback_query
    query.answer()

    
    #Capturando el id del producto seleccionado
    id_producto = int(query.data)
    
    
    #Capturando el producto
    producto = None

    for i in Lista_de_Productos:
    
        if i[0] == id_producto:
            producto = i


    id_categoria = int(producto[1])

    
    #Cargando en nuestra lista de productos el boton de volver al menu principal 
    boton1 = InlineKeyboardButton(
        text='👈 Volver',
        callback_data= id_categoria)

    
    boton2 = InlineKeyboardButton(
        text='💵 Hacer Pedido 💵',
        url= 'https://t.me/ElChanchy')

    query.edit_message_text(
        text=producto[2],  
    )
    
    
    
    Enviar_Imagenes(update,context,id_producto)

    bot.send_message(
        chat_id=update.callback_query.message.chat.id,
        text=producto[3]
    )

    bot.send_message(
        chat_id=update.callback_query.message.chat.id,
        text='Que desea hacer a continuaciòn:',
        reply_markup= InlineKeyboardMarkup([[boton1,boton2]])    
    )
     
    return ESPERANDO_QUE_SELECCIONE_VOLVER




#Cargando Datos




#Cargando los estados de categorias para el conversationhandler
for i in Categorias_Productos:
    
    lista_estados_del_handler_categorias.append(
        CallbackQueryHandler(pattern=i[0],callback=ListarProductos),
    )




#Cargando los estados de productos para el conversationhandler
lista_estados_del_handler_productos=[CallbackQueryHandler(pattern='Volver_Al_start',callback=start)]
for i in Lista_de_Productos:
    
    lista_estados_del_handler_productos.append(
        CallbackQueryHandler(pattern=i[0],callback=Detallar_Producto_Seleccionado),
    )




#Cargando Datos (END)





def main() -> None:

    persistence = PicklePersistence(filename='tienda_bot')

    updater = Updater(TOKEN_BOT,persistence=persistence)
    dispatcher = updater.dispatcher
    


    Conversacion = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states={

            ESPERANDO_QUE_ELIJA_CATEGORIA: lista_estados_del_handler_categorias,


            ESPERANDO_QUE_ELIJA_PRODUCTO:lista_estados_del_handler_productos,

            ESPERANDO_QUE_SELECCIONE_VOLVER:lista_estados_del_handler_categorias,
        },

        fallbacks=[]

    )

    dispatcher.add_handler(Conversacion)

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()