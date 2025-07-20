from api.baostock_api import BaoStockDataReceiver
from api.akshare_api import AkShareDataReceiver
import pandas as pd
from typing import List, Dict  

def load_all_stock_data_to_list():

    stock_data = {
        "a_stock": [],
        "hk_stock": [],
        "us_stock": []
    }

    try:
        # 读取A股数据
        df_a = pd.read_csv("data/stock_name/a_stock_name.csv", encoding='utf_8_sig', dtype=str, keep_default_na=False)
        stock_data["a_stock"] = df_a.to_dict('records')  # 转换为字典列表

        # 读取港股数据
        df_hk = pd.read_csv("data/stock_name/hk_stock_name.csv", encoding='utf_8_sig', dtype=str, keep_default_na=False)
        stock_data["hk_stock"] = df_hk.to_dict('records')

        # 读取美股数据
        df_us = pd.read_csv("data/stock_name/us_stock_name.csv", encoding='utf_8_sig', dtype=str, keep_default_na=False)
        stock_data["us_stock"] = df_us.to_dict('records')
        print("所有股票数据已加载到列表中")
        return stock_data

    except Exception as e:
        print(f"读取文件失败: {e}")
        return None

def fuzzy_search_company(name_part: str) -> List[Dict[str, str]]:
    """
    模糊匹配公司名称并返回匹配结果
    
    参数:
        name_part: 要搜索的公司名称部分
        data_list: 包含公司信息的字典列表
        
    返回:
        匹配结果的列表，每个结果包含公司名称和代码/代号
    """
    matches = []
    name_part = name_part.lower().strip()
    data_list = load_all_stock_data_to_list()
    
    for company in data_list["a_stock"]:
        if name_part in company['code'] or name_part in company['name'].lower():
            matches.append({
                'name': company['name'],
                'code': company['code'],
                'type': 'A股'
            })
    
    
    for company in data_list["hk_stock"]:
        if name_part in company['中文名称'].lower() or name_part in company['代码'] or name_part in company['英文名称'].lower():
            matches.append({
                'name': company['中文名称'],
                'code': company['代码'],
                'type': '港股'
            })
    
    for company in data_list["us_stock"]:
        if name_part in company['name'].lower() or name_part in company['cname'].lower() or name_part in company['symbol'].lower():
            matches.append({
                'name': company['name'],
                'code': company['symbol'],
                'type': '美股'
            })
    
    return matches