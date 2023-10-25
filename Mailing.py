# - `to_address` (тип данных `Address`),
# - `from_address` (тип данных `Address`),
# - `cost` (тип данных `число`),
# - `track` (тип данных строка).

class Mailing:
    def __init__(self, to_address, from_address, cost, track):         
        self.to_address= to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

# m = Mailing ("111888", "Moscow", "Arbat", "45", "1")
# print(m.to_address)
# print(m.from_address)
# print(m.cost)
# print(m.track)
