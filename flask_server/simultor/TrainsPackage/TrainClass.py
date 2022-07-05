class Train:

    def __init__(self, name, train_type, cur_supply, cur_pos, onTheWay = True):
        self.name = name
        self.max_supply = train_type['max_supply']
        self.speed = train_type['speed']

        self.cur_supply = cur_supply
        self.cur_pos = cur_pos
        #self.distance = 0
        self.onTheWay = onTheWay
        self.train_type = train_type['type']

    def __repr__(self):
        return 'Name: {}, Supply: {} / {} '.format(self.name, self.cur_supply, self.max_supply)

    def Load(self, amount):
        extra_supply = 0
        if (self.cur_supply + amount) <= self.max_supply:
            self.cur_supply += amount
            extra_supply = amount
        else:
            extra_supply = self.max_supply - self.cur_supply
            self.cur_supply = self.max_supply

        return extra_supply

    def Unload(self, amount):
        extra_supply = 0
        if (self.cur_supply - amount) >= 0:
            self.cur_supply -= amount
            extra_supply = 0
        else:
            extra_supply = amount - self.cur_supply
            self.cur_supply = 0

        return extra_supply

    def Full(self):
        return self.cur_supply == self.max_supply

    def Empty(self):
        return self.cur_supply == 0

    def Move(self):
        if self.Empty():
            self.cur_pos -= self.speed

        elif self.Full():
            self.cur_pos += self.speed

