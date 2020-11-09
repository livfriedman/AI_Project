#import modules
#chatbot class used to instantiate chatbot object 
from chatterbot import ChatBot
#train chatbot on custom list of statements (we define)
from chatterbot.trainers import ListTrainer
#train on datasets from chatterbot corpus project (*not sure*)
from chatterbot.trainers import ChatterBotCorpusTrainer

#instantiate
#use "chatbot" object -> name and reference logic/storage adapters 
#read_only = false -> learn from user inputs 
GainesvilleBot = ChatBot(name = 'GainesvilleBot', 
						read_only = False, 
						logic_adapters = ["chatterbot.logic.BestMatch"], 
						storage_adapter = "chatterbot.storage.SQLStorageAdapter")

#use training data for greetings and conversation 
corpus_trainer = ChatterBotCorpusTrainer(GainesvilleBot)
corpus_trainer.train("chatterbot.corpus.english")
corpus_trainer.train("chatterbot.corpus.english.greetings")
corpus_trainer.train("chatterbot.corpus.english.gainesville")
corpus_trainer.train("chatterbot.corpus.english.conversations")

#use by calling get_response
while(True):
    user_input = input()
    if(user_input == 'q'):
        break
    response = GainesvilleBot.get_response(user_input)
    print(response)
