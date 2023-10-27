import unittest

from spotify.spotify_requests import SpotifyRequests


class SpotifyRequestTests(unittest.TestCase):
    def setUp(self):
        self.spotify = SpotifyRequests()

    # 1. get album with id, test status code and content
    # https://developer.spotify.com/documentation/web-api/reference/get-an-album

    def test_get_album(self):
        resp_album = self.spotify.get_album('4aawyAB9vmqN3uQ7FjRGTy')
        # test if we get the corresponding status code
        assert 200 == resp_album.status_code

        # test if the body of the response contains an "artists" key, and it's value is a list

        is_artists_present = resp_album.json()['artists'] is not None

        assert is_artists_present
        is_list = isinstance(resp_album.json()['artists'], list)
        assert is_list

    # 2. get album with id and market test status code and content
    def test_get_album_market(self):
        resp_album_market = self.spotify.get_album_market('4aawyAB9vmqN3uQ7FjRGTy', market="ES")
        # test if we get the corresponding status code
        assert 200 == resp_album_market.status_code

        is_album_dict = isinstance(resp_album_market.json(), dict)
        print(resp_album_market.json())
        assert is_album_dict

    # 3. get several albums test status code and content
    def test_several_albums(self):
        resp_several_albums = self.spotify.get_several_albums("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,"
                                                              "2noRn2Aes5aoNVsU6iWThc", market="ES")
        print(resp_several_albums.status_code)
        # test if we get the corresponding status code
        assert 200 == resp_several_albums.status_code

        is_album_dict = isinstance(resp_several_albums.json(), dict)
        print(resp_several_albums.json())
        assert is_album_dict

        albums = resp_several_albums.json()["albums"]
        print(len(albums))
        assert len(albums) == 3

        # testam faptul ca primim info cu privire la cele 3 albume mentionate
        print(albums[0]["id"])
        assert "382ObEPsp2rxGrnsizN5TX" == albums[0]["id"]
        assert "1A2GTWGtFfWp7KSQTwWOyo" == albums[1]["id"]
        assert "2noRn2Aes5aoNVsU6iWThc" == albums[2]["id"]

    # Alta varianta

    # folosim self.assetIn verificam existenta unei chei in primul dictionar din lista de albume
    # self.assertIn(member="id", container=albums[0], msg="Sucess")

    # 5. get album tracks
    # https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks

    def test_album_tracks(self):
        resp_album_tracks = self.spotify.get_album_tracks("4aawyAB9vmqN3uQ7FjRGTy", market="ES", limit=10, offset=5)
        print(resp_album_tracks.status_code)
        # test if we get the corresponding status code
        assert 200 == resp_album_tracks.status_code

        is_album_dict = isinstance(resp_album_tracks.json(), dict)
        print(resp_album_tracks.json())
        assert is_album_dict

        items = resp_album_tracks.json()["items"]
        print(len(items))
        # validam ca avem 10 tracks pe albumul cu id "4aawyAB9vmqN3uQ7FjRGTy"
        assert len(items) == 10
        # Alternativa self.assert
        self.assertEqual(10, len(items), msg="Error number of tracks")

    # 6. get artist

    def test_artist(self):
        resp_artist = self.spotify.get_artist('0TnOYISbd1XYRBk9myaseg')
        # test if we get the corresponding status code
        assert 200 == resp_artist.status_code

        is_album_dict = isinstance(resp_artist.json(), dict)
        # print(resp_artist.json())
        assert is_album_dict

        genres = resp_artist.json()["genres"]
        print(len(genres))
        # validam ca avem 3 genuri pe albumul cu id "0TnOYISbd1XYRBk9myaseg"
        assert len(genres) == 3

        name = resp_artist.json()["name"]
        # print(name)
        self.assertEqual("Pitbull", name, msg="Error the name doesn't match")

    def test_several_artists(self):
        resp_several_artists = self.spotify.get_several_artists("2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,"
                                                                "1vCWHaC5f2uS3yhpwWbIA6")
        # print(resp_several_artists.request.headers)
        # print(resp_several_artists.request.url)
        assert 200 == resp_several_artists.status_code

        is_album_dict = isinstance(resp_several_artists.json(), dict)
        # print(resp_several_artists.json())
        assert is_album_dict

        nr_of_artists = len(resp_several_artists.json()["artists"])
        # print(nr_of_artists)
        # validam ca am primit acelasi nr de artisti cate id am dat in metoda get_several_artists (3)
        assert nr_of_artists == 3



    def test_artists_albums(self):
        resp_artists_albums = self.spotify.get_artists_albums("0TnOYISbd1XYRBk9myaseg",
                                                              include_groups="single, appears_on", market="ES",
                                                              limit=10, offset=5)
        # print(resp_artists_albums.status_code)
        # test if we get the corresponding status code
        assert 200 == resp_artists_albums.status_code

        is_album_dict = isinstance(resp_artists_albums.json(), dict)
        # print(resp_artists_albums.json())
        assert is_album_dict

    def test_artist_top_tracks(self):
        resp_artist_top_tracks = self.spotify.get_artist_top_tracks('0TnOYISbd1XYRBk9myaseg', market="ES")
        print(resp_artist_top_tracks.status_code)
        # test if we get the corresponding status code
        assert 200 == resp_artist_top_tracks.status_code

        is_album_dict = isinstance(resp_artist_top_tracks.json(), dict)
        print(resp_artist_top_tracks.json())
        assert is_album_dict

    # CTRL + ALT + L, formateaza un fisier, pentru a fi mai usor de citit
