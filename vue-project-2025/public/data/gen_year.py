# 本代码由AI生成
# 调用方式：python3 gen_year.py -y 2024

# gen_year.py
import json
import argparse
from datetime import datetime, timedelta

def generate_days(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    delta = timedelta(days=1)
    dates = []
    
    while start_date <= end_date:
        date_str = start_date.strftime('%Y-%m-%d')
        dates.append(date_str)
        start_date += delta
    
    return {date: {"url": "", "games": []} for date in dates}

def main():
    parser = argparse.ArgumentParser(description='Generate a JSON file where each day is on a new line.')
    parser.add_argument('-y', '--year', type=int, help='Year to generate days for', required=True)
    args = parser.parse_args()

    days = generate_days(args.year)
    
    # Open the file to write
    with open(f"{args.year}_days.json", "w") as file:
        file.write("{\n")  # Open the JSON dictionary
        # Process each day, ensuring it is on its own line
        last_day = len(days)
        for index, (day, data) in enumerate(days.items(), 1):
            # Serialize the data for each day
            json_data = json.dumps(data)
            # Format the day entry as a single line
            line = f'    "{day}": {json_data}'
            if index < last_day:
                line += ','
            line += '\n'
            file.write(line)
        file.write("}\n")  # Close the JSON dictionary

    print(f"Formatted JSON file created for the year {args.year}")

if __name__ == '__main__':
    main()

