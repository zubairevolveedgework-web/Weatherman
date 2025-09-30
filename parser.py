import os
import csv
from typing import List
from weather_reading import WeatherReading  # ou put the dataclass in this file

from datetime import datetime

class WeatherDataParser:
    """Parses weather .txt files and converts rows into WeatherReading objects."""

    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def parse_files(self) -> List[WeatherReading]:
        """Parse all .txt files in the folder and return a list of WeatherReading objects."""
        readings: List[WeatherReading] = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.folder_path, filename)
                readings.extend(self._parse_file(file_path))

        return readings

    def _parse_file(self, file_path: str) -> List[WeatherReading]:
        readings: List[WeatherReading] = []

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Convert date string like "2004-8-3" → datetime.date
                date_str = row.get("PKT", "")
                parsed_date = None
                try:
                    parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    try:
                        parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    except Exception:
                        continue  # skip bad rows

                reading = WeatherReading(
                    date=parsed_date,
                    max_temp_c=self._to_float(row.get("Max TemperatureC")),
                    mean_temp_c=self._to_float(row.get("Mean TemperatureC")),
                    min_temp_c=self._to_float(row.get("Min TemperatureC")),
                    dew_point_c=self._to_float(row.get("Dew PointC")),
                    mean_dew_point_c=self._to_float(row.get("MeanDew PointC")),
                    min_dew_point_c=self._to_float(row.get("Min DewpointC")),
                    max_humidity=self._to_float(row.get("Max Humidity")),
                    mean_humidity=self._to_float(row.get("Mean Humidity")),
                    min_humidity=self._to_float(row.get("Min Humidity")),
                    max_sea_level_pressure_hpa=self._to_float(row.get("Max Sea Level PressurehPa")),
                    mean_sea_level_pressure_hpa=self._to_float(row.get("Mean Sea Level PressurehPa")),
                    min_sea_level_pressure_hpa=self._to_float(row.get("Min Sea Level PressurehPa")),
                    max_visibility_km=self._to_float(row.get("Max VisibilityKm")),
                    mean_visibility_km=self._to_float(row.get("Mean VisibilityKm")),
                    min_visibility_km=self._to_float(row.get("Min VisibilitykM")),
                    max_wind_speed_kmh=self._to_float(row.get("Max Wind SpeedKm/h")),
                    mean_wind_speed_kmh=self._to_float(row.get("Mean Wind SpeedKm/h")),
                    max_gust_speed_kmh=self._to_float(row.get("Max Gust SpeedKm/h")),
                    precipitation_mm=self._to_float(row.get("Precipitationmm")),
                    cloud_cover=self._to_float(row.get("CloudCover")),
                    events=row.get("Events"),
                    wind_dir_degrees=self._to_float(row.get("WindDirDegrees")),
                )
                readings.append(reading)

        return readings


    @staticmethod
    def _to_float(value: str):
        """Helper to safely convert string to float (or None)."""
        try:
            return float(value) if value not in ("", None) else None
        except ValueError:
            return None
