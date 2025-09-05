from .connect import get_connect

conn = get_connect()
conn.autocommit = True

def is_register(chat_id):
    with  conn as db:
        with db.cursor() as dbc:
            try:
                dbc.execute("select * from users where chat_id = %s",(chat_id,))

                return dbc.fetchone()
            except:
                return None
        

def save_user(chat_id,fullname,phone,lat,long,username=None):
    with  conn as db:
        with db.cursor() as dbc:
            try:
                dbc.execute("""
                    Insert into users (chat_id,fullname,username, phone,lat,long) values(%s,%s,%s,%s,%s,%s);
                    """,(chat_id,fullname,username,phone,lat,long))
                return "Success"
            except:

                return None
            
        

def get_foods():
    with conn as db:
        with db.cursor() as dbc:

            dbc.execute("select * from food")
            foods = dbc.fetchall()

    return foods


def get_food(id):
    with conn as db:
        with db.cursor() as dbc:
            dbc.execute("select * from food where id =%s",(id,))
            foods = dbc.fetchone()
    print(foods)
    print("+++++++++++++++++++++++")
    return foods

    


