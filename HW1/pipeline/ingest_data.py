{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c49bbc1a-e974-4710-a96b-6a5519b7d54b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100, 18)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Read a sample of the data\n",
    "prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'\n",
    "df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)\n",
    "\n",
    "url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'\n",
    "\n",
    "# Display first rows\n",
    "df.head()\n",
    "\n",
    "# Check data types\n",
    "df.dtypes\n",
    "\n",
    "# Check data shape\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6d0bf314-b518-4cb6-ba07-d2623f394dd8",
   "metadata": {},
   "outputs": [],
   "source": [
    "dtype = {\n",
    "    \"VendorID\": \"Int64\",\n",
    "    \"passenger_count\": \"Int64\",\n",
    "    \"trip_distance\": \"float64\",\n",
    "    \"RatecodeID\": \"Int64\",\n",
    "    \"store_and_fwd_flag\": \"string\",\n",
    "    \"PULocationID\": \"Int64\",\n",
    "    \"DOLocationID\": \"Int64\",\n",
    "    \"payment_type\": \"Int64\",\n",
    "    \"fare_amount\": \"float64\",\n",
    "    \"extra\": \"float64\",\n",
    "    \"mta_tax\": \"float64\",\n",
    "    \"tip_amount\": \"float64\",\n",
    "    \"tolls_amount\": \"float64\",\n",
    "    \"improvement_surcharge\": \"float64\",\n",
    "    \"total_amount\": \"float64\",\n",
    "    \"congestion_surcharge\": \"float64\"\n",
    "}\n",
    "\n",
    "parse_dates = [\n",
    "    \"tpep_pickup_datetime\",\n",
    "    \"tpep_dropoff_datetime\"\n",
    "]\n",
    "\n",
    "df = pd.read_csv(\n",
    "    prefix + 'yellow_tripdata_2021-01.csv.gz',\n",
    "    nrows=100,\n",
    "    dtype=dtype,\n",
    "    parse_dates=parse_dates\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "26842f8d-48d9-4d0f-96e7-eb118716a0b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2mResolved \u001b[1m118 packages\u001b[0m \u001b[2min 0.64ms\u001b[0m\u001b[0m\n",
      "\u001b[2mAudited \u001b[1m10 packages\u001b[0m \u001b[2min 0.17ms\u001b[0m\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!uv add sqlalchemy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "93257a7e-a1eb-41e3-acb0-fed70aaed717",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import create_engine\n",
    "engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8871c53d-4cfd-407f-8159-fb3a0ff8624e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2mResolved \u001b[1m118 packages\u001b[0m \u001b[2min 0.62ms\u001b[0m\u001b[0m\n",
      "\u001b[2mAudited \u001b[1m10 packages\u001b[0m \u001b[2min 0.18ms\u001b[0m\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!uv add psycopg2-binary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e5151b31-a776-4001-a5fb-ec2810ea9476",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import create_engine\n",
    "engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4c383c3e-9fa6-430c-ad77-8c078a90df44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "CREATE TABLE yellow_taxi_data (\n",
      "\t\"VendorID\" BIGINT, \n",
      "\ttpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, \n",
      "\ttpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, \n",
      "\tpassenger_count BIGINT, \n",
      "\ttrip_distance FLOAT(53), \n",
      "\t\"RatecodeID\" BIGINT, \n",
      "\tstore_and_fwd_flag TEXT, \n",
      "\t\"PULocationID\" BIGINT, \n",
      "\t\"DOLocationID\" BIGINT, \n",
      "\tpayment_type BIGINT, \n",
      "\tfare_amount FLOAT(53), \n",
      "\textra FLOAT(53), \n",
      "\tmta_tax FLOAT(53), \n",
      "\ttip_amount FLOAT(53), \n",
      "\ttolls_amount FLOAT(53), \n",
      "\timprovement_surcharge FLOAT(53), \n",
      "\ttotal_amount FLOAT(53), \n",
      "\tcongestion_surcharge FLOAT(53)\n",
      ")\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3bed4d37-fbed-4093-be49-962b524304e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "272242a6-c766-4a43-9bde-2dd97b2b2cde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "d85e3f78-74e2-46e6-a5dc-30f9525b5c48",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_iter = pd.read_csv(\n",
    "    url,\n",
    "    dtype=dtype,\n",
    "    parse_dates=parse_dates,\n",
    "    iterator=True,\n",
    "    chunksize=100000\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "915d17be-b4bb-43ef-929e-8b64695ac680",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table created\n",
      "Inserted first chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 100000\n",
      "Inserted chunk: 69765\n"
     ]
    }
   ],
   "source": [
    "first_chunk = next(df_iter)\n",
    "\n",
    "first_chunk.head(0).to_sql(\n",
    "    name=\"yellow_taxi_data\",\n",
    "    con=engine,\n",
    "    if_exists=\"replace\"\n",
    ")\n",
    "\n",
    "print(\"Table created\")\n",
    "\n",
    "first_chunk.to_sql(\n",
    "    name=\"yellow_taxi_data\",\n",
    "    con=engine,\n",
    "    if_exists=\"append\"\n",
    ")\n",
    "\n",
    "print(\"Inserted first chunk:\", len(first_chunk))\n",
    "\n",
    "for df_chunk in df_iter:\n",
    "    df_chunk.to_sql(\n",
    "        name=\"yellow_taxi_data\",\n",
    "        con=engine,\n",
    "        if_exists=\"append\"\n",
    "    )\n",
    "    print(\"Inserted chunk:\", len(df_chunk))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "82670bda-d6af-4886-82ee-8a08b9472001",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[2K\u001b[2mResolved \u001b[1m119 packages\u001b[0m \u001b[2min 492ms\u001b[0m\u001b[0m                                       \u001b[0m\n",
      "\u001b[2K\u001b[2mPrepared \u001b[1m1 package\u001b[0m \u001b[2min 20ms\u001b[0m\u001b[0m                                               \n",
      "\u001b[2K░░░░░░░░░░░░░░░░░░░░ [0/1] \u001b[2mInstalling wheels...                                 \u001b[0m\u001b[1m\u001b[33mwarning\u001b[39m\u001b[0m\u001b[1m:\u001b[0m \u001b[1mFailed to hardlink files; falling back to full copy. This may lead to degraded performance.\n",
      "         If the cache and target directories are on different filesystems, hardlinking may not be supported.\n",
      "         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.\u001b[0m\n",
      "\u001b[2K\u001b[2mInstalled \u001b[1m1 package\u001b[0m \u001b[2min 7ms\u001b[0m\u001b[0m                                  \u001b[0m\n",
      " \u001b[32m+\u001b[39m \u001b[1mtqdm\u001b[0m\u001b[2m==4.67.1\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!uv add tqdm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0a54c948-df00-4567-bc9d-13da1d02bb51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a5b0e0f2ef6d40d0a982593ef2babc6a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "0it [00:00, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from tqdm.auto import tqdm\n",
    "for df_chunk in tqdm(df_iter):\n",
    "    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd322018-ba02-44cc-a2d6-393ad41c75f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
