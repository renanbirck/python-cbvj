#
#
#

import sqlite3

class TweetStorage:
    def __init__(self, database_name = 'tweets.db'):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.initialize_table()

    def __del__(self):  
        """ Quando o objeto TweetStorage for deletado, fechar o banco de dados. """
        self.connection.close()

    def initialize_table(self):
        """ Configura a tabela onde serão armazenados nossos tweets coletados. """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tweets (tweet_ID INTEGER NOT NULL UNIQUE,  
                            tweet_text TEXT NOT NULL, created INTEGER NOT NULL)''')
    
    def add_tweet(self, tweet_ID, tweet_text, creation_date):
        self.cursor.execute('INSERT INTO tweets VALUES (?, ?, ?)', (tweet_ID, tweet_text, creation_date))
        self.connection.commit()
    
    def get_tweet_by_ID(self, tweet_ID):
        return list(self.cursor.execute('SELECT tweet_ID, tweet_text, created FROM tweets WHERE tweet_ID = ?', tweet_ID))

    def get_all_events(self):
        """ Consulta o banco e retorna tudo aquilo que for ocorrência. """

        return list(self.cursor.execute('SELECT tweet_ID, tweet_text, created FROM tweets WHERE tweet_text LIKE "Ocorrência:%" ORDER BY tweet_ID DESC'))