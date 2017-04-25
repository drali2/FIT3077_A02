from zeep import Client

class weather(object):
    '''
    Weather class, act as model and connection to the web services through the SOAP protocols
    @author: Denata & Katty
    @pre:  zeep install and implemented to connect to SOAP protocols. Web service must be valid.
    @post: Weather object created with relevant data.
    @version: 1.4.1
    '''
    def __init__(self,location):
        '''
        Initialization of weather object
        :param location:
        '''
        self.url = 'http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl'
        self.client = Client(self.url)
        self.location = location
        self.date = self.client.service.getTemperature(self.location)[0].split(" ")[0]
        self.time = self.client.service.getTemperature(self.location)[0].split(" ")[-1]
        self.temperature = self.client.service.getTemperature(self.location)[-1]
        self.rainfall = self.client.service.getRainfall(self.location)[-1]

    def update(self):
        '''
        Update values in Weather
        :return:
        '''
        self.date = self.client.service.getTemperature(self.location)[0].split(" ")[0]
        self.time = self.client.service.getTemperature(self.location)[0].split(" ")[-1]
        self.temperature = self.client.service.getTemperature(self.location)[-1]
        self.rainfall = self.client.service.getRainfall(self.location)[-1]

    def getTemperature(self):
        '''
        :return: updated Temperature
        '''
        return self.temperature

    def getRainfall(self):
        '''
        :return: Update getRainfall
        '''
        return self.rainfall

