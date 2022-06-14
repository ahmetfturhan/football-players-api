run:
	docker-compose up --build -d
	docker logs -f
down:
	docker-compose down