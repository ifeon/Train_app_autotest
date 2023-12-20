from pydantic import BaseModel, Field

from settings import base_settings


class AuthUser(BaseModel):
    login: str = Field(default=base_settings.login)
    password: str = Field(default=base_settings.password)


class Authentication(BaseModel):
    auth_token: str | None = None
    user: AuthUser | None = AuthUser()


class CreateUser(BaseModel):
    login: str = Field(default=base_settings.login)
    password: str = Field(default=base_settings.password)


class DeleteUser(BaseModel):
    token: str
