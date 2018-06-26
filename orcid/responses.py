RECIDS_PUTCODES = {
    1498589: '991498589',  # 1 orcid
    1498185: '991498185',  # 100 orcids
}


_WORKS_RESPONSE = """{
        "path": "/0000-0002-1825-0097/works",
        "group": [
          {
            "work-summary": [
              {
                "put-code": 991498589,
                "title": {
                  "translated-title": null,
                  "subtitle": null,
                  "title": {
                    "value": "Partial Symmetries of Weak Interactions"
                  }
                },
                "last-modified-date": {
                  "value": 1519143190177
                },
                "external-ids": {
                  "external-id": [
                    {
                      "external-id-value": "10.1016/0029-5582(61)90469-2",
                      "external-id-relationship": "SELF",
                      "external-id-url": {
                        "value": "http://dx.doi.org/10.1016/0029-5582(61)90469-2"
                      },
                      "external-id-type": "doi"
                    }
                  ]
                },
                "created-date": {
                  "value": 1516716146242
                },
                "visibility": "PUBLIC",
                "source": {
                  "source-orcid": null,
                  "source-name": {
                    "value": "INSPIRE-PROFILE-PUSH"
                  },
                  "source-client-id": {
                    "path": "CHANGE_ME",
                    "host": "sandbox.orcid.org",
                    "uri": "http://sandbox.orcid.org/client/CHANGE_ME"
                  }
                },
                "publication-date": {
                  "month": null,
                  "day": null,
                  "media-type": null,
                  "year": {
                    "value": "1961"
                  }
                },
                "display-index": "0",
                "path": "/0000-0002-1825-0097/work/991498589",
                "type": "JOURNAL_ARTICLE"
              }
            ],
            "external-ids": {
              "external-id": [
                {
                  "external-id-value": "10.1016/0029-5582(61)90469-2",
                  "external-id-relationship": "SELF",
                  "external-id-url": {
                    "value": "http://dx.doi.org/10.1016/0029-5582(61)90469-2"
                  },
                  "external-id-type": "doi"
                }
              ]
            },
            "last-modified-date": {
              "value": 1519143190177
            }
          },
          
          {
            "work-summary": [
              {
                "put-code": 991498185,
                "title": {
                  "translated-title": null,
                  "subtitle": null,
                  "title": {
                    "value": "Partial Symmetries of Weak Interactions"
                  }
                },
                "last-modified-date": {
                  "value": 1519143190177
                },
                "external-ids": {
                  "external-id": [
                    {
                      "external-id-value": "10.1016/0029-5582(61)90469-2",
                      "external-id-relationship": "SELF",
                      "external-id-url": {
                        "value": "http://dx.doi.org/10.1016/0029-5582(61)90469-2"
                      },
                      "external-id-type": "doi"
                    }
                  ]
                },
                "created-date": {
                  "value": 1516716146242
                },
                "visibility": "PUBLIC",
                "source": {
                  "source-orcid": null,
                  "source-name": {
                    "value": "INSPIRE-PROFILE-PUSH"
                  },
                  "source-client-id": {
                    "path": "CHANGE_ME",
                    "host": "sandbox.orcid.org",
                    "uri": "http://sandbox.orcid.org/client/CHANGE_ME"
                  }
                },
                "publication-date": {
                  "month": null,
                  "day": null,
                  "media-type": null,
                  "year": {
                    "value": "1961"
                  }
                },
                "display-index": "0",
                "path": "/0000-0002-1825-0097/work/991498185",
                "type": "JOURNAL_ARTICLE"
              }
            ],
            "external-ids": {
              "external-id": [
                {
                  "external-id-value": "10.1016/0029-5582(61)90469-2",
                  "external-id-relationship": "SELF",
                  "external-id-url": {
                    "value": "http://dx.doi.org/10.1016/0029-5582(61)90469-2"
                  },
                  "external-id-type": "doi"
                }
              ]
            },
            "last-modified-date": {
              "value": 1519143190177
            }
          }
          
        ],
        "last-modified-date": {
          "value": 1519143233490
        }
      }"""


def create_works_response(*args, **kwargs):
    return (
        200,
        _WORKS_RESPONSE.encode('utf8'),
        {
            'content-type': '[application/orcid+json; qs=2;charset=UTF-8]',
            # 'content-length': "['4774']",
        }
    )


