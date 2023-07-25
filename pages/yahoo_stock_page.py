from selenium.webdriver.common.by import By
from selenium import webdriver

class StockPage:

    dictionary ={
        "current_stock_price": "",
        "market_cap":"",
        "pe_ratio": "",
        "dividend_yield": "",
        "eps": "",
    }
    current_stock_price="//*[@id='quote-header-info']/div[3]/div[1]/div[1]/fin-streamer[1]"
    market_cap= "//*[@id='quote-summary']/div[2]/table/tbody/tr[1]/td[2]"
    pe_ratio= "//*[@id='quote-summary']/div[2]/table/tbody/tr[3]/td[2]"
    dividend_yield= "//*[@id='quote-summary']/div[2]/table/tbody/tr[6]/td[2]"
    eps= "//*[@id='quote-summary']/div[2]/table/tbody/tr[4]/td[2]"

    def __init__(self,stock):
        self.url = "https://finance.yahoo.com/quote/" + stock
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)

    def get_url(self):
        return self.url

    def getDict(self):
        return self.dictionary

    def convertMarketCap(self,string):

        if string[-1]=="T":
            return str(int(float(string[0:len(string)-1])*1000000000000))

        if string[-1]=="B":
            return str(int(float(string[0:len(string) - 1]) * 1000000000))

        else:
            return string

    def setData(self):
        market_cap = self.driver.find_element(By.XPATH,self.market_cap)
        market_cap=self.convertMarketCap(market_cap.text)
        self.dictionary["market_cap"]=market_cap

        current_stock_price = self.driver.find_element(By.XPATH, self.current_stock_price)
        self.dictionary["current_stock_price"] = current_stock_price.text

        pe_ratio = self.driver.find_element(By.XPATH, self.pe_ratio)
        self.dictionary["pe_ratio"] = pe_ratio.text

        dividend_yield = self.driver.find_element(By.XPATH, self.dividend_yield)
        self.dictionary["dividend_yield"] = dividend_yield.text

        eps = self.driver.find_element(By.XPATH, self.eps)
        self.dictionary["eps"] = eps.text

        return self.dictionary





