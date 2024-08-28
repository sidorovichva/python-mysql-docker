build:
	docker-compose --profile dev build

up:
	docker-compose --profile dev up

down:
	docker-compose --profile dev down

delete:
	docker-compose --profile dev down --rmi all

start:
	docker-compose --profile dev start

stop:
	docker-compose --profile dev stop

restart:
	docker-compose --profile dev restart

logs:
	docker-compose --profile dev logs -f

list:
	docker-compose --profile dev ps