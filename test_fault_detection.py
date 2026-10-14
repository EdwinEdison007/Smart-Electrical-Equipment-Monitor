from src.fault_detection import classify_status

def test_normal_readings(): assert classify_status(3.2, 35)[0] == "NORMAL"
def test_current_warning(): assert classify_status(5.2, 35)[0] == "WARNING"
def test_temperature_warning(): assert classify_status(3.2, 52)[0] == "WARNING"
def test_current_critical(): assert classify_status(7.1, 35)[0] == "CRITICAL"
def test_temperature_critical(): assert classify_status(3.2, 72)[0] == "CRITICAL"
def test_missing_reading(): assert classify_status(None, 35)[0] == "SENSOR FAULT"
def test_non_numeric_reading(): assert classify_status("high", 35)[0] == "SENSOR FAULT"
def test_negative_current(): assert classify_status(-1, 35)[0] == "SENSOR FAULT"
def test_out_of_range_temperature(): assert classify_status(2, 250)[0] == "SENSOR FAULT"
def test_boolean_is_not_a_reading(): assert classify_status(True, 35)[0] == "SENSOR FAULT"
