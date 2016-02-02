import sqlite3

# Init the spam database and loads this module up.
def initSpamDb():
    return True

# key - the spam word
# isSpam - is this word a spammy word.
def updateSpamKey(key, isSpam):
    return key

# returns how spammy a word is from the database
def getSpaminess(key):
    return 0.4
