#!/usr/bin/env python
from cocaine.worker import Worker
from cocaine.logger import Logger
from cocaine.decorators import http

import uuid

log = Logger(endpoints=(("2a02:6b8:0:1a16:556::200", 10053),))

@http
def http_echo(request, response):

    req_id = uuid.uuid4().hex

    log.info("request %s: start" % req_id)

    req = yield request.read()

    log.info("request %s: got body of %s bytes" % (req_id, len(req.body)))

    response.write_head(200, {})

    log.info("request %s: responding with original body" % req_id)

    response.write(req.body)

    log.info("request %s: done" % req_id)


if __name__ == '__main__':
    W = Worker()
    W.run({"http": http_echo})