_PUTCODES_RESPONSE = """{
      "bulk": [
        {
          "work": {
            "language-code": null,
            "put-code": 991498589,
            "contributors": {
              "contributor": [
                {
                  "contributor-orcid": null,
                  "contributor-attributes": {
                    "contributor-role": "AUTHOR",
                    "contributor-sequence": "FIRST"
                  },
                  "credit-name": {
                    "value": "Glashow, S.L."
                  },
                  "contributor-email": null
                }
              ]
            },
            "title": {
              "translated-title": null,
              "subtitle": null,
              "title": {
                "value": "Partial Symmetries of Weak Interactions"
              }
            },
            "url": {
              "value": "http://labs.inspirehep.net/record/1498589"
            },
            "external-ids": {
              "external-id": [
                {
                  "external-id-value": "10.1016/0029-5582(61)90469-2",
                  "external-id-relationship": "SELF",
                  "external-id-url": {
                    "value": "http://dx.doi.org/10.1016/0029-5582(61)90469-2"
                  },
                  "external-id-type": "doi"
                }
              ]
            },
            "last-modified-date": {
              "value": 1519143190177
            },
            "citation": {
              "citation-type": "BIBTEX",
              "citation-value": ""
            },
            "created-date": {
              "value": 1516716146242
            },
            "visibility": "PUBLIC",
            "source": {
              "source-orcid": null,
              "source-name": {
                "value": "INSPIRE-PROFILE-PUSH"
              },
              "source-client-id": {
                "path": "CHANGE_ME",
                "host": "sandbox.orcid.org",
                "uri": "http://sandbox.orcid.org/client/CHANGE_ME"
              }
            },
            "publication-date": {
              "month": null,
              "day": null,
              "media-type": null,
              "year": {
                "value": "1961"
              }
            },
            "journal-title": {
              "value": "Nucl.Phys."
            },
            "country": null,
            "path": null,
            "short-description": null,
            "type": "JOURNAL_ARTICLE"
          }
        },
        
        {
          "work": {
            "language-code": null,
            "put-code": 991498185,
            "contributors": {
              "contributor": [
                {
                  "contributor-orcid": null,
                  "contributor-attributes": {
                    "contributor-role": "AUTHOR",
                    "contributor-sequence": "FIRST"
                  },
                  "credit-name": {
                    "value": "Glashow, S.L."
                  },
                  "contributor-email": null
                }
              ]
            },
            "title": {
              "translated-title": null,
              "subtitle": null,
              "title": {
                "value": "Partial Symmetries of Weak Interactions"
              }
            },
            "url": {
              "value": "http://labs.inspirehep.net/record/1498185"
            },
            "external-ids": {
              "external-id": [
                {
                  "external-id-value": "10.1016/0029-5582(61)90469-2",
                  "external-id-relationship": "SELF",
                  "external-id-url": {
                    "value": "http://dx.doi.org/10.1016/0029-5582(61)90469-2"
                  },
                  "external-id-type": "doi"
                }
              ]
            },
            "last-modified-date": {
              "value": 1519143190177
            },
            "citation": {
              "citation-type": "BIBTEX",
              "citation-value": ""
            },
            "created-date": {
              "value": 1516716146242
            },
            "visibility": "PUBLIC",
            "source": {
              "source-orcid": null,
              "source-name": {
                "value": "INSPIRE-PROFILE-PUSH"
              },
              "source-client-id": {
                "path": "CHANGE_ME",
                "host": "sandbox.orcid.org",
                "uri": "http://sandbox.orcid.org/client/CHANGE_ME"
              }
            },
            "publication-date": {
              "month": null,
              "day": null,
              "media-type": null,
              "year": {
                "value": "1961"
              }
            },
            "journal-title": {
              "value": "Nucl.Phys."
            },
            "country": null,
            "path": null,
            "short-description": null,
            "type": "JOURNAL_ARTICLE"
          }
        }

      ]
    }
"""


def create_putcodes_response(*args, **kwargs):
    return (
        200,
        _PUTCODES_RESPONSE.encode('utf8'),
        {
            'content-type': '[application/orcid+json; qs=2;charset=UTF-8]',
            # 'content-length': "['4774']",
        }
    )


def create_new_record_response(*args, **kwargs):
    recid = kwargs['recid']
    putcode = RECIDS_PUTCODES[recid]
    return (
        200,
        b'{"message": "ok"}',
        {
            'Content-Type': 'application/json',
            'location': 'http://api.sandbox.orcid.org/orcid-api-web/v2.0/0000-0002-1825-0097/work/{}'.format(putcode),
        }
    )


def create_200_response(*args, **kwargs):
    return (
        200,
        b'{"message": "ok"}',
        {
            'Content-Type': 'application/json',
        }
    )


def create_500_response(*args, **kwargs):
    return (
        500,
        b'500 Internal Server Error',
        {
            'Content-Type': 'text/plain; charset=utf-8',
        }
    )

_409_CONFLICT_RESPONSE = """{
    "response-code":409,
    "developer-message":"409 Conflict: You have already added this activity (matched by external identifiers.) If you are trying to edit the item, please use PUT instead of POST.",
    "user-message":"There was an error when updating the record. Please try again. If the error persists, please contact INSPIRE-HEP for assistance.",
    "error-code":9021,
    "more-info":"https://members.orcid.org/api/resources/troubleshooting"
}
"""


def create_409_response(*args, **kwargs):
    return (
        409,
        _409_CONFLICT_RESPONSE.encode('utf8'),
        {
            'content-type': '[application/orcid+json; qs=2;charset=UTF-8]',
        }
    )
