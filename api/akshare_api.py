import akshare as ak
import pandas as pd

class AkShareDataReceiver:
    """用于接收和处理来自 AkShare 接口的数据"""

    def __init__(self, retry=3):
        self.retry = retry

    def get_a_code_name(self):
        """获取A股代码和名称"""
        stock_a_df = ak.stock_info_a_code_name()
        return stock_a_df
    
    def get_hk_code_name(self):
        """获取港股代码和名称等数据"""
        stock_hk_df = ak.stock_hk_spot()
        return stock_hk_df
    
    def get_us_code_name(self):
        """获取美股代码和名称等数据"""
        stock_us_df = ak.get_us_stock_name()
        return stock_us_df


    def get_basic_info(self, stock_code):
        """获取股票的基本信息"""
        stock_individual_basic_info_xq_df = ak.stock_individual_basic_info_xq(stock_code)
        return stock_individual_basic_info_xq_df
    
    def get_balance_sheet(self, stock_code):
        """获取A股股票的资产负债表"""
        balance_sheet_df = ak.stock_financial_debt_ths(symbol=stock_code)
        return balance_sheet_df

    def get_benefit_sheet(self, stock_code):
        """获取A股股票的利润表"""
        benefit_sheet_df = ak.stock_financial_benefit_ths(symbol=stock_code)
        return benefit_sheet_df
    
    def get_cash_sheet(self, stock_code):
        """获取A股股票的利润表"""
        cash_sheet_df = ak.stock_financial_cash_ths(symbol=stock_code)
        return cash_sheet_df
    
    def get_hk_finance_sheet(self, stock_code, symbol, indicator):
        """获取港股股票的财务报表"""
        hk_finance_sheet_df = ak.stock_financial_hk_report_em(stock_code, symbol,  indicator)
        return hk_finance_sheet_df