

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