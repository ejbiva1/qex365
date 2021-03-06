# coding:utf-8

from sqlalchemy import func

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

sys.path.append('..')
from entity.Strategy_log import Log
from entity.Strategy_account import AccountDBSession, Account

# from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:Quant123@localhost:3306/quantcoin?charset=utf8MB4',
                       max_overflow=0,  # 超过连接池大小外最多创建的连接
                       pool_size=50,  # 连接池大小
                       pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                       pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                       )
# engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4',
#                        max_overflow=0,  # 超过连接池大小外最多创建的连接
#                        pool_size=50,  # 连接池大小
#                        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
#                        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
#                        )
# session = sessionmaker(bind=engine)
SessionFactory = sessionmaker(bind=engine)
# session = scoped_session(SessionFactory)
session = SessionFactory()


def insert_2_strategy_transaction(dataframe):
    # engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4')
    dataframe.to_sql('strategy_transaction', engine, index=False, if_exists='append')
    # print('insert strategy_transaction successfully')


def insert_2_strategy_log(new_log):
    # engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4')
    # dataframe.to_sql('strategy_log', engine, index=False, if_exists='append')
    # new_log = Log()
    # session = LogDBSession()
    session.add(new_log)
    try:
        session.commit()
    except:
        session.rollback()
    log_id = session.query(func.max(Log.strategy_log_id)).one()[0]
    session.close()
    # print('insert to strategy_log successfully')
    return log_id


def insert_2_strategy_account(new_account):
    # engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4')
    # dataframe.to_sql('strategy_account', engine, index=False, if_exists='append')
    # session = AccountDBSession()
    session.add(new_account)
    try:
        session.commit()
    except:
        session.rollback()
    account_id = session.query(func.max(Account.strategy_account_id)).one()[0]
    session.close()
    # print('insert to strategy_account successfully')
    return account_id


# todo 更新结果数据
def update_strategy_log(log2update):
    # session = LogDBSession()
    sql = 'UPDATE strategy_log SET final_margin = ' + str(log2update.final_margin) + ',benchmark = ' + str(
        log2update.benchmark) + ' WHERE strategy_log_id = ' + str(
        log2update.strategy_log_id)
    try:
        session.execute(sql)
        session.commit()
        # print('update final_margin,benchmark to strategy_log successfully')

    except:
        # 发生错误时回滚
        session.rollback()
    # 关闭数据库连接
    session.close()


# todo 更新结果数据
def update_strategy_log_max_drawdown(log2update):
    # session = LogDBSession()
    sql = 'UPDATE strategy_log SET max_drawdown = ' + str(
        log2update.max_drawdown) + ' WHERE strategy_log_id = ' + str(
        log2update.strategy_log_id)
    try:
        session.execute(sql)
        session.commit()
        # print('update final_margin,benchmark to strategy_log successfully')

    except:
        # 发生错误时回滚
        session.rollback()
    # 关闭数据库连接
    session.close()


# todo 更新account数据
def update_strategy_account(account):
    # session = LogDBSession()
    sql = 'UPDATE strategy_account SET current_total_margin_rate = ' + str(account.current_total_margin_rate) + \
          ' WHERE strategy_account_id = ' + str(account.strategy_account_id)
    try:
        session.execute(sql)
        session.commit()
        # print('update final_margin,benchmark to strategy_log successfully')

    except:
        # 发生错误时回滚
        session.rollback()
    # 关闭数据库连接
    session.close()


if __name__ == '__main__':
    # start = 1508990400
    #     # end = 1509004800
    #     # print(read_datas(start, end))
    # print(get_trade_info(1508990400, 1, 0))

    # data = {'strategy_account_id': [1, 2, 3],
    #         't': [1508990400, 1508994000, 1508997600],
    #         'cost': [7.929392, 7.929392, 7.929392],
    #         'volumn': [0.9, 1, 2.1],
    #         'commission': [0.00, 0.00, 0.00],
    #         'pre_position': [0, 0.90, 1.90],
    #         'post_position': [90, 80, 85],
    #         'position_gap': [90, 80, 85],
    #         'pre_balance': [90, 80, 85],
    #         'post_balance': [90, 80, 85],
    #         'balance_gap': [90, 80, 85],
    #         'flag': [1, 0, 1],
    #         'strategy_id': [0, 1, 0]}
    # df = pd.DataFrame(data)
    # insert_2_strategy_transaction(df)

    # new_log = Log(strategy_id=1, creator=1, start_date=1509001200,
    #               end_date=1509022800, init_balance=20000,
    #               coin_category='btc')
    # id = insert_2_strategy_log(new_log)
    # print(id)
    log = Log(strategy_log_id=1, final_margin=666)
    update_strategy_log(log)
