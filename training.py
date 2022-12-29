import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


def train(chat_export_file):
    bot = ChatBot('Dan',
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
        }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )

    trainer = ListTrainer(bot)

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
        
    content_corpus = content.split("\n")

    for i in range(0, len(content_corpus) - 2, 2):
        pair = [content_corpus[i], content_corpus[i+1]]
        trainer.train(pair)
        
    trainer_corpus = ChatterBotCorpusTrainer(bot)
    trainer_corpus.train('chatterbot.corpus.english')
    
    """
    with open(chat_export_file, "r") as corpus_file:
            content = corpus_file.read()
    
    dialogues = content.split("\n")

    for dialogue in dialogues:
        sample = dialogue.split("__eou__")
        sample.pop(-1)
        trainer.train(sample)
    """

    """
    trainer = ListTrainer(chatbot)
    cleaned_corpus = clean_corpus(CORPUS_FILE)
    trainer.train(cleaned_corpus)
    """

    """
    message_corpus = remove_chat_metadata(chat_export_file)
    return message_corpus
    """

def remove_chat_metadata(chat_export_file):
    pattern1 = r"\n"
    pattern2 = r"__eou__"

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern1, "", content)
    cleaned_corpus = re.sub(pattern2, "\n", cleaned_corpus)
    # print(cleaned_corpus)
    return tuple(cleaned_corpus.split("\n"))