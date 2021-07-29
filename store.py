#
#
#

import sqlite3
DATABASE_NAME = 'tweets.db'

class TweetStorage:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()
        self.initialize_table()
    
    def initialize_table(self):
        """ Configura a tabela onde serão armazenados nossos tweets coletados. """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tweets (tweet_ID INTEGER NOT NULL UNIQUE,  
                            tweet_text TEXT NOT NULL, created INTEGER NOT NULL)''')
    
    def add_tweet(self, tweet_ID, tweet_text, creation_date):
        self.cursor.execute('INSERT INTO tweets VALUES (?, ?, ?)', (tweet_ID, tweet_text, creation_date))
    
    def get_tweet_by_ID(self, tweet_ID):
        self.cursor.execute('SELECT tweet_ID, tweet_text, created FROM tweets WHERE tweet_ID = ?', tweet_ID)
                    