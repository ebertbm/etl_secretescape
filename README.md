# Installation Guide

## Requirements
Install postgres
Install all the python requirements `pip install -r requirements.txt`

## Steps to Run the ETL
Run `bash build_database.sh` which creates the database, user and schemas.
Run `python3 main.py` which executes the ETL job that load the data from the booking and sales datasets.


###### Data Task 1 output comments
-- First of all, the marketing team can measure the overall performance of each sale based on the total bookings received, where it can lead to ask more questions like why X sale was more successful than Y sale.
-- The marketing team can get insights on which dates the sales have more bookings and focus their effort to improve seasonal campaigns.
-- The marketing team can get insights on which sales have a good performance based on the amount of time the sale has been published.
-- The marketing team can measure the sales' performance based on the percentage of discount provided. For example, in some cases, giving high discounts do not neccesarly mean getting higher number of bookings.
-- They also could know which rates the customer are more willing to pay and create target campaign groups based on the income level
-- The locations of the sales are important for the marketing team, as they can target their campaigns based on location interests. For example, improve the marketing effort in countries where there are not so many bookings.
-- NOTE: As the current date was not given the sales have been organized by start and end date, the marketing team would need to filter by end date to see only the current active sales.


###### Data Task 2 output comments
-- They might use the data to find out which check-in days are more attractive, and which seasons have more demand.
-- Also they would like to know the amount of time the users prefer to book on each Hotel and Sale. This could help the supply team in looking more deals that include only X amount of days.
-- They would like to check which day of the week has more check-ins and check-outs. There would be some cases where weekends breaks have more bookings if they start on Thursday rather on Friday, or maybe they customers prefere to return back on Monday rather than Sunday.
-- It would be interesting to see the ratio of bookings against the rate and the discount on each season. This could give an idea of how much the customers are willing to pay for each discount on each particular calendar dates.
-- **NOTE:** There are bookings that are not in the current sales.
