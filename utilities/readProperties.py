import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")






class ReadConfig:
    def __init__(self):
        # Initialization code, if any
        pass

   
    def getApplicationURL(self):
        url = config.get('common info', 'baseURL')
        return url

    
    def getApplicationUsername(self):
        usrname = config.get('common info', 'username')
        return usrname

    def getApplicaitonpassword(self):
        pwd = config.get('common info', 'password')
        return pwd
    


    
