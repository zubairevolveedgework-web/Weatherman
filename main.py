import argparse
from parser import WeatherDataParser
from calculator import WeatherCalculator
from reporter import WeatherReportGenerator


def main():
    parser = argparse.ArgumentParser(description="Weather Report Generator")
    parser.add_argument(
        "--data-folder",
        type=str,
        default="Weatherman/weather_reports/",
        help="Path to the folder containing weather .txt files",
    )
    args = parser.parse_args()

    # Step 1: Parse weather data
    data_parser = WeatherDataParser(args.data_folder)
    readings = data_parser.parse_files()

    if not readings:
        print("No weather data found. Please check your data folder.")
        return

    # Step 2: Compute statistics
    calculator = WeatherCalculator(readings)
    stats = calculator.compute_stats()

    # Step 3: Generate report
    reporter = WeatherReportGenerator(stats)
    report = reporter.generate_text_report()

    print(report)


if __name__ == "__main__":
    main()
