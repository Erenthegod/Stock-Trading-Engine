class Trade:
    def __init__(self, trade_type, stock, amount, cost):
        self.trade_type = trade_type
        self.stock = stock
        self.amount = amount
        self.cost = cost

    def __repr__(self):
        return f"{self.trade_type} {self.amount} of {self.stock} at {self.cost}"

class TradeNode:
    def __init__(self, trade):
        self.trade = trade
        self.next = None

class TradeList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_trade(self, trade, descending=False):
        new_node = TradeNode(trade)
        if not self.head:
            self.head = self.tail = new_node
            return
        
        prev, curr = None, self.head
        while curr and ((curr.trade.cost > trade.cost) if descending else (curr.trade.cost < trade.cost)):
            prev, curr = curr, curr.next
        
        if prev is None:
            new_node.next = self.head
            self.head = new_node
        else:
            prev.next = new_node
            new_node.next = curr
        
        if new_node.next is None:
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        node = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return node.trade

class Exchange:
    def __init__(self):
        self.buys = TradeList()
        self.sells = TradeList()

    def place_order(self, trade):
        print(f"Placing order: {trade}")
        if trade.trade_type == "Buy":
            self.buys.add_trade(trade, descending=True)
        else:
            self.sells.add_trade(trade, descending=False)
        self.process_trades()
    
    def process_trades(self):
        while self.buys.head and self.sells.head:
            buy_order = self.buys.head.trade
            sell_order = self.sells.head.trade
            if buy_order.cost >= sell_order.cost:
                matched_amount = min(buy_order.amount, sell_order.amount)
                print(f"Matched {matched_amount} shares of {buy_order.stock} at ${sell_order.cost}!")
                buy_order.amount -= matched_amount
                sell_order.amount -= matched_amount
                if buy_order.amount == 0:
                    self.buys.remove_head()
                if sell_order.amount == 0:
                    self.sells.remove_head()
            else:
                break

# Sample Input with Creativity

def sample_run():
    market = Exchange()
    print("The trading floor is now open!")
    
    market.place_order(Trade("Buy", "APEX", 100, 150))
    market.place_order(Trade("Sell", "APEX", 50, 140))
    market.place_order(Trade("Buy", "NEBULA", 75, 220))
    market.place_order(Trade("Sell", "NEBULA", 100, 215))
    market.place_order(Trade("Buy", "QUANT", 60, 310))
    market.place_order(Trade("Sell", "QUANT", 30, 300))
    market.place_order(Trade("Buy", "COSMO", 90, 410))
    market.place_order(Trade("Sell", "COSMO", 80, 400))
    
    print("The market has spoken! Final trades executed.")

sample_run()
