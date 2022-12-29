from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from training import train


CORPUS_FILE = "dan.txt"

# train(CORPUS_FILE)

chatbot = ChatBot("Dan", 
database_uri='sqlite:///db.sqlite3')

exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"> {chatbot.get_response(query)}")
