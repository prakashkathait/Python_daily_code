/* DROP TABLE IF EXISTS Friends;

CREATE TABLE Friends
(
	Friend1 	VARCHAR(10),
	Friend2 	VARCHAR(10)
);
INSERT INTO Friends VALUES ('Jason','Mary');
INSERT INTO Friends VALUES ('Mike','Mary');
INSERT INTO Friends VALUES ('Mike','Jason');
INSERT INTO Friends VALUES ('Susan','Jason');
INSERT INTO Friends VALUES ('John','Mary');
INSERT INTO Friends VALUES ('Susan','Mary');
*/
-- Finding the mutual friends 
with all_friends as (
select friend1,friend2 from friends
UNION ALL 
select friend2,friend1 from friends)
select distinct f.*,
count(af.friend2) OVER(partition by f.friend1,f.friend2 order by f.friend1,f.friend2
                       range between unbounded preceding and unbounded following) as mutual_friends_count 
from friends f LEFT JOIN all_friends af ON f.friend1 = af.friend1
and af.friend2 in (select af2.friend2
                   from all_friends af2 
                   where af2.friend1 = f.friend2) 
-- where f.friend1 = 'Jason';