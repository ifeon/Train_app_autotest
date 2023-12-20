import requests
from typing import Optional
from requests import Response


class APIClient:

    def get(self,
            url: str,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
            ) -> Response:
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self,
             url: str,
             data: str | dict,
             params: Optional[dict] = None,
             headers: Optional[dict] = None
             ) -> Response:
        session = requests.Session()
        response = session.post(url, data=data, params=params, headers=headers)
        return response

    # def put(self,
    #         url: str,
    #         params: Optional[dict] = None,
    #         headers: Optional[dict] = None
    #         ) -> Response:
    #     response = requests.get(url, params=params, headers=headers)
    #     return response
    #
    # def delete(self,
    #            url: str,
    #            params: Optional[dict] = None,
    #            headers: Optional[dict] = None
    #            ) -> Response:
    #     response = requests.get(url, params=params, headers=headers)
    #
    #     return response
