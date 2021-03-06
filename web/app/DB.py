# coding:utf-8
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from DBUtils.PooledDB import PooledDB

import web.app.db_setting as db

sys.path.append("../..")
from entity.Strategy_account import Account


# connection = pymysql.connect("localhost", "root", "Quant123", "quantcoin", charset='utf8')

# connection = pymysql.connect("52.163.218.233", "root", "Quant123", "quantcoin", charset='utf8')
# connection = pymysql.connect("35.162.98.89", "root", "Quant123", "quantcoin", charset='utf8')


# connection = db.OPMysql.conn


class StrategyLog:
    strategy_log_id = 0
    strategy_id = 0
    start_date = ""
    end_date = ""
    init_balance = 0.0
    coin_category = 0
    creator = 0
    create_time = ""
    execution_result = ""
    strategy_name = ""
    final_margin = 0.0
    benchmark = 0.0
    max_drawdown = 0.0

    def __init__(self, strategy_log_id,
                 strategy_id,
                 start_date,
                 end_date,
                 init_balance,
                 coin_category,
                 creator,
                 create_time,
                 execution_result,
                 strategy_name,
                 final_margin,
                 benchmark,
                 max_drawdown):
        self.strategy_log_id = strategy_log_id
        self.strategy_id = strategy_id
        self.start_date = start_date
        self.end_date = end_date
        self.init_balance = init_balance
        self.coin_category = coin_category
        self.creator = creator
        self.create_time = create_time
        self.execution_result = execution_result
        self.strategy_name = strategy_name
        self.final_margin = final_margin
        self.benchmark = benchmark
        self.max_drawdown = max_drawdown

    def get_strategy_log_id(self):
        return self.strategy_log_id

    def get_strategy_id(self):
        return self.strategy_id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_init_balance(self):
        return self.init_balance

    def get_coin_category(self):
        return self.coin_category

    def get_creator(self):
        return self.creator

    def get_create_time(self):
        return self.create_time

    def get_execution_result(self):
        return self.execution_result

    def get_final_margin(self):
        return self.final_margin

    def get_strategy_name(self):
        return self.strategy_name

    def set_strategy_log_id(self, strategy_log_id):
        self.strategy_log_id = strategy_log_id

    def set_strategy_id(self, strategy_id):
        self.strategy_id = strategy_id

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_init_balance(self, init_balance):
        self.init_balance = init_balance

    def set_coin_category(self, coin_category):
        self.coin_category = coin_category

    def set_creator(self, creator):
        self.creator = creator

    def set_create_time(self, create_time):
        self.create_time = create_time

    def set_execution_result(self, execution_result):
        self.execution_result = execution_result

    def set_strategy_name(self, strategy_name):
        self.strategy_name = strategy_name

    def set_final_margin(self, final_margin):
        self.final_margin = final_margin


class StrategyConf:
    strategy_conf_id = 0
    creator = 0
    create_time = ""
    update_time = ""
    strategy_id = 0
    Strategy_conf_items = []

    def __init__(self, strategy_conf_id, creator, create_time, update_time, strategy_id, coin_category):
        self.strategy_conf_id = strategy_conf_id
        self.creator = creator
        self.create_time = create_time
        self.update_time = update_time
        self.strategy_id = strategy_id
        self.coin_category = coin_category

    def printAll(self):
        print(str(self.strategy_conf_id) + "|" + str(self.creator) + "|" + str(self.create_time) + "|" + str(
            self.update_time) + "|" + str(self.strategy_id) + "|" + self.coin_category)
        for item in self.get_Strategy_conf_items():
            item.printAll()

    def get_strategy_conf_id(self):
        return self.strategy_conf_id

    def get_creator(self):
        return self.creator

    def get_create_time(self):
        return self.create_time

    def get_update_time(self):
        return self.update_time

    def get_strategy_id(self):
        return self.strategy_id

    def get_coin_category(self):
        return self.coin_category

    def get_Strategy_conf_items(self):
        return self.Strategy_conf_items

    def set_strategy_conf_id(self, strategy_conf_id):
        self.strategy_conf_id = strategy_conf_id

    def set_creator(self, creator):
        self.creator = creator

    def set_create_time(self, create_time):
        self.create_time = create_time

    def set_update_time(self, update_time):
        self.update_time = update_time

    def set_strategy_id(self, strategy_id):
        self.strategy_id = strategy_id

    def set_coin_category(self, coin_category):
        self.coin_category = coin_category

    def set_Strategy_conf_items(self, Strategy_conf_items):
        self.Strategy_conf_items = Strategy_conf_items


