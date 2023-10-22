import  phonenumbers
from number import number

from phonenumbers import  geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)