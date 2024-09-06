select * from products;
select concat(pr2.name,' ',pr1.name) as Pairs, count(1) as pair 
from orders o1 JOIN orders o2 ON o1.order_id = o2.order_id
INNER JOIN products pr1 ON pr1.id = o1.product_id
INNER JOIN products pr2 ON pr2.id = o2.product_id
where o1.product_id > o2.product_id
GROUP BY pr1.name, pr2.name