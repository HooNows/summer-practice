from simultor.TrainsPackage.TrainClass import Train
from simultor.TerminalsPackage.TerminalClass import Terminal


class Path:
    def __init__(self, path_len, load_stations, unload_stations, trains_list):
        self.path_len = path_len
        self.load_stations = load_stations
        self.unload_stations = unload_stations
        self.trains_list = trains_list

    def __repr__(self):
        return 'PATH:\n Load Station Info: \n{}\n Unload Station Info: \n{}\n  Len: {}\n  PathTrains:{}\n----------------------------'.format(self.load_stations, self.unload_stations, self.path_len,self.trains_list)

    def CheckArrival(self):
        for t in self.trains_list:
            if t.cur_pos <= 0 and t.onTheWay == True and t.cur_supply == 0:
                #print('TRAIN ', t, 'ARRIVED AT LOAD')
                t.cur_pos = 0
                t.onTheWay = False
                self.load_stations.trains.append(t)
            elif t.cur_pos >= self.path_len and t.onTheWay == True and t.cur_supply == t.max_supply:
                #print('TRAIN ', t, 'ARRIVED AT UNLOAD')
                t.cur_pos = self.path_len
                t.onTheWay = False
                self.unload_stations.trains.append(t)

    def CheckReadyTrains(self):
        for t in self.trains_list:
            print(t)
            if (t.cur_supply == t.max_supply) and (t.onTheWay == False) and (t.cur_pos == 0):
                #print('TRAIN IS READY TO TRAVEL')
                self.DelTrain(t, self.load_stations.trains)
                t.onTheWay = True
            elif (t.cur_supply == 0) and (t.onTheWay == False) and (t.cur_pos == self.path_len):
                self.DelTrain(t, self.unload_stations.trains)
                t.onTheWay = True

    def MoveTrains(self):
        #print(self.load_stations)   
        for t in self.trains_list:
            if (t not in self.load_stations.trains) and (t not in self.unload_stations.trains):
                t.Move()
        
        for t in self.trains_list:
            if t.cur_pos > self.path_len:
                t.cur_pos = self.path_len
            elif t.cur_pos < 0:
                t.cur_pos = 0


    def DelTrain(self, tr, trlist):
        for i,t in enumerate(trlist):
            if t == tr:
                trlist.pop(i)

    def Tick(self):
        self.CheckReadyTrains()
        self.CheckArrival()
        self.MoveTrains()

