from numpy.random import normal
from simultor.TrainsPackage.TrainClass import Train
from simultor.TrainsPackage.TrainTemplates import polar_train

class Terminal:

    def __init__(self, terminal_type, cur_supply):
        self.trains = []
        self.name = terminal_type['type_name']

        self.cur_supply = cur_supply
        self.max_supply = terminal_type['max_supply']

        self.mean_income = terminal_type['mean_income']
        self.std_income = terminal_type['std_income']

        self.load_speed = terminal_type['load_speed']
        self.unload_speed = terminal_type['unload_speed']
        self.num_rails = terminal_type['num_rails']
        self.terminal_type = terminal_type['type']
        self.income = 0

    def __repr__(self):
        return '  Name: {}\n  Trains: {}\n  MaxSupply: {}  Supply: {}\n'.format(self.name, self.trains, self.max_supply, self.cur_supply)

    def Income(self):
        if self.mean_income == 0:
            return

        self.income = round(normal(self.mean_income, self.std_income))
        self.cur_supply += self.income

        if self.cur_supply > self.max_supply:
            self.cur_supply = self.max_supply

    def Load(self):
        if self.load_speed == 0:
            return

        choose_min = min(self.num_rails, len(self.trains))

        for i in range(choose_min):
            train = self.trains[i]

            if self.cur_supply >= self.load_speed and self.terminal_type == train.train_type:
                self.cur_supply -= train.Load(self.load_speed)

    def Unload(self):
        if self.unload_speed == 0:
            return

        choose_min = min(self.num_rails, len(self.trains))

        for i in range(choose_min):
            train = self.trains[i]

            if train.train_type == 'polar':
                continue

            if train.cur_supply > 0:
                if (((self.cur_supply + self.unload_speed) <= self.max_supply) and (train.cur_supply >= self.unload_speed)):
                    self.cur_supply += self.unload_speed - train.Unload(self.unload_speed)
                elif ((self.cur_supply + self.unload_speed) > self.max_supply) and (train.cur_supply >= (self.max_supply - self.cur_supply)):
                    self.cur_supply += (self.max_supply - self.cur_supply) - train.Unload(self.max_supply - self.cur_supply)
                else:
                    train.Unload(train.cur_supply)
                    self.cur_supply += train.cur_supply

    def AddPolarTrain(self):
        if self.unload_speed == 0:
            return

        polar_flag = False
        for i,t in enumerate(self.trains):
            if t.train_type == self.terminal_type:
                polar_flag = True
                if t.cur_supply == t.max_supply:
                    self.trains.pop(i)

        if self.cur_supply >= 10000 and len(self.trains) < 3 and not polar_flag:
            tmp_train = Train('PolarTrain', polar_train, 0, 0, False)
            self.trains.append(tmp_train)

    def Tick(self):
        self.AddPolarTrain()
        self.Income()
        self.Load()
        self.Unload()
