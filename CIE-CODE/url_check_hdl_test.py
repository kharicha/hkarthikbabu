#########################################################################################
#
# url_check_hdl_test -
#   This is the python script which executes the url_check usecase using python unittest
#
#  Revision History
#    * 1.0 - 5.28.21 - Karthik Babu Harichandra Babu - Initial version
#
#########################################################################################

from url_check_main import URL_Check
from optparse import OptionParser
import json

def url_check(url):
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
