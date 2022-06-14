from datetime import date
import json
from django.test import TestCase, Client
from players.models import Player
# Create your tests here.


class PlayerTestCase(TestCase):
    def setUp(self):
        Player.objects.create(identifier=3030,
                              first_name="Ulas Eren",
                              last_name="Demir",
                              team="Fenerbahce",
                              position="Defender",
                              image="ulaserendemir.jpg",
                              created_at="2022-06-14 15:15:15",
                              updated_at="2022-06-14 15:15:15")

        Player.objects.create(identifier=3434,
                              first_name="Furkan",
                              last_name="Ertas",
                              team="Fenerbahce",
                              position="Midfielder",
                              image="furkanertas.jpg",
                              created_at="2022-06-14 15:15:15",
                              updated_at="2022-06-14 15:15:15")

        self.client = Client()

    def test_get_players(self):
        response = self.client.get('/api/players')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json()
        #     .get('metadata'), [{'id': 1, 'metadata': "{'test': 'test'}"}])
        editCreatedAt = response.json()[0]['created_at'][0:10]
        editUpdatedAt = response.json()[0]['updated_at'][0:10]

        response.json()[0]['created_at'] = editCreatedAt
        response.json()[0]['updated_at'] = editUpdatedAt

        # print("\n\n", response.json()[0], "\n\n")

        self.assertEqual(response.json()[0], {'identifier': 3030, 'first_name': "Ulas Eren", 'last_name': 'Demir', 'team': 'Fenerbahce',
                         'position': 'Defender', 'image': 'ulaserendemir.jpg', 'created_at': '2022-06-14', 'updated_at': '2022-06-14'})

    def test_get_player_not_found(self):
        response = self.client.get('/api/players/999')
        self.assertEqual(response.status_code, 404)

    def test_get_particular_player(self):
        response = self.client.get('/api/players/1')

        editCreatedAt = response.json()['created_at'][0:10]
        editUpdatedAt = response.json()['updated_at'][0:10]

        response.json()['created_at'] = editCreatedAt
        response.json()['updated_at'] = editUpdatedAt
        self.assertEqual(response.json(), {'identifier': 3030, 'first_name': "Ulas Eren", 'last_name': 'Demir', 'team': 'Fenerbahce',
                         'position': 'Defender', 'image': 'ulaserendemir.jpg', 'created_at': '2022-06-14', 'updated_at': '2022-06-14'})

    def test_create_player(self):
        response = self.client.post('/api/players', data=json.dumps({"identifier": 2222, "first_name": "Kylian", "last_name": "Mbappe", "team": "Tottenham Hotspur",
                                                                     "position": "Forward", "image": "kylianmbappe.jpg", "created_at": "2022-06-14T06:03:07.777Z", "updated_at": "2022-06-14T06:03:07.777Z"}), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.json()
                         .get('first_name'), 'Kylian')

        self.assertEqual(response.json()
                         .get('identifier'), 2222)
        self.assertEqual(response.json()
                         .get('updated_at')[0:10], date.today().strftime('%Y-%m-%d'))

    def test_create_player_bad_data(self):
        response = self.client.post('/api/players', data=json.dumps(
            {"identifier": 2223, "first_name": "deneme"}), content_type="applications/json")
        self.assertEqual(response.status_code, 422)
