from simultor.TrainsPackage.TrainClass import Train
from simultor.TrainsPackage.TrainTemplates import *

from simultor.TerminalsPackage.TerminalClass import Terminal
from simultor.TerminalsPackage.TerminalTemplates import *

from simultor.PathPackage.PathClass import Path

import datetime
from tqdm import tqdm

from sql import Sql

db = Sql()
trains_templ = db.train_templ
terminals_templ = db.term_templ
db_paths = db.paths

def GetTrains():
    #get trains
    trains = []
    for train in db.trains:
        trains.append( Train(train['name'], trains_templ[train['template']-1], train['cur_supply'], train['cur_pos'], train['priority'] ) )
    return trains


def GetTerminals():
    #get terminals
    terminals = []
    for terminal in db.terminals:
        terminals.append( Terminal(terminals_templ[terminal['template']-1], terminal['cur_supply']) )
    return terminals


def GetPaths():
    #get paths
    paths = []
    for p in db_paths:
        lenght = p['len']
        load = 0
        unload = 0
        p_trains = []

        #find terminals
        for t in terminals:
            if t.name == p['load_terminals']:
                load = t
            if t.name == p['unload_terminals']:
                unload = t
        
        #find trains
        for p_train in p['trains'].split(','):
            for t in trains:
                if t.name == p_train:
                    p_trains.append(t)
        paths.append( Path(lenght,load,unload,p_trains) )
    return paths


trains = GetTrains()
terminals = GetTerminals()
paths = GetPaths()

def main():

    d = datetime.datetime(2021, 11, 1, 0)

    TIME = 0
    TIMER = 24*30 + 1

    for i in tqdm(range(TIME, TIMER)):
        for o in (paths + terminals):
            o.Tick()

        for t in trains:
            db.WriteTrain(t.name, d, t.cur_supply, t.distance)
        
        for t in terminals:
            trains_len = min(t.num_rails, len(t.trains))
            #if trains_len:
            db.WriteTerminal(t.name, d, t.cur_supply, t.max_supply, t.income, t.trains[0:trains_len])
        
        d += datetime.timedelta(hours=1)

    print('Success!')