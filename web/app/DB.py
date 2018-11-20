import pymysql

#connection = pymysql.connect("localhost", "root", "root", "quant_coin", charset='utf8')
connection = pymysql.connect("35.162.98.89", "root", "Quant123", "quantcoin", charset='utf8')


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
                 final_margin):
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
    init_balance = 0
    start_time = ""
    end_time = ""
    last_run = ""
    run_times = 0
    strategy_conf_items = []
    duration = 0
    benchmar = 0.0
    drawdown = 0.0
    def __init__(self, strategy_id, strategy_name, description, create_time, update_time, loading_times, creator,
                 script_url, peroid,init_balance,start_time,end_time,last_run,run_times,duration,benchmark,drawdown):
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.description = description
        self.create_time = create_time
        self.update_time = update_time
        self.loading_times = loading_times
        self.creator = creator
        self.script_url = script_url
        self.peroid = peroid
        self.init_balance = init_balance
        self.start_time = start_time
        self.end_time = end_time
        self.last_run = last_run
        self.run_times = run_times
        self.duration = duration
        self.benchmark = benchmark
        self.drawdown = drawdown
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


def getALLStrategy(creator):
    cursor = connection.cursor()
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
          " init_balance," \
          " start_time," \
          " end_time,(select create_time from strategy_log sl where sl.strategy_id=s.strategy_id order by create_time desc limit 1) last_run" \
          " (select count(1) from strategy_log sl where sl.strategy_id=s.strategy_id) run_times," \
          " duration,benchmark,drawdown FROM strategy " \
          " where creator=%s"

    # 执行SQL语句
    cursor.execute(sql,creator)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # 打印结果
        strategy = Strategy(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16])
        strategyList.append(strategy)
    cursor.close()
    return strategyList


