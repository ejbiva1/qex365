from util.ReadData import *
from decimal import Decimal
from util.Trader import *


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

    def strategy(self, T):
        # 是否总仓小于20%
        if self.position.coin_cash_rate > Decimal('0.2'):
            persent = (self.position.init_balance - self.position.balance) / self.position.init_balance
            # 判断总资产减少10%？   yes，减持50%
            if persent >= 0.1:
                #         todo send signal
                df = self.datas[(self.idt == T)]
                price = df.iat[0, 2]
                amount = Decimal(self.position.coin_amount) * Decimal('0.5')
                strategy_id = 2
                Trader.position_judge(position=self.position, strategy_id=strategy_id, price=price, timestamp=T,
                                      trade_amount=amount)
            else:
                # 没有买卖操作
                calculator = Calculator(self.position, T, price=0, amount=0, signal=0, strategy_id=3,
                                        strategy_account_id=1)
                calculator.non_trade()
        else:
            # 没有买卖操作
            calculator = Calculator(self.position, T, price=0, amount=0, signal=0, strategy_id=3, strategy_account_id=1)
            calculator.non_trade()