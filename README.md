# Secret Escape small ETL in Python and Postgres
This ETL extracts and loads data from two data sources(located in `input/`) into a Postgres database.
Once the data is loaded, it runs two queries and extracts two summary reports in `output/`.

The ETL was built in Python 3.6.

With more time I would have included some unit tests to make sure that the data is loaded and extracted correctly. Also, I
would have added some missing nodes that where in a deeper level in sales XML like images and categories.

## Installation requirements
1. Install Postgres on your local machine.
2. Install Python 3.6 on your local machine.
3. Install Python requirements using: `pip3 install -r requirements.txt`

## Steps to Run the ETL
1. Make sure that the postgres database is up and running in your local machine.
2. Run `bash build_database.sh` which creates the database, user and schemas.
3. Run `python3 etl.py` which executes the ETL job that loads the data from the booking and sales datasets.

## Comments about the outputs
This section shows my assumptions about each one of the SQL modelling tasks:

###### Data Task 1 output comments
- First of all, the marketing team can measure the overall performance of each sale based on the total bookings received, which could lead to ask more questions such as  why X sale was more successful than Y sale.

- The marketing team can get insights on which dates the sales got more bookings and focus their efforts to improve seasonal campaigns.

- The marketing team can get insights on which sales have had a good performance based on the length of time the sale has been published.

- The marketing team can measure the sales' performance based on the percentage of discount provided. For example, in some cases, giving high discounts do not always mean getting higher number of bookings.

- They also could know which rates the customer are more willing to pay and create campaigns to targeted groups based on income level.

- The locations of the sales are important for the marketing team, as they could target their campaigns based on location interests. For example, improving the marketing effort in countries where there are not so many bookings.

**NOTE:** As the current date was not given,  sales have been organized by start and end date. The marketing team would need to filter by end date to see only to check the current active sales.


###### Data Task 2 output comments

- The supply team could use the data to find out which check-in days are more attractive, and which seasons have more demand.

- Also the supply team could know the amount of time users prefer to book on each Hotel and Sale. This could help them look for more deals that include only X amount of days.

- The team could to check which day of the week has more check-ins and check-outs. There would be some cases in which weekend breaks have more bookings if they start on a Thursday rather than on a Friday, or maybe customers prefer to check out on Mondays rather than Sundays.

- It could also  be interesting  for the team to see the ratio of bookings against the rate and the discount on each season. This could give them an idea of how much the customers are willing to pay for each discount on each particular calendar dates.

**NOTE:** There are bookings that are not in the current sales dataset.
