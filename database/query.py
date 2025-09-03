from .connect import get_connect


def is_register(chat_id):
    with get_connect() as db:
        with db.cursor() as dbc:
            dbc.execute("select * from users where chat_id = %s",(chat_id,))

            return dbc.fetchone()

