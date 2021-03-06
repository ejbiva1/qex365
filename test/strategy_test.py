from util.Position import Position
from strategy.core.sell_a import SellA
from strategy.core.sell_b import SellB
from strategy.core.buy_b import BuyB
from strategy.core.buy_a import BuyA
from util.WriteData import *
from decimal import Decimal
from util.ReadData import read_datas_1day_test
from strategy.core.poc import sell_signal, buy_signal
from web.app.DB import getStrategyConf, getStrategyConfItem
import pandas as pd
from entity.Poc_response import Poc_response


# todo type define
def strategy_combination_b(start_time, end_time, init_balance):
    # 写入strategy_log表
    # todo get creator from token
    new_log = Log(strategy_id=3, start_date=start_time, end_date=end_time, init_balance=init_balance,
                  coin_category='btc', creator=1)
    log_id = insert_2_strategy_log(new_log)
    position = Position(start_date=start_time, end_date=end_time, balance=init_balance, strategy_type=3)
    dates = position.datas['id']
    print(dates.size)
    sell_b = SellB(start_time=start_time, end_time=end_time, position=position)
    buy_b = BuyB(start_time=start_time, end_time=end_time, position=position)
    for t in dates:
        status = 0
        sell_flag = sell_b.strategy(t, position)
        position = sell_b.position
        if sell_flag.flag is not 0:
            status = 1
            # todo signal 策略中的信号放到一个对象返回到这里
        account_id_sell = account_insert(position=position, t=t, strategy_log_id=log_id, signal=int(sell_flag.signal),
                                         transaction_status=status)
        buy_flag = buy_b.strategy(t, position)
        position = buy_b.position
        # strategy_account 写入
        if buy_flag.flag is not 0:
            status = 2
            # todo signal 策略中的信号放到一个对象返回到这里
        account_id_buy = account_insert(position=position, t=t, strategy_log_id=log_id, signal=int(buy_flag.signal),
                                        transaction_status=status)

    # 回写策略执行后总资产到strategy_log表
    write_back2log(position, log_id)


def strategy_combination_a(start_time, end_time, init_balance):
    # 写入strategy_log表
    new_log = Log(strategy_id=1, start_date=start_time, end_date=end_time, init_balance=init_balance,
                  coin_category='btc', creator=1)
    log_id = insert_2_strategy_log(new_log)
    position = Position(start_date=start_time, end_date=end_time, balance=init_balance, strategy_type=1)
    dates = position.datas['id']
    dates = dates[dates >= start_time]
    print(dates.size)
    sell_a = SellA(start_time=start_time, end_time=end_time, position=position)
    buy_a = BuyA(start_time=start_time, end_time=end_time, position=position)
    for t in dates:
        status = 0
        sell_flag = sell_a.strategy(t, position)
        position = sell_a.position
        if sell_flag.flag is not 0:
            status = 1
            # todo signal 策略中的信号放到一个对象返回到这里
        account_id_sell = account_insert(position=position, t=t, strategy_log_id=log_id, signal=int(sell_flag.signal),
                                         transaction_status=status)
        buy_flag = buy_a.strategy(t, position)
        position = buy_a.position
        if buy_flag is not 0:
            status = 2
            # todo signal 策略中的信号放到一个对象返回到这里
        account_id_buy = account_insert(position=position, t=t, strategy_log_id=log_id, signal=int(buy_flag.signal),
                                        transaction_status=status)

    #  回写策略执行后总资产到strategy_log表
    write_back2log(position, log_id)


def account_insert(position, t, strategy_log_id, signal, transaction_status):
    df = position.datas[position.datas['id'] == t]
    open_price = Decimal(df.iat[0, 1]).quantize(Decimal('0.00'))
    close = Decimal(df.iat[0, 2]).quantize(Decimal('0.00'))
    low = Decimal(df.iat[0, 3]).quantize(Decimal('0.00'))
    high = Decimal(df.iat[0, 4]).quantize(Decimal('0.00'))
    cost = Decimal(position.price).quantize(Decimal('0.00'))
    current_cash_balance = Decimal(position.balance).quantize(Decimal('0.00'))
    current_position = Decimal(position.current_position).quantize(Decimal('0.000000'))
    new_account = Account(strategy_log_id=strategy_log_id, current_cash_balance=current_cash_balance,
                          current_coin_balance=position.coin_amount, cost=cost,
                          total_net_balance=position.total_net_balance, current_net_value=position.total,
                          current_total_margin_rate=position.rate_of_return,
                          current_margin_rate=position.cur_rate_of_return,
                          current_position=current_position, signal=signal,
                          transaction_status=transaction_status, t=t,
                          open=open_price, close=close, high=high, low=low)
    account_id = insert_2_strategy_account(new_account=new_account)
    return account_id


def write_back2log(position, log_id):
    total = position.total
    log = Log(strategy_log_id=log_id, final_margin=total)
    update_strategy_log(log)


