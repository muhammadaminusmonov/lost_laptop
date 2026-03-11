run:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose down
	docker compose up --build

logs:
	docker compose logs -f

shell:
	docker compose exec api bash

test:
	docker compose exec api pytest

build:
	docker compose build
	docker compose up

rebuild:
	docker compose down -v
	docker compose up --build

clean:
	docker system prune -f
