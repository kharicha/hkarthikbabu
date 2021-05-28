import unittest, json
from url_check_hdl_test import url_check

class Testurlcheck(unittest.TestCase):
    def test_url_clean(self):
        result = url_check("cafatc.com")
        res = json.loads(result)
        for k,v in res.items():
            self.assertEqual(v, "The Given URL is Clean - cafatc.com")
    def test_url_malware(self):
        result = url_check("foxionserl.com")
        res = json.loads(result)
        for k,v in res.items():
            self.assertEqual(v, "The Given URL is Malware Affected - foxionserl.com")
    def test_url_unknown(self):
        result = url_check("google.com")
        res = json.loads(result)
        for k,v in res.items():
            self.assertEqual(v, "The Given URL is Malware Affected - google.com")
    def test_url_wrong_format(self):
        result = url_check("google")
        res = json.loads(result)
        for k,v in res.items():
            self.assertEqual(v, "The Given URL is Not in Valid URL Format - google")
