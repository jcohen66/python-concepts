import pyotp
import time


totp = pyotp.TOTP('base32secret3232')
now = totp.now()
print(now)

#OTP verified for current time
print(totp.verify(now))
time.sleep(30)
print(totp.verify(now))



