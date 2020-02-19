import telebot
from cens import *
from reqcens import *
from questions import *
from variables import *
import random

bot = telebot.TeleBot(token_api)


keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.add(locate, number, price)
key = telebot.types.InlineKeyboardMarkup()
key2 = telebot.types.InlineKeyboardMarkup()
iphone5 = telebot.types.InlineKeyboardButton(text="iPhone 5S/SE", callback_data="iphone5")
iphone6 = telebot.types.InlineKeyboardButton(text="iPhone 6", callback_data="iphone6")
iphone6s = telebot.types.InlineKeyboardButton(text="iPhone 6S", callback_data="iphone6s")
iphone7 = telebot.types.InlineKeyboardButton(text="iPhone 7", callback_data="iphone7")
iphone8 = telebot.types.InlineKeyboardButton(text="iPhone 8", callback_data="iphone8")
iphonex = telebot.types.InlineKeyboardButton(text="iPhone X", callback_data="iphonex")
iphonexs = telebot.types.InlineKeyboardButton(text="iPhone XS", callback_data="iphonexs")
iphone11 = telebot.types.InlineKeyboardButton(text="iPhone 11", callback_data="iphone11")
iphone11pro = telebot.types.InlineKeyboardButton(text="iPhone 11 Pro", callback_data="iphone11pro")
glassrep = telebot.types.InlineKeyboardButton(text="Замена стекла", callback_data="glassrep")
bad = telebot.types.InlineKeyboardButton(text="Плохо 😒", callback_data="bad")
good = telebot.types.InlineKeyboardButton(text="Отлично 😏", callback_data="good")

includemsg = (iphone5, iphone6, iphone6s, iphone7, iphone8, iphonex, iphonexs, iphone11, iphone11pro, glassrep, good, bad, locate, number, price,
            'спасибо', '/start', 'спасибо', 'привет', 'как зовут мастера?', censes, reqcen, hello_to)
key.add(iphone5, iphone6, iphone6s, iphone7, iphone8, iphonex, iphonexs, iphone11, iphone11pro, glassrep)
key2.add(good, bad)
@bot.message_handler(commands=['start']) #Стартовый диалог, который пробудит бота

#while True:
  #  try:
      #  bot.pooling(none_stop = True, interval = 0, timeout = 20)
  #  except Exception as E:
      #  print(E:args)
     #   time.sleep(2)

def start_message(message):

         sent = bot.send_message(message.chat.id, hello_message)
         bot.register_next_step_handler(sent,name)

def name(message):
    bot.send_message(message.chat.id, '{name}. Что тебе подсказать?'.format(name=message.text), reply_markup=keyboard2)



@bot.message_handler(content_types=['text']) #Написание всех диалогов, в том числе вызов прайса и знакомства
def dialog(message):

             if message.text == locate:
                bot.send_message(message.chat.id, location)
             elif message.text == number:
                bot.send_message(message.chat.id, phone_numbers)
             if message.text == price:
                bot.send_message(message.chat.id, 'Какой у тебя аппарат?', reply_markup=key)

        #Ответы на любезности
             if message.text.lower() == 'как тебя зовут?':
                bot.send_message(message.chat.id, 'Меня зовут AppleService бот')
             if message.text.lower() == 'спасибо':
                bot.send_message(message.chat.id, 'Это тебе спасибо 🥰')
             if message.text.lower() == 'привет':
                bot.send_message(message.chat.id, 'Привет, как у тебя дела?', reply_markup=key2)
             if message.text.lower() == 'как зовут мастера?':
                bot.send_message(message.chat.id, 'Вообще мастер тут я, но со мной работают ещё Арменак и Николай! ')
             else:
                for censfilter in censes:
          # Ответы на оскорбления
                  if message.text.lower() == censfilter:
                    censfil = random.choice(reqcen)
                    bot.send_message(message.chat.id, censfil)
                    break


