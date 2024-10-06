-- Given is user login table for , identify dates where a user has logged in for 5 or more consecutive days.
-- Return the user id, start date, end date and no of consecutive days, sorting based on user id.
-- If a user logged in consecutively 5 or more times but not spanning 5 days then they should be excluded.

/*
-- Output:
USER_ID		START_DATE		END_DATE		CONSECUTIVE_DAYS
1			10/03/2024		14/03/2024		5
1 			25/03/2024		30/03/2024		6
3 			01/03/2024		05/03/2024		5
*/
/*
drop table if exists user_login;
create table user_login
(
	user_id		int,
	login_date	date
);
insert into user_login values(1, '2024-03-01');
insert into user_login values(1, '2024-03-02');
insert into user_login values(1, '2024-03-03');
insert into user_login values(1, '2024-03-04');
insert into user_login values(1, '2024-03-06');
insert into user_login values(1, '2024-03-10');
insert into user_login values(1, '2024-03-11');
insert into user_login values(1, '2024-03-12');
insert into user_login values(1, '2024-03-12');
insert into user_login values(1, '2024-03-14');

insert into user_login values(1,'2024-03-20');
insert into user_login values(1, '2024-03-25');
insert into user_login values(1, '2024-03-26');
insert into user_login values(1, '2024-03-27');
insert into user_login values(1, '2024-03-28');
insert into user_login values(1, '2024-03-29');
insert into user_login values(1, '2024-03-30');

insert into user_login values(2, '2024-03-01');
insert into user_login values(2, '2024-03-02');
insert into user_login values(2, '2024-03-03');
insert into user_login values(2, '2024-03-04');

insert into user_login values(3, '2024-03-01');
insert into user_login values(3, '2024-03-02');
insert into user_login values(3, '2024-03-03');
insert into user_login values(3, '2024-03-04');
insert into user_login values(3, '2024-03-04');
insert into user_login values(3, '2024-03-04');
insert into user_login values(3, '2024-03-05');

insert into user_login values(4, '2024-03-01');
insert into user_login values(4, '2024-03-02');
insert into user_login values(4, '2024-03-03');
insert into user_login values(4, '2024-03-04');
insert into user_login values(4, '2024-03-04');
*/

WITH cte as(
select *,login_date - INTERVAL(row_number() over(partition by user_id 
                           order by login_date)) DAY as date_group
 from user_login)
 select user_id, date_group,
 min(login_date) as start_date, max(login_date) as end_date,
 (max(login_date)-min(login_date)) +1 as consequtive_days
 from cte 
 group by user_id,date_group
 having (max(login_date)-min(login_date)) >=4;