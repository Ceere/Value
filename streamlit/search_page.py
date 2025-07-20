import streamlit as st
import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))
from search_company import fuzzy_search_company

st.title("Value")

st.markdown("""
### 输入股票代码或名称进行搜索，目前仅支持A股、港股。
- A股：如 600519/ 招商银行
- 港股：如 00700 / 腾讯控股
- 美股：如 AAPL / apple （未来支持）
""")

# 创建输入框
stock_code_or_name = st.text_input(
    '请输入股票代码或名称',
    value='000001'
)

if st.button('查询'):
    company = fuzzy_search_company(stock_code_or_name)
    if company:
        company_df = pd.DataFrame(company)
        company_df["detail"] = [f"/detail?stock_code={code}" for code in company_df["code"]]
        st.data_editor(
            company_df,
            column_config={
                "detail": st.column_config.LinkColumn(display_text="详情"),
            },
            hide_index=True,
            disabled=True
        )
            
    else:
        st.warning("未找到相关股票信息，请检查输入的代码或名称是否正确。")



