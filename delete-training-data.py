from chatterbot import ChatBot
chatbot = ChatBot("GUI Bot", storage_adapter="chatterbot.storage.MongoDatabaseAdapter")

chatbot.storage.drop()
