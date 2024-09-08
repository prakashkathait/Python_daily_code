/* create table UserActivity
(
username      varchar(20) ,
activity      varchar(20),
startDate     Date   ,
endDate      Date
);

insert into UserActivity values 
('Alice','Travel','2020-02-12','2020-02-20')
,('Alice','Dancing','2020-02-21','2020-02-23')
,('Alice','Travel','2020-02-24','2020-02-28')
,('Bob','Travel','2020-02-11','2020-02-18');
*/
WITH cte as (
select *,
RANK() OVER(PARTITION BY username ORDER BY startDate DESC) AS rnk,
COUNT(1) OVER(PARTITION BY username) as Activity_count
from useractivity)
SELECT * 
FROM cte WHERE Activity_count = 1 or rnk =2;
