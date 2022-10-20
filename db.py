import sqlalchemy
import pg8000

engine = sqlalchemy.create_engine("postgresql+pg8000://postgres:postgres@34.78.165.179/eep-p33-hack1-db")
result = engine.execute("SELECT * FROM greetings").fetchall()
for row in result:
    print (row[2])


signiture = input('What\'s your name?')
greeting = input ('what do you want to say to your colleague?')



def save_down_db (table, recipients, title, signiture,greeting):
    if table == 'greetings':
        greeting_sql = ("INSERT INTO greetings (virtual_card_id, signature, greeting) "\
                      f"SELECT virtual_card.id, '{signiture}', '{greeting}'"\
                      f"FROM virtual_card where recipients in ('{recipients}') and title in ('{title}');")
        engine.execute(greeting_sql)

save_down_db ("greetings","Vivian", "Happy Birthday!",signiture,greeting)
