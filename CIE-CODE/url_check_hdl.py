#########################################################################################
#
# url_check_hdl -
#   This is the python script which executes the url_check usecase using command line args
#
#  Revision History
#    * 1.0 - 5.28.21 - Karthik Babu Harichandra Babu - Initial version
#
#########################################################################################

from url_check_main import URL_Check
from optparse import OptionParser
import json

def url_check():
    parser = OptionParser('')
    parser.add_option("--url", type="string", default='google.com',
                      help="any url")

    (o, args) = parser.parse_args()
    url = o.url

    result = {}
    urlcheckinst = URL_Check(url)
    validity, url_failed = urlcheckinst.url_verify()
  
    if validity and not url_failed:
        result[url] = f"The Given URL is Clean - {url}"
    elif not validity and not url_failed:
        result[url] = f"The Given URL is Malware Affected - {url}"
    elif url_failed:
        result[url] = f"The Given URL is Not in Valid URL Format - {url}"

    print(json.dumps(result))
    return(json.dumps(result))

if __name__ == '__main__':
    url_check()
