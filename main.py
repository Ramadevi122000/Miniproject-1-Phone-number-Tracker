#importing library
import phonenumbers
from test import number

#number = "+91 9876543210"
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH") #Country History
print(geocoder.description_for_number(ch_number, "en"))  #displays  the country name of the number


#service provider of number
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))


#Timezone of the number
from phonenumbers import timezone
gb_number = phonenumbers.parse(number,"GB")
print(timezone.time_zones_for_number(gb_number))