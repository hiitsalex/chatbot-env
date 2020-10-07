from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Terminal',
storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.serbian')
print('Pitaj me nesto...')
while True:
    try:
        pitanje = input()
        odgovor = bot.get_response(pitanje)
        print(odgovor)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break