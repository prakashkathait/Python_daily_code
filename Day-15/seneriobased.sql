/* CREATE table activity
(
user_id varchar(20),
event_name varchar(20),
event_date date,
country varchar(20)
);
delete from activity;
insert into activity values (1,'app-installed','2022-01-01','India')
,(1,'app-purchase','2022-01-02','India')
,(2,'app-installed','2022-01-01','USA')
,(3,'app-installed','2022-01-01','USA')
,(3,'app-purchase','2022-01-03','USA')
,(4,'app-installed','2022-01-03','India')
,(4,'app-purchase','2022-01-03','India')
,(5,'app-installed','2022-01-03','SL')
,(5,'app-purchase','2022-01-03','SL')
,(6,'app-installed','2022-01-04','Pakistan')
,(6,'app-purchase','2022-01-04','Pakistan');
*/

SELECT * FROM activity;
-- CASE1 : Find the active users on each day 

select event_date, count(DISTINCT user_id) as active_count 
FROM activity
GROUP BY event_date;

-- Total users on each week 
select EXTRACT(WEEK FROM event_date) as week_num, COUNT(DISTINCT user_id) as users
FROM activity
GROUP BY EXTRACT(WEEK FROM event_date);

-- CASE3: Users who have purchase the app on the same day 

SELECT event_date,count(new_users) FROM (
SELECT
user_id,event_date, CASE WHEN COUNT(DISTINCT event_name)=2 THEN user_id ELSE NULL END as new_users
FROM activity
GROUP BY user_id,event_date
) a
GROUP BY event_date;

-- CASE % Paid users 

with country_count as (
SELECT CASE WHEN country in ('USA','India') THEN country ELSE 'others' END as new_country
,count(1) as total_count FROM activity
WHERE event_name = 'app-purchase'
group by CASE WHEN country in ('USA','India') THEN country ELSE 'others' END),
total as (SELECT SUM(total_count) as total_countries FROM country_count) 
SELECT new_country, ROUND(total_count/total_countries*100,2) as Percen
FROM country_count,total;

-- CASE5 : Among all users who have purchase on the very next day , return the records date-wise 

with prev_data as(
SELECT *,
LAG(event_name,1) OVER(PARTITION BY user_id ORDER BY event_date) as prev_event_name,
LAG(event_date,1) OVER(PARTITION BY user_id ORDER BY event_date) as prev_event_date
FROM activity)
SELECT event_date, 
count(CASE WHEN event_name ='app-purchase' AND prev_event_name ='app-installed' AND TIMESTAMPDIFF(day,prev_event_date,event_date)=1
 THEN user_id ELSE NULL END) as cnt_users  FROM prev_data
GROUP BY event_date;