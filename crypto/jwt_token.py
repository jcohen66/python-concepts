from jwcrypto import jwk, jwt
import json

with open('key.pem', 'rb') as pemfile:
    key = jwk.JWK.from_pem(pemfile.read())
    
publickey = key.export(private_key=False)
print(publickey)

jwks = {}
jwks["keys"] = [json.loads(publickey)]

print(jwks)

with open("jwks.json", "w") as h:
    h.write(json.dumps(jwks))
    
Token = jwt.JWT(    
    header = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": key.key_id,
        "jkd": "http://johnhammond.org/tmp/jwks.json"
    },
    claims={'username': 'admin', "iat": 1627389731, "exp": 99999999}
)


Token.make_signed_token(key)
print(Token.serialize())