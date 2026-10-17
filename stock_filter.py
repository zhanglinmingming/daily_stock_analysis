import akshare as ak
import os

def get_filter_stocks():
    try:
        # 获取当日A股行情
        df = ak.stock_zh_a_spot_em()
        # 简单选股示例，你后面可以自己修改条件
        # 条件：成交额大于1亿，收盘价大于5元，小于50元
        df = df[
            (df["成交额"] > 100000)
            & (df["最新价"] > 5)
            & (df["最新价"] < 50)
        ]
        # 提取股票代码，转为逗号分隔字符串
        stock_codes = df["代码"].tolist()
        if len(stock_codes) == 0:
            return ""
        return ",".join(stock_codes)
    except Exception as e:
        print(f"选股异常：{e}")
        return ""

if __name__ == "__main__":
    # 判断今天是否交易日
    trade_date_df = ak.tool_trade_date_hist_sina()
    today_str = ak.get_recent_day()[0]
    if today_str not in trade_date_df["trade_date"].values:
        print("NOT_TRADE")
    else:
        res = get_filter_stocks()
        if res == "":
            print("")
        else:
            print(res)
