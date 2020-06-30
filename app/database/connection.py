import pymysql


class Connection:
    def __init__(self, config_parameters):
        self.config_parameters = config_parameters

    def create_connection(self):
        try:
            connection = pymysql.connect(**self.config_parameters)
            return connection
        except pymysql.Error as e:
            print("database Connection Error - ", e)


    @staticmethod
    def close_connection(connection):
        connection.close()
