# coding=utf-8

from driver import load_driver
from app import create_app
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    driver = load_driver()
    pool = ThreadPoolExecutor(max_workers=10)  # 数量为 10 的线程池
    app = create_app(driver, pool)

    app.run(host="127.0.0.1", port=9997, debug=False)

# terminal input > python main.py
# Chrome Access http://127.0.0.1:9997/login

# Chrome Access http://127.0.0.1:9997/buy?event=216934&ticketId=ad9528257d4e7a2446dba0bd1409b42f&ticketNum=1
# http://127.0.0.1:9997/buy
# ?event=216934
# &ticketId=ad9528257d4e7a2446dba0bd1409b42f
# &ticketNum=1
# &cron_time=2023 12 23 16 00 00
# &need_select=True
# &select_num=1
#
#
# event: url or click立即购票F12/Network/XHR/Response >> activityID
# ticketId: click立即购票F12/Network/XHR/Response >> ticketId
# ticketNum: 购票数量
# cron_time: 预定时间
# need_select: 是否需要选择观演人
# select_num: 观演人数
