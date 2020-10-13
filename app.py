from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pymongo import MongoClient
from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer

client = MongoClient("mongodb+srv://Test:Test@chatbotcluster.twqsk.gcp.mongodb.net/testbaza?retryWrites=true&w=majority")
db=client.get_database('testbaza')
docs=db.test



app = Flask(__name__)


bot = ChatBot('Web bot',
storage_adapter='chatterbot.storage.SQLStorageAdapter')



trainer = ChatterBotCorpusTrainer(bot)


trainer.train('chatterbot.corpus.serbian')




@app.route("/")

def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_odgovor():
    pitanje = request.args.get('poruka')
    print(pitanje)
    x=docs.find_one(pitanje)
    if x is None: 
      new = {'name':'Pitanje', 'message':pitanje,'odgovor':''}
      docs.insert_one(new)
    
    
    return str(bot.get_response(pitanje))
      
if __name__=="__main__":
    app.run()