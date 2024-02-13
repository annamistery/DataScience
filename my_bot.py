from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

from dotenv import load_dotenv
import time
import os
# возьмем переменные окружения из .env
load_dotenv()

# загружаем токен бота
TOKEN = os.environ.get("TOKEN")


# функция команды /start
async def start(update, context):
    await update.message.reply_text('Первая задача выполнена!')
    
async def warcraft(update, context):
     # создаем список Inline кнопок
    keyboard = [[InlineKeyboardButton("Альянс", callback_data="Альянс"),
                InlineKeyboardButton("Орда", callback_data="Орда")]]  
    # создаем Inline клавиатуру
    reply_markup = InlineKeyboardMarkup(keyboard)

    # прикрепляем клавиатуру к сообщению
    await update.message.reply_text('Выберите функцию', reply_markup=reply_markup)   

async def button_callback(update, context):
    query = update.callback_query
    query.answer()  # Ответ на запрос callback

    # Удаляем оригинальное сообщение с клавиатурой
    await query.delete_message()
        
    
# функция для текстовых сообщений /text
async def text(update, context):
    await update.message.reply_text(len(update.message.text.split()))

async def voice(update, context):
    await update.message.reply_text(f'Голосовое сообщение c id: {update.message.message_id} получено!')  
    
# функция для изображений
async def image(update, context):
    
    # await update.message.reply_text('Мы получили от тебя изображение!')
    if not os.path.exists('images'):
       os.makedirs('images')
       
    # достаем файл изображения из сообщения
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_id = photo.file_id
    
    # сохраняем изображение на диск
    download_path = f"images/{file_id}.jpg"  # Формируем путь с ID файла
    await file.download_to_drive(download_path)  # Скачиваем файл
    
    await update.message.reply_text(f'Изображение c id: {file_id} получено!')
    
    await update.message.reply_text(f"Файл сохранён в {download_path}")   
   
    
def main():

    # точка входа в приложение
    application = Application.builder().token("TOKEN").build()

    print('Бот запущен...')

    # добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    application.add_handler(CommandHandler("warcraft", warcraft))
    
    application.add_handler(CallbackQueryHandler(button_callback))
       # добавляем обработчик текстовых сообщений
       
    application.add_handler(MessageHandler(filters.TEXT, text))
    
        # добавляем обработчик голосовых сообщений
    application.add_handler(MessageHandler(filters.VOICE, voice))
    
        # добавляем обработчик сообщений с изображением
    application.add_handler(MessageHandler(filters.PHOTO, image))
    

    # запуск приложения (для остановки нужно нажать Ctrl-C)
    application.run_polling()


if __name__ == "__main__":
    main()
