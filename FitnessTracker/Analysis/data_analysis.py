from datetime import datetime
from collections import defaultdict
from models import Readings

def weekly_changes(input):
    # here input is a queryset of objects
    
    # Step 1: Track the sum of quantities and the count of readings for each date
    sum_dict = defaultdict(float)  # Dictionary to store the sum of quantities
    count_dict = defaultdict(int)   # Dictionary to store the count of readings

    # Step 2: Iterate over the readings
    for reading in input:
        date_str = reading.date.strftime("%Y-%m-%d")
        sum_dict[date_str] += reading.quantity  # Accumulate the sum of quantities
        count_dict[date_str] += 1               # Count the number of readings

    # Step 3: Calculate the average for each date
    average_dict = {date: sum_dict[date] / count_dict[date] for date in sum_dict}

    # Output the dictionary containing the average quantities for each date
    return average_dict

print(weekly_changes(Readings.objects.filter(metric__title="vo2_max").order_by('date')))
