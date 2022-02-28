import os
import pandas as pd
import transform_functions as tf 

import warnings
warnings.filterwarnings('ignore')

def lambda_function(request, context):
    CSV_ENDPOINT_BTC = os.environ.get("CSV_ENDPOINT_BTC")
    BTC_df = pd.read_csv(CSV_ENDPOINT_BTC)

    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.dialects import postgresql
    from sqlalchemy.dialects.postgresql import insert
    #print(insert_stmt.compile(dialect=postgresql.dialect()))

    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_SERVER_NAME = os.environ.get("DB_SERVER_NAME")
    DB_DATABASE_NAME = os.environ.get("DB_DATABASE_NAME")
    connection_url = URL.create(
        drivername = "postgresql+pg8000", 
        username = DB_USER,
        password = DB_PASSWORD,
        host = DB_SERVER_NAME, 
        port = 5432,
        database = DB_DATABASE_NAME, 
        )

    engine = create_engine(connection_url) 

    from sqlalchemy import MetaData
    from sqlalchemy import Table
    metadata_obj = MetaData()
    metadata_obj.reflect(bind=engine)
    btc = metadata_obj.tables["btc"]
   # btc=Table("btc",metadata_obj)
        
    # ## Upsert: 
    insert_statement = postgresql.insert(btc).values(BTC_df.to_dict(orient='records'))
    upsert_statement = insert_statement.on_conflict_do_update(
        index_elements=['date'],
        set_={c.key: c for c in insert_statement.excluded if c.key not in ['date']})
    engine.execute(upsert_statement)