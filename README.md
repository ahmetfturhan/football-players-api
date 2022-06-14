# football-players-api
Simple API to Create, Retrieve, Update, Delete football players data using Django-Ninja.

# Running with Docker
``` docker-compose up ```

# Taking Down the Application
``` docker-compose down ```

# Access to Home Page
``` http://127.0.0.1:8000/index ```

# Retrieve all Players
``` http://127.0.0.1:8000/api/players ```

# Retrieve a Particular Player Using ID
``` http://127.0.0.1:8000/api/players/{insert_id_here_and_delete_curly_brackets} ```

# Retrieve a Player Using Identifier
``` http://127.0.0.1:8000/api/players/identifier/{insert_identifier_here_and_delete_curly_brackets} ```

# Creating a Player
``` Send a POST request to http://127.0.0.1:8000/api/players along with a JSON data. You can see the JSON format at docs.```

# Updating a Player
``` Send a PUT request to http://127.0.0.1:8000/api/players/{player_id} along with a JSON data. ```

# Deleting a Player
``` Send a DELETE request to http://127.0.0.1:8000/api/players/{player_id} ```

#Further explanation and more endpoints can be see here
``` http://127.0.0.1:8000/api/docs ```

