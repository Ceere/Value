import streamlit as st
import sys
from pathlib import Path
from hk_information import hk_stock_information

sys.path.append(str(Path(__file__).parent.parent))
from search_company import fuzzy_search_company

stock_code = st.query_params.get("stock_code", None)
company = fuzzy_search_company(stock_code)
for item in company:
    if item['code'] == stock_code:
        st.title(f"{item['name']} - ({item['code']}) - 港股")

hk_stock = hk_stock_information(stock_code)

basic_information = hk_stock.get_basic_info()
st.subheader("基本信息")
st.dataframe(basic_information)

st.subheader("资产负债表")
balance_sheet = hk_stock.get_hk_finance_sheet("资产负债表")
get_latest_financial_data = hk_stock.get_latest_financial_data(balance_sheet)
st.bar_chart(get_latest_financial_data,x="STD_ITEM_NAME", y="AMOUNT")

st.subheader("现金流量表")
cash_flow_sheet = hk_stock.get_hk_finance_sheet("现金流量表")
get_latest_financial_data = hk_stock.get_latest_financial_data(cash_flow_sheet)
st.bar_chart(get_latest_financial_data,x="STD_ITEM_NAME", y="AMOUNT")

st.subheader("利润表")
income_sheet = hk_stock.get_hk_finance_sheet("利润表")
get_latest_financial_data = hk_stock.get_latest_financial_data(income_sheet)
st.bar_chart(get_latest_financial_data,x="STD_ITEM_NAME", y="AMOUNT")



if st.button("返回搜索页面"):
   st.switch_page("search_page.py")