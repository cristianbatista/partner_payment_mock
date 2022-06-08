-include .env
export $(shell sed 's/=.*//' .env)

export APP_NAME = prescriptions
export PYTHONPATH=$(CURDIR)

format:
	@black prescriptions
	@isort --recursive prescriptions

lint:
	@flake8 prescriptions
	@black --check prescriptions --diff
	@isort --recursive --check-only prescriptions

####################################
# Dependencies Commands
####################################
packages:
	@printf "Installing libraries... "
	@venv/bin/pip install -q --no-cache-dir -r requirements.txt
	@echo "OK"

env-create: env-destroy
	@printf "Creating virtual environment... "
	@virtualenv -q venv -p python3.8
	@echo "OK"

env-destroy:
	@printf "Destroing virtual environment... "
	@rm -rfd venv
	@echo "OK"

install: env-create packages

infra-up:
	@docker-compose up -d


####################################
# App (Run, Debug and Test) Commands
####################################
debug-api:
	@uvicorn payment_mock.api.main:app --workers 3 --reload

run-api:
	@gunicorn payment_mock.api.main:app -w 3 -k uvicorn.workers.UvicornWorker
