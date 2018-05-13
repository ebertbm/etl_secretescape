import xml.etree.ElementTree
import pandas as pd
from functions import load_to_postgres, extract_data
import logging

# set logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_bookings(input):
    """
    Read Bookings from csv and load data to Postgres.

    :param input: bookings csv input location
    :type df: string
    """
    # Read the csv file in pandas as it has a cleaner way to cast
    # strings to date types
    logger.info('Reading {}...'.format(input))
    df = pd.read_csv(input)

    # format the dates
    df['checkIn'] = pd.to_datetime(df['checkIn'], format='%d/%m/%Y').dt.strftime('%m/%d/%Y')
    df['checkOut'] = pd.to_datetime(df['checkOut'], format='%d/%m/%Y').dt.strftime('%m/%d/%Y')

    # load the dataframe to postgres
    logger.info('Loading into Postgres...')
    load_to_postgres(df, 'bookings')


def load_sales(input):
    """
    Read Sales from xml and load data into Postgres.

    :param input: sales xml input location
    :type df: string
    """

    logger.info('Reading {}...'.format(input))
    xmldata = xml.etree.ElementTree.parse(input).getroot()
    list_nodes = []

    colnodes = ['id', 'title', 'sale_title', 'start', 'end', 'url',
                'destination_type', 'destination_name', 'rate', 'defaultCurrencyRate',
                'discount', 'discount_value', 'description', 'image',
                'image_thumb', 'image_medium', 'county', 'country',
                'division', 'city', 'city_district', 'product_type',
                'travel', 'highlights'
                ]

    dfcols = colnodes
    df_xml = pd.DataFrame(columns=dfcols)

    # get value of one node within the xml
    def getvalueofnode(node):
        """ return node text or None """
        return node.text if node is not None else None

    # Go through all the nodes in the xml and append them
    # into a list that is added to a dataframe
    for node in xmldata:
        for col in colnodes:
            list_nodes.append(getvalueofnode(node.find(col)))

        df_xml = df_xml.append(
            pd.Series(list_nodes, index=dfcols),
            ignore_index=True)
        list_nodes = []

    # cast to datetime format
    df_xml['start'] = pd.to_datetime(df_xml['start'])
    df_xml['end'] = pd.to_datetime(df_xml['end'])

    # load the dataframe to postgres
    logger.info('Loading into Postgres...')
    load_to_postgres(df_xml, 'sales')


def extract_task1(output):
    """
    Extract the data from Postgres passing a SQL query

    :param output: output location
    :type output: string
    """

    logger.info('Extracting data to {}...'.format(output))
    sql_task = """
                COPY(
                    SELECT title, sales.country, sales.product_type, rate, discount,
                    start_date, end_date, EXTRACT(DAY FROM end_date-start_date) AS sale_lenght, count(*)
                    FROM sales
                    left join bookings on bookings.id = sales.id
                    group by title , sales.country, sales.product_type, rate, discount,
                    start_date , end_date, sale_lenght
                    order by count(*) desc
                ) TO
                STDOUT
                WITH
                CSV
                HEADER
                DELIMITER
                ','
                """
    extract_data(output, sql_task)


def extract_task2(output):
    """
    Extract the data from Postgres passing a SQL query

    :param output: output location
    :type output: string
    """

    logger.info('Extracting data to {}...'.format(output))
    sql_task = """
                COPY(
                    SELECT salename as booking_name, title, rate, discount, checkin, checkout,
                      to_char(checkin, 'Month') as month_checkin,
                      to_char(checkout, 'Month') as month_checkout,
                      to_char(checkin, 'Day') as day_checkin,
                      to_char(checkout, 'Day') as day_checkout,
                      (checkout-checkin) AS booking_length,
                      CASE
                        WHEN to_char(checkin, 'MM-DD') between '01-01' and '03-19' THEN 'Winter'
                        WHEN to_char(checkin, 'MM-DD') between '12-21' and '12-31' THEN 'Winter'
                        WHEN to_char(checkin, 'MM-DD') between '03-20' and '06-20' THEN 'Spring'
                        WHEN to_char(checkin, 'MM-DD') between '06-21' and '09-21' THEN 'Summer'
                        WHEN to_char(checkin, 'MM-DD') between '09-22' and '12-20' THEN 'Autumn'
                        ELSE 'UNKNOWN'
                      END AS season,
                      count(*) as bookings
                    FROM bookings
                    LEFT JOIN sales on bookings.id = sales.id
                    group by booking_name, title, rate, discount, checkin , checkout, month_checkin, month_checkout,
                      day_checkin, day_checkout, booking_length, season
                    order by count(*) desc
                ) TO
                STDOUT
                WITH
                CSV
                HEADER
                DELIMITER
                ','
                """
    extract_data(output, sql_task)


if __name__ == '__main__':
    # Load the sales
    load_sales("input/sales.xml")

    # Load bookings
    load_bookings("input/bookings.csv")

    # Extract the output of both tasks
    extract_task1("output/data-task1-output.csv")
    extract_task2("output/data-task2-output.csv")

