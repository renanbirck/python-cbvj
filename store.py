#
#
#

import sqlite3, parse, logging

class TweetStorage:
    """ Uma classe para tratamento do armazenamento dos _tweets_ coletados. """
    def __init__(self, database_name = 'tweets.db'):
        """ Quando o objeto é instanciado, criar uma conexão com o BD e uma instância
        do logger. """
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.initialize_table()

        # Configuração de logging.
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()
        self.logger.info("Criado o objeto para interação com o BD.")

    def __del__(self):  
        """ Quando o objeto TweetStorage for deletado, fechar o banco de dados. """
        self.connection.commit() # não deveria ser necessário! Mas não dói.
        self.connection.close()

    def initialize_table(self):
        """ Configura a tabela onde serão armazenados nossos tweets coletados. """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tweets (tweet_ID INTEGER NOT NULL UNIQUE,  
                            tweet_text TEXT NOT NULL, created INTEGER NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS parsed_tweets (tweet_ID INTEGER NOT NULL UNIQUE,
                            date TEXT NOT NULL, time TEXT NOT NULL, type TEXT NOT NULL,
                            place TEXT NOT NULL, neighbourhood TEXT NOT NULL, created INTEGER NOT NULL)''')
    
    def add_tweet(self, tweet_ID, tweet_text, creation_date):
        """ Adiciona um tweet. """
        self.cursor.execute('INSERT INTO tweets VALUES (?, ?, ?)', (tweet_ID, tweet_text, creation_date))
        self.connection.commit()
    
    def get_tweet_by_ID(self, tweet_ID):
        """ Puxa um tweet por ID. """
        return list(self.cursor.execute('SELECT tweet_ID, tweet_text, created FROM tweets WHERE tweet_ID = ?', tweet_ID))

    def get_all_events(self):
        """ Consulta o banco e retorna tudo aquilo que for ocorrência. """
        return list(self.cursor.execute('SELECT tweet_ID, tweet_text, created FROM tweets WHERE tweet_text LIKE "Ocorrência:%" ORDER BY tweet_ID DESC'))
    
    def parse_all_tweets(self):
        """ Consulta o banco e processa todos os tweets, adicionando na tabela parsed_tweet """
        all_tweets = self.get_all_events()
        for (tweet_ID, tweet_text, creation_date) in all_tweets:
            parsed_tweet = parse.parse_tweet(tweet_text)
            to_insert = (tweet_ID, *parsed_tweet, creation_date)
            try: # O tweet não está na base
                self.cursor.execute('INSERT INTO parsed_tweets VALUES (?, ?, ?, ?, ?, ?, ?)', to_insert)
                self.logger.info(f"O tweet com ID {tweet_ID} foi processado e adicionado na base.")
            except:  # O tweet já está na base
                pass
                #self.logger.info(f"O tweet com ID {tweet_ID} já tinha sido processado.")

        self.connection.commit()
