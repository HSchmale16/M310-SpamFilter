import sqlite3

INIT_DB_SQL = """
PRAGMA synchronous = 0;
PRAGMA journal_mode = TRUNCATE;
CREATE TABLE IF NOT EXISTS SpamWords (
    word            TEXT PRIMARY KEY,
    spamCount       INTEGER DEFAULT 0,
    hamCount        INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS KeyValue (
    key             TEXT PRIMARY KEY,
    value           INTEGER
);
CREATE VIEW spamCalc AS
SELECT
	word,
	spamCount,
	hamCount,
	(CAST(spamCount AS REAL)/ spamMsgCount) AS spamRate,
	(CAST(hamCount AS REAL) / hamMsgCount) AS hamRate,
    spamMsgCount,
    hamMsgCount
FROM
	(SELECT
		value as spamMsgCount
	FROM KeyValue
	WHERE
		key="SPAM_MSG_COUNT"),
	(SELECT
		value as hamMsgCount
	FROM KeyValue
	WHERE
		key="HAM_MSG_COUNT"),
	SpamWords AS sw
WHERE
	sw.hamCount + sw.spamCount > 5;
INSERT INTO KeyValue VALUES
    ('SPAM_MSG_COUNT', 0),
    ('TOTAL_MSG_COUNT', 0),
    ('HAM_MSG_COUNT', 0);
"""

# Init the spam database and loads this module up.
def initSpamDb():
    # The database connection is module global
    global dbconn
    dbconn = sqlite3.connect('spam.db')
    dbconn.execute(INIT_DB_SQL)
    return True

# key - the spam word
# isSpam - is this word a spammy word.
def updateSpamKey(key, isSpam):
    return key

# TODO: IMPLEMENT ME!!!!
# returns how spammy a word is from the database
def getSpaminess(key):
    return 0.4
