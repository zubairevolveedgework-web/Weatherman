from typing import List, Optional
from weather_reading import WeatherReading
from weather_stats import WeatherStats


class WeatherCalculator:
    """Computes weather statistics from a list of WeatherReading objects."""

    def __init__(self, readings: List[WeatherReading]):
        self.readings = readings

    def compute_stats(self) -> WeatherStats:
        """Compute weather statistics and return as a WeatherStats object."""

        if not self.readings:
            return WeatherStats(
                hottest_day=None,
                hottest_temp_c=None,
                coldest_day=None,
                coldest_temp_c=None,
                most_humid_day=None,
                max_humidity=None,
                average_max_temp=None,
                average_min_temp=None,
                average_mean_temp=None,
                total_precipitation_mm=None,
            )

        # Find hottest day
        hottest = max(
            self.readings, key=lambda r: r.max_temp_c if r.max_temp_c is not None else float("-inf")
        )

        # Find coldest day
        coldest = min(
            self.readings, key=lambda r: r.min_temp_c if r.min_temp_c is not None else float("inf")
        )

        # Most humid day
        most_humid = max(
            self.readings, key=lambda r: r.max_humidity if r.max_humidity is not None else float("-inf")
        )

        # Averages
        avg_max_temp = self._average([r.max_temp_c for r in self.readings])
        avg_min_temp = self._average([r.min_temp_c for r in self.readings])
        avg_mean_temp = self._average([r.mean_temp_c for r in self.readings])

        # Total precipitation
        total_precipitation = sum(
            r.precipitation_mm for r in self.readings if r.precipitation_mm is not None
        )

        return WeatherStats(
            hottest_day=hottest.date,
            hottest_temp_c=hottest.max_temp_c,
            coldest_day=coldest.date,
            coldest_temp_c=coldest.min_temp_c,
            most_humid_day=most_humid.date,
            max_humidity=most_humid.max_humidity,
            average_max_temp=avg_max_temp,
            average_min_temp=avg_min_temp,
            average_mean_temp=avg_mean_temp,
            total_precipitation_mm=total_precipitation,
        )

    @staticmethod
    def _average(values: List[Optional[float]]) -> Optional[float]:
        """Helper to calculate average while ignoring None values."""
        clean_values = [v for v in values if v is not None]
        return sum(clean_values) / len(clean_values) if clean_values else None
