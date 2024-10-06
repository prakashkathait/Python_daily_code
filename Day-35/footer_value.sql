/* DROP TABLE IF EXISTS FOOTER;
CREATE TABLE FOOTER 
(
	id 			INT PRIMARY KEY,
	car 		VARCHAR(20), 
	length 		INT, 
	width 		INT, 
	height 		INT
);

INSERT INTO FOOTER VALUES (1, 'Hyundai Tucson', 15, 6, NULL);
INSERT INTO FOOTER VALUES (2, NULL, NULL, NULL, 20);
INSERT INTO FOOTER VALUES (3, NULL, 12, 8, 15);
INSERT INTO FOOTER VALUES (4, 'Toyota Rav4', NULL, 15, NULL);
INSERT INTO FOOTER VALUES (5, 'Kia Sportage', NULL, NULL, 18); 
*/
-- Solution 1 :

select * from 
(SELECT car from FOOTER where car is not null order by id desc limit 1) a
CROSS JOIN (SELECT length from FOOTER where length is not null order by id desc limit 1) length
CROSS JOIN (SELECT width from FOOTER where width is not null order by id desc limit 1) width
CROSS JOIN (SELECT height from FOOTER where height is not null order by id desc limit 1) height;

-- solution 2

with cte as (
select *,
sum(case when car is not null then 1 else 0 end) over(order by id) as car_segment,
sum(case when length is not null then 1 else 0 end) over(order by id) as length_segment,
sum(case when width is not null then 1 else 0 end) over(order by id) as width_segment,
sum(case when height is not null then 1 else 0 end) over(order by id) as height_segment
from footer)
select 
first_value(car) over(partition by car_segment) as new_car,
first_value(length) over(partition by length_segment) as new_length,
first_value(width) over(partition by width_segment) as new_width,
first_value(height) over(partition by height_segment) as new_height
from cte 
order by id desc
limit 1 ;




