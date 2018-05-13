import xml.etree.ElementTree
import pandas as pd
from functions import load_to_postgres
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