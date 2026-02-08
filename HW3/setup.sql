CREATE SCHEMA IF NOT EXISTS `taxi_dataset`
OPTIONS(location='US');

CREATE OR REPLACE EXTERNAL TABLE `taxi_dataset.yellow_taxi_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://dezoomcamp_hw3_hyw/yellow_tripdata_2024-*.parquet']
);

CREATE OR REPLACE TABLE taxi_dataset.yellow_taxi AS
SELECT * FROM taxi_dataset.yellow_taxi_external;

CREATE OR REPLACE TABLE taxi_dataset.yellow_taxi_partitioned
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM taxi_dataset.yellow_taxi;
