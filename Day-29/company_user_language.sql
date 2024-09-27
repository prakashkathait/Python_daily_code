/* create table company_users 
(
company_id int,
user_id int,
language varchar(20)
);

insert into company_users values (1,1,'English')
,(1,1,'German')
,(1,2,'English')
,(1,3,'German')
,(1,3,'English')
,(1,4,'English')
,(2,5,'English')
,(2,5,'German')
,(2,5,'Spanish')
,(2,6,'German')
,(2,6,'Spanish')
,(2,7,'English');
*/
-- find the company who have atleast 2 users who speaks English and german both languages

select company_id, count(1) from (
select company_id, user_id from company_users
where language in ('English','German')
group by company_id,user_id
having count(1) =2)a 
group by company_id 
having count(1) >=2;

