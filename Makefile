BASEDIR=./reproductive_rights_project

.PHONY: format
format:
	isort ${BASEDIR}/
	black ${BASEDIR}/

.PHONY: test
test:
	pytest -vs ${BASEDIR}/test/

.PHONY: test-and-fail
test-and-fail:
	pytest -vsx ${BASEDIR}/test/

.PHONY: lint
lint:
	ruff ${BASEDIR}/ 

.PHONY: api
api:
	python -m reproductive_rights_project --api

.PHONY: parse-data
parse-data:
	python -m reproductive_rights_project --parse-data

.PHONY: visualize
visualize:
	python -m reproductive_rights_project --visualize

.PHONY: run
run:
	make api parse-data visualize
