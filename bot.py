from os import PRIO_PGRP
from aiogram import Bot,Dispatcher,types,executor
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.message import Message

btn=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
btn.add("USD🇺🇸-UZS🇺🇿","USD🇺🇸-RUB🇷🇺","USD🇺🇸-EUR🇪🇺","USD🇺🇸-CHIN🇨🇳","USD🇺🇸-JAP🇯🇵","USD🇺🇸-KAZ🇰🇿","RUB🇷🇺-USD🇺🇸","RUB🇷🇺-UZS🇺🇿","RUB🇷🇺-EUR🇪🇺","RUB🇷🇺-KAZ🇰🇿","RUB🇷🇺-JAP🇯🇵","RUB🇷🇺-CHIN🇨🇳","EUR🇪🇺-UZS🇺🇿","EUR🇪🇺-RUB🇷🇺","EUR🇪🇺-USD🇺🇸","EUR🇪🇺-KAZ🇰🇿","EUR🇪🇺-CHIN🇨🇳","EUR🇪🇺-JAP🇯🇵","KAZ🇰🇿-UZS🇺🇿","KAZ🇰🇿-EUR🇪🇺","KAZ🇰🇿-USD🇺🇸","KAZ🇰🇿-RUB🇷🇺","KAZ🇰🇿-CHIN🇨🇳","KAZ🇰🇿-JAP🇯🇵","CHIN🇨🇳-EUR🇪🇺","CHIN🇨🇳-UZS🇺🇿","CHIN🇨🇳-USD🇺🇸","CHIN🇨🇳-RUB🇷🇺","CHIN🇨🇳-JAP🇯🇵","CHIN🇨🇳-KAZ🇰🇿","UZS🇺🇿-CHIN🇨🇳","UZS🇺🇿-JAP🇯🇵","UZS🇺🇿-KAZ🇰🇿","UZS🇺🇿-EUR🇪🇺","UZS🇺🇿-RUB🇷🇺","UZS🇺🇿-USD🇺🇸","JAP🇯🇵-UZS🇺🇿","JAP🇯🇵-USD🇺🇸","JAP🇯🇵-RUB🇷🇺","JAP🇯🇵-EUR🇪🇺","JAP🇯🇵-KAZ🇰🇿","JAP🇯🇵-CHIN🇨🇳")
token=''
bot=Bot(token=token)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def first(message: types.Message):
    await bot.send_message(message.chat.id, text=f"Salom, {message.from_user.first_name}! \nbotimizga hush kelibsiz valyutalarni ko'rib boring .\nBu bot @Im_young_developer tomonidan yartilgan",reply_markup=btn)


