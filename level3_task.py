from datetime import date
import re
# task 10 
def num_of_days(date1, date2):
    if date2 > date1:  
        return (date2-date1).days
    else:
        return (date1-date2).days
 

date1 = date(2018, 12, 13)
date2 = date(2015, 2, 25)
print(num_of_days(date1, date2), "days")



# task 11
class TemperatureConverter:
    def __init__(self):
        message = """
----------------------------------------------------------------
convertToFahrenheit() take temperature as a parameter in Celcius
convertToCelcius() take temperature as a parameter in Fahrenheit
----------------------------------------------------------------
        """
        print(message)

    def convertToFahrenheit(self, temperature):
        return  (temperature * 9/5) + 32, 'F'
    
    def convertToCelcius(self, temperature):
        return  (temperature - 32) * 5/9, 'C'
    
convertor = TemperatureConverter()
print(convertor.convertToFahrenheit(50))
print(convertor.convertToCelcius(50))



# task 12
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
    if(re.fullmatch(regex, email)):
        return email
    else:
        raise Exception("Invalid Email")
            
 
def email_spliter(function):
    username, domain = function.split('@')
    return f"username : {username}, domain : {domain}"

print(email_spliter(check('test123456789@test.com')))

# task 13

class CurrencyConverter:
    def __init__(self):
        message = """
----------------------------------------------------------------
DollarToEgyptPound() take money as a parameter in dollar currency
EgyptPoundToDollar() take money as a parameter in Egyptian pound currency
AutoDetect() take 3 parameters money , from_, to 
          |
          ----> AutoDetect(money=555 ,from_='$' ,to= 'LE')
----------------------------------------------------------------
        """
        print(message)

    @classmethod
    def raise_exception(cls):
        raise Exception("Error : can't handle this")

    def DollarToEgyptPound(self, money):
        return f"{money * 30.9} LE"
    
    def EgyptPoundToDollar(self, money):
        return f"{money / 30.9} $"
    
    def AutoDetect(self, money ,from_,to ):
        if from_ == '$' and to == 'LE':
            return self.DollarToEgyptPound(money)
        elif from_ == 'LE' and to == '$':
            return self.EgyptPoundToDollar(money)
        else:
            self.raise_exception()
    

currencyConvertor = CurrencyConverter()
print(currencyConvertor.DollarToEgyptPound(1000))
print(currencyConvertor.EgyptPoundToDollar(30900))
print(currencyConvertor.AutoDetect(1000, '$', 'LE'))
print(currencyConvertor.AutoDetect(30900, 'LE', '$'))
print(currencyConvertor.AutoDetect(5000, '$', '$'))