class StrategyConfItem:
    strategy_conf_item_id = 0
    strategy_id = 0
    index_label = ""
    formular = ""
    price = 0.0
    direction = ""

    def __init__(self, strategy_conf_item_id, strategy_id, index_label, formular, price, direction):
        self.strategy_conf_item_id = strategy_conf_item_id
        self.strategy_id = strategy_id
        self.index_label = index_label
        self.formular = formular
        self.price = price
        self.direction = direction

    def printAll(self):
        print(str(self.strategy_conf_item_id))
        print(str(self.strategy_id))
        print(self.index_label)
        print(self.formular)
        print(str(self.price))
        print(self.direction)

    def get_strategy_conf_item_id(self):
        return self.strategy_conf_item_id

    def get_strategy_id(self):
        return self.strategy_id

    def get_index_label(self):
        return self.index_label

    def get_formular(self):
        return self.formular

    def get_price(self):
        return self.price

    def get_direction(self):
        return self.direction

    def set_strategy_conf_item_id(self, strategy_conf_item_id):
        self.strategy_conf_item_id = strategy_conf_item_id

    def set_strategy_id(self, strategy_id):
        self.strategy_id = strategy_id

    def set_index_label(self, index_label):
        self.index_label = index_label

    def set_formular(self, formular):
        self.formular = formular

    def set_price(self, price):
        self.price = price

    def set_direction(self, direction):
        self.direction = direction


class Strategy:
    strategy_id = 0
    strategy_name = ""
    description = ""
    create_time = ""
    update_time = ""
    loading_times = 0
    creator = 0
    script_url = ""
    peroid = 0
    method_name = ""
    coin_category = ""
    init_balance = 0
    start_time = ""
    end_time = ""
    last_run = ""
    run_times = 0
    strategy_conf_items = []
    duration = 0
    benchmar = 0.0
    drawdown = 0.0
    status = 0

    def __init__(self, strategy_id, strategy_name, description, create_time, update_time, loading_times, creator,
                 script_url, peroid, method_name, coin_category, init_balance, start_time, end_time, last_run,
                 run_times, duration,
                 benchmark,
                 drawdown, status):
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.description = description
        self.create_time = create_time
        self.update_time = update_time
        self.loading_times = loading_times
        self.creator = creator
        self.script_url = script_url
        self.peroid = peroid
        self.method_name = method_name
        self.coin_category = coin_category
        self.init_balance = init_balance
        self.start_time = start_time
        self.end_time = end_time
        self.last_run = last_run
        self.run_times = run_times
        self.duration = duration
        self.benchmark = benchmark
        self.drawdown = drawdown
        self.status = status

    def get_strategy_id(self):
        return self.strategy_id

    def get_strategy_name(self):
        return self.strategy_name

    def get_description(self):
        return self.description

    def get_create_time(self):
        return self.create_time

    def get_update_time(self):
        return self.update_time

    def get_loading_times(self):
        return self.loading_times

    def get_creator(self):
        return self.creator

    def get_script_url(self):
        return self.script_url

    def get_peroid(self):
        return self.peroid

    def get_strategy_conf_items(self):
        return self.strategy_conf_items

    def get_coin_category(self):
        return self.coin_category

    def get_init_balance(self):
        return self.init_balance

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_last_run(self):
        return self.last_run

    def get_run_times(self):
        return self.run_times

    def get_duration(self):
        return self.duration

    def get_benchmark(self):
        return self.benchmark

    def get_drawdown(self):
        return self.drawdown

    def get_status(self):
        return self.status

    def set_strategy_id(self, strategy_id):
        self.strategy_id = strategy_id

    def set_strategy_name(self, strategy_name):
        self.strategy_name = strategy_name

    def set_description(self, description):
        self.description = description

    def set_create_time(self, create_time):
        self.create_time = create_time

    def set_update_time(self, update_time):
        self.update_time = update_time

    def set_loading_times(self, loading_times):
        self.loading_times = loading_times

    def set_creator(self, creator):
        self.creator = creator

    def set_script_url(self, script_url):
        self.script_url = script_url

    def set_peroid(self, peroid):
        self.peroid = peroid

    def set_method_name(self, method_name):
        self.method_name = method_name

    def set_init_balance(self, init_balance):
        self.init_balance = init_balance

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_strategy_conf_items(self, strategy_conf_items):
        self.strategy_conf_items = strategy_conf_items

    def set_last_run(self, last_run):
        self.last_run = last_run

    def set_run_times(self, run_times):
        self.run_times = run_times

    def set_duration(self, duration):
        self.duration = duration

    def set_benchmark(self, benchmark):
        self.benchmark = benchmark

    def set_drawdown(self, drawdown):
        self.drawdown = drawdown

    def set_status(self, status):
        self.status = status


