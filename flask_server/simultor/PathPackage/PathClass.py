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
            if t.distance <= 0 and t.onTheWay == True:
                t.distance = 0
                t.onTheWay = False
                if t.Empty():
                    #print('TRAIN ', t, 'ARRIVED AT LOAD')
                    self.load_stations.trains.append(t)
                    self.load_stations.trains.sort(key = lambda tr:(tr.priority, tr.cur_supply), reverse=True)
                elif t.Full():
                    #print('TRAIN ', t, 'ARRIVED AT UNLOAD')
                    self.unload_stations.trains.append(t)
                    self.unload_stations.trains.sort(key = lambda t:(t.priority, t.cur_supply), reverse=True)

    def CheckReadyTrains(self):
        for t in self.trains_list:
            print(t)
            if (t.onTheWay == False):
                if t.Full() and (t in self.load_stations.trains):
                    self.DelTrain(t, self.load_stations.trains)
                    t.onTheWay = True
                    t.distance = self.path_len
                elif t.Empty() and (t in self.unload_stations.trains):
                    self.DelTrain(t, self.unload_stations.trains)
                    t.onTheWay = True
                    t.distance = self.path_len

    def MoveTrains(self):   
        for t in self.trains_list:
            if (t not in self.load_stations.trains) and (t not in self.unload_stations.trains):
                t.Move()
        
        for t in self.trains_list:
            if t.distance < 0:
                t.distance = 0


    def DelTrain(self, tr, trlist):
        for i,t in enumerate(trlist):
            if t == tr:
                trlist.pop(i)

    def Tick(self):
        self.CheckReadyTrains()
        self.CheckArrival()
        self.MoveTrains()

