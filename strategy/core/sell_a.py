# coding:utf-8
from util.ReadData import *
from decimal import Decimal

import sys

sys.path.append('..')
from util.Trader import *
from entity.Signal import Signal


class SellA:
    # todo 定义全局的strategy_id
    # 初始化策略参数
    def __init__(self, start_time, end_time, position):
        self.start_time = start_time
        self.end_time = end_time

        self.position = position
        self.datas = position.datas
        self.idt = self.datas['id']
        self.price = 0.00
        self.trade_amount = 0.000000
        self.cal = Decimal('1')

    def strategy(self, T, position):
        signal = Signal(signal=0, flag=0)

        self.position = position
        # 是否总仓小于20%
        calculator = Calculator(self.position, T, signal=0, strategy_id=3,
                                strategy_account_id=1)
        if self.position.current_position > Decimal('0.2'):
            # persent = (self.position.init_balance - self.position.balance) / self.position.init_balance
            base = self.position.init_balance * self.cal
            persent = (self.position.init_balance - self.position.balance) / base
            # 判断当前总资产减少10%?   yes,减持50%
            if persent >= 0.1:
                # send signal
                df = self.datas[(self.idt == T)]
                price = df.iat[0, 2]
                amount = Decimal(self.position.coin_amount) * Decimal('0.5')
                strategy_id = 2
                print_signal(T, price, amount, 'sell_a True')
                signal.signal = 1
                flag_inner = Trader.position_judge(position=self.position, strategy_id=strategy_id, price=price,
                                                   calculator=calculator,
                                                   trade_amount=amount)
                if flag_inner is not 0:
                    signal.flag = 1
                    self.cal *= Decimal('0.9')
            else:
                # 没有买卖操作
                calculator.non_trade()
        else:
            # 没有买卖操作
            # calculator = Calculator(self.position, T, price=0, amount=0, signal=0, strategy_id=3, strategy_account_id=1)
            calculator.non_trade()
        self.position = calculator.position
        return signal


def print_signal(T, price, amount, reason):
    print('********** SIGNAL **********')
    print('signal_type= sell_a')
    print('signal_reason= ' + str(reason))
    print('price= ' + str(price))
    print('amount= ' + str(amount))
    print('timestamp= ' + str(T))
    print('********** SIGNAL **********')