class StrategyAccount:
    strategy_account_id = 0
    strategy_log_id = 0
    current_cash_balance = 0.0
    current_coin_balance = 0.0
    cost = 0.0
    total_net_balance = 0.0
    current_net_value = 0.0
    current_total_margin_rate = 0.0
    current_margin_rate = 0.0
    current_position = 0.0
    signal = 0
    transaction_status = 0
    t = "'"
    open = 0.0
    close = 0.0
    high = 0.0
    low = 0.0

    def __init__(self, strategy_account_id,
                 strategy_log_id,
                 current_cash_balance,
                 current_coin_balance,
                 cost,
                 total_net_balance,
                 current_net_value,
                 current_total_margin_rate,
                 current_margin_rate,
                 current_position,
                 signal,
                 transaction_status,
                 t,
                 open,
                 close,
                 high,
                 low):
        self.strategy_account_id = strategy_account_id
        self.strategy_log_id = strategy_log_id
        self.current_cash_balance = current_cash_balance
        self.current_coin_balance = current_coin_balance
        self.cost = cost
        self.total_net_balance = total_net_balance
        self.current_net_value = current_net_value
        self.current_total_margin_rate = current_total_margin_rate
        self.current_margin_rate = current_margin_rate
        self.current_position = current_position
        self.signal = signal
        self.transaction_status = transaction_status
        self.t = t
        self.open = open
        self.close = close
        self.high = high
        self.low = low

    def get_strategy_account_id(self):
        return self.strategy_account_id

    def get_strategy_log_id(self):
        return self.strategy_log_id

    def get_current_cash_balance(self):
        return self.current_cash_balance

    def get_current_coin_balance(self):
        return self.current_coin_balance

    def get_cost(self):
        return self.cost

    def get_total_net_balance(self):
        return self.total_net_balance

    def get_current_net_value(self):
        return self.current_net_value

    def get_current_total_margin_rate(self):
        return self.current_total_margin_rate

    def get_current_margin_rate(self):
        return self.current_margin_rate

    def get_current_position(self):
        return self.current_position

    def get_signal(self):
        return self.signal

    def get_transaction_status(self):
        return self.transaction_status

    def get_t(self):
        return self.t

    def get_open(self):
        return self.open

    def get_close(self):
        return self.close

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low


class StrategyTransaction:
    strategy_transaction_id = 0
    strategy_account_id = 0
    t = ""
    cost = 0.0
    volumn = 0.0
    commission = 0.0
    pre_position = 0.0
    post_position = 0.0
    position_gap = 0.0
    pre_balance = 0.0
    post_balance = 0.0
    balance_gap = 0.0

    def __init__(self, strategy_account_id,
                 strategy_log_id,
                 current_cash_balance,
                 current_coin_balance,
                 cost,
                 total_net_balance,
                 current_net_value,
                 current_total_margin_rate,
                 current_margin_rate,
                 current_position,
                 signal,
                 transaction_status,
                 t,
                 open,
                 close,
                 high,
                 low):
        self.strategy_account_id = strategy_account_id
        self.strategy_log_id = strategy_log_id
        self.current_cash_balance = strategy_log_id
        self.current_coin_balance = current_coin_balance
        self.cost = cost
        self.total_net_balance = total_net_balance
        self.current_net_value = current_net_value
        self.current_total_margin_rate = current_total_margin_rate
        self.current_margin_rate = current_margin_rate
        self.current_position = current_position
        self.signal = signal
        self.transaction_status = transaction_status
        self.t = t
        self.open = open
        self.close = close
        self.high = high
        self.low = low

    def get_strategy_account_id(self):
        return self.strategy_account_id

    def get_strategy_log_id(self):
        return self.strategy_log_id

    def get_current_cash_balance(self):
        return self.current_cash_balance

    def get_current_coin_balance(self):
        return self.current_coin_balance

    def get_cost(self):
        return self.cost

    def get_total_net_balance(self):
        return self.total_net_balance

    def get_current_net_value(self):
        return self.current_net_value

    def get_current_total_margin_rate(self):
        return self.current_total_margin_rate

    def get_current_margin_rate(self):
        return self.current_margin_rate

    def get_current_position(self):
        return self.current_position

    def get_signal(self):
        return self.signal

    def get_transaction_status(self):
        return self.transaction_status

    def get_t(self):
        return self.t

    def get_open(self):
        return self.open

    def get_close(self):
        return self.close

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def set_strategy_account_id(self, strategy_account_id):
        self.strategy_account_id = strategy_account_id

    def set_strategy_log_id(self, strategy_log_id):
        self.strategy_log_id = strategy_log_id

    def set_current_cash_balance(self, current_cash_balance):
        self.current_cash_balance = current_cash_balance

    def set_current_coin_balance(self, current_coin_balance):
        self.current_coin_balance = current_coin_balance

    def set_cost(self, cost):
        self.cost = cost

    def set_total_net_balance(self, total_net_balance):
        self.total_net_balance = total_net_balance

    def set_current_net_value(self, current_net_value):
        self.current_net_value = current_net_value

    def set_current_total_margin_rate(self, current_total_margin_rate):
        self.current_total_margin_rate = current_total_margin_rate

    def set_current_margin_rate(self, current_margin_rate):
        self.current_margin_rate = current_margin_rate

    def set_current_position(self, current_position):
        self.current_position = current_position

    def set_signal(self, signal):
        self.signal = signal

    def set_transaction_status(self, transaction_status):
        self.transaction_status = transaction_status

    def set_t(self, t):
        self.t = t

    def set_open(self, open):
        self.open = open

    def set_close(self, close):
        self.close = close

    def set_high(self, high):
        self.high = high

    def set_low(self, low):
        self.low = low


