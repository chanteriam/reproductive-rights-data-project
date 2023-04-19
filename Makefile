BASEDIR=./reproductive_rights_data_project

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
	pylint ${BASEDIR}/api/ ${BASEDIR}/test/ ${BASEDIR}/visualization/ ${BASEDIR}/ ${BASEDIR}/util

.PHONY: api
api:
	python -m reproductive_rights_data_project --api

.PHONY: parse-data
parse-data:
	python -m reproductive_rights_data_project --parse-data

.PHONY: visualize
visualize:
	python -m reproductive_rights_data_project --visualize

.PHONY: run
run:
	make api parse-data visualize
