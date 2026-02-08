-- Q1
SELECT COUNT(*) FROM taxi_dataset.yellow_taxi;

-- Q2
SELECT COUNT(DISTINCT PULocationID)
FROM taxi_dataset.yellow_taxi_external;

SELECT COUNT(DISTINCT PULocationID)
FROM taxi_dataset.yellow_taxi;

-- Q3
SELECT PULocationID FROM taxi_dataset.yellow_taxi;
SELECT PULocationID, DOLocationID FROM taxi_dataset.yellow_taxi;

-- Q4
SELECT COUNT(*) FROM taxi_dataset.yellow_taxi
WHERE fare_amount = 0;

-- Q6
SELECT COUNT(DISTINCT VendorID)
FROM taxi_dataset.yellow_taxi
WHERE DATE(tpep_dropoff_datetime)
BETWEEN '2024-03-01' AND '2024-03-15';

SELECT COUNT(DISTINCT VendorID)
FROM taxi_dataset.yellow_taxi_partitioned
WHERE DATE(tpep_dropoff_datetime)
BETWEEN '2024-03-01' AND '2024-03-15';

--Q7 GCP Bucket

--Q8 False 

--Q9 
SELECT COUNT(*) FROM taxi_dataset.yellow_taxi; 
--0mb, because it gets the row count from the table metadata without scanning the data.