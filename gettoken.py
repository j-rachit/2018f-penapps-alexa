import requests

blah = requests.post("http://pennapps.us-east-1.elasticbeanstalk.com/api/login",
                     data={"username": "test", "password": "password"})
print blah.text
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJyb2xlIjoicGF0aWVudCIsImlhdCI6MTUzNjQzNjQxOSwiZXhwIjoxNTk5NTA4NDE5fQ.z7eRo6TiGrhEW5dK2_-V6d2MK8hT40RZ-ztecYjIjPQ