def strategy_poc(strategy_id, user_id, coin_category, start_time, end_time, init_balance):
    balance = init_balance
    data = read_datas_1day_test(start_time - 172800, end_time)
    if data.empty:
        print('load data error!')
        return False
    strategy_conf_list = getStrategyConf(strategyId=strategy_id, userId=user_id, coin_category=coin_category)
    if not strategy_conf_list:
        print('no strategy!')
        return False
    strategy_conf = strategy_conf_list[0]
    strategy_conf_id = strategy_conf.strategy_conf_id
    item_list = getStrategyConfItem(strategy_conf_id=strategy_conf_id)
    # temp_list = []
    item_id_list = []
    conf_id_list = []
    label_list = []
    price_list = []
    formula_list = []
    direction_list = []
    for it in item_list:
        item_id = it.strategy_conf_item_id
        conf_id = it.strategy_conf_id
        label = it.index_label
        price = it.price
        formula = it.formular
        direction = it.direction

        item_id_list.append(item_id)
        conf_id_list.append(conf_id)
        label_list.append(label)
        price_list.append(price)
        formula_list.append(formula)
        direction_list.append(direction)

    temp_list = {"0": item_id_list, "1": conf_id_list, "2": label_list, "3": price_list, "4": formula_list,
                 "5": direction_list}
    # labs = [0, 1, 2, 3, 4, 5]
    df = pd.DataFrame(temp_list)
    # df = pd.DataFrame.from_records(temp_list)
    df_sell = df[df['5'] == 2]
    df_buy = df[df['5'] == 1]
    # 转换构造sell和buy的所有条件
    sell_dict = create_conditions_dictionary(df_sell)
    buy_dict = create_conditions_dictionary(df_buy)
    position = 0.000000
    end_time_close = data[data['id'] == end_time].iat[0, 2]

    for t in data['id']:
        data_t = data[data['id'] == t]
        close_t = data_t.iat[0, 2]
        # 返回价钱和数量signal
        signal = buy_signal(t, buy_dict, data)
        if signal.signal == 1:
            # todo 买入并返回余额，买入数量
            amount = Decimal(balance) / Decimal(close_t)
            position = amount
        # balance -= Decimal(amount) * Decimal(close_t)

        signal = sell_signal(t, sell_dict, data)
        if signal.signal == 2:
            # todo 卖出并返回余额
            balance += Decimal(position) * Decimal(close_t)
            position = 0

    # todo 计算最后的收益率和基准收益率
    if position is 0:
        strategy_profit = (balance - Decimal(init_balance)) / Decimal(init_balance)
    else:
        balance += Decimal(position) * Decimal(end_time_close)
        strategy_profit = (balance - Decimal(init_balance)) / Decimal(init_balance)
    df_start = data[data['id'] == start_time]
    df_end = data[data['id'] == end_time]

    new_balance = init_balance
    if df_start.iat[0, 2] is not 0:
        amount = Decimal(init_balance) / Decimal(df_start.iat[0, 2])
    else:
        amount = 0
    new_balance -= Decimal(amount) * Decimal(df_start.iat[0, 2])
    new_balance += amount * Decimal(df_end.iat[0, 2])
    benchmark_profit = (new_balance - Decimal(init_balance)) / Decimal(init_balance)

    return Poc_response(strategy_profit=Decimal(strategy_profit).quantize(Decimal('0.0000')),
                        benchmark_profit=Decimal(benchmark_profit).quantize(Decimal('0.0000')))


# 内部方法
def create_conditions_dictionary(df):
    dictionary = {'close(T-1)': 0, 'open(T-1)': 0, 'high(T-1)': 0, 'low(T-1)': 0,
                  'close(T-2)': 0, 'open(T-2)': 0, 'high(T-2)': 0, 'low(T-2)': 0}
    for index, condition in df.iterrows():
        technical_index = condition[2]
        price = condition[3]
        operator = condition[4]
        if technical_index == 11:
            formula = get_formula(operator, price)
            dictionary['close(T-1)'] = formula
        elif technical_index == 21:
            formula = get_formula(operator, price)
            dictionary['open(T-1)'] = formula
        elif technical_index == 31:
            formula = get_formula(operator, price)
            dictionary['high(T-1)'] = formula
        elif technical_index == 41:
            formula = get_formula(operator, price)
            dictionary['low(T-1)'] = formula
        elif technical_index == 12:
            formula = get_formula(operator, price)
            dictionary['close(T-2)'] = formula
        elif technical_index == 22:
            formula = get_formula(operator, price)
            dictionary['open(T-2)'] = formula
        elif technical_index == 32:
            formula = get_formula(operator, price)
            dictionary['high(T-2)'] = formula
        elif technical_index == 42:
            formula = get_formula(operator, price)
            dictionary['low(T-2)'] = formula
    return dictionary


# 内部方法
def get_formula(operator, price):
    if operator == '3':
        value = price.split(',')
        formula = value[0] + '<x<' + value[1]
        # condition_sell = Poc_condition(technical_index, formular)
    else:
        formula = 'x' + operator + price
    return formula


if __name__ == '__main__':
    # start_time = 1510070400
    # start_time = 1508990400
    start_time = 1509292800
    # end_time = 1510675200
    # end_time = 1509022800
    end_time = 1511452800
    init_balance = 200000
    # strategy_combination_b(start_time=start_time, end_time=end_time, init_balance=init_balance)
    response = strategy_poc(strategy_id=2, user_id=1, coin_category='btc', start_time=start_time, end_time=end_time,
                            init_balance=init_balance)
    print('benchmark_profit=' + str(response.benchmark_profit))
    print('strategy_profit=' + str(response.strategy_profit))
