# Task-1-Secure-Encoding

## Overview
Here we can see three different files where in foundation.py file we can encode or decode any message or letter in it. Whereas, on the other cilent and server file we can established a commucation using the socket. Normal we can communicate in socket, it is secured because whenever the hacker tries to read the text, hackers cannot read it because it has encoded message in between the path.
## Learning Objective
- Understanding Encoding
- Analyze Injection Prevention
- Evaluate Efficiency
- Protocal  Interoperability

## Tools and Tech
- Python
- base64, urllib.prase, zlib, json
## Setup
```bash
#clone the repo
git clone https://github.com/Phurbasherpa13/Task-1-Secure-Encoding.git
cd Task-1-Secure-Encoding
```

## Procedure 
- Installation
Since this project uses Python's standard libraries, there is no need of external pip install.
- Running the script
```bash
python foundation.py
# for any string or message to encode or decode it 
```
- Result
<img src="/image.png" height="500" width="500">

As we can see we inputed the text hello world and it excuted and shows the outcome "aGVsbG8gd29ybGQ=" in base64 and "hello%20world" in URL encoding.

As we can also connect to the server and client where we host a connection inbetween clinet so we can generate a messaage which is secure and concept of HTTP format.

# Author
- Phurba Sherpa
# License
- This project is under MIT License. [license](https://github.com/Phurbasherpa13/Task-1-Secure-Encoding/blob/main/LICENSE)

