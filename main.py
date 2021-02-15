from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
import sys


TOKEN = os.getenv("TOKEN")
API_URL = "https://api.telegram.org/bot" + TOKEN

# Mode ortam değişkeni
mode = os.getenv("MODE")

# Mod'a uyarlı, updater başlatma fonksiyonu belirler
if mode == "dev":
    def run(updater):
        updater.start_polling()
        start(CallbackContext(updater.dispatcher))
elif mode == "prod":
    def run(updater):
        # Port ve Uygulamanızın adını içeren ortam değişkenleri
        PORT = int(os.environ.get("PORT", 8443))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
        start(CallbackContext(updater.dispatcher))
        updater.idle()
else:
    print("Bir mod seçilmedi")
    sys.exit(1)

def run(updater):
    print("Bot başlatıldı.")
    updater.start_polling()


def start(update, context):
    message = "Bot başlatıldı.\n"
    message += "Daha fazla bilgi için /yardim komutunu gönderin."
    # Bot gönderilen mesaja özel yanıt döndürüyor
    update.message.reply_text(message)


def help(update, context):
    help_message = "Mevcut komutları aşağıdan görebilirsin.\n\n"
    help_message += "/hakkinda - Chatbot hakkındaki bilgileri verir.\n"
    help_message += "/yardim - Tüm komutları listeler.\n"
    help_message += "/start - Chatbotu başlatır.\n"
    help_message += "/selam - selam verir.\n"
    help_message += "/naber - soruna yanıt verir.\n"
    help_message += "/sen_kimsin - kendini tnaıtır.\n"
    help_message += "/burdamisin - soruna yanıt verir.\n"
    help_message += "/nereyekayboldun - soruna yanıt verir.\n"
    # Bot gönderilen mesaja özel yanıt döndürüyor
    update.message.reply_text(help_message)


def about(update, context):
    message = "Merhaba, ben bir test chatbotum.\n"
    message += "Sana hizmet etmek için buradayım."
    # Bot gönderilen mesaja özel yanıt döndürüyor
    update.message.reply_text(message)


def selam(update, context):
    message = "Selam dostum nası gidiyo \n"

    # Bot gönderilen mesaja özel yanıt döndürüyor
    update.message.reply_text(message)

def naber(update, context):
    message = "İyilik.\n"
    message += "Senden naber?"
    # Bot gönderilen mesaja özel yanıt döndürüyor
    update.message.reply_text(message)

def sen_kimsin(update, context):
    message = "Ya bu nası soru!\n"
    message += "Benim ben Kübraa \n"
    message += "Kimle konuştuğunu bilmiyor musun heeğ ?\n"
    message += "Neyse asıl sen kimsin?"
    # Bot gönderilen mesaja özel yanıt döndürüyor
    update.message.reply_text(message)
    
def burdamisin(update, context):
     message = "Burdayım burda :b \n"
     message += "Gitmedim bir yere!"
     message += "Seni bırakır mıyım hiç!"
     # Bot gönderilen mesaja özel yanıt döndürüyor
     update.message.reply_text(message)
         
def nereyekayboldun(update, context):
     message = "İşim çıkmıştı ya \n"
     message += "Hayırdır ne olduydu ?"
     message += "Bensiz iki dk yapamıyon dimii ?  "
     # Bot gönderilen mesaja özel yanıt döndürüyor
     update.message.reply_text(message)
   

def wrongCommand(update, context):
     update.message.reply_text("Üzgünüm, gönderdiğiniz mesajı anlayamıyorum.")


def main():
    # Telegram Api güncellemelerini yakalayan bir Updater oluşturduk
    updater = Updater(TOKEN, use_context=True)
    # Api güncellemelerini yönlendirmek için Dispatcher oluşturduk
    dp = updater.dispatcher

    # Dispatchera komut yakalayıcılarımızı ekledik
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("yardim", help))
    dp.add_handler(CommandHandler("hakkinda", about))
    dp.add_handler(CommandHandler("selam", selam))
    dp.add_handler(CommandHandler("naber", naber))
    dp.add_handler(CommandHandler("sen_kimsin", sen_kimsin))
    dp.add_handler(CommandHandler("burdamisin", burdamisin))
    dp.add_handler(CommandHandler("nereyekayboldun", nereyekayboldun))
    # Yanlış bir komut girildiyse burada yakalanacak
    dp.add_handler(MessageHandler(Filters.text, wrongCommand))

    run(updater)


if __name__ == '__main__':
    main()
