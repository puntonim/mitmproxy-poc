# MITMPROXY

https://mitmproxy.org/

How to run this examples:
- create a python3 virtual environment
- install the requirements in requirements.txt
- run:
`$ mitmdump -s poc.py`
- now make a request using the proxy like:
`$ curl -i -x 127.0.0.1:8080 google.com`

More examples here:
https://github.com/mitmproxy/mitmproxy/tree/master/examples
