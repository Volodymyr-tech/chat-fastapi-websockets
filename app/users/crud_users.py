from app.crud.base_crud import BaseCrud
from app.users.models import User


class UserCrud(BaseCrud):
    model = User
