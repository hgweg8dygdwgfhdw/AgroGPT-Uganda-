# AgroGPT Uganda API Documentation

Base URL: `/api/v1`

## Authentication

### Login
- **POST** `/token`
- **Description**: Authenticate user and get access token
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```

## Farm Management

### Create Farm
- **POST** `/farms/`
- **Auth**: Required
- **Request Body**:
  ```json
  {
    "name": "string",
    "location": "string",
    "size_hectares": "number",
    "main_crops": "string",
    "soil_type": "string"
  }
  ```

### Get User's Farms
- **GET** `/farms/`
- **Auth**: Required
- **Response**: List of farms

### Get Specific Farm
- **GET** `/farms/{farm_id}`
- **Auth**: Required
- **Parameters**:
  - `farm_id`: integer (path)

### Update Farm
- **PUT** `/farms/{farm_id}`
- **Auth**: Required
- **Parameters**:
  - `farm_id`: integer (path)
- **Request Body**: Same as Create Farm

### Delete Farm
- **DELETE** `/farms/{farm_id}`
- **Auth**: Required
- **Parameters**:
  - `farm_id`: integer (path)

## Crop Management

### Create Crop
- **POST** `/crops/`
- **Auth**: Required
- **Request Body**:
  ```json
  {
    "name": "string",
    "variety": "string",
    "planting_date": "datetime",
    "expected_harvest_date": "datetime",
    "field_location": "string",
    "area_size": "number",
    "description": "string"
  }
  ```

### Get User's Crops
- **GET** `/crops/`
- **Auth**: Required
- **Response**: List of crops

### Get Specific Crop
- **GET** `/crops/{crop_id}`
- **Auth**: Required
- **Parameters**:
  - `crop_id`: integer (path)

### Update Crop
- **PUT** `/crops/{crop_id}`
- **Auth**: Required
- **Parameters**:
  - `crop_id`: integer (path)
- **Request Body**: Same as Create Crop (all fields optional)

### Delete Crop
- **DELETE** `/crops/{crop_id}`
- **Auth**: Required
- **Parameters**:
  - `crop_id`: integer (path)

## Weather Services

### Get Current Weather
- **GET** `/weather/current/{location}`
- **Auth**: Required
- **Parameters**:
  - `location`: string (path)

### Get Weather Forecast
- **GET** `/weather/forecast/{location}`
- **Auth**: Required
- **Parameters**:
  - `location`: string (path)
  - `days`: integer (query, default=7)

### Get Weather Alerts
- **GET** `/weather/alerts/{location}`
- **Auth**: Required
- **Parameters**:
  - `location`: string (path)

### Get Agricultural Metrics
- **GET** `/weather/agricultural-metrics/{location}`
- **Auth**: Required
- **Parameters**:
  - `location`: string (path)

## Disease Diagnosis

### Diagnose Disease
- **POST** `/diagnose-disease`
- **Request Body**:
  ```json
  {
    "image_url": "string",
    "description": "string",
    "crop_type": "string",
    "language": "string"
  }
  ```

## Market Information

### Get Market Prices
- **GET** `/market-prices`
- **Parameters**:
  - `crop`: string (query)
  - `region`: string (query)
  - `language`: string (query, default="en")

## SMS Services

### Send SMS
- **POST** `/send-sms`
- **Request Body**:
  ```json
  {
    "phone_number": "string",
    "message": "string"
  }
  ```

### Handle USSD
- **POST** `/ussd`
- **Parameters**:
  - `session_id`: string (query)
  - `phone_number`: string (query)
  - `ussd_code`: string (query)
  - `text`: string (query)

## Utility Endpoints

### Get Supported Languages
- **GET** `/supported-languages`
- **Response**:
  ```json
  {
    "status": "success",
    "languages": {
      "en": "English",
      "lg": "Luganda",
      "nyn": "Runyankole",
      "ach": "Acholi"
    }
  }
  ```

### Get Supported Regions
- **GET** `/supported-regions`
- **Response**:
  ```json
  {
    "status": "success",
    "regions": ["central", "eastern", "northern", "western"]
  }
  ```

## Error Responses

All endpoints may return the following error responses:

- **401 Unauthorized**:
  ```json
  {
    "detail": "Could not validate credentials"
  }
  ```

- **403 Forbidden**:
  ```json
  {
    "detail": "Not authorized to access this resource"
  }
  ```

- **404 Not Found**:
  ```json
  {
    "detail": "Resource not found"
  }
  ```

- **500 Internal Server Error**:
  ```json
  {
    "detail": "Internal server error message"
  }
  ``` 