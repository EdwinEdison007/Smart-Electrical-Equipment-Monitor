import random

def generate_reading(mode="AUTO"):
    """Generate illustrative readings; these are not physical measurements."""
    mode = mode.upper()
    if mode == "NORMAL":
        return {"current": round(random.uniform(1.0, 4.4), 2), "temperature": round(random.uniform(25.0, 44.0), 1)}
    if mode == "WARNING":
        return {"current": round(random.uniform(5.0, 6.8), 2), "temperature": round(random.uniform(50.0, 66.0), 1)}
    if mode == "CRITICAL":
        if random.choice([True, False]):
            return {"current": round(random.uniform(7.0, 9.0), 2), "temperature": round(random.uniform(55.0, 68.0), 1)}
        return {"current": round(random.uniform(3.0, 6.5), 2), "temperature": round(random.uniform(70.0, 95.0), 1)}
    if mode == "SENSOR FAULT":
        return {"current": None, "temperature": round(random.uniform(25.0, 40.0), 1)}
    return {"current": round(random.uniform(1.0, 7.8), 2), "temperature": round(random.uniform(25.0, 76.0), 1)}
