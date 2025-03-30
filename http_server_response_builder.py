class Response:
    def __init__(self, http_version, status_code, status_message, headers, body):
        self.http_version = http_version
        self.status_code = status_code
        self.status_message = status_message
        self.headers = headers
        self.body = body

    def __str__(self):
        response_line = f"{self.http_version} {self.status_code} {self.status_message}"
        headers = "\r\n".join(f"{key}: {value}" for key, value in self.headers.items())
        return f"{response_line}\r\n{headers}\r\n\r\n{self.body}"


class ResponseBuilder:
    def __init__(self):
        """Initialize"""
        self.http_version = "HTTP/1.1"
        self.status_code = "200"
        self.status_message = "OK"
        self.headers = {}
        self.body = ""

    def withHttpVersion(self, version):
        self.http_version = version
        return self

    def withStatusCode(self, code):
        self.status_code = code
        return self

    def withStatusMessage(self, message):
        self.status_message = message
        return self

    def withHeader(self, key, value):
        self.headers[key] = value
        return self

    def addBody(self, body):
        self.body = body
        self.withHeader("Content-Length", str(len(body)))
        return self

    def build(self):
        return Response(self.http_version, self.status_code, self.status_message, self.headers, self.body)

if __name__ == "__main__":
    response = (ResponseBuilder()
                .withHttpVersion("HTTP/1.1")
                .withStatusCode("200")
                .withStatusMessage("OK")
                .withHeader("Date", "Wed, 31 Jul 2019 07:31:00 GMT")
                .withHeader("Content-Type", "text/plain")
                .addBody("Hello")
                .build())

    print(str(response)) 
