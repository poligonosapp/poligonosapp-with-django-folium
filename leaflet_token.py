# https://github.com/mapbox/tilesets-cli

# https://jwcrypto.readthedocs.io/en/latest/jwt.html#examples

from jwcrypto import jwt, jwk
k = {"k": "Wal4ZHCBsml0Al_Y8faoNTKsXCkw8eefKXYFuwTBOpA", "kty": "oct"}
key = jwk.JWK(**k)
e = u'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0.ST5RmjqDLj696xo7YFTFuKUhcd3naCrm6yMjBM3cqWiFD6U8j2JIsbclsF7ryNg8Ktmt1kQJRKavV6DaTl1T840tP3sIs1qz.wSxVhZH5GyzbJnPBAUMdzQ.6uiVYwrRBzAm7Uge9rEUjExPWGbgerF177A7tMuQurJAqBhgk3_5vee5DRH84kHSapFOxcEuDdMBEQLI7V2E0F57-d01TFStHzwtgtSmeZRQ6JSIL5XlgJouwHfSxn9Z_TGl5xxq4TksORHED1vnRA.5jPyPWanJVqlOohApEbHmxi3JHp1MXbmvQe2_dVd8FI'
ET = jwt.JWT(key=key, jwt=e)
ST = jwt.JWT(key=key, jwt=ET.claims)
ST.claims
u'{"info":"I\'m a signed token"}'
