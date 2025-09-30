from weather_stats import WeatherStats


class WeatherReportGenerator:
    """Generates reports from WeatherStats."""

    def __init__(self, stats: WeatherStats):
        self.stats = stats

    def generate_text_report(self) -> str:
        """Generate a human-readable weather report in plain text."""

        report_lines = []
        report_lines.append("📊 Weather Report")
        report_lines.append("-" * 40)

        if not self.stats or self.stats.hottest_day is None:
            report_lines.append("No data available to generate report.")
            return "\n".join(report_lines)

        report_lines.append(f"Hottest Day: {self.stats.hottest_day} ({self.stats.hottest_temp_c}°C)")
        report_lines.append(f"Coldest Day: {self.stats.coldest_day} ({self.stats.coldest_temp_c}°C)")
        report_lines.append(f"Most Humid Day: {self.stats.most_humid_day} ({self.stats.max_humidity}%)")

        report_lines.append("")
        report_lines.append(f"Average Max Temperature: {self._format(self.stats.average_max_temp)}°C")
        report_lines.append(f"Average Min Temperature: {self._format(self.stats.average_min_temp)}°C")
        report_lines.append(f"Average Mean Temperature: {self._format(self.stats.average_mean_temp)}°C")

        report_lines.append("")
        report_lines.append(f"Total Precipitation: {self._format(self.stats.total_precipitation_mm)} mm")

        return "\n".join(report_lines)

    @staticmethod
    def _format(value):
        """Helper to format None as N/A, otherwise round to 2 decimals."""
        if value is None:
            return "N/A"
        return round(value, 2)
