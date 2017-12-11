class Requester(object):

    def __init__(self):
        pass

    class Response():
        status_code = 0
        header = ""
        body = ""

        def set_status_code(self, status_code):
            self.status_code = status_code

        def set_header(self, header):
            self.header = header

        def set_body(self, body):
            self.body = body
