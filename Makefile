# Author(s): Michael Plunkett
BASEDIR=./reproductive_rights_data_project

# Author(s): Michael Plunkett
.PHONY: format
format:
	black ${BASEDIR}/__main__.py ${BASEDIR}/api/ ${BASEDIR}/test/ ${BASEDIR}/visualization/ ${BASEDIR}/data_handling/ ${BASEDIR}/util --line-length=80

# Author(s): Michael Plunkett
.PHONY: test
test:
	pytest -vs ${BASEDIR}/test/

# Author(s): Michael Plunkett
.PHONY: test-and-fail
test-and-fail:
	pytest -vsx ${BASEDIR}/test/

# Author(s): Michael Plunkett
.PHONY: lint
lint:
	pylint ${BASEDIR}/api/ ${BASEDIR}/test/ ${BASEDIR}/visualization/ ${BASEDIR}/ ${BASEDIR}/util

# Author(s): Michael Plunkett
.PHONY: api
api:
	python -m reproductive_rights_data_project --api

# Author(s): Michael Plunkett
.PHONY: parse-data
parse-data:
	python -m reproductive_rights_data_project --parse-data

# Author(s): Michael Plunkett
.PHONY: visualize
visualize:
	python -m reproductive_rights_data_project --visualize

# Author(s): Kate Habich
.PHONY: run
run:
	make api parse-data visualize
