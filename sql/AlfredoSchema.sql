/*******************

  Create the schema

********************/

CREATE TABLE IF NOT EXISTS customer (
	id VARCHAR(16),
	password VARCHAR(64) NOT NULL,
	first_name VARCHAR(64) NOT NULL,
	last_name VARCHAR(64) NOT NULL,
	gender VARCHAR(6) NOT NULL CHECK (gender IN ('Male', 'Female')),
	email VARCHAR(64) UNIQUE NOT NULL,
	address VARCHAR(255) UNIQUE NOT NULL,
	PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS provider (
	id VARCHAR(16),
	password VARCHAR(64) NOT NULL,
	first_name VARCHAR(64) NOT NULL,
	last_name VARCHAR(64) NOT NULL,
	gender VARCHAR(6) NOT NULL CHECK (gender IN ('Male', 'Female')),
	email VARCHAR(64) UNIQUE NOT NULL,
	expertise VARCHAR(64) NOT NULL,
	address VARCHAR(255) UNIQUE NOT NULL,
	PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS jobs (
	name VARCHAR(64) PRIMARY KEY,
	descrip VARCHAR(255) NOT NULL,
	price DEC(16, 2) NOT NULL,
	category VARCHAR(64) NOT NULL);

CREATE TABLE IF NOT EXISTS transaction (
	customer_id VARCHAR(16) REFERENCES customer(id),
	provider_id VARCHAR(16) REFERENCES provider(id),
	cust_address VARCHAR(255) NOT NULL,
	expertise VARCHAR(64) NOT NULL, 
	price DEC(16, 2) NOT NULL);
