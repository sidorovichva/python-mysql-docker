build:
	docker-compose --profile dev build

up:
	docker-compose --profile dev up

down:
	docker-compose --profile dev down

delete:
	docker-compose --profile dev down --rmi all