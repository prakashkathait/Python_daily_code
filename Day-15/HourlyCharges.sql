/* create table billings 
(
emp_name varchar(10),
bill_date date,
bill_rate int
);
delete from billings;
insert into billings values
('Sachin','1990-01-01',25)
,('Sehwag' ,'1989-01-01', 15)
,('Dhoni' ,'1989-01-01', 20)
,('Sachin' ,'1991-02-05', 30)
;

create table HoursWorked 
(
emp_name varchar(20),
work_date date,
bill_hrs int
);
insert into HoursWorked values
('Sachin', '1990-07-01' ,3)
,('Sachin', '1990-08-01', 5)
,('Sehwag','1990-07-01', 2)
,('Sachin','1991-07-01', 4);
*/
WITH date_range as (
SELECT *,
TIMESTAMPADD(DAY,-1,LEAD(bill_date,1,'9999-12-31') OVER(PARTITION BY emp_name ORDER BY bill_date ASC)) as bill_date_end  
FROM billings
)
SELECT hw.emp_name,sum(dr.bill_rate*hw.bill_hrs) as Charges
FROM date_range dr JOIN HoursWorked hw on dr.emp_name = hw.emp_name AND hw.work_date BETWEEN dr.bill_date AND dr.bill_date_end
GROUP BY hw.emp_name;
