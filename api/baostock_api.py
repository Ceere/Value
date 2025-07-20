import baostock as bs
import pandas as pd

class BaoStockDataReceiver:
    """用于接收和处理来自 baostock 接口的数据"""

    def __init__(self, retry=3):
        self.bs = bs
        self.is_login = False
        self._login(retry)

    def _login(self, retry):
        for _ in range(retry):
            try:
                login_result = self.bs.login()
                if login_result.error_code == '0':
                    self.is_login = True
                    return
                print(f"登录失败: {login_result.error_msg}")
            except Exception as e:
                print(f"登录异常: {e}")
        raise ConnectionError("登录失败，请检查网络或账号")

    def get_basic_info(self, stock_code):
        """获取股票的基本信息"""
        if not self.is_login:
            raise ConnectionError("请先登录 baostock")
        
        rs = self.bs.query_stock_basic(code=stock_code)
        if rs.error_code != '0':
            raise ValueError(f"查询基本信息失败: {rs.error_msg}")
        
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
            
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    def __del__(self):
        if self.is_login:
            try:
                self.bs.logout()
            except (ModuleNotFoundError, AttributeError):
                pass  # 忽略模块已卸载的错误