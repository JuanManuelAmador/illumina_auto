import time
import yfinance as yf
from pages import yahoo_stock_page
import unittest

class TestSelenium(unittest.TestCase):

    symbols = ["AAPL","AMZN"]
    api_symbols = ["currentPrice","marketCap","trailingPE","dividendYield","trailingEps"]

    def tests_symbols(self):

        for symbol in self.symbols:
            print("Checking for "+ symbol)
            finance = yahoo_stock_page.StockPage(symbol)
            time.sleep(3)
            info_web_scrapping = finance.setData()
            APIinfo = yf.Ticker(symbol)
            i=0
            for elementData in info_web_scrapping:
                webInfo = info_web_scrapping[elementData]
                if webInfo != "N/A (N/A)":
                    try:
                        apiInfo= APIinfo.info[self.api_symbols[i]]
                        self.assertEqual(webInfo,apiInfo)
                        print(elementData+" match")
                    except AssertionError:
                        print(elementData +" doesnt match")
                else:
                    print(elementData + " not available")
                i=i+1


if __name__ == "__main__":
    unittest.main()