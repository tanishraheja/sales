use mydb;
select * from sales
-- how many category are sold and whats the total sales

select sub_category ,count(category) as total,round(sum(profit)) as sum from sales
group by sub_category 
order by sum desc

-- whats the fequency od discount applied
select count(discount) as discount_use ,round( (select sum(discount) from sales where discount_applied = 'yes')) as total_discount
from sales
where discount = 0

-- total quantity sold by category and how much profit genreate

select sub_category , count(quantity) , sum(profit) as sum
from sales
group by sub_category
order by sum desc;

select date_format(order_date,"%m") as years , sum(profit) as sum from sales
group by years;



