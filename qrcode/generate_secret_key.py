# Use with https://github.com/soldair/node-qrcode to render qr code.
import pyotp

# For use with Google Authenticator.
def generate_google32_secret():
    return pyotp.random_base32()

# 40 char hex-encoded secret.
def generate_hex_secret():
    return pyotp.random_hex()

def qr_provisioning_uri(password, provisioner, app_name):
    return pyotp.hotp.HOTP(password).provisioning_uri(name=provisioner, issuer_name=app_name, initial_count=0)

if __name__ == "__main__":

    print(pyotp.random_base32()) 
    print(pyotp.random_hex())

    otp1 = qr_provisioning_uri('JBSWY3DPEHPK3PXP', 'jcohen66g@gmail.com', 'my_app.com')
    print(otp1)

    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    print("Current OTP:", totp.now())