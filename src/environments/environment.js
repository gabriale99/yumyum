export const environment = {

  production: true,

  // TODO: make sure you have the correct region
  region: 'us-east-1',


  // TODO: This id can be retrieved in output section of the cognito ui
  // cloud formation stack.
  cognitoIdentityPoolId: 'us-east-1:dc7e6ff8-3555-4f6f-ba1b-a30c5510fe13',

  // TODO: Facebook app id can be retrieved from the application in your
  // facebook developer account.
  facebookAppId: '2550952455058803',

  // TODO: The API URL is available in the API Gateway console under Stage
  // NOTE: don't forget trailing "/"  For example:
  // https://api.example.com/prod/
  yumyumapi: 'https://x5w7nr0vf9.execute-api.us-east-1.amazonaws.com'

};