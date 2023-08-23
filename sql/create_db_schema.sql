DROP DATABASE IF EXISTS readflow;
CREATE DATABASE readflow;
\c readflow

DROP SCHEMA IF EXISTS rfmain_test;
CREATE SCHEMA rfmain_test;
SET SEARCH_PATH TO rfmain_test; 