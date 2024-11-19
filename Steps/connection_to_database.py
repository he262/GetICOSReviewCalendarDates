import pandas as pd
from sqlalchemy import create_engine
from logging import basicConfig,DEBUG,debug

basicConfig(level=DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')


def execute_sql_query(server_name, database_name, query):
    debug(f"connecting to server : {server_name}, database:{database_name}")
    connection_string = f"mssql+pyodbc://{server_name}/{database_name}?trusted_connection=yes&driver=SQL+Server"
    engine = create_engine(connection_string)
    result_df = pd.read_sql(query, engine)
    return result_df