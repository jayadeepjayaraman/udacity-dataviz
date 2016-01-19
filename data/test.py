import csv

def FloatOrZero(value):
    try:
        return float(value)
    except:
        return 0.0


tot_arr_delay = 0.00;
tot_carrier_delay = 0.00;
tot_security_delay = 0.00;
tot_weather_delay = 0.00;
tot_nas_delay = 0.00;
tot_aircraft_delay = 0.00;

tot_year_arr_delay = 0.00;
tot_year_carrier_delay = 0.00;
tot_year_security_delay = 0.00;
tot_year_weather_delay = 0.00;
tot_year_nas_delay = 0.00;
tot_year_late_aircraft_delay = 0.00;

prev_carrier_name = '';
prev_year = ''

with open('transposed.csv', 'wb') as destfile, open('year_agg.csv', 'wb') as year_destfile:
	writer = csv.writer(destfile)
	writer.writerow(['year', 'carrier_name','delay_cause', 'delay_mins', 'percentage_delay'])    

	writeryear = csv.writer(year_destfile)
	writeryear.writerow(['year','delay_cause', 'delay_mins', 'percentage_delay'])    

	with open('randomized.csv', 'rb') as sourcefile:
		for d in csv.DictReader(sourcefile):
		
		    year = d.pop('year')
		    carrier_name = d.pop('carrier_name')

		    for key, value in sorted(d.items()):

			if key.strip(' ') == 'arr_delay':
				tot_arr_delay = tot_arr_delay + FloatOrZero(value)
				tot_year_arr_delay = tot_year_arr_delay + FloatOrZero(value)

			elif key.strip(' ') == 'carrier_delay':
				tot_carrier_delay = tot_carrier_delay + FloatOrZero(value)
				tot_year_carrier_delay = tot_year_carrier_delay + FloatOrZero(value)

			elif key.strip(' ') == 'security_delay':
				tot_security_delay = tot_security_delay + FloatOrZero(value)
				tot_year_security_delay = tot_year_security_delay + FloatOrZero(value)

			elif key.strip(' ') == 'weather_delay':
				tot_weather_delay = tot_weather_delay + FloatOrZero(value)
				tot_year_weather_delay = tot_year_weather_delay + FloatOrZero(value)

			elif key.strip(' ') == 'nas_delay':
				tot_nas_delay = tot_nas_delay + FloatOrZero(value)
				tot_year_nas_delay = tot_year_nas_delay + FloatOrZero(value)

			elif key.strip(' ') == 'late_aircraft_delay':
				tot_aircraft_delay = tot_aircraft_delay + FloatOrZero(value)
				tot_year_late_aircraft_delay = tot_year_late_aircraft_delay + FloatOrZero(value)
		    		
		    if  ((carrier_name <> prev_carrier_name) or (year <> prev_year )):

		        if ((year <> prev_year )):
		        
				tot_year_delay = tot_year_arr_delay + tot_year_carrier_delay + tot_year_security_delay + tot_year_weather_delay + tot_year_nas_delay + tot_year_late_aircraft_delay
			
				row = [year,'arr_delay',tot_year_arr_delay,round((tot_year_arr_delay/tot_year_delay),4)]
				writeryear.writerow(row)

				row = [year,'carrier_delay',tot_year_carrier_delay,round((tot_year_carrier_delay/tot_year_delay),4)]
				writeryear.writerow(row)

				row = [year,'security_delay',tot_year_security_delay,round((tot_year_security_delay/tot_year_delay),4)]
				writeryear.writerow(row)

				row = [year,'weather_delay',tot_year_weather_delay,round((tot_year_weather_delay/tot_year_delay),4)]
				writeryear.writerow(row)

				row = [year,'nas_delay',tot_year_nas_delay,round((tot_year_nas_delay/tot_year_delay),4)]
				writeryear.writerow(row)

				row = [year,'late_aircraft_delay',tot_year_late_aircraft_delay,round((tot_year_late_aircraft_delay/tot_year_delay),4)]
				writeryear.writerow(row)
		        	
				tot_year_arr_delay = 0.00;
				tot_year_carrier_delay = 0.00;
				tot_year_security_delay = 0.00;
				tot_year_weather_delay = 0.00;
				tot_year_nas_delay = 0.00;
				tot_year_late_aircraft_delay = 0.00;

		    	total_delay = tot_arr_delay + tot_carrier_delay + tot_security_delay + tot_weather_delay + tot_nas_delay + tot_aircraft_delay

			row = [year, carrier_name, 'arr_delay',tot_arr_delay,round((tot_arr_delay/total_delay),4)]
			writer.writerow(row)

			row = [year, carrier_name, 'carrier_delay',tot_carrier_delay, round((tot_carrier_delay/total_delay),4)]
			writer.writerow(row)

			row = [year, carrier_name, 'security_delay',tot_security_delay,round((tot_security_delay/total_delay),4)]
			writer.writerow(row)

			row = [year, carrier_name, 'weather_delay',tot_weather_delay,round((tot_weather_delay/total_delay),4)]
			writer.writerow(row)

			row = [year, carrier_name, 'nas_delay',tot_nas_delay, round((tot_nas_delay/total_delay),4)]
			writer.writerow(row)

			row = [year, carrier_name, 'late_aircraft_delay',tot_aircraft_delay, round((tot_aircraft_delay/total_delay),4)]
			writer.writerow(row)
				
			tot_arr_delay      = 0.00;
			tot_carrier_delay  = 0.00;
			tot_security_delay = 0.00;
			tot_weather_delay  = 0.00;
			tot_nas_delay      = 0.00;
			tot_aircraft_delay = 0.00;
			
		    prev_year = year;
		    prev_carrier_name = carrier_name;