@dp.message_handler(content_types=['text'])
async def second(message: types.Message):
    text=message.text
    if text=="USD🇺🇸-UZS🇺🇿":
       inputs='USD'
       outputs='UZS'
    if text=="USD🇺🇸-RUB🇷🇺":
        inputs='USD'
        outputs='RUB'
    if text=="USD🇺🇸-EUR🇪🇺":
        inputs="USD"
        outputs="EUR"
    if text=="USD🇺🇸-CHIN🇨🇳":
        inputs="USD"
        outputs="CNY"
    if text=="USD🇺🇸-JAP🇯🇵":
        inputs="USD"
        outputs="JPY"
    if text=="USD🇺🇸-KAZ🇰🇿":
        inputs="USD"
        outputs="KZT"
    
    if text=="RUB🇷🇺-USD🇺🇸":
        outputs='USD'
        inputs='RUB'
    if text=="RUB🇷🇺-UZS🇺🇿":
        inputs='RUB'
        outputs='UZS'
    if text=="RUB🇷🇺-EUR🇪🇺":
        outputs="EUR"
        inputs="RUB"
    if text=="RUB🇷🇺-KAZ🇰🇿":
        inputs="RUB"
        outputs="KZT"
    if text=="RUB🇷🇺-JAP🇯🇵":
        inputs="RUB"
        outputs="JPY"
    if text=="RUB🇷🇺-CHIN🇨🇳":
        inputs="RUB"
        outputs="CNY"

    if text=="EUR🇪🇺-UZS🇺🇿":
        inputs="EUR"
        outputs="UZS"
    if text=="EUR🇪🇺-RUB🇷🇺":
        inputs="EUR"
        outputs="RUB"
    if text=="EUR🇪🇺-USD🇺🇸":
        outputs="USD"
        inputs="EUR"
    if text=="EUR🇪🇺-KAZ🇰🇿":
        inputs="EUR"
        outputs="KZT"
    if text=="EUR🇪🇺-CHIN🇨🇳":
        inputs="EUR"
        outputs="CNY"
    if text=="EUR🇪🇺-JAP🇯🇵":
        inputs="EUR"
        outputs="JPY"
 
    
    if text=="KAZ🇰🇿-UZS🇺🇿":
        inputs="KZT"
        outputs="UZS"
    if text=="KAZ🇰🇿-EUR🇪🇺":
        outputs="EUR"
        inputs="KZT"
    if text=="KAZ🇰🇿-USD🇺🇸":
        inputs="KZT"
        outputs="USD"
    if text=="KAZ🇰🇿-RUB🇷🇺":
        inputs="KZT"
        outputs="RUB"
    if text=="KAZ🇰🇿-CHIN🇨🇳":
        inputs="KZT"
        outputs="CNY"
    if text=="KAZ🇰🇿-JAP🇯🇵":
        inputs="KZT"
        outputs="JPY"
   

    if text=="CHIN🇨🇳-EUR🇪🇺":
        inputs="CNY"
        outputs="EUR"
    if text=="CHIN🇨🇳-UZS🇺🇿":
        inputs="CNY"
        outputs="UZS"
    if text=="CHIN🇨🇳-USD🇺🇸":
        outputs="USD"
        inputs="CNY"
    if text=="CHIN🇨🇳-RUB🇷🇺":
        inputs="CNY"
        outputs="RUB"
    if text=="CHIN🇨🇳-JAP🇯🇵":
        inputs="CNY"
        outputs="JPY"
    if text=="CHIN🇨🇳-KAZ🇰🇿":
        inputs="CNY"
        outputs="KZT"
    
    if text=="UZS🇺🇿-CHIN🇨🇳":
        outputs="CNY"
        inputs="UZS"
    if text=="UZS🇺🇿-JAP🇯🇵":
        outputs="JPY"
        inputs="UZS"
    if text=="UZS🇺🇿-KAZ🇰🇿":
        outputs="KZT"
        inputs="UZS"
    if text=="UZS🇺🇿-EUR🇪🇺":
        outputs="UZS"
        inputs="EUR" 
    if text=="UZS🇺🇿-RUB🇷🇺":
        outputs='RUB'
        inputs='UZS'  
    if text=="UZS🇺🇿-USD🇺🇸":
        outputs='USD'
        inputs='UZS'


    if text=="JAP🇯🇵-UZS🇺🇿":
        inputs="JPY"
        outputs="UZS"
    if text=="JAP🇯🇵-USD🇺🇸":
        inputs="JPY"
        outputs="USD"
    if text=="JAP🇯🇵-RUB🇷🇺":
        inputs="JPY"
        outputs="RUB"
    if text=="JAP🇯🇵-EUR🇪🇺":
        inputs="JPY"
        outputs="EUR"
    if text=="JAP🇯🇵-KAZ🇰🇿":
        inputs="JPY"
        outputs="KZT"
    if text=="JAP🇯🇵-CHIN🇨🇳":
        inputs="JPY"
        outputs="CNY"
  
    import requests
    import json
    url='https://v6.exchangerate-api.com/v6/056edfc7e154317e02b8f85c/latest/'+inputs
    response=requests.get(url)
    rest=json.loads(response.text)
    result=str(rest['conversion_rates'][outputs])
    await bot.send_message(message.chat.id,result)

        





if __name__=='__main__':
    executor.start_polling(dp)
