#!/usr/bin/env python
# -*- coding=utf-8 -*-
import socket
from libs.requester import Requester


class HTTPRequester(Requester):
    _body = ""
    _headers = []
    _host = ""
    _port = ""
    _payload = ""

    def __init__(self, host="localhost", port=80):
        super().__init__()
        self._host = host
        self._port = port

    def _make_payload(self, method="GET", url="/"):
        general = "%s %s HTTP/1.1\r\n" % (method, url)
        if self._body:
            body = self._body
        else:
            body = ""
        if method == "POST":
            content_length = str(len(body))
            self._headers.append("Content-Length: %s" % content_length)
        self._headers.append("Host: %s" % self._host)
        self._headers.append("User-Agent: Requester")
        self._headers.append("Connection: close")
        headers = "\r\n".join(self._headers) + "\r\n\r\n"
        payload = general + headers + body
        self._payload = payload.encode("utf-8")

    def set_body(self, body):
        if isinstance(body, str):
            self._body = body
        else:
            self._body = body.decode("utf-8")

    def set_header(self, headers):
        headers = [header if isinstance(header, str) else header.decode("utf-8") for header in headers]
        self._headers = headers

    def request(self, method="GET", url="/"):
        response = self.Response()
        self._make_payload(method, url)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self._host, self._port))
        sock.send(self._payload)
        res = ""
        res_recv = sock.recv(50000)
        while res_recv:
            res += res_recv.decode("utf-8")
            res_recv = sock.recv(50000)
        responses = res.split("\r\n")
        status_code = int(responses[0].split(" ")[1])
        header = responses[1]
        body = "\r\n".join(responses[2:])
        response.set_status_code(status_code)
        response.set_header(header)
        response.set_body(body)
