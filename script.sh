printf "Getting token for Fyle account...\n"
TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=fyle&password=fyle_password' https://exercise-test.herokuapp.com/auth/token/ | jq -r '.access') 
printf "\nAccess token obtained : $TOKEN\n"
printf "\nGetting details of bank with IFSC: ABHY0065116\n\n"
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" https://exercise-test.herokuapp.com/api/bank/ABHY0065116/
printf "\n\nGetting branches of Allahabad Bank at Kolkata..\n\n"
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" https://exercise-test.herokuapp.com/api/bank/Allahabad%20Bank/Kolkata/
printf "\n\nGetting branches of Allahabad Bank at Kolkata with offset=100 and limit=10\n\n"
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" https://exercise-test.herokuapp.com/api/bank/Allahabad%20Bank/Kolkata/?offset=100&limit=10