from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''Hi iam welcome messanger bot 
Add me to your group 
 
 Made with Love ❤️ by @lntechnical

  ''')
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name} ,  LÜTFEN BURA MESAJI OKUMADAN KATILMIŞ OLDUĞUNUZ "EkoHarita - SADEC ACİL ÇAĞRILAR - www.ekoharita.org" (https://t.me/ekoharita) GRUBUNA MESAJ ATMAYIN. (2dk) 
-------------------------------------------------------------------------
:cyclone: Bu grup bir sohbet grubu değildir. 
:cyclone: Bu grup sadece ACİL çağrılar/paylaşımlar/duyurular için oluşturulmuştur. 
:cyclone: Bilgi kirliliği, spam ve gereksiz karşılıklı polemikler oluşmaması adına grup 30sn'de bir mesaj atılacak şekilde kısıtlanmıştır. 
:cyclone: Sadece haberleşme ve haber ağı yaratma amacıyla kurulmuştur. Lütfen emin olmadığınız, spekülatif, asılsız haberleri paylaşmayın. Gerçek bir haber bir canın hayatının kurtarılmasına, değişmesine vesile olabilir; asılsız bir haber ise tam tersine...
:cyclone: Siyasi parti propagandası ve reklam yapanlar gruptan uzaklaştırılacaktır.
:cyclone: Her türlü nefret söylemi içeren içerik paylaşımcıları gruptan uzaklaştırılacaktır. 
:cyclone: Şiddet içerikli ya da pornografik içerikli görsel paylaşanlar gruptan uzaklaştırılacaktır.
:cyclone: Grup kamuya açıktır. Bütünün hayrı için moderatörlerin bu grubu, gruptaki kişileri ve haber ağını riske atan ya da atacağını düşündüğü her türlü post yayınlandıktan sonra silinecektir.

Hassasiyet gösterdiğiniz için teşekkür ederiz.
Sağlıklı bir ortam oluşabilmesi için bu kuralların uygun olacağını düşündük. Önerilerinizi her zaman özel mesajla ya da info@ekoharita.org adresine iletebilirsiniz.
İzin aldığınız ve ilgileneceğini düşündüğünüz dostlarınızı da gruba eklemeyi unutmayınız lütfen. 🙂
-------------------------------------------------------------------------
Tamamen gönüllü çabalarla yürütülen EkoHarita'nın yıllık teknik masraflarına ve gelecek projelerine destek olmak isterseniz armağanda bulunabilirsiniz:
:gift::arrow_right: www.patreon.com/ekoharita
eğer sorun yaşarsanız TR web için,
:gift::arrow_right: www.kreosus.com/EkoHarita
adresinden destek miktarını seçip düzenli destekçi olabilirsiniz.
:white_check_mark: Web sitesini ziyaret ederek EkoHarita'yı keşfe çıkabilirsiniz. www.ekoharita.org - Şimdi üye olabilirsiniz.
:white_check_mark: Ekoloji alanında faaliyet gösteren bir oluşum/kolektif/inisiyatif/kurum/grup iseniz haritaya eklenmek için formu doldurabilirsiniz: https://www.ekoharita.org/ekoloji-haritasi/nokta-ekle/  ')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
