Build
-----

    docker build -t cocaine-proxy .

Run
---

    docker run --net=host --rm -ti -v `pwd`:/app -p 8080:8080 cocaine-proxy-test /app/overlord --slave /app/echo.py --locator '[2a02:6b8:0:1a16:556::200]:10053'
