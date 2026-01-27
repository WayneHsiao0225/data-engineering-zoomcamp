import pandas as pd
from pathlib import Path

file_path = Path("./data/green_tripdata_2025-11.parquet")
zone_file = Path("./data/taxi_zone_lookup.csv")

zone_df = pd.read_csv(zone_file)
zone_mapping = dict(zip(zone_df['LocationID'], zone_df['Zone']))

# Q3
df = pd.read_parquet(file_path, engine="pyarrow")

df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], errors='coerce')

df_nov = df[
    (df['lpep_pickup_datetime'] >= '2025-11-01') &
    (df['lpep_pickup_datetime'] < '2025-12-01')
]

short_trips = df_nov[df_nov['trip_distance'] <= 1]
print("Q3:", len(short_trips))

# Q4
df_nov_valid = df_nov[df_nov['trip_distance'] < 100]

daily_max = df_nov_valid.groupby(df_nov_valid['lpep_pickup_datetime'].dt.date)['trip_distance'].max()
longest_trip_day = daily_max.idxmax()
print("Q4:", longest_trip_day)

# Q5
nov_18 = df_nov[df_nov['lpep_pickup_datetime'].dt.date == pd.to_datetime('2025-11-18').date()]

pickup_zone_total = nov_18.groupby('PULocationID')['total_amount'].sum()
largest_total_zone_id = pickup_zone_total.idxmax()
largest_total_zone_name = zone_mapping.get(largest_total_zone_id, f"Unknown ID {largest_total_zone_id}")
print("Q5:", largest_total_zone_name)

# Q6
east_harlem_north_ids = zone_df[zone_df['Zone'] == "East Harlem North"]['LocationID'].tolist()

east_north_trips = df_nov[df_nov['PULocationID'].isin(east_harlem_north_ids)]

dropoff_tip = east_north_trips.groupby('DOLocationID')['tip_amount'].sum()

largest_tip_zone_id = dropoff_tip.idxmax()
largest_tip_zone_name = zone_mapping.get(largest_tip_zone_id, f"Unknown ID {largest_tip_zone_id}")
print("Q6: Dropoff zone with largest tip from East Harlem North:", largest_tip_zone_name)
