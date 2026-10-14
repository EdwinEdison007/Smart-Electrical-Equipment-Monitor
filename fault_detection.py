import math

def _valid_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)

def classify_status(current, temperature):
    """Return status and message using illustrative demo thresholds."""
    if not _valid_number(current) or not _valid_number(temperature):
        return "SENSOR FAULT", "Missing or invalid sensor data. Actuation should remain disabled."
    if current < 0 or temperature < -40 or temperature > 200:
        return "SENSOR FAULT", "Reading is outside the accepted simulation range."
    if current >= 7 or temperature >= 70:
        return "CRITICAL", "Critical threshold reached. Check equipment immediately."
    if current >= 5 or temperature >= 50:
        return "WARNING", "Reading is above the normal operating range."
    return "NORMAL", "Readings are within the configured demo limits."
