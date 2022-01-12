import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers.phonenumberutil import is_valid_number

mobileNo = input("Enter mobile number with country code: ")
mobileNo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, "en"))

print(geocoder.description_for_number(mobileNo, "en"))

print(phonenumbers,is_valid_number(mobileNo))

print(phonenumbers.is_possible_number(mobileNo))