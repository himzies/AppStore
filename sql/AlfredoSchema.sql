/*******************

  Create the schema

********************/

CREATE TABLE IF NOT EXISTS customer (
 id VARCHAR(16) PRIMARY KEY,
 password VARCHAR(64) NOT NULL,
 first_name VARCHAR(64) NOT NULL,
 last_name VARCHAR(64) NOT NULL,
 gender VARCHAR(6) NOT NULL CHECK (gender IN ('Male', 'Female')),
 email VARCHAR(64) UNIQUE NOT NULL,
 address VARCHAR(255) UNIQUE NOT NULL);
 
CREATE TABLE IF NOT EXISTS provider (
 id VARCHAR(16) PRIMARY KEY,
 password VARCHAR(64) NOT NULL,
 first_name VARCHAR(64) NOT NULL,
 last_name VARCHAR(64) NOT NULL,
 gender VARCHAR(6) NOT NULL CHECK (gender IN ('Male', 'Female')),
 email VARCHAR(64) UNIQUE NOT NULL,
 expertise VARCHAR(64) NOT NULL,
 address VARCHAR(255) UNIQUE NOT NULL);
 
 CREATE TABLE IF NOT EXISTS job_category(
  name VARCHAR(64) PRIMARY KEY);
 
 CREATE TABLE IF NOT EXISTS cleaning(
  name VARCHAR(64) PRIMARY KEY,
  descrip VARCHAR(255));
 
 CREATE TABLE IF NOT EXISTS pet_care(
  name VARCHAR(64) PRIMARY KEY,
  descrip VARCHAR(255));
 
 CREATE TABLE IF NOT EXISTS tuition(
  name VARCHAR(64) PRIMARY KEY,
  descrip VARCHAR(255));
 
CREATE TABLE IF NOT EXISTS transaction (
 customer_id VARCHAR(16) NOT NULL,
 provider_id VARCHAR(16) NOT NULL,
 customer_name VARCHAR(128) NOT NULL,
 provider_name VARCHAR(128) NOT NULL,
 address VARCHAR(255) UNIQUE NOT NULL);
 job VARCHAR(64) NOT NULL, 
 price DEC(16, 2) NOT NULL); 
