from datetime import date
import json
from django.test import TestCase, Client
from players.models import Player
# Create your tests here.


class PlayerTestCase(TestCase):
    # set up some mock data to run our tests
    def setUp(self):
        Player.objects.create(identifier=3030,
                              first_name="Ulas Eren",
                              last_name="Demir",
                              team="Fenerbahce",
                              position="Defender",
                              image="ulaserendemir.jpg")

        Player.objects.create(identifier=3434,
                              first_name="Furkan",
                              last_name="Ertas",
                              team="Fenerbahce",
                              position="Midfielder",
                              image="furkanertas.jpg")

        self.client = Client()  # Initialize the client

    def test_get_players(self):
        # send a retrieve all players request
        response = self.client.get('/api/players')
        # If the response is 200, test case is passed.
        self.assertEqual(response.status_code, 200)

        # slice the time fields in date-time
        editCreatedAt = response.json()[0]['created_at'][0:10]
        # slice the time fields in date-time
        editUpdatedAt = response.json()[0]['updated_at'][0:10]

        # update the datetime values, now they only contain date
        response.json()[0]['created_at'] = editCreatedAt
        # update the datetime values
        response.json()[0]['updated_at'] = editUpdatedAt

        # print("\n\n", response.json()[0], "\n\n") #debugging purposes

        # if the response equals to the mock data, test case is passed.
        self.assertEqual(response.json()[0], {'identifier': 3030, 'first_name': "Ulas Eren", 'last_name': 'Demir', 'team': 'Fenerbahce',
                         'position': 'Defender', 'image': 'ulaserendemir.jpg'})

    # a test case for cases that player does not exist
    def test_get_player_not_found(self):
        # send a retrieve request
        response = self.client.get('/api/players/999')
        # if the returned response equals to 404, pass.
        self.assertEqual(response.status_code, 404)

    # a test case for getting a particular player based on his id.
    def test_get_particular_player(self):
        response = self.client.get('/api/players/1')  # send a request

        # slice the time fields.
        editCreatedAt = response.json()['created_at'][0:10]
        editUpdatedAt = response.json()['updated_at'][0:10]

        response.json()['created_at'] = editCreatedAt  # update the datetime
        response.json()['updated_at'] = editUpdatedAt
        self.assertEqual(response.json(), {'identifier': 3030, 'first_name': "Ulas Eren", 'last_name': 'Demir', 'team': 'Fenerbahce','position': 'Defender', 'image': 'ulaserendemir.jpg'})

    # a test case for creating a player.
    def test_create_player(self):
        # send a request along with a JSON data.
        response = self.client.post('/api/players', data=json.dumps({"identifier": 2222, "first_name": "Kylian", "last_name": "Mbappe", "team": "Tottenham Hotspur",
                                                                     "position": "Forward", "image": "kylianmbappe.jpg"}), content_type="application/json")
        # if the response code is 201, pass
        self.assertEqual(response.status_code, 201)

        # if the first name matches with the mock data, pass
        self.assertEqual(response.json()
                         .get('first_name'), 'Kylian')

        # if the identifier matches with the mock data, pass
        self.assertEqual(response.json()
                         .get('identifier'), 2222)
        # if the date matches with the mock data, pass
        self.assertEqual(response.json()
                         .get('updated_at')[0:10], date.today().strftime('%Y-%m-%d'))

    # Test case for creating a player with missing fields.
    def test_create_player_bad_data(self):
        response = self.client.post('/api/players', data=json.dumps(
            {"identifier": 2223, "first_name": "deneme"}), content_type="applications/json")
        self.assertEqual(response.status_code, 422)
