
from dataclasses import dataclass
from typing import Optional

# Define a data structure for holding each weather reading.

@dataclass
class WeatherReading:
    date: str  # PKT column (assuming it's the date)
    max_temp_c: Optional[float]
    mean_temp_c: Optional[float]
    min_temp_c: Optional[float]
    dew_point_c: Optional[float]
    mean_dew_point_c: Optional[float]
    min_dew_point_c: Optional[float]
    max_humidity: Optional[float]
    mean_humidity: Optional[float]
    min_humidity: Optional[float]
    max_sea_level_pressure_hpa: Optional[float]
    mean_sea_level_pressure_hpa: Optional[float]
    min_sea_level_pressure_hpa: Optional[float]
    max_visibility_km: Optional[float]
    mean_visibility_km: Optional[float]
    min_visibility_km: Optional[float]
    max_wind_speed_kmh: Optional[float]
    mean_wind_speed_kmh: Optional[float]
    max_gust_speed_kmh: Optional[float]
    precipitation_mm: Optional[float]
    cloud_cover: Optional[float]
    events: Optional[str]
    wind_dir_degrees: opt[float]
