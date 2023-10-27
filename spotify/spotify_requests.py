from requests_oauth2client import *


class SpotifyRequests:
    CLIENT_ID = "cc2ad828bb30441d85e223f3b05f8f03"
    CLIENT_SECRET = "de1b88468aa9425093e4b7e200f5f728"
    REDIRECT_URL = "www.itfactory.ro"

    TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"
    AUTH_CREDENTIALS = (CLIENT_ID, CLIENT_SECRET)
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self):
        self.token = self.__gettoken()

    def __gettoken(self):
        oauth_client = OAuth2Client(self.TOKEN_ENDPOINT, auth=self.AUTH_CREDENTIALS)
        token = oauth_client.client_credentials(resource=self.REDIRECT_URL)
        return token

    def get_album(self, id):
        album_endpoint = self.BASE_URL + f"/albums/{id}"
        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"})
        return response

    # 1. test if we get the corresponding status code test if the body of the response contains an "artists" key, and it's value is a list
    # 2. get album with id and market test status code and content
    def get_album_market(self, id, market=None):
        album_endpoint = self.BASE_URL + f"/albums/{id}"
        query_params = {'market': market}
        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"},
                                params=query_params)
        return response

    # 3. get several albums test status code and content
    # 4. get several albums with id and markets
    def get_several_albums(self, ids, market):
        album_endpoint = self.BASE_URL + "/albums/"
        query_params = {'market': market, 'ids': ids}
        print(f"ids {ids}")
        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"},
                                params=query_params)
        return response

    # 5. get album tracks
    # https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks
    def get_album_tracks(self, id, market, limit='', offset='', album_tracks=None):
        album_endpoint = self.BASE_URL + f"/albums/{id}/tracks"
        query_params = {'market': market}

        if album_tracks != '' and limit == '':
            album_endpoint += f'?type={album_tracks}'

        if album_tracks == '' and limit != '':
            album_endpoint += f'?limit={limit}'

        if album_tracks != '' and limit != '':
            album_endpoint += f'?type={album_tracks}&limit={limit}'

        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"},
                                params=query_params)
        return response

    # 6. get artist
    # https://developer.spotify.com/documentation/web-api/reference/get-an-artist

    def get_artist(self, id):
        album_endpoint = self.BASE_URL + f"/artists/{id}"
        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"})
        return response

    # 7. get several artists
    # https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists

    def get_several_artists(self, ids):
        album_endpoint = self.BASE_URL + f"/artists/"
        query_params = {'ids': ids}
        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"},
                                params=query_params)
        return response

    # 8. get artist's albums
    # https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums
    def get_artists_albums(self, id, include_groups, market, limit, offset, artists_albums=None):
        album_endpoint = self.BASE_URL + f"/artists/{id}/albums"
        query_params = {'market': market}
        if artists_albums != '' and limit == '':
            album_endpoint += f'?type={artists_albums}'

        if artists_albums == '' and limit != '':
            album_endpoint += f'?limit={limit}'

        if artists_albums != '' and limit != '':
            album_endpoint += f'?type={artists_albums}&limit={limit}'

        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"},
                                params=query_params)
        return response

    # 9. get artist's top tracks
    # https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks

    def get_artist_top_tracks(self, id, market):
        album_endpoint = self.BASE_URL + f"/artists/{id}/top-tracks"
        query_params = {'market': market}

        response = requests.get(album_endpoint, headers={"Authorization": f"Bearer {self.token}"},
                                params=query_params)
        return response

# obj1 = SpotifyRequests()
# print(obj1.token)
# response = obj1.get_album('4aawyAB9vmqN3uQ7FjRGTy')
# print(response.status_code)
# print(response.json())