class TradeHistory:
    t = 0
    signal = 0
    pre_position = 0
    post_position = 0
    pre_balance = 0
    post_balance = 0
    transaction_status = 0

    def __init__(self, t, signal, pre_position, post_position, pre_balance, post_balance, transaction_status):
        self.t = t
        self.signal = signal
        self.pre_position = pre_position
        self.post_position = post_position
        self.pre_balance = pre_balance
        self.post_balance = post_balance
        self.transaction_status = transaction_status

    def get_trade_history_t(self):
        return self.t

    def get_trade_history_signal(self):
        return self.signal

    def get_trade_history_pre_position(self):
        return self.pre_position

    def get_trade_hisoty_post_position(self):
        return self.post_position

    def get_trade_history_pre_balance(self):
        return self.pre_balance

    def get_trade_history_post_balance(self):
        return self.post_balance

    def get_trade_history_transaction_status(self):
        return self.transaction_status


class User:
    user_id = 0
    phone = 0
    password = 0
    nick_name = ""
    open_id = ''
    age = 0
    gender = 0
    avator = ''
    levels = 0
    strategy_amount = 0
    history_amount = 0
    style = 0
    experience = 0

    def __init__(self, user_id,
                 phone,
                 password,
                 nick_name,
                 open_id,
                 age,
                 gender,
                 avator,
                 levels,
                 strategy_amount,
                 history_amount,
                 style,
                 experience):
        self.user_id = user_id
        self.phone = phone
        self.password = password
        self.nick_name = nick_name
        self.open_id = open_id
        self.age = age
        self.gender = gender
        self.avator = avator
        self.levels = levels
        self.strategy_amount = strategy_amount
        self.history_amount = history_amount
        self.style = style
        self.experience = experience


class UserByPhone:
    user_id = 0
    phone = 0
    password = 0
    nick_name = ""
    open_id = ''
    age = 0
    gender = 0
    avator = ''
    levels = 0
    style = 0
    experience = 0

    def __init__(self, user_id,
                 phone,
                 password,
                 nick_name,
                 open_id,
                 age,
                 gender,
                 avator,
                 levels,
                 style,
                 experience):
        self.user_id = user_id
        self.phone = phone
        self.password = password
        self.nick_name = nick_name
        self.open_id = open_id
        self.age = age
        self.gender = gender
        self.avator = avator
        self.levels = levels
        self.style = style
        self.experience = experience


# 用于myStrategy查询接口
class MyStrategy:
    strategy_id = 0
    strategy_name = ""
    create_time = ""
    run_times = 0

    def __init__(self, strategy_id, strategy_name, create_time, run_times):
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.create_time = create_time
        self.run_times = run_times


