#!/usr/bin/env python
# -*- coding=utf-8 -*-
import json
from libs.http_requester import HTTPRequester

req = HTTPRequester(host="example.com", port=80)
req.set_header(["User-Agent: Example"]) # Override the user-agent, default is "Requester".
bodies = {}
bodies["user"] = "example user"
bodies["password"] = "example password"
req.set_body(json.dumps(bodies))
res = req.request("POST", "/login")
print(res.body)
