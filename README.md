# API List

## Main
### Login
- Path : /login
- Description : For User and Store login
- Input : username , password
- Return - True : status 200 , jwt token
- Return - False : status 404

### Register
- Path : /register
- Description : For User register
- Input : username , password , phone
- Return - True : status 200 , jwt token
- Return - False : Exception(409 , User already exists)

### Update Location
- Path : /report/{store}/
- Description : Update user's location by scanning QRCode
- Input : jwt , location
- Return - True : status 200
- Return - False : Exception(403 , JWTDecodeError)

### Profile
- Path : /profile
- Description : List account data
- Input : jwt token
- Return - True : username , password , location , phone
- Return - False : Exception(403 , JWTDecodeError)

### QRCode Generator
- Path : /{store}/qrcode
- Description : Generate QRCode for user to scan
- Input : store
- Return : base64(QRCode) 

### Visitors List
- Path : /{store}/list
- Description : List all visitors
- Input : jwt
- Return - True : List([username])
- Return - False : Exception(403 , JWTDecodeError)
