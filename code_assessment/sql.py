-- Step 1: Choose the database folder (please select line 2 then run), optional!
use intra2

-- Step 2: Create Tables and insert data (please select line 5 to line 37 then run)
create table product
(
product_id int primary key,
name varchar(128) not null,
rrp decimal(20,2) not null,
available_from date not null
);

create table orders
(
order_id int primary key,
product_id int not null,
quantity int not null,
order_price decimal(20,2) not null,
dispatch_date date not null,
foreign key (product_id) references product(product_id)
);

INSERT INTO product (product_id, name, rrp, available_from) VALUES (101, 'Bayesian Methods for Nonlinear Classification and Regression', 94.95, '2019-02-21 00:00:00.000')
INSERT INTO product (product_id, name, rrp, available_from) VALUES (102, '(next year) in Review (preorder)', 21.95, '2020-02-25')
INSERT INTO product (product_id, name, rrp, available_from) VALUES (103, 'Learn Python in Ten Minutes', 2.15, '2018-11-25')
INSERT INTO product (product_id, name, rrp, available_from) VALUES (104, 'sports almanac (1999-2049)', 3.38, '2017-02-25')
INSERT INTO product (product_id, name, rrp, available_from) VALUES (105, 'finance for dummies', 84.99, '2018-02-25')
INSERT INTO product (product_id, name, rrp, available_from) VALUES (106, 'Python CF', 20.00, '2018-02-25')
INSERT INTO product (product_id, name, rrp, available_from) VALUES (107, 'SQL CF', 18.00, '2018-01-25')

INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1000, 101, 1, 90.00, '2018-12-25')
INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1001, 103, 1, 1.15, '2019-01-15')
INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1002, 101, 10, 90.00, '2018-03-25')
INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1003, 104, 11, 3.38, '2018-08-25')
INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1004, 105, 11, 501.33, '2017-02-25')
INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1005, 106, 5, 25.00, '2018-10-25')
INSERT INTO orders (order_id, product_id, quantity, order_price, dispatch_date) VALUES (1006, 106, 4, 25.00, '2018-03-25')


-- Step 3: Make sure data satisfied requiried criteria(please select line 41 to line 62 then run)
create table #table1
(
product_id int not null
)

insert into #table1
select distinct o.product_id
from orders as o
join (select product_id, sum(quantity) as total_quantity
      from orders
      group by product_id)
      as s on o.product_id = s.product_id
where s.total_quantity < 10
union
select distinct o.product_id
from orders as o
join (select product_id, sum(quantity) as total_quantity
      from orders
      group by product_id)
      as s on o.product_id = s.product_id
where o.dispatch_date < DATEADD(Year,-1,GETDATE())
order by product_id

-- Step 4: Generate Final Result (please select line 65 to line 70 then run)
select o.order_id, p.*, o.quantity, o.order_price, o.dispatch_date
from product p, orders o, #table1 t
where p.product_id = o.product_id
and p.available_from !> DATEADD(Month,-1,GETDATE())
and p.product_id = t.product_id
order by order_id