import csv
import operator

with open('453597967_102015_5327_airline_delay_causes.csv') as sample, open('randomized.csv', "w") as out:
    csv1=csv.reader(sample)
    header = next(csv1, None)
    csv_writer = csv.writer(out)
    
    if header:
        csv_writer.writerow(header)
    csv_writer.writerows(sorted(csv1, key=operator.itemgetter(0,3)))