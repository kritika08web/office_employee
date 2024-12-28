create database office;
use office;
truncate table employee ;
drop table employee;
show tables;
create table employee (__emp_id int primary key,emp_name varchar(50),__password varchar(12));
create table salary ( __account_no int primary key, __emp_id int,credit_ammount float, bonus float, balance_salary float , 
                       Foreign key (__emp_id) REFERENCES employee(__emp_id)  );
select * from employee;
select* from salary;accounts