def getALLStrategy(creator):
    strategyList = []
    # SQL 查询语句
    sql = "SELECT strategy_id," \
          " strategy_name," \
          " description," \
          " create_time," \
          " update_time," \
          " loading_times," \
          " creator," \
          " script_url," \
          " peroid," \
          " method_name," \
          " coin_category, " \
          " init_balance," \
          " start_time," \
          " end_time," \
          " (select create_time from strategy_log sl where sl.strategy_id=s.strategy_id order by create_time desc limit 1) last_run," \
          " (select count(1) from strategy_log sl where sl.strategy_id=s.strategy_id) run_times," \
          " duration,benchmark,drawdown,status FROM strategy s" \
          " where creator=%s and del_flag = 0"

    # 执行SQL语句
    # 获取所有记录列表
    results = db.fetch_db_with_param(sql, creator)
    for row in results:
        # 打印结果
        strategy = Strategy(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                            row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
        strategyList.append(strategy)
    return strategyList


def getStrategyDetail(creator, strategy_id):
    # SQL 查询语句
    sql = "SELECT strategy_id," \
          " strategy_name," \
          " description," \
          " create_time," \
          " update_time," \
          " loading_times," \
          " creator," \
          " script_url," \
          " peroid," \
          " method_name," \
          " coin_category, " \
          " init_balance," \
          " start_time," \
          " end_time," \
          " (select create_time from strategy_log sl where sl.strategy_id=s.strategy_id order by create_time desc limit 1) last_run," \
          " (select count(1) from strategy_log sl where sl.strategy_id=s.strategy_id) run_times," \
          " duration,benchmark,drawdown,status FROM strategy s" \
          " where creator=%s and strategy_id = %s "

    # 执行SQL语句
    param = (creator, strategy_id)
    rows = db.fetch_db_with_param(sql, param)
    # 获取所有记录列表
    row = rows[0]
    strategy = Strategy(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
    return strategy


def getStrategyLogList(creator):
    strategyLogList = []
    # SQL 查询语句
    sql = " SELECT strategy_log_id," \
          " strategy_id," \
          " start_date," \
          " end_date," \
          " init_balance," \
          " coin_category," \
          " creator," \
          " create_time," \
          " execution_result," \
          " (select strategy_name from strategy where strategy.strategy_id = strategy_log.strategy_id) strategy_name," \
          " final_margin," \
          " benchmark,max_drawdown " \
          " FROM strategy_log" \
          " where creator=%s and del_flag = 0 " \
          " order by create_time desc "

    # print(sql)
    # 执行SQL语句
    results = db.fetch_db_with_param(sql, creator)
    # 获取所有记录列表
    for row in results:
        # 打印结果
        pro = StrategyLog(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                          row[11], row[12])
        # print("row[0]:"+str(row[0])+"|row[a]:"+row[a]+"|row[b]:"+str(row[b])+"|row[3]:"+str(row[3])+"|row[4]:"+row[4]+"|row[5]:"+str(row[5])+"|row[6]:"+row[6]+"|row[7]:"+str(row[7]))
        strategyLogList.append(pro)
    return strategyLogList


def getStrategyLogsByStrategyId(creator, strategy_id):
    strategyLogList = []
    # SQL 查询语句
    sql = " SELECT strategy_log_id," \
          " strategy_id," \
          " start_date," \
          " end_date," \
          " init_balance," \
          " coin_category," \
          " creator," \
          " create_time," \
          " execution_result," \
          " (select strategy_name from strategy where strategy.strategy_id = strategy_log.strategy_id) strategy_name," \
          " final_margin ," \
          " benchmark,max_drawdown " \
          " FROM strategy_log" \
          " where creator=%s and strategy_id =%s and del_flag = 0 " \
          " order by create_time desc"

    # 执行SQL语句
    param = (creator, strategy_id)
    # print(sql)
    results = db.fetch_db_with_param(sql, param)
    for row in results:
        # 打印结果
        pro = StrategyLog(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                          row[11], row[12])
        # print("row[0]:"+str(row[0])+"|row[a]:"+row[a]+"|row[b]:"+str(row[b])+"|row[3]:"+str(row[3])+"|row[4]:"+row[4]+"|row[5]:"+str(row[5])+"|row[6]:"+row[6]+"|row[7]:"+str(row[7]))
        strategyLogList.append(pro)
    return strategyLogList


def getLogDetail(strategyLogId, creator):
    log_details = []
    #   SQL 查询语句
    sql = " SELECT strategy_log_id," \
          " strategy_id," \
          " start_date," \
          " end_date," \
          " init_balance," \
          " coin_category," \
          " creator," \
          " create_time," \
          " execution_result, " \
          " (select strategy_name from strategy where strategy.strategy_id = strategy_log.strategy_id) strategy_name," \
          " final_margin," \
          " benchmark,max_drawdown" \
          " FROM strategy_log" \
          " where del_flag = 0 and  strategy_log_id=%s and creator=%s" % (strategyLogId, creator)

    # 执行SQL 语句
    results = db.fetch_db(sql)
    row = results[0]
    log_details = StrategyLog(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                              row[7], row[8], row[9], row[10], row[11], row[12])
    return log_details


# def getStrategyAccountList(strategyLogId):
#     cursor = connection.cursor()
#     strategyAccountList = []
#     # SQL 查询语句
#     sql = " SELECT strategy_account_id,strategy_log_id,current_cash_balance,current_coin_balance,cost,total_net_balance,current_net_value," \
#           " current_total_margin_rate,current_margin_rate,current_position,`signal`,transaction_status,t,open,close,high,low FROM strategy_account where strategy_log_id = %s"
#
#     # 执行SQL语句
#     cursor.execute(sql, strategyLogId)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         # 打印结果
#         pro = StrategyAccount(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
#                               row[11], row[12], row[13], row[14], row[15], row[16])
#         strategyAccountList.append(pro)
#     cursor.close()
#     return strategyAccountList


def getStrategyAccountList(strategyLogId):
    # engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4',
    #                        max_overflow=0,  # 超过连接池大小外最多创建的连接
    #                        pool_size=50,  # 连接池大小
    #                        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    #                        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    #                        )
    engine = create_engine('mysql+pymysql://root:Quant123@localhost:3306/quantcoin?charset=utf8MB4',
                           max_overflow=0,  # 超过连接池大小外最多创建的连接
                           pool_size=50,  # 连接池大小
                           pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                           pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                           )
    SessionFactory = sessionmaker(bind=engine)
    session = SessionFactory()
    strategyAccountList = []
    results = session.query(Account).filter(Account.strategy_log_id == strategyLogId).all()
    for row in results:
        # 打印结果
        strategyAccountList.append(row)
    session.close()
    return strategyAccountList


def getStrategy(userId, strategyId):
    strategyList = []
    # SQL 查询语句
    sql = " SELECT strategy_id," \
          " strategy_name," \
          " description," \
          " create_time," \
          " update_time," \
          " loading_times," \
          " creator," \
          " script_url," \
          " peroid," \
          " method_name," \
          " coin_category,  " \
          " init_balance," \
          " start_time," \
          " end_time," \
          " (select create_time from strategy_log sl where sl.strategy_id=s.strategy_id order by create_time desc limit 1) last_run," \
          " (select count(1) from strategy_log sl where sl.strategy_id=s.strategy_id) run_times," \
          " duration,benchmark,drawdown,status" \
          " FROM strategy s where creator=%s and strategy_id=%s and del_flag = 0 "

    # 执行SQL语句
    param = (userId, strategyId)
    rows = db.fetch_db_with_param(sql, param)
    # 获取所有记录列表
    # 打印结果
    row = rows[0]
    strategy = Strategy(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
    # print(strategy)
    strategy.set_strategy_conf_items(getStrategyConfItem(row[0]))
    # strategyConf.printAll()
    return strategy


def getStrategyConfItem(strategy_id):
    strategyConfItemList = []
    # SQL 查询语句
    sql = " SELECT strategy_conf_item_id,strategy_id,index_label,formular,price,direction" \
          " FROM strategy_conf_item where strategy_id=%s"

    # 执行SQL语句
    param = (strategy_id)
    results = db.fetch_db_with_param(sql, param)
    # 获取所有记录列表
    for row in results:
        # 打印结果
        item = StrategyConfItem(row[0], row[1], row[2], row[3], row[4], row[5])

        strategyConfItemList.append(item)
    return strategyConfItemList


def saveStrategy(strategy_name, creator, coin_category, init_balance, start_time, end_time):
    strategyConfList = []
    # SQL 查询语句
    sql = " INSERT INTO strategy(strategy_name,creator, coin_category,init_balance,start_time,end_time)VALUES(%s,%s,%s,%s,%s, %s);"
    param = (strategy_name, creator, coin_category, init_balance, start_time, end_time)
    strategy_id = db.update_db_with_params(sql, param)
    return strategy_id


# 保存策略名称
def saveStrategyName(strategy_id, strategy_name, creator):
    strategyConfList = []
    # SQL 查询语句
    sql = " update strategy set strategy_name=%s where strategy_id=%s and creator=%s"
    param = (strategy_name, strategy_id, creator)
    db.update_db_with_params(param)


def checkStrategyName(strategy_name, creator):
    strategyConfList = []
    # SQL 查询语句
    sql = " select * from strategy where strategy_name=%s and creator=%s"
    param = (strategy_name, creator)
    results = db.fetch_db_with_param(sql, param)
    if (len(results) > 0):
        return True
    else:
        return False


def checkPreviousStrategyName(strategy_id, creator, strategy_name):
    # sql 查询语句
    sql = "select strategy_name from strategy where strategy_id=%s and creator=%s"
    params = (strategy_id, creator)
    while True:
        result = db.fetch_db_with_param(sql, params)
        if result == None:
            break
        if result[0][0] == strategy_name:
            return True
        else:
            return False


def saveStrategyConfItem(strategy_id, index_label, formular, price, direction):
    strategyConfList = []

    # SQL 查询语句  添加数据
    sql = " INSERT INTO strategy_conf_item(strategy_id,index_label,formular,price, direction)VALUES(%s,%s,%s,%s, %s);"
    param = (strategy_id, index_label, formular, price, direction)
    db.update_db_with_params(sql, param)


#
# def deleteStrategyById(strategy_id):
#     cursor = connection.cursor()
#     strategyConfList = []
#     # SQL 查询语句
#     sql = " delete from strategy_conf_item where strategy_id=%s;"
#     param = (strategy_id)
#     cursor.execute(sql, param)
#     sql = " delete from strategy_account where strategy_log_id in " \
#           "       (select strategy_log_id from strategy_log where strategy_id=%s);"
#     param = (strategy_id)
#     cursor.execute(sql, param)
#     sql = " delete from strategy_log where strategy_id=%s;"
#     param = (strategy_id)
#     cursor.execute(sql, param)
#     sql = " delete from strategy where strategy_id=%s;"
#     param = (strategy_id)
#     cursor.execute(sql, param)
#     connection.commit()


def deleteStrategyById(strategy_id, userId):
    # sql 查询语句
    sql = " update strategy set del_flag = 1 where strategy_id=%s and creator = %s"
    param = (strategy_id, userId)
    db.update_db_with_params(sql, param)


# 删除 指定 strategy_log
def deleteStrategyLogById(strategy_log_id):
    # SQL 查询语句
    # sql = " delete from strategy_log where strategy_log_id = %s;"
    sql = "update strategy_log set del_flag = 1 where strategy_log_id = %s; "
    param = (strategy_log_id)
    db.update_db_with_params(sql, param)


# 更新策略
def updateStrategy(strategy_id, strategy_name, creator, coin_category, init_balance, start_time, end_time):
    # param = (strategy_name, creator)
    # cursor.execute(sql, param)
    # results = cursor.fetchall()
    strategyConfList = []
    # SQL update 语句
    sql = "update strategy set strategy_name=%s, coin_category = %s, init_balance = %s, start_time= %s, end_time = %s " \
          " where strategy_id = %s and creator = %s "
    param = (strategy_name, coin_category, init_balance, start_time, end_time, strategy_id, creator)
    db.update_db_with_params(sql, param)
    # cursor.execute('SELECT LAST_INSERT_ID();')
    # strategy_id = cursor.fetchone()

    return strategy_id


# 更新策略 conf
def updateStrategyConf(strategy_id):
    strategyConfList = []
    #  首先删除 之前配置的conf
    sql = "delete from strategy_conf_item where strategy_id= %s "
    db.update_db_with_params(sql, strategy_id)
    # strategy_id = cursor.fetchone()
    return strategy_id


def mob_updateStrategy(strategy_id, userId, coin_category, init_balance, start_time, end_time):
    sql = "update strategy set  coin_category = %s, init_balance = %s, start_time= %s, end_time = %s" \
          " where strategy_id = %s and creator = %s "

    params = (coin_category, init_balance, start_time, end_time, strategy_id, userId)
    db.update_db_with_params(sql, params)


def insertStrategyLog(strategy_id, userId, coin_category, init_balance, start_time, end_time):
    sql = "insert into strategy_log(strategy_id, start_date, end_date, init_balance, coin_category,creator, create_time ) " \
          " values(%s, %s, %s, %s, %s, %s, now()); "

    params = (strategy_id, start_time, end_time, init_balance, coin_category, userId)
    strategy_log_id = db.update_db_with_params(sql, params)
    return strategy_log_id


def mob_trade_history(strategy_log_id):
    trade_historys = []
    sql = "select st.t, st.flag, " \
          "st.pre_position,  " \
          "st.post_position, " \
          "st.pre_balance," \
          "st.post_balance," \
          "st.flag from strategy_log sl " \
          "inner join strategy s on sl.strategy_id = s.strategy_id " \
          "inner join  strategy_account sa on sl.strategy_log_id = sa.strategy_log_id " \
          "inner join strategy_transaction  st on sa.strategy_account_id = st.strategy_account_id " \
          "where  sl.strategy_log_id = %s;"

    params = (strategy_log_id)
    results = db.fetch_db_with_param(sql, params)

    for item in results:
        trade_history = TradeHistory(item[0], item[1], item[2], item[3], item[4], item[5], item[6])

        trade_historys.append(trade_history)
    return trade_historys


def mob_my_strategy_list(creator):
    my_strategy_list = []
    sql0 = "CREATE OR REPLACE VIEW MY_STRATEGY_LIST AS " \
           "SELECT s.strategy_id, s.strategy_name, sl.create_time from strategy s " \
           "inner join strategy_log sl on sl.strategy_id = s.strategy_id " \
           "where s.creator = %s " \
           "order by sl.create_time desc; "

    sql1 = "select strategy_id,strategy_name,max(create_time),count(create_time)" \
           " from MY_STRATEGY_LIST  " \
           "group by strategy_id;"

    sql2 = "DROP VIEW MY_STRATEGY_LIST"
    params = (creator)
    db.fetch_db_with_param(sql0, params)
    results = db.fetch_db(sql1)
    db.update_db(sql2)

    for item in results:
        strategy = MyStrategy(strategy_id=item[0], strategy_name=item[1], create_time=item[2], run_times=item[3])
        my_strategy_list.append(strategy)
    return my_strategy_list


def getUser(user_id):
    UserList = []
    # SQL 查询语句
    sql = "SELECT u.user_id,u.phone,u.password,u.nick_name,u.open_id,u.age,u.gender," \
          "u.avator,u.levels," \
          "(SELECT COUNT(s.strategy_id) FROM strategy s WHERE s.creator = u.user_id and s.del_flag = 0) strategy_amount," \
          "(SELECT COUNT(sl.strategy_log_id) FROM strategy_log sl WHERE sl.creator = u.user_id and sl.del_flag = 0) history_amount," \
          "style,experience FROM user_info u WHERE u.user_id = %s"

    # 执行SQL语句
    param = (user_id)
    results = db.fetch_db_with_param(sql, param)
    for row in results:
        # 打印结果
        item = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12])

        UserList.append(item)
    return UserList


def getUserByPhone(phone):
    UserList = []
    # SQL 查询语句
    sql = "SELECT u.user_id,u.phone,u.password,u.nick_name,u.open_id,u.age,u.gender," \
          "u.avator,u.levels," \
          "style,experience FROM user_info u WHERE u.phone = %s"

    # 执行SQL语句
    param = (phone)
    results = db.fetch_db_with_param(sql, param)
    for row in results:
        # 打印结果
        item = UserByPhone(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

        UserList.append(item)
    return UserList


def saveUserItem(phone, password, nick_name, open_id, age, gender, avator, levels,
                 strategy_amount, history_amount, style, experience):
    strategyConfList = []
    # SQL  添加数据
    sql = "INSERT INTO user_info(phone,password,nick_name,open_id,age,gender,avator,levels," \
          "strategy_amount,history_amount,style,experience)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    param = (phone, password, nick_name, open_id, age, gender, avator, levels,
             strategy_amount, history_amount, style, experience)
    db.update_db_with_params(sql, param)


# 修改用户密码
def update_user_pwd(user_id, new_pwd):
    # SQL update 语句
    sql = "update user_info set password=%s" \
          " where user_id = %s"
    param = (new_pwd, user_id)
    db.update_db_with_params(sql, param)


# 修改用户密码
def update_user_phone_num(phone, user_id):
    # SQL update 语句
    sql = "update user_info set phone=%s" \
          " where user_id = %s"
    param = (phone, user_id)
    db.update_db_with_params(sql, param)


# 修改用户信息
def update_user_info(user_id, nick_name, open_id, age, gender, avator, style, experience):
    # SQL update 语句
    sql = "update user_info set nick_name=%s,open_id=%s,age=%s,gender=%s," \
          "avator=%s,style=%s,experience=%s" \
          " where user_id = %s"
    param = (nick_name, open_id, age, gender, avator, style, experience, user_id)
    db.update_db_with_params(sql, param)


def mob_get_strategy_log_list(strategy_id, creator):
    strategy_logs = []
    sql = "select sl.create_time,s.strategy_name, " \
          "sl.final_margin, sl.strategy_log_id," \
          "sl.benchmark,sl.start_date,sl.end_date,sl.max_drawdown " \
          "from strategy_log sl " \
          "inner join strategy s on sl.strategy_id = s.strategy_id " \
          "where  sl.strategy_id = %s  and s.creator = %s " \
          "order by sl.create_time desc ;"

    params = (strategy_id, creator)
    results = db.fetch_db_with_param(sql, params)

    for item in results:
        strategy_log = StrategyLog(strategy_log_id=item[3],
                                   create_time=item[0], strategy_name=item[1],
                                   final_margin=item[2], benchmark=item[4],
                                   strategy_id=strategy_id, start_date=item[5], end_date=item[6], creator=creator,
                                   coin_category=None, execution_result=None, init_balance=None, max_drawdown=item[7])
        strategy_logs.append(strategy_log)
    return strategy_logs


def get_all_strategy_name(creator):
    strategy_name_list = []

    sql = " SELECT strategy_name FROM strategy where  del_flag = 0  and creator = %s  " \
          " order by strategy_name asc "

    params = (creator)
    results = db.fetch_db_with_param(sql, params)

    for item in results:
        strategy_name_list.append(item[0])

    return strategy_name_list


def get_strategy_profit_list(strategy_log_id):
    strategy_profit_list = []

    sql = " SELECT current_total_margin_rate FROM strategy_account where  strategy_log_id = %s  " \
          " order by strategy_account_id asc "

    params = (strategy_log_id)
    results = db.fetch_db_with_param(sql, params)

    for item in results:
        strategy_profit_list.append(item[0])

    return strategy_profit_list
