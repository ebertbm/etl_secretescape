import psycopg2
from io import StringIO


def load_to_postgres(df, table):
    """
    This function loads a dataframe into a Postgres table.

    :param df: Dataframe in pandas that contains the data to load
    :type df: dataframe
    :param table: Table where the dataframe will be loaded
    :type table: string
    """
    # Get the connection to the postgres database
    conn = psycopg2.connect("host=localhost dbname=secretescapes user=eberto")
    cur = conn.cursor()

    # sql script to copy data to the table
    copy_sql = """
               COPY {} FROM stdin WITH CSV
               DELIMITER as ','
               """.format(table)

    # Using a string buffer which makes the write process much quicker
    # Initialize a string buffer
    sio = StringIO()
    sio.write(df.to_csv(index=None, header=None))  # Write the Pandas DataFrame as a csv to the buffer
    sio.seek(0)  # Be sure to reset the position to the start of the stream

    # Copy the string buffer to the database, as if it were an actual file
    with conn.cursor() as c:
        c.copy_expert(sql=copy_sql, file=sio)
        conn.commit()

    conn.commit()
    cur.close()