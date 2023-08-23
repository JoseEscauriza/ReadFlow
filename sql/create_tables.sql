-- Drop tables
DROP TABLE IF EXISTS logs CASCADE;
DROP TABLE IF EXISTS permission CASCADE;
DROP TABLE IF EXISTS book_status CASCADE;
DROP TABLE IF EXISTS book_copy CASCADE;
DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS author CASCADE;
DROP TABLE IF EXISTS book_user CASCADE;
DROP TABLE IF EXISTS book_user_role CASCADE;

-- Create types
DROP TYPE IF EXISTS urole CASCADE;
CREATE TYPE urole AS ENUM ('Admin', 'book_user');

DROP TYPE IF EXISTS perm CASCADE;
CREATE TYPE perm AS ENUM ('Create', 'Edit', 'Read', 'Delete');

-- Create tables
CREATE TABLE book_user_role (
  id CHAR(1) PRIMARY KEY,
  role urole NOT NULL
);

CREATE TABLE author (
  id serial PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255) NOT NULL
);

CREATE TABLE book (
  id serial PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author_id serial NOT NULL,
  book_desc TEXT,
  genre VARCHAR(100) NOT NULL,
  ISBN CHAR(17),
  CONSTRAINT fk_author_id FOREIGN KEY (author_id) REFERENCES author(id)
);

CREATE TABLE book_copy (
  id serial PRIMARY KEY,
  book_id serial NOT NULL,
  book_available BOOLEAN NOT NULL,
  book_location CHAR(2) NOT NULL,
  creation_time TIMESTAMP,
  modification_time TIMESTAMP,
  CONSTRAINT fk_book_id FOREIGN KEY (book_id) REFERENCES book(id)
);

CREATE TABLE book_user (
  id serial PRIMARY KEY,
  book_username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(15),
  role_id CHAR(1) NOT NULL DEFAULT '2',
  creation_time TIMESTAMP,
  modification_time TIMESTAMP,
  CONSTRAINT fk_role_id FOREIGN KEY (role_id) REFERENCES book_user_role(id) ON DELETE CASCADE
);

CREATE TABLE book_status (
  id serial PRIMARY KEY,
  book_user_id serial,
  available BOOLEAN NOT NULL DEFAULT FALSE
  -- DATES??
);

CREATE TABLE borrowed_book (
  id serial PRIMARY KEY,
  book_user_id serial NOT NULL,
  copy_id serial NOT NULL,
  borrow_date TIMESTAMP,
  return_date TIMESTAMP,
  due_date DATE,
  CONSTRAINT fk_book_user_id FOREIGN KEY (book_user_id) REFERENCES book_user(id),
  CONSTRAINT fk_copy_id FOREIGN KEY (copy_id) REFERENCES book_copy(id)
);

CREATE TABLE permission (
  id serial PRIMARY KEY,
  permission_type perm NOT NULL DEFAULT 'Read'
);

CREATE TABLE role_permission (
  id serial PRIMARY KEY,
  role_id CHAR(1),
  permission_id serial,
  CONSTRAINT fk_role_id FOREIGN KEY (role_id) REFERENCES book_user_role(id),
  CONSTRAINT fk_permission_id FOREIGN KEY (permission_id) REFERENCES permission(id)
);

CREATE TABLE logs (
  id serial PRIMARY KEY,
  logs_event TEXT,
  error VARCHAR(50) NOT NULL,
  book_user_activity TEXT
);
