-- Data Task 1 query
SELECT title, sales.country, sales.product_type, rate, discount,
  start_date, end_date, EXTRACT(DAY FROM end_date-start_date) AS sale_lenght, count(*)
FROM sales
left join bookings on bookings.id = sales.id
group by title , sales.country, sales.product_type, rate, discount,
  start_date , end_date, sale_lenght
order by count(*) desc ;

-- Data Task 2 query
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
order by count(*) desc;
