import pyotp

hotp = pyotp.HOTP('base32secret3232')
counter = 1401
c1 = hotp.at(0)
c2 = hotp.at(1) 
c3 = hotp.at(2)
c4 = hotp.at(counter)

# OTP verified with a counter
print(hotp.verify(c4, counter))
print(hotp.verify(c4, counter + 1))
