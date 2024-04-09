import sqlalchemy
from faker import Faker 
from math import ceil, floor
from random import randint

fake = Faker()

def db_connection():
# take creds from encrypted file?
# take creds from command line?
# use ldap or equivalent?
    engine = sqlalchemy.create_engine('postgresql://jesse@localhost/playground')
    return engine

def populate_contest(db_conn, num_contests, hackers_per_contest, variation):
    contest_data = []
    
    for contest in range(1, num_contests + 1):
        contest_id = fake.uuid4()
        hacker_count = randint(ceil(hackers_per_contest * (1 - variation)),
                               floor(hackers_per_contest * (1 + variation))
                              )
    
        for _ in range(hacker_count):
            hacker_id = fake.uuid4()
            hacker_name = fake.name()
            contest_data.append((contest_id, hacker_id, hacker_name))
    
    metadata = sqlalchemy.MetaData(bind=db_conn)
    table = sqlalchemy.Table('contest', metadata, autoload=True)
    
    with db_conn.begin() as conn:
        conn.execute(table.insert(), contest_data) 

if __name__ == "__main__":
    conn = db_connection()
    populate_contest(conn, 2, 5, 0.8)


