# Fault detection flow

```text
Start -> Generate simulated current and temperature
  -> Missing, invalid, or out-of-range data?
      Yes -> SENSOR FAULT
      No -> Current >= 7 A OR temperature >= 70 C?
               Yes -> CRITICAL
               No -> Current >= 5 A OR temperature >= 50 C?
                        Yes -> WARNING
                        No -> NORMAL
```
