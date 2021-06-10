# t.me/Pepe_el_tiza_bot

# 1789009907:AAHq9GBmVkfBqkcGFbevw8iLuiB3SLMed_k

from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler,CallbackQueryHandler, Filters

from telegram import PhotoSize,ChatAction,Bot,InlineKeyboardMarkup,InlineKeyboardButton,InputMedia,InputMediaPhoto

Lista_de_Productos = [
    (1,'Bombones a Domicilio'),
    (2,'Pipas de Madera'),  
    ]

Categorias_Productos = [
    (1,'Chucheria'),
    (2,'Artesania'),
]

lista = []
'''
boton1 = InlineKeyboardButton(
    text='Artesania',
    callback_data= 'Comida'
)

boton2 = InlineKeyboardButton(
    text='PEPE',
    callback_data= 'Artesania'
)
'''
for i in Categorias_Productos:
    lista.append(
    InlineKeyboardButton(text=i[1],callback_data= i[1])
    )
   

def start(update,context):
    
    
   
    #foto = PhotoSize(file_id=open('2.jpg','rb'),file_unique_id='s',width=4,height =5)
    #foto = InputMediaPhoto(media=open('2.jpg','rb'))

    #foto = open('2.jpg','rb')

    print(update.message.chat.id)
    bot.send_message(
        chat_id=update.message.chat.id,
        text='BIENVENIDO A ESTA HUMILDE TIENDA:',
        reply_markup= InlineKeyboardMarkup([
            lista,
        ]),    
        )
    #update.message.chat.send_action(action=ChatAction.UPLOAD_PHOTO,timeout=None)   

    '''
    bot.send_photo(
        chat_id=update.message.chat.id,
        photo=foto,
        caption='Reloj Pillo',
        reply_markup= InlineKeyboardMarkup([
            lista,
        ]),     
    )
    '''


def FuncionCallback(update,context):
    query = update.callback_query
    query.answer()

    print(update.callback_query.message.chat.id)

    boton1 = InlineKeyboardButton(
        text='Volver',
        callback_data= 'Volver')


   
    query.edit_message_text(
        text='Estas son las ofertas en esta rama Artesania:',
        reply_markup= InlineKeyboardMarkup([
            [boton1]
        ])
    )


def FuncionCallback2(update,context):
    query = update.callback_query
    query.answer()



    boton1 = InlineKeyboardButton(
        text='Volver',
        callback_data= 'Volver')


   
    query.edit_message_text(
        text='Estas son las ofertas en esta rama '+query.data+':',
        reply_markup= InlineKeyboardMarkup([
            [boton1]
        ])
    )



if __name__ == '__main__':

    updater = Updater(token='1789009907:AAHq9GBmVkfBqkcGFbevw8iLuiB3SLMed_k',use_context=True)
    dp = updater.dispatcher
    bot = Bot(token='1789009907:AAHq9GBmVkfBqkcGFbevw8iLuiB3SLMed_k') 
    dp.add_handler(CommandHandler('start',start))

    dp.add_handler(

        ConversationHandler(

        entry_points = [

            CallbackQueryHandler(pattern='Artesania',callback=FuncionCallback),
            CallbackQueryHandler(pattern='Chucheria',callback=FuncionCallback2),
            CallbackQueryHandler(pattern='Volver',callback=start),

        ],
        states={},
        fallbacks=[]
        )
    )

  
    updater.start_polling()
    updater.idle()