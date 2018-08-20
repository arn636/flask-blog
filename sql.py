import sqlite3

with sqlite3.connect("blog.db") as connection:

    c = connection.cursor()

    c.execute("""Create Table posts
            (title TEXT, post TEXT)
                """)

    c.execute('Insert into posts values("Good", "I\'m good.")')
    c.execute('Insert into posts values("Well", "I\'m well.")')
    c.execute('Insert into posts values("Excellent", "I\'m excellent.")')
    c.execute('Insert into posts values("Okay", "I\'m okay.")')
