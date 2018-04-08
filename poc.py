from bs4 import BeautifulSoup

from mitmproxy import http


class AddHeader:
    """
    Add an header to any response.

    $ curl -i -x 127.0.0.1:8080 google.com
    HTTP/1.1 302 Found
    Cache-Control: private
    ...
    myheader: foo

    <HTML><HEAD>...
    """
    def response(self, flow):
        flow.response.headers["myheader"] = "foo"


class DirectResponse:
    """
    Match a request and return a response (w/out contacting the destination).

    $ curl -i -x 127.0.0.1:8080 http://cern.ch
    HTTP/1.1 200 OK
    Content-Type: text/html
    content-length: 18
    myheader: foo

    There you go CERN
    """
    def request(self, flow):
        # pretty_url takes the "Host" header of the request into account, which
        # is useful in transparent mode where we usually only have the IP otherwise.
        if flow.request.pretty_url == "http://cern.ch/":
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"There you go CERN\n",  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )


class EditResponse:
    """
    Match a request, forward to the actual destination and edit the response.

    $ curl -i -x 127.0.0.1:8080 http://inspirehep.net
    HTTP/1.1 200 OK
    Date: Sun, 08 Apr 2018 21:16:03 GMT
    myheader: foo
    content-length: 17237
    ...

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    ...
    <p>CERN!!!!!</p></body>
    </html>
    """
    def response(self, flow):
        if flow.request.pretty_url == "http://inspirehep.net/":
            html = BeautifulSoup(flow.response.content, "html.parser")
            if html.body:
                flow.response.content = str(html).encode("utf8")
                # Inject a new tag at the end of the body.
                tag = html.new_tag("p")
                tag.string = "CERN!!!!!"
                html.body.insert(len(list(html.body.children)), tag)
                flow.response.content = str(html).encode("utf8")


addons = [AddHeader(), DirectResponse(), EditResponse()]
