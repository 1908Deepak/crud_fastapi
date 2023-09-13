
# FastAPI - CRUD Operations
CRUD refers to the four basic operations a software application should be able to perform – Create, Read, Update, and Delete.

In such apps, users must be able to create data, have access to the data in the UI by reading the data, update or edit the data, and delete the data.

In full-fledged applications, CRUD apps consist of 3 parts: an API (or server), a database, and a user interface (UI).

The API contains the code and methods, the database stores and helps the user retrieve the information, while the user interface helps users interact with the app.




## Requirements

 - [Python](https://www.python.org/downloads/)
 - [MongoDB](https://account.mongodb.com/account/register)
 - [VsCode](https://code.visualstudio.com/download)
 - [BootStrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
 


## Installation
```bash
  pip install virtualenv
```
Create virtualenv 
```bash
  python -m virtualenv XYZ(FolderName)

```
Install Dependencies
```bash
  pip install fastapi
  pip install uvicorn
  pip install pydantic
  pip install pymongo
  pip install Jinja2
  pip install multipart
```


    
## Clone Repository
```bash
  git clone https://github.com/1908Deepak/crud_fastapi.git
```
## Database Connection
```bash
  mongodb+srv://alford:alford@cluster0.kljzgft.mongodb.net/?retryWrites=true&w=majority
```


## Deployment

To deploy this project run

```bash
  uvicorn fastapi_crud_ui_server:app
```


## Roadmap

- Download latest Version of python and set the path variable of Python if needed.

- Now, Download the package virtualenv by using the command "pip install Virtualenv"

- Create virtual env by using the command python -m virtualenv XYZ(foldername).
- Now move to Script folder after virtual environment created and now use command "activate" to activate the virtualenv.
- Now create a mongoDb account and creater your database user and password.
- After that install all the above listed dependencies using "pip install XYZ.
- Now clone the github repository in XYZ(folder) using "git clone https://github.com/1908Deepak/crud_fastapi.git".
- Now connect your appliaction with MongoDB using "Mongo Client url generated during the database creation in fastapi_crud_ui_server.py file"
- Now run the command "uvicorn fastapi_crud_ui_server:app"




## Tech Stack

**Client:** HTML , CSS , Bootstrap , JavaScript

**Server:** Python

**Database:** MongoDB


## Work Demo
 [Assigment](https://drive.google.com/file/d/1KoAihq_0_wkei8IFUJueidCMt2oYqlj3/view?usp=drivesdk)



## Support

For support, email deepaksingh190810@gmail.com


## License

[MIT](https://choosealicense.com/licenses/mit/)



