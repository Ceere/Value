from api.akshare_api import AkShareDataReceiver

AkShare_api = AkShareDataReceiver()

a_stock = AkShare_api.get_a_code_name()
hk_stock = AkShare_api.get_hk_code_name()
us_stock = AkShare_api.get_us_code_name()

a_stock.to_csv("data/stock_name/a_stock_name.csv", index=False, encoding="utf-8-sig")
hk_stock.to_csv("data/stock_name/hk_stock_name.csv", index=False, encoding="utf-8-sig")
us_stock.to_csv("data/stock_name/us_stock_name.csv", index=False, encoding="utf-8-sig")
