from zeep import Client

class weather(object):
    def __init__(self,location):
        self.url = 'http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl'
        self.client = Client(self.url)
        self.location = location
        self.date = self.client.service.getTemperature(self.location)[0].split(" ")[0]
        self.time = self.client.service.getTemperature(self.location)[0].split(" ")[-1]
        self.temperature = self.client.service.getTemperature(self.location)[-1]
        self.rainfall = self.client.service.getRainfall(self.location)[-1]

    def update(self):
        self.date = self.client.service.getTemperature(self.location)[0].split(" ")[0]
        self.time = self.client.service.getTemperature(self.location)[0].split(" ")[-1]
        self.temperature = self.client.service.getTemperature(self.location)[-1]
        self.rainfall = self.client.service.getRainfall(self.location)[-1]

    def getTemperature(self):
        return self.temperature

    def getRainfall(self):
        return self.rainfall