def getStrategyLogList(creator):
    cursor = connection.cursor()
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
          " (final_margin - init_balance)/init_balance final_margin" \
          " FROM strategy_log" \
          " where creator=%s" \
          " order by "

    # 执行SQL语句
    cursor.execute(sql, creator)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # 打印结果
        pro = StrategyLog(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        # print("row[0]:"+str(row[0])+"|row[a]:"+row[a]+"|row[b]:"+str(row[b])+"|row[3]:"+str(row[3])+"|row[4]:"+row[4]+"|row[5]:"+str(row[5])+"|row[6]:"+row[6]+"|row[7]:"+str(row[7]))
        strategyLogList.append(pro)
    cursor.close()
    return strategyLogList


def getLogDetail(strategyLogId, creator):
    cursor = connection.cursor()
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
          " (final_margin - init_balance)/init_balance final_margin" \
          " FROM strategy_log" \
          " where strategy_log_id=%s and creator=%s" % (strategyLogId, creator)

    # 执行SQL 语句
    cursor.execute(sql)

    results = cursor.fetchone()
    # for row in results:
    #     pro = StrategyLog(row[0], row[a], row[b], row[3], row[4], row[5], row[6], row[7], row[8])
    #
    #     log_details.append(pro)
    log_details = StrategyLog(results[0], results[1], results[2], results[3], results[4], results[5], results[6],
                              results[7], results[8], results[9], results[10])
    cursor.close()
    return log_details


def getStrategyAccountList(strategyLogId):
    cursor = connection.cursor()
    strategyAccountList = []
    # SQL 查询语句
    sql = " SELECT strategy_account_id,strategy_log_id,current_cash_balance,current_coin_balance,cost,total_net_balance,current_net_value," \
          " current_total_margin_rate,current_margin_rate,current_position,`signal`,transaction_status,t,open,close,high,low FROM strategy_account where strategy_log_id = %s"

    # 执行SQL语句
    cursor.execute(sql, strategyLogId)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # 打印结果
        pro = StrategyAccount(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                              row[11], row[12], row[13], row[14], row[15], row[16])
        strategyAccountList.append(pro)
    cursor.close()
    return strategyAccountList


def getStrategy(userId, strategyId, coin_category):
    cursor = connection.cursor()
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
          " init_balance," \
          " start_time," \
          " end_time,(select create_time from strategy_log sl where sl.strategy_id=s.strategy_id order by create_time desc limit 1) last_run" \
          " (select count(1) from strategy_log sl where sl.strategy_id=s.strategy_id) run_times," \
          " duration,benchmark,drawdown" \
          " FROM strategy where creator=%s and strategy_id=%s and coin_category=%s"

    # 执行SQL语句
    param = (userId, strategyId, coin_category)
    cursor.execute(sql, param)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # 打印结果
        strategy = Strategy(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                            row[11],row[12],row[13],row[14],row[15],row[16])
        strategy.set_strategy_conf_items(getStrategyConfItem(row[0]))
        # strategyConf.printAll()
        strategyList.append(strategy)
    cursor.close()
    return strategyList


def getStrategyConfItem(strategy_id):
    cursor = connection.cursor()
    strategyConfItemList = []
    # SQL 查询语句
    sql = " SELECT strategy_conf_item_id,strategy_id,index_label,formular,price,direction" \
          " FROM strategy_conf_item where strategy_id=%s"

    # 执行SQL语句
    param = (strategy_id)
    cursor.execute(sql, param)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # 打印结果
        item = StrategyConfItem(row[0], row[1], row[2], row[3], row[4], row[5])

        strategyConfItemList.append(item)
    cursor.close()
    return strategyConfItemList


def saveStrategy(strategy_name,creator, coin_category,init_balance,start_time,end_time):
    cursor = connection.cursor()
    strategyConfList = []
    # SQL 查询语句
    sql = " INSERT INTO strategy(strategy_name,creator, coin_category,init_balance,start_time,end_time)VALUES(%s,%s,%s,%s,%s, %s);"
    param = (strategy_name,creator, coin_category,init_balance,start_time,end_time)
    cursor.execute(sql, param)
    cursor.execute('SELECT LAST_INSERT_ID();')
    strategy_id = cursor.fetchone()
    connection.commit()
    return strategy_id
#保存策略名称
def saveStrategyName(strategy_id,strategy_name,creator):
    cursor = connection.cursor()
    strategyConfList = []
    # SQL 查询语句
    sql = " update strategy set strategy_name=%s where strategy_id=%s and creator=%s"
    param = (strategy_name,strategy_id,creator)
    cursor.execute(sql, param)
    connection.commit()

def checkStrategyName(strategy_name,creator):
    cursor = connection.cursor()
    strategyConfList = []
    # SQL 查询语句
    sql = " select * from strategy where strategy_name=%s and creator=%s"
    param = (strategy_name,creator)
    cursor.execute(sql, param)
    results = cursor.fetchall()
    if (len(results)>0):
        return True
    else:
        return False
def saveStrategyConfItem(strategy_id, index_label, formular, price, direction):
    cursor = connection.cursor()
    strategyConfList = []
    # SQL 查询语句
    sql = " INSERT INTO strategy_conf_item(strategy_id,index_label,formular,price, direction)VALUES(%s,%s,%s,%s, %s);"
    param = (strategy_id, index_label, formular, price,direction)
    cursor.execute(sql, param)
    connection.commit()
def deleteStrategyById(strategy_id):
    cursor = connection.cursor()
    strategyConfList = []
    # SQL 查询语句
    sql = " delete from strategy_conf_item where strategy_id=%s;"
    param = (strategy_id)
    cursor.execute(sql, param)
    sql = " delete from strategy_account where strategy_log_id in " \
          "       (select strategy_log_id from strategy_log where strategy_id=%s);"
    param = (strategy_id)
    cursor.execute(sql, param)
    sql = " delete from strategy_log where strategy_id=%s;"
    param = (strategy_id)
    cursor.execute(sql, param)
    sql = " delete from strategy where strategy_id=%s;"
    param = (strategy_id)
    cursor.execute(sql, param)
    connection.commit()

# list = getStrategyLogList(a)
# for sl in list:
#     print(sl.get_strategy_log_id())
#     print(sl.get_strategy_id())
#     print(sl.get_start_date())
#     print(sl.get_end_date())
#     print(sl.get_init_balance())
#     print(sl.get_coin_category())
#     print(sl.get_creator())
#     print(sl.get_create_time())
#     print(sl.get_strategy_log_id())
#     print(sl.get_execution_result())
#     print(sl.get_strategy_name())
#     print(sl.get_final_margin())


# list = getStrategyAccountList(a)
# for sl in list:
#     print("----------------------")
#     print(sl.get_strategy_account_id())
#     print(sl.get_strategy_log_id())
#     print(sl.get_current_cash_balance())
#     print(sl.get_current_coin_balance())
#     print(sl.get_cost())
#     print(sl.get_total_net_balance())
#     print(sl.get_current_net_value())
#     print(sl.get_current_total_margin_rate())
#     print(sl.get_current_margin_rate())
#     print(sl.get_current_position())
#     print(sl.get_signal())
#     print(sl.get_transaction_status())
#     print(sl.get_t())
#     print(sl.get_close())
#     print(sl.get_high())
#     print(sl.get_low())
#saveStrategyName(2,'BTC',1)
# saveStrategyConfItem(1,'close(t-1)','<',20)
# pro = getStrategyConf(1, 2, "BTC")
#pro = getStrategy(1, 4, "BTC")
#print(checkStrategyName("测试策略"))
