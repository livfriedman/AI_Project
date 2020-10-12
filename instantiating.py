#import modules
#chatbot class used to instantiate chatbot object 
from chatterbot import ChatBot
#train chatbot on custom list of statements (we define)
from chatterbot.trainers import ListTrainer
#train on datasets from chatterbot corpus project (*not sure*)
from chatterbot.trainers import ChatterBotCorpusTrainer

#instantiate
#read_only = false -> learn from user inputs 
GainesvilleBot = ChatBot(name = 'GainesvilleBot', 
						read_only = False, 
						logic_adapters = ["chatterbot.logic.BestMatch"], 
						storage_adapter = "chatterbot.storage.SQLStorageAdapter")
