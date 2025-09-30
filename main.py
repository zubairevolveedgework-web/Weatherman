import argparse
from parser import WeatherDataParser
from calculator import WeatherCalculator
from reporter import WeatherReportGenerator
from datetime import date

def report_extremes(readings, year):
    """For a given year: highest temp, lowest temp, most humid day."""
    year_readings = [r for r in readings if r.date.year == year]

    if not year_readings:
        print(f"No data found for year {year}")
        return

    hottest = max(year_readings, key=lambda r: r.max_temp_c or float("-inf"))
    coldest = min(year_readings, key=lambda r: r.min_temp_c or float("inf"))
    humid = max(year_readings, key=lambda r: r.max_humidity or float("-inf"))

    print(f"Highest: {hottest.max_temp_c}C on {hottest.date.strftime('%B %d')}")
    print(f"Lowest: {coldest.min_temp_c}C on {coldest.date.strftime('%B %d')}")
    print(f"Humidity: {humid.max_humidity}% on {humid.date.strftime('%B %d')}")


def report_averages(readings, year, month):
    """For a given month: average highest, lowest, mean humidity."""
    month_readings = [r for r in readings if r.date.year == year and r.date.month == month]

    if not month_readings:
        print(f"No data found for {year}/{month}")
        return

    avg_high = sum(r.max_temp_c for r in month_readings if r.max_temp_c is not None) / len(month_readings)
    avg_low = sum(r.min_temp_c for r in month_readings if r.min_temp_c is not None) / len(month_readings)
    avg_humidity = sum(r.mean_humidity for r in month_readings if r.mean_humidity is not None) / len(month_readings)

    print(f"Highest Average: {round(avg_high)}C")
    print(f"Lowest Average: {round(avg_low)}C")
    print(f"Average Mean Humidity: {round(avg_humidity)}%")
def main():
    parser = argparse.ArgumentParser(description="Weather Report Generator")
    parser.add_argument(
        "--data-folder",
        type=str,
        help="Path to the folder containing weather .txt files",
    )
    parser.add_argument("-e", type=int, help="Report extremes for given year")
    parser.add_argument("-a", type=str, help="Report averages for given year/month (format: YYYY/MM)")

    args = parser.parse_args()

    # Load data
    data_parser = WeatherDataParser(args.data_folder)
    readings = data_parser.parse_files()

    if args.e:
        report_extremes(readings, args.e)

    if args.a:
        year, month = map(int, args.a.split("/"))
        report_averages(readings, year, month)


if __name__ == "__main__":
    main()