from fastapi import APIRouter, Response
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException, PasswordMismatchException
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.crud_users import UserCrud
from app.users.schemas import SUserRegister, SUserAuth
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['Chat'])
templates = Jinja2Templates(directory='app/templates')


@router.get("/chat/", response_class=HTMLResponse, name="chat_page")
async def get_categories(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})