create database testdb;

use testdb;

create table users (
    id int primary key auto_increment,
    name varchar(50) not null,
    age int not null
);