from url_check_main import URL_Check
import json

url = "cricinfo.com"

urlcheckinst = URL_Check(url)
validity = urlcheckinst.url_verify()

result = {}
if validity:
    result[url] = f"The Given URL is Clean - {url}"
else:
    result[url] = f"The Given URL is Malware Affected - {url}"
print(json.dumps(result))
