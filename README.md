# chat_bot_backend

**How to run through bash in linux machine:-**

- step1:-
    Make the script executable using the chmod command:
    chmod +x run_backend.sh

- step2:- run the script in your terminal to execute both steps by the following commands:
        ./run_backend.sh

**How to run through bash in windows machine:-**

- step1:- run the command
        run_backend.bat


**How to run Through terminal :-**

- step1:- clone the chat_bot_backend repository on your local machine.
- step2:- go into the folder cloned folded where Dockerfile is present.

The below command will create a docker image.
- step3:- run the command in terminal:- docker build -t backend .


The below command will run the docker image of the backend in a container
- step4:- docker run -d -p 8000:8000 --name backend-container backend


After starting the Container you will have to wait for several minutes(depending on the internet speed)  so that the **llama2** can load on the backend and then the server can start.