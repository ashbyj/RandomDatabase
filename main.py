import sqlalchemy

def db_connection():
    engine = sqlalchemy.create_engine('postgresql://jesse@localhost/playground')
    return engine

if __name__ == "__main__":
    conn = db_connection()