from pprint import pprint
import requests

BASE_URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

sess = requests.Session()
sess.headers.update({'token': TOKEN})

response = sess.get(
    BASE_URL,
    params={
        'datasetid': 'PRECIP_HLY',
        'stationid': 'COOP:010957',
        'startdate': '1970-01-01',
        'enddate': '1970-12-31',
    },
    verify=False,
)

pprint(response.json())
