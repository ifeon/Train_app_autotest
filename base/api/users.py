import json

from clients.http.client import APIClient
from constants.routes import APIRoutes
from settings import base_settings


class AuthenticationClient(APIClient):
    base_data = {"login": base_settings.login,
                 "pass": base_settings.password}

    def get_all_users(self):
        url = f'{base_settings.api_url}{APIRoutes.USERS}'
        response = self.get(url)
        return response.json()

    def user_signup(self, data=None):
        if data is None:
            data = self.base_data
        url = f'{base_settings.api_url}{APIRoutes.SIGNUP}'
        headers = {'Content-Type': 'application/json'}
        response = self.post(url, data=json.dumps(data), headers=headers)
        return response.json()

    def user_login(self, data=None):
        if data is None:
            data = self.base_data
        url = f'{base_settings.api_url}{APIRoutes.LOGIN}'
        headers = {'Content-Type': 'application/json'}
        response = self.post(url, data=json.dumps(data), headers=headers)
        jwt_token = response.json()['token']
        return jwt_token

    def user_info(self, jwt_token):
        url = f'{base_settings.api_url}{APIRoutes.USER}'
        headers = {'Authorization': jwt_token}
        response = self.get(url, headers=headers)
        return response.json()

    # def user_pass_update(self):
    #     url = f'{base_settings.api_url}{APIRoutes.USER}'
    #     response = self.get(url)
    #     return response.json()
    #
    # def user_delete(self):
    #     url = f'{base_settings.api_url}{APIRoutes.USER}'
    #     response = self.get(url)
    #     return response.json()
    #
