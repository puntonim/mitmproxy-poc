"""
Stubhub for ORCID.

Run it with:
$ mitmdump -s orcid_stubhub.py


More info:
- launch inspire locally
- oveer
"""
import random
import re

from time import sleep

from mitmproxy import http

from responses import (
    create_200_response,
    create_409_response,
    create_500_response,
    create_new_record_response,
    create_putcodes_response,
    create_works_response,
)


IS_DELAY_ACTIVE = True


class DirectResponse:
    def request(self, flow):
        if flow.request.method == 'GET' and re.match(r'^http://api\.sandbox\.orcid\.org/v2\.0/[\d\-X]{19}/works$', flow.request.pretty_url):
            responses = [create_works_response] * 5
            # responses.append(create_500_response)
            self._respond_randomly(flow, responses)

        elif flow.request.method == 'GET' and re.match(r'^http://api\.sandbox\.orcid\.org/v2\.0/[\d\-X]{19}/works/[\d,]*$', flow.request.pretty_url):
            responses = [create_putcodes_response] * 5
            # responses.append(create_500_response)
            self._respond_randomly(flow, responses)

        elif flow.request.method == 'POST' and re.match(r'^http://api\.sandbox\.orcid\.org/v2\.0/[\d\-X]{19}/work$', flow.request.pretty_url):
            data = flow.request.data.content.decode('utf-8')
            try:
                recid = re.search(r'<work:url>http://inspirehep\.net/record/(\d*)</work:url>', data).groups()[0]
                recid = int(recid)
            except (AttributeError, ValueError):
                flow.response = create_500_response()
                return

            responses = [create_new_record_response] * 5
            responses.extend([create_500_response, create_409_response])
            #responses = [create_409_response]
            self._respond_randomly(flow, responses, recid)

        elif flow.request.method == 'PUT' and re.match(r'^http://api\.sandbox\.orcid\.org/v2\.0/[\d\-X]{19}/work/[\d,]*', flow.request.pretty_url):
            responses = [create_200_response] * 5
            responses.append(create_500_response)
            self._respond_randomly(flow, responses)

    def _respond_randomly(self, flow, responses, recid=None):
        if IS_DELAY_ACTIVE:
            sleep(random.random())  # range [0.0, 1.0).

        response = random.SystemRandom().choice(responses)
        flow.response = http.HTTPResponse.make(*response(recid=recid))


addons = [DirectResponse()]
