from dataclasses import dataclass
from typing import Optional

@dataclass
class WeatherStats:
    hottest_day: Optional[str]
    hottest_temp_c: Optional[float]

    coldest_day: Optional[str]
    coldest_temp_c: Optional[float]

    most_humid_day: Optional[str]
    max_humidity: Optional[float]

    average_max_temp: Optional[float]
    average_min_temp: Optional[float]
    average_mean_temp: Optional[float]

    total_precipitation_mm: Optional[float]
