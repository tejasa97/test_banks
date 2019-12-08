# test_banks

Hosting URL : https://exercise-test.herokuapp.com/

Database : Added the first *9780* rows from the `branches` table to Heroku Postgres addon (free tier)<br>
Requirement : **jq** package to parse the JWT token from the authentication API response. <br>

Installation:<br>
``` sudo apt install jq ```<br>

Then the `script.sh` file which contains the necessary CURL requests to demonstrate the various APIs can be executed.<br>
Usage :<br>
```./script.sh```

API calls made:<br>
1. Get an access token for the *Fyle* account (valid for 5 days).<br>
Using the obtained token,<br>
2. Get a bank branch with the IFSC code as input.<br>
3. Get the branches of a bank in a city. <br>
4. Get the branches of a bank in a city with *offset* and *limit* parameters.
