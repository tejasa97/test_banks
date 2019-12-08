# test_banks

Hosting URL : https://exercise-test.herokuapp.com/

Database : Added the first *9780* rows from the `branches` table to Heroku Postgres addon (free tier)

Requirement : **jq** package to parse the JWT token from the authentication API response

Installation:

``` sudo apt install jq ```

Then the `script.sh` file which contains the necessary CURL requests to demonstrate the various APIs can be executed.

Usage : 

```./script.sh```

API calls made:

1. Get an access token for the *Fyle* account (valid for 5 days).

Using the obtained token,

2. Get a bank branch with the IFSC code as input.

3. Get the branches of a bank in a city. 

4. Get the branches of a bank in a city with *offset* and *limit* parameters.
