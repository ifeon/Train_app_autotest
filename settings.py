from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    base_url: str
    login: str
    password: str

    @property
    def api_url(self) -> str:
        return f'{self.base_url}/api'


base_settings = Settings()
