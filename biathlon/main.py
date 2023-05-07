

import os

from sqlalchemy import and_, or_, not_, desc, func, distinct, text
from biathlon.database import DATABASE_NAME, Session
import create_database_bia as db_creator
from biathlon.result_table import ResultTable
from biathlon.biathlete import Athlete


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()


for it in session.query(Athlete):
    print(it.last_name)
print("*" * 50)

print(session.query(Athlete).count())
print("*" * 50)

for it in session.query(Athlete).filter(Athlete.points > 400):
    print(it)
print("*" * 50)

for it in session.query(ResultTable).filter(ResultTable.lag > 30):
    print(it)
print("*" * 50)

for it in session.query(Athlete).filter((Athlete.last_name.like('Л%'))):
    print(it)
print("*" * 50)

for it in session.query(Athlete).filter((Athlete.region.like('Башкортостан'))):
    print(it)
print("*" * 50)

for it in session.query(ResultTable).filter((ResultTable.place.like('1'))):
    print(it)
print("*" * 50)

for it in session.query(Athlete.region).distinct():
    print(it)
print("*" * 50)

for it in session.query(ResultTable).filter((ResultTable.place < 4)):
    print(it)
print("*" * 50)

for it in session.query(Athlete.first_name).filter((Athlete.last_name.like('Халили '))):
    print(it)
print("*" * 50)