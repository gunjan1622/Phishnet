from PhishnetAPI.services.Address import AddressBar as addr
import time

print(addr.get_url())
addr.set_url("https://www.google.com")
time.sleep(5)

addr.redirect_url("https://www.google.com")