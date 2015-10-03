Build
-----

    docker build -t cocaine-proxy .

Run
---

    docker run --rm -ti -v `pwd`:/app -p 8080:8080 cocaine-proxy /app/overlord --slave /app/echo.py
