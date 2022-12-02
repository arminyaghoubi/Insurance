import pyodbc as pyodbc


class BaseAccessLayer:
    def __init__(self):
        self.connectionString = "Driver={SQL Server};" \
                                "Server=.;" \
                                "Database=Insurance;" \
                                "Trusted_Connection=yes;"

    def getAllEntity(self, commandText):
        with pyodbc.connect(self.connectionString) as connection:
            command = connection.cursor()
            command.execute(commandText)
            return command.fetchall()

    def getFirstEntity(self, commandText,params):
        with pyodbc.connect(self.connectionString) as connection:
            command = connection.cursor()
            command.execute(commandText,params)
            return command.fetchone()

    def execute(self, spname, params):
        with pyodbc.connect(self.connectionString) as connection:
            command = connection.cursor()
            command.execute(f'Execute {spname}', params)
            id = command.fetchone()[0]
            command.commit()
            return id
