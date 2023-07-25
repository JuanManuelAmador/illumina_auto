import time
import yfinance as yf
from pages import yahoo_stock_page
import unittest
import math

class TestSelenium(unittest.TestCase):

    def test_API_WebData(self):

        finance= yahoo_stock_page.StockPage("AAPL")
        info_web_scrapping = finance.setData()
        APIinfo=yf.Ticker("AAPL")
        time.sleep(2)

        try:
            a=int(info_web_scrapping["market_cap"])
            b=int(APIinfo.info["marketCap"])
            self.assertLess(a-b,a/200)
            print("market cap matches")
        except AssertionError:
            print("market cap doesnt match",info_web_scrapping["market_cap"] + " not equal to "+ str(APIinfo.info["marketCap"]))

        try:
            self.assertEqual(float(info_web_scrapping["eps"]),float(APIinfo.info["trailingEps"]))
            print("eps matches")
        except AssertionError:
            print("eps doesnt match",info_web_scrapping["eps"] + " not equal to "+ str(APIinfo.info["trailingEps"]))

        if info_web_scrapping["dividend_yield"] != "N/A (N/A)":
            try:
                a=float(info_web_scrapping["dividend_yield"][6:10])/100
                self.assertEqual(a,float(APIinfo.info["dividendYield"]))
                print("dividend matches")
            except AssertionError:
                print("dividend doesnt match",info_web_scrapping["dividend_yield"] + " not equal to "+ str(APIinfo.info["dividendYield"]))

        try:
            self.assertEqual(math.trunc(float(info_web_scrapping["current_stock_price"])),math.trunc(float(APIinfo.info["currentPrice"])))
            print("current price matches")
        except AssertionError:
            print("current price doesnt match",info_web_scrapping["current_stock_price"] + " not equal to "+ str(APIinfo.info["currentPrice"]))

        try:
            self.assertEqual(math.trunc(float(info_web_scrapping["pe_ratio"])),math.trunc(float(APIinfo.info["trailingPE"])))
            print("PE ratio matches")
        except AssertionError:
            print("PE ratio doesnt match",info_web_scrapping["pe_ratio"] + " not equal to "+ str(APIinfo.info["trailingPE"]))

if __name__ == "__main__":
    unittest.main()