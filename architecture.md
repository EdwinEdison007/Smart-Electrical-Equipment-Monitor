# Architecture

```text
Browser: HTML + CSS + JavaScript + Chart.js
                    | HTTP / JSON
                    v
              Flask application
             /       |         \
            v        v          v
       Simulator  Fault logic  Session history
                       |
                       v
              Status + message
                       |
                       v
      Dashboard cards, chart, events, CSV export
```

History is stored in memory and resets when the Python server restarts. SQLite persistence, authentication, device management, and real sensor ingestion are possible future enhancements.
