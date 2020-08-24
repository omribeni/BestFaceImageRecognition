# BestFaceImageRecognition
Retrieve best recognize image from local images paths using azure face api


Steps to use:

1. configure the enviermant verable  'FACE_ENDPOINT' and 'FACE_SUBSCRIPTION_KEY' to your azure face account
2. run the program.py main to start the server.
3. the server has 2 endpoint. http://localhost:'port given'/BestImage will answer this task.
  3.1 run a post request to that url with a json body of type {"data":[{"path": "local path 1"},{"path":"local path 2"}]}
4. the program will return the most popular face's best image json as returned from the azure api.
