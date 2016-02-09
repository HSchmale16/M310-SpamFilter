import sqlite3

SPAM_TBL_SQL = """
CREATE TABLE IF NOT EXISTS SpamWords (
    word TEXT PRIMARY KEY,
    spamCount INTEGER DEFAULT 0,
    hamCount INTEGER DEFAULT 0
);
"""

# Init the spam database and loads this module up.
def initSpamDb():
    print SPAM_TBL_SQL
    return True

# key - the spam word
# isSpam - is this word a spammy word.
def updateSpamKey(key, isSpam):
    return key

# returns how spammy a word is from the database
def getSpaminess(key):
    return 0.4
