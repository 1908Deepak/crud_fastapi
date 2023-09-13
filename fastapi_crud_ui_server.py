__author__="Deepak Singh"

#imports
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response,status
from pymongo import MongoClient
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, Cookie, Depends
from starlette.responses import RedirectResponse, Response
import datetime,time

#MongoDB Connection info
client = MongoClient("mongodb+srv://alford:alford@cluster0.kljzgft.mongodb.net/?retryWrites=true&w=majority")
#Database
pets_db = client['pets_db']
#Collection
user_collection = pets_db['user']

#Model
class User(BaseModel):
    user_id: int
    user_name: str
    user_image:str
    user_email:str
    user_password:str
    user_mobile:str
    user_description:str

#Initialize
app = FastAPI()

#Static file serv
app.mount("/static", StaticFiles(directory="static"), name="static")
#Jinja2 Template directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/user/{id}", response_class=HTMLResponse)
def read_user(request: Request, id: int):
    print('find user called with id :'+str(id))
    result = user_collection.find_one({'user_id': id})
    print(result['user_name'])
    return templates.TemplateResponse("view_user.html", {"request": request, "user": result})

@app.get("/user", response_class=HTMLResponse)
def read_all_user(request: Request):
    result = user_collection.find({})
    print(result)
    return templates.TemplateResponse("list_user.html", {"request": request, "user_list": result})

@app.get("/createui", response_class=HTMLResponse)
async def create_user_ui(request: Request):
    return templates.TemplateResponse("new_user.html", {"request": request})


@app.post("/create",response_class=HTMLResponse)
def create_user(request:Request,userId:str = Form(...),userName:str = Form(...),userImage:str = Form(...),userEmail:str = Form(...),userPassword:str = Form(...),userMobile:str = Form(...),userDescription:str = Form(...)):
    print('user_id :'+str(userId) +', user_name:'+str(userName)+', userimage:'+str(userImage)+', fisdescription:'+str(userDescription),'user_email:'+str(userEmail)+',user_password:'+str(userPassword)+'user_mobile:'+str(userMobile))
    #initialize the model
    user = User(user_id=userId,user_name=userName,user_image=userImage,user_email=userEmail,user_password=userPassword,user_mobile=userMobile,user_description=userDescription)
    print(str(user.dict()))
    id = user_collection.insert_one(user.dict()).inserted_id
    print(" User added : now db size " + str(id))
    time.sleep(1)
    result = user_collection.find({})
    return templates.TemplateResponse("list_user.html", {"request": request, "user_list": result})


@app.get("/user/delete/{id}",response_class=HTMLResponse)
def delete_user(id:int,response:Response,request:Request):
    print(" delete user method called :"+str(id))
    result = user_collection.delete_one({'user_id':id})
    time.sleep(1)
    result = user_collection.find({})
    print(result)
    return templates.TemplateResponse("list_user.html", {"request": request, "user_list": result})

@app.get("/user/edit/{id}",response_class=HTMLResponse)
def edit_user(id:int,response:Response,request:Request):
    print(" method called :"+str(id))
    result = user_collection.find_one({'user_id':id})
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": result})

@app.post("/update",response_class=HTMLResponse)
def update_user(request:Request,response:Response,userId:str = Form(...),userName:str = Form(...),userImage:str = Form(...),userDescription:str = Form(...),userEmail:str = Form(...),userPassword:str = Form(...),userMobile:str = Form(...)):
    print('user_id :'+str(userId))
    print('username '+str(userName))
    print('userimage ' + str(userImage))
    print('user_email ' + str(userEmail))
    print('user_password ' + str(userPassword))
    print('user_mobile ' + str(userMobile))
    print('userdescription ' + str(userDescription))
    #initialize the model
    user = User(user_id=userId,user_name=userName,user_image=userImage,user_email=userEmail,user_password=userPassword,user_mobile=userMobile,user_description=str(userDescription))
    print(str(user.dict()))
    #call internal api
    update_api(user)
    time.sleep(1)
    #get the updated list
    result = user_collection.find({})
    print(str(result))
    return templates.TemplateResponse("list_user.html", {"request": request, "user_list": result})


@app.put("/updateapi",status_code=202)
def update_api(user:User):
    print('Update api called....'+str(user.user_name))
    result = user_collection.update_one({'user_id':user.user_id},{"$set" : {'user_name':user.user_name}})
    return "UPDATE SUCCESS"

