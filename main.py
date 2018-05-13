from etl import load_sales
from etl import load_bookings

#Load the sales
load_sales("input/sales.xml")

#Load bookings
load_bookings("input/bookings.csv")
