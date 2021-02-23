ROOT_DIR = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

FASTAUTH_MIGRATION_NAME ?= migration
FASTAUTH_DATABASE ?= sqlite:///:memory:

makemigrations:
	cd "$(ROOT_DIR)/fastauth"
	pw_migrate create "$(FASTAUTH_MIGRATION_NAME)" \
		--auto \
		--auto-source "fastauth" \
		--directory "$(ROOT_DIR)/fastauth/migrations" \
		--database "$(FASTAUTH_DATABASE)"

migrate:
	cd "$(ROOT_DIR)/fastauth"
	pw_migrate migrate \
		--directory "$(ROOT_DIR)/fastauth/migrations" \
		--database "$(FASTAUTH_DATABASE)"

type:
	mypy "$(ROOT_DIR)"

test:
	pytest "$(ROOT_DIR)/tests.py" -v --log-cli-level INFO