@bot.callback_query_handler(func=lambda button:True)
def inline_buttons(button):
  if button.data == 'iphone5':

      bot.send_message(button.message.chat.id,'<b>Apple iPhone 5S / SE</b>'                                       '\n' + '\n'
                                              '• <b>Замена дисплея</b> '+ '—' +' 2000₽ копия  / 3000₽ оригинал'   '\n' + '\n'
                                              '• <b>Замена аккумулятора</b> '+ '—' +'    1500₽'                   '\n' + '\n'
                                              '• <b>Замена корпуса</b> ' '—' + '         2500₽'                   '\n' + '\n'
                                              '• <b>Замена нижнего разъёма</b> ' '—' + ' 1500₽'                   '\n' + '\n'
                                              '• <b>Замена основной камеры</b> ' '—' + ' 1500₽ / 3000₽'           '\n' + '\n'
                                              '• <b>Замена передней камеры</b> ' '—' + ' 1500₽'                   '\n' + '\n'
                                                                                                        ,parse_mode='HTML')
  elif button.data == 'iphone6':
      bot.send_message(button.message.chat.id,'<b>Apple iPhone 6</b>'                                             '\n' + '\n'
                                              '• <b>Замена дисплея</b> ' + '—' + ' 2500₽ копия  / 3500₽ оригинал' '\n' + '\n'
                                              '• <b>Замена аккумулятора</b> ' + '—' + '  2000₽'                   '\n' + '\n'
                                              '• <b>Замена корпуса</b> ' '—' + '         2700₽'                   '\n' + '\n'
                                              '• <b>Замена нижнего разъёма</b> ' '—' + ' 2000₽'                   '\n' + '\n'
                                              '• <b>Замена основной камеры</b> ' '—' + ' 2000₽'                   '\n' + '\n'
                                              '• <b>Замена передней камеры</b> ' '—' + ' 2000₽'                   '\n' + '\n'
                                                                                                         , parse_mode='HTML')
  elif button.data == 'iphone6s':
      bot.send_message(button.message.chat.id,'<b>Apple iPhone 6S</b>'                                            '\n' + '\n'
                                              '• <b>Замена дисплея</b> ' + '—' + ' 2700₽ копия  / 4700₽ оригинал' '\n' + '\n'
                                              '• <b>Замена аккумулятора</b> ' + '—' + '  2500₽'                   '\n' + '\n'
                                              '• <b>Замена корпуса</b> ' '—' + '         2700₽'                   '\n' + '\n'
                                              '• <b>Замена нижнего разъёма</b> ' '—' + ' 2200₽'                   '\n' + '\n'
                                              '• <b>Замена основной камеры</b> ' '—' + ' 2500₽'                   '\n' + '\n'
                                              '• <b>Замена передней камеры</b> ' '—' + ' 2000₽'                   '\n' + '\n'
                                                                                                         , parse_mode='HTML')
  elif button.data == 'iphone7':
      bot.send_message(button.message.chat.id,'<b>Apple iPhone 7</b>'                                             '\n' + '\n'
                                              '• <b>Замена дисплея</b> ' + '—' + ' 3200₽ копия  / 6500₽ оригинал' '\n' + '\n'
                                              '• <b>Замена аккумулятора</b> ' + '—' + '  2800₽'                   '\n' + '\n'
                                              '• <b>Замена корпуса</b> ' '—' + '         3000₽'                   '\n' + '\n'
                                              '• <b>Замена нижнего разъёма</b> ' '—' + ' 2800₽'                   '\n' + '\n'
                                              '• <b>Замена основной камеры</b> ' '—' + ' 4500₽'                   '\n' + '\n'
                                              '• <b>Замена передней камеры</b> ' '—' + ' 2500₽'                   '\n' + '\n'
                                                                                                         , parse_mode='HTML')
  elif button.data == 'iphone8':
      bot.send_message(button.message.chat.id,'<b>Apple iPhone 8</b>'                                             '\n' + '\n'
                                              '• <b>Замена дисплея</b> ' + '—' + ' 3200₽ копия  / 7500₽ оригинал' '\n' + '\n'
                                              '• <b>Замена аккумулятора</b> ' + '—' + '  3300₽'                   '\n' + '\n'
                                              '• <b>Замена корпуса</b> ' '—' + '         4000₽'                   '\n' + '\n'
                                              '• <b>Замена нижнего разъёма</b> ' '—' + ' 3000₽'                   '\n' + '\n'
                                              '• <b>Замена основной камеры</b> ' '—' + ' 5500₽'                   '\n' + '\n'
                                              '• <b>Замена передней камеры</b> ' '—' + ' 3000₽'                   '\n' + '\n'
                                                                                                         , parse_mode='HTML')
  elif button.data == 'iphonex':
      bot.send_message(button.message.chat.id,'<b>Apple iPhone X</b>'                                             '\n' + '\n'
                                              '• <b>Замена дисплея</b> ' + '—' + ' 10000₽ копия / 18000₽ оригинал''\n' + '\n'
                                              '• <b>Замена аккумулятора</b> ' + '—' + '  5000₽'                   '\n' + '\n'
                                              '• <b>Замена корпуса</b> ' '—' +          '6000₽'                   '\n' + '\n'
                                              '• <b>Замена нижнего разъёма</b> ' '—' + ' 4000₽'                   '\n' + '\n'
                                              '• <b>Замена основной камеры</b> ' '—' + ' 4000₽'                   '\n' + '\n'
                                              '• <b>Замена передней камеры</b> ' '—' + ' 7500₽'                   '\n' + '\n'
                                                                                                         , parse_mode='HTML')
  elif button.data == 'glassrep':
      bot.send_message(button.message.chat.id,'<b>Замена стекла</b>'                                              '\n' + '\n'
                                              '• <b>iPhone 5S</b> ' + '—' + ' 2500₽'                              '\n' + '\n'
                                              '• <b>iPhone 6</b> ' + '—' + '  2800₽'                              '\n' + '\n'
                                              '• <b>iPhone 6 Plus</b> ' '—' +'3500₽'                              '\n' + '\n'
                                              '• <b>iPhone 6S</b> ' '—' + ' 3500₽'                                '\n' + '\n'
                                              '• <b>iPhone 6S Plus</b> ' '—' + ' 4500₽'                           '\n' + '\n'
                                              '• <b>iPhone 7</b> ' '—' + ' 4500₽'                                 '\n' + '\n'
                                              '• <b>iPhone 7 Plus</b> ' '—' + ' 5800₽'                            '\n' + '\n'
                                              '• <b>iPhone 8</b> ' '—' + ' 5500₽'                                 '\n' + '\n'
                                              '• <b>iPhone 8 Plus</b> ' '—' + ' 6800₽'                            '\n' + '\n'
                                              '• <b>iPhone X</b> ' '—' + ' 12000₽'                                '\n' + '\n'
                                              '• <b>iPhone XR</b> ' '—' + ' 10000₽'                               '\n' + '\n'
                                              '• <b>iPhone XS</b> ' '—' + ' 17000₽'                               '\n' + '\n'
                                                                                                         , parse_mode='HTML')
  elif button.data == 'iphonexs':
      bot.send_message(button.message.chat.id,'Мне не сказали ещё цены на этот телефон 🤫')
  elif button.data == 'iphone11':
      bot.send_message(button.message.chat.id,'Мне не сказали ещё цены на этот телефон 🤫')
  elif button.data == 'iphone11pro':
      bot.send_message(button.message.chat.id,'Мне не сказали ещё цены на этот телефон 🤫')
  elif button.data == 'bad':
      bot.send_message(button.message.chat.id, 'Ты чего? Держи промокод на скидку 5% на аксессуары! <b>HXmj4</b>',parse_mode='HTML')
  elif button.data == 'good':
      bot.send_message(button.message.chat.id, 'Отличное настроение - залог успеха!')

bot.polling(none_stop=True)