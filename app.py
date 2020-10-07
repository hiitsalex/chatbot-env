from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pymongo import MongoClient
from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer

client = MongoClient("mongodb+srv://Test:Test@chatbotcluster.twqsk.gcp.mongodb.net/testbaza?retryWrites=true&w=majority")
db=client.get_database('testbaza')
docs=db.test
#importujemo flask da bismo kreirali veb aplikaciju
#render_template modul nam omogućava da renderujemo html
#request modul nam omogućava da upravljamo HTTP zahtevima
#importujemo ChatBot da bismo kreirali našeg bota
#importujemo trenera kako bismo mogli da istreniramo neseg bota sa korpusom za engleski jezik

#kreiramo flask aplikaciju
app = Flask(__name__)

#kreiramo bota, koji kao prvi parametar ima ime bota
#može imati niz različitih parametara **kwargs https://chatterbot.readthedocs.io/en/stable/chatterbot.html
#storage_adapter nam definise tip baze u kojoj cemo cuvati podatke 
bot = ChatBot('Web bot',
storage_adapter='chatterbot.storage.SQLStorageAdapter')

#kreiramo trenera nad nasim botom

trainer = ChatterBotCorpusTrainer(bot)
#trainer = ListTrainer(bot)


#treniramo bota predefinisanim korpusom fraza iz Chatterbot korpusa
#https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data

trainer.train('chatterbot.corpus.serbian')



#kreiramo home rutu
@app.route("/")
#kreiramo funkciju koja obradjuje home rutu. 
#Potrebno je da ova funkcija ide direktno ispod definisane rute
def home():
    #u okviru home rute renderujemo index.html fajl koji se nalazi u templates folderu
    return render_template("index.html")

@app.route("/get")
#get putanja nam služi da obradimo pitanja koja korisnik šalje sa weba
def get_bot_odgovor():
    #pitanje cemo slati kroz GET zahtev sa argumentom 'poruka'
    #ovaj argument ce se definisati u index.html fajlu
    pitanje = request.args.get('poruka')
    print(pitanje)
    x=docs.find_one(pitanje)
    if x is None: 
      new = {'name':'Pitanje', 'message':pitanje,'odgovor':''}
      docs.insert_one(new)
    
    
    return str(bot.get_response(pitanje))
    #odgovor cast-ujemo u string
    #i kroz taj GET zahtev saljemo odgovor od bota do klijenta

#pokrecemo aplikaciju    
if __name__=="__main__":
    app.run()