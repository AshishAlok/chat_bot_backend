# chat_bot_backend
**Points to be noted**
- I have created the git hub workflow actions which creates a docker image of the app whenever a push is made into the repository. This image gets stored on the Docker Hub which can be easily pulled.
- Using **bb.yaml** file I have successfully deployed my application to a Kubernetes environment on my development machine.
- **bash** files for both ubuntu and windows has been provided to run the app easily and succesfully.
- **Django** for front end and **streamlit** for frontend has been used.

**TO PROCEED CLONE THE CHAT_BOT_BACKEND REPOSITORY**

**How to run through bash file in linux machine:-**

- step1:-
    go into the cloned folder and make the script executable using the chmod command:
    chmod +x run_backend.sh

- step2:- run the script in your terminal to execute the steps by the following commands:
        ./run_backend.sh

**How to run through bash file in windows machine:-**

- step1:- go into the cloned folder and run the command
        run_backend.bat


**How to run through terminal (machine having Docker) :-**

- step1:- clone the chat_bot_backend repository on your local machine.
- step2:- go into the folder cloned folded where Dockerfile is present.
- step3:- run the command **./login_cred_HF.sh** if in linux or **login_cre_HF.bat** if in windows.
The below command will create a docker image.
- step4:- run the command in terminal:- docker build -t backend .


The below command will run the docker image of the backend in a container
- step5:- docker run -d -p 8000:8000 --name backend-container backend


**Note**:- After starting the Container you will have to wait for several minutes(depending on the internet speed)  so that the **llama2** can load on the backend and then the server can start. 