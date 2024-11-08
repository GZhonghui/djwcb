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
        dates.append(start_date.strftime('%Y-%m-%d'))
        start_date += delta
    
    return {date: [] for date in dates}

def main():
    parser = argparse.ArgumentParser(description='Generate a JSON file of days for a specified year with empty lists.')
    parser.add_argument('-y', '--year', type=int, help='Year to generate days for', required=True)
    args = parser.parse_args()

    days = generate_days(args.year)
    
    with open(f"{args.year}_days.json", "w") as file:
        json.dump(days, file, indent=4)

    print(f"JSON file created for the year {args.year}")

if __name__ == '__main__':
    main()
