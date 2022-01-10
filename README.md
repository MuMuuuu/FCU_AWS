# API List

## Database (class)
### init_connect
- Description : Connect to specific MongoDB

### get_user
- Description : Find user

### create_user
- Description : Create user in MongoDB for /register

### update_user_location
- Description : Update user's location for /{store}/report

### get_store_locations
- Description : List all locations for /profile

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

### Profile
- Path : /profile
- Description : List account data
- Input : jwt token
- Return - True : username , password , location , phone
- Return - False : Exception(403 , JWTDecodeError)

## Store
### QRCode Generator
- Path : /{store}/qrcode
- Description : Generate QRCode for user to scan
- Input : store
- Return : base64(QRCode) 

### Visitors List
- Path : /{store}/history
- Description : List all visitors
- Input : jwt
- Return - True : List([username])
- Return - False : Exception(403 , JWTDecodeError)

### Update Location
- Path : /{store}/report
- Description : Update user's location by scanning QRCode
- Input : jwt , location
- Return - True : status 200
- Return - False : Exception(403 , JWTDecodeError)

## Auth
### parse_token
- Description : Check jwt token for login

### get_login_state
- Descriptino : Return loginstate for React.Index.jsx 
