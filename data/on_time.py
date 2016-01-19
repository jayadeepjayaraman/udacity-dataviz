import pandas as pd

filtered_carrier_name = ['American Airlines Inc.','Delta Air Lines Inc.','Southwest Airlines Co.','United Air Lines Inc.','US Airways Inc.'];

df_init = pd.read_csv('453597967_102015_5327_airline_delay_causes.csv');

df = df_init[df_init['carrier_name'].isin(filtered_carrier_name)];

transformed = df.groupby(['year', 'carrier_name']).sum()[['arr_flights','arr_del15','arr_cancelled','arr_diverted']]


transformed['on_time']= 1 - transformed['arr_del15']/transformed['arr_flights']

transformed.to_csv('output.csv', header=['arrivals','delayed','cancelled','diverted','on_time']);