from chatterbot import ChatBot

bot = ChatBot("Pametni bot",
logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.TimeLogicAdapter'
])

# pitanje1 = 'What is 4+9?'
# pitanje2 = "Koliko je 5+5?"
# pitanje3 = "What time is it?"

response1 = bot.get_response('What time is it?')
# response2 = bot.get_response(pitanje2)
# response3 = bot.get_response(pitanje3)
print(response1)
# print(response2)
# print(response3)

