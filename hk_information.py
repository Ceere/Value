import akshare as ak
import pandas as pd

class hk_stock_information:
    """
    获取港股股票的资产负债表数据
    """

    def __init__(self, stock_code: str):
        self.stock_code = stock_code

    def get_basic_info(self):
        """
        获取港股股票的基本信息
        """
        try:
            basic_info_df = ak.stock_individual_basic_info_hk_xq(symbol=self.stock_code)
            if basic_info_df.empty:
                print(f"没有找到港股 {self.stock_code} 的基本信息")
                return None
            
            return basic_info_df
        
        except Exception as e:
            print(f"获取港股基本信息失败: {e}")
            return None
    
    def get_hk_finance_sheet(self, symbol: str = "资产负债表"):
        """获取港股股票的财务报表"""
        hk_finance_sheet_df = ak.stock_financial_hk_report_em(
                stock=self.stock_code,
                symbol=symbol,
                indicator="报告期"
        )
        print(hk_finance_sheet_df)
        return hk_finance_sheet_df
    
    def get_latest_financial_data(self, hk_finance_df: pd.DataFrame = None):
        """获取港股股票的最新财务数据"""
        hk_finance_sheet_data = sorted(hk_finance_df["REPORT_DATE"].unique())
        the_latest_date = hk_finance_sheet_data[-1]

        print(f"港股 {self.stock_code} 的最新财务数据日期：{the_latest_date}")

        latest_data = hk_finance_df[hk_finance_df["REPORT_DATE"] == the_latest_date]

        return latest_data
