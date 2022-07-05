from mysql.connector import connect

class Sql:
    def __init__(self):
        self.db = connect(
        host='localhost',
        username = 'root',
        password = '',
        database = 'SUMMER'
        )
        self.cursor = self.db.cursor()

        self.storage = connect(
        host='localhost',
        username = 'root',
        password = '',
        )
        self.storage_cursor = self.storage.cursor()


        self.trains = []
        self.terminals = []
        self.term_templ = []
        self.train_templ = []
        self.paths = []
        self.train_names = []

        self.GetTerminalsTemplates()
        self.GetTrainsTemplates()
        self.GetTrains()
        self.GetTerminals()
        self.GetPaths()
        self.DropCreateDatabase()
        self.CreateTables()

    def GetTrainsTemplates(self):
        sql =   '''
                select * from trains_templates 
                '''
        self.cursor.execute(sql)

        res = self.cursor.fetchall()
        row = dict(zip(self.cursor.column_names, res[0]))

        for sample in res:
            tmp = {}
            for name,value in zip(row, sample):
                tmp[str(name)] = value
            self.train_templ.append(tmp)

    def GetTerminalsTemplates(self):
        sql =   '''
                select * from terminals_templates 
                '''
        self.cursor.execute(sql)

        res = self.cursor.fetchall()
        row = dict(zip(self.cursor.column_names, res[0]))

        for sample in res:
            tmp = {}
            for name,value in zip(row, sample):
                tmp[str(name)] = value
            self.term_templ.append(tmp)
    
    def GetTrains(self):
        sql =   '''
                select * from trains 
                '''
        self.cursor.execute(sql)

        res = self.cursor.fetchall()
        row = dict(zip(self.cursor.column_names, res[0]))

        for sample in res:
            tmp = {}
            for name,value in zip(row, sample):
                if name == 'id':
                    continue
                if name == 'name':
                    self.train_names.append(value)
                tmp[str(name)] = value
            self.trains.append(tmp)

    def GetTerminals(self):
        self.term_names = []
        sql =   '''
                select * from terminals 
                '''
        self.cursor.execute(sql)

        res = self.cursor.fetchall()
        row = dict(zip(self.cursor.column_names, res[0]))

        for sample in res:
            tmp = {}
            for name,value in zip(row, sample):
                if name == 'id':
                    continue
                if name == 'name':
                    self.term_names.append(value)
                tmp[str(name)] = value
            self.terminals.append(tmp)
        
    def GetPaths(self):
        sql =   '''
                select * from paths 
                '''
        self.cursor.execute(sql)

        res = self.cursor.fetchall()
        row = dict(zip(self.cursor.column_names, res[0]))

        for sample in res:
            tmp = {}
            for name,value in zip(row, sample):
                if name == 'id':
                    continue
                tmp[str(name)] = value
            self.paths.append(tmp)

    def DropCreateDatabase(self):
        sql_drop = 'drop database if exists storage'
        sql_create = 'create database if not exists storage'

        self.storage_cursor.execute(sql_drop)
        self.storage_cursor.execute(sql_create)

        self.inner_storage = connect(
        host='localhost',
        username = 'root',
        password = '',
        database = 'storage'
        )
        self.inn_st_cursor = self.inner_storage.cursor()


    def CreateTables(self):
        self.storage = connect(
        host='localhost',
        username = 'root',
        password = '',
        database = 'storage'
        )
        self.storage_cursor = self.storage.cursor()
        
        sql = 'create table if not exists '

        for t in self.trains:
            self.storage_cursor.execute(sql + t['name'] + ''' 
                                                        (Date datetime,
                                                        Supply INT,
                                                        Position INT)
                                                        ''')
        for t in self.terminals:
            self.storage_cursor.execute(sql + t['name'] + ''' 
                                                        (Date datetime,
                                                        Supply INT,
                                                        Max_supply INT,
                                                        Income INT,
                                                        Trains VARCHAR(300))
                                                        ''')
        


    def WriteTrain(self, name, date, supply, pos):
        sql = "insert into `{}` (`Date`, `Supply`, `Position`) VALUES ('{}','{}','{}')".format(name, date, supply, pos)
        self.storage_cursor.execute(sql)
        self.storage.commit()
    
    def WriteTerminal(self, name, date, supply, max_supply, income, trains):
        sql = "insert into `{}` (`Date`, `Supply`, `Max_supply`, `Income`, `Trains`) VALUES ('{}','{}','{}','{}','{}')".format(name, date, supply, max_supply, income, trains)
        self.storage_cursor.execute(sql)
        self.storage.commit()

    def TrainsRes(self):
        self.trains_res = []
        sql = 'select * from '

        for name in self.train_names:
            self.inn_st_cursor.execute(sql + name)
            self.trains_res.append( self.inn_st_cursor.fetchall())
    
    def TermsRes(self):
        self.term_res = []
        sql = 'select * from '

        for name in self.term_names:
            self.inn_st_cursor.execute(sql + name)
            self.term_res.append( self.inn_st_cursor.fetchall())


