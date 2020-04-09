# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:03:50 2020

@author: Admin
"""
import os
import logging
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="I'm a bot that reminds you to take temperature!")
    
def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Nha minh co 7 nguoi: Austin, Yoong, Andy, Hung, LG, Dang va Duong")
    
def covid(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Coronavirus!")
    
def austin(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="GEHHHHH!")
    
def yoong(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Xinh dep ahihi!")
    
def andy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Xam bm!")
    
def hung(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="nhamquochung!")
    
def lg(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="CHIHAI")
    
def dang(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="deng deng deng!")
    
def duong(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="fun-sized")
    
def error(update, context, error):
    logger.warning('Update "%s" caused error "%s"', context, error)
    
def callback_alarm(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text='Take temp guys!')

def callback_timer(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Setting a timer for every 12h!')
    context.job_queue.run_repeating(callback_alarm, 43200, context=update.message.chat_id)


if __name__ == "__main__":
    updater = Updater(token='1230478984:AAEVrxbJxXo3vpX2ChbpM5qcDxLFdusziNQ', use_context=True)
    dispatcher = updater.dispatcher
    TOKEN = "1230478984:AAEVrxbJxXo3vpX2ChbpM5qcDxLFdusziNQ"
    NAME = "taketemp"
    
    # Port is given by Heroku
    PORT = os.environ.get('PORT')
    
    # Logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # All the handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    info_handler = CommandHandler('info', info)
    dispatcher.add_handler(info_handler)
    
    covid_handler = CommandHandler('covid', covid)
    dispatcher.add_handler(covid_handler)
    
    austin_handler = CommandHandler('austin', austin)
    dispatcher.add_handler(austin_handler)
    
    yoong_handler = CommandHandler('yoong', yoong)
    dispatcher.add_handler(yoong_handler)
    
    andy_handler = CommandHandler('andy', andy)
    dispatcher.add_handler(andy_handler)
    
    hung_handler = CommandHandler('hung', hung)
    dispatcher.add_handler(hung_handler)
    
    lg_handler = CommandHandler('lg', lg)
    dispatcher.add_handler(lg_handler)
    
    dang_handler = CommandHandler('dang', dang)
    dispatcher.add_handler(dang_handler)
    
    duong_handler = CommandHandler('duong', duong)
    dispatcher.add_handler(duong_handler)
    
    error_handler = CommandHandler('error', error)
    dispatcher.add_handler(error_handler)
    
    timer_handler = CommandHandler('timer', callback_timer)
    dispatcher.add_handler(timer_handler)
    
    
    """updater.start_polling()
    updater.idle()
    updater.stop()"""
    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()