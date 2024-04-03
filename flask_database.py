from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Set up SQLite database
conn = sqlite3.connect('poems.db')
c = conn.cursor()

# Create poems table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS poems (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                text TEXT
            )''')

# Insert provided list of poems into the database
poems = [
    ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
    ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
    ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
    ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
    ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
]

c.executemany('INSERT INTO poems (title, author, text) VALUES (?, ?, ?)', poems)
conn.commit()

@app.route('/')
def index():
    # Retrieve poems from the database
    c.execute('SELECT * FROM poems')
    poems = c.fetchall()
    return render_template('index.html', poems=poems)

if __name__ == '__main__':
    app.run(debug=True)
