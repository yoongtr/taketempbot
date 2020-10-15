# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:03:50 2020

@author: Admin
"""
import datetime
import os
import logging
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

HEROKU_TOKEN = 'token' # change to your token on Heroku
HEROKU_APPNAME = 'appname' # change to your Heroku appname

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="""I'm a bot that reminds you to take temperature!\n 
                             Try /timer to set a reminder every 12 hours, or /nani for fun ;;)!\n 
                             Alternatively you can try these commands:\n
                             /info \n
                             /name1 \n
                             /name2 \n
                             /name3 \n
                             /name4 \n
                             ...\n
                             and so on! See if you can find all the hidden commands! :x""")
    
def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Yo whatsup")
    
def covid(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Coronavirus!")
    
def name1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="loves apple")
    
def name2(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="loves potato")
    
def name3(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="loves broccoli")
    
def name4(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="loves salmon")
    
def name5(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="loves dogs")
    
def name6(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="loves cats")
    
def name7(update, context):
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

def callback_alarm2(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text='Omae wa mou shindeiru!')

def callback_timer2(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Bugging you every 3s with...')
    context.job_queue.run_repeating(callback_alarm2, 3, context=update.message.chat_id)
   
def stop_job(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Stopping...')
    context.job_queue.stop()
    
def fake_stop1(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Say please stop!:P")
    
def fake_stop2(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Meh")
    
def daily_reminder_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="orhor")

def daily_reminder(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Setting a daily reminder at 09:00:00')
    context.job_queue.run_daily(daily_reminder_message, time = datetime.time(9,00,00), context=update.message.chat_id)

if __name__ == "__main__":
    updater = Updater(token=HEROKU_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    TOKEN = HEROKU_TOKEN
    NAME = HEROKU_APPNAME
    
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
    
    austin_handler = CommandHandler('name1', name1)
    dispatcher.add_handler(austin_handler)
    
    yoong_handler = CommandHandler('name2', name2)
    dispatcher.add_handler(yoong_handler)
    
    andy_handler = CommandHandler('name3', name3)
    dispatcher.add_handler(andy_handler)
    
    hung_handler = CommandHandler('name4', name4)
    dispatcher.add_handler(hung_handler)
    
    lg_handler = CommandHandler('name5', name5)
    dispatcher.add_handler(lg_handler)
    
    dang_handler = CommandHandler('name6', name6)
    dispatcher.add_handler(dang_handler)
    
    duong_handler = CommandHandler('name7', name7)
    dispatcher.add_handler(duong_handler)
    
    error_handler = CommandHandler('error', error)
    dispatcher.add_handler(error_handler)
    
    timer_handler = CommandHandler('timer', callback_timer)
    dispatcher.add_handler(timer_handler)

    nani_handler = CommandHandler('nani', callback_timer2)
    dispatcher.add_handler(nani_handler)

    stop_handler = CommandHandler('pleasestop', stop_job, pass_job_queue=True)
    dispatcher.add_handler(stop_handler)
    
    fakestop_handler1 = CommandHandler('stop', fake_stop1)
    dispatcher.add_handler(fakestop_handler1)
    
    fakestop_handler2 = CommandHandler('dumastop', fake_stop2)
    dispatcher.add_handler(fakestop_handler2)
    
    daily_reminder_handler = CommandHandler('reminder', daily_reminder)
    dispatcher.add_handler(daily_reminder_handler)
    
    """updater.start_polling()
    updater.idle()
    updater.stop()"""
    
    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
