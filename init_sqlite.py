import sqlite3

conn = sqlite3.connect('clairvoyant.db')
cursor = conn.cursor()

# DATA TYPES:
# NULL. The value is a NULL value.
# INTEGER. The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
# REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
# TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
# BLOB. The value is a blob of data, stored exactly as it was input.


# DAILY
# create dailyTable
cursor.execute("""CREATE TABLE IF NOT EXISTS dailyTable
                  (
               id INTEGER PRIMARY KEY, 
               date TEXT,
               user_id TEXT
               )""")
conn.commit()

# SLEEP
# create sleepTable
cursor.execute("""CREATE TABLE IF NOT EXISTS sleepTable
                  (
               id INTEGER PRIMARY KEY,
               daily_id INTEGER,
               duration INTEGER,
               efficiency INTEGER,
               end_time TEXT,
               start_time TEXT,
               info_code INTEGER,
               is_main_sleep INTEGER,
               log_id INTEGER,
               minutes_after_wakeup INTEGER,
               minutes_asleep INTEGER,
               minutes_awake INTEGER,
               minutes_to_fall_asleep INTEGER,
               log_type TEXT,
               time_in_bed INTEGER,
               type TEXT,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
# create sleepLevelTable
cursor.execute("""CREATE TABLE IF NOT EXISTS sleepLevelTable
                  (
               id PRIMARY KEY,
               sleep_id INTEGER,
               daily_id INTEGER,
               level TEXT, 
               seconds INTEGER,
               FOREIGN KEY (sleep_id) REFERENCES sleepTable(id)
               )""")
# create sleepLevelSummaryTable
cursor.execute("""CREATE TABLE IF NOT EXISTS sleepLevelSummaryTable
                  (
               id INTEGER PRIMARY KEY, 
               sleep_id INTEGER,
               level TEXT,
               count INTEGER,
               minutes INTEGER,
               FOREIGN KEY (sleep_id) REFERENCES sleepTable(id)
               )""")

# CARDIO
# create cardioTable
cursor.execute("""CREATE TABLE IF NOT EXISTS cardioTable
                  (
               daily_id INTEGER PRIMARY KEY, 
               daily_rmssd REAL,
               deep_rmssd REAL,
               vo2_max REAL,
               spo2_avg REAL,
               spo2_min REAL,
               spo2_max REAL,
               resting_hr REAL,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
# create hrTable
cursor.execute("""CREATE TABLE IF NOT EXISTS hrTable
                  (
               id INTEGER PRIMARY KEY,
               daily_id INTEGER, 
               TIME_INTERVAL REAL,
               hr REAL,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
conn.commit()
# TEMP
# create skinTempTable
cursor.execute("""CREATE TABLE IF NOT EXISTS skinTempTable
                  (
               daily_id INTEGER PRIMARY KEY, 
               nightly_relative REAL,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
conn.commit()

# RESPIRATORY
# create breathingRateTable
cursor.execute("""CREATE TABLE IF NOT EXISTS breathingRateTable
                  (
               daily_id INTEGER PRIMARY KEY, 
               breathing_rate REAL,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
conn.commit()

# EXERCISE
# create activeZoneTable
cursor.execute("""CREATE TABLE IF NOT EXISTS activeZoneTable
                  (
               daily_id INTEGER PRIMARY KEY, 
               active_zone_minutes INTEGER,
               fat_burn_minutes INTEGER,
               cardio_zone_minutes INTEGER,
               peak_active_zone_minutes INTEGER,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
conn.commit()

# create activitySummaryTable
cursor.execute("""CREATE TABLE IF NOT EXISTS activitySummaryTable
                  (
               daily_id INTEGER PRIMARY KEY, 
               activity_calories INTEGER,
               calories_est_mu INTEGER,
               calories_bmr INTEGER,
               calories_out INTEGER,
               calories_out_unest INTEGER,
               sedentary_minutes INTEGER,
               light_activity_minutes INTEGER,
               high_activity_minutes INTEGER,
               steps INTEGER,
               FOREIGN KEY (daily_id) REFERENCES dailyTable(id)
               )""")
conn.commit()

# MEDICATION

# BLOOD PRESSURE

# PAIN

# WEIGHT

cursor.close()
conn.close()