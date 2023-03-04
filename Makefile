# Author(s): Michael Plunkett
.PHONY: format
format:
	black ./__main__.py ./api/ ./test/ ./visualization/ ./data_handling/ ./util --line-length=80

# Author(s): Michael Plunkett
.PHONY: test
test:
	pytest -vs ./test/

# Author(s): Michael Plunkett
.PHONY: test-and-fail
test-and-fail:
	pytest -vsx ./test/

# Author(s): Michael Plunkett
.PHONY: lint
lint:
	pylint ./api/ ./test/ ./visualization/ ./data_handling/ ./util

# Author(s): Michael Plunkett
.PHONY: api
api:
	python ./ --api

# Author(s): Michael Plunkett
.PHONY: parse-data
parse-data:
	python ./ --parse-data

# Author(s): Michael Plunkett
.PHONY: visualize
visualize:
	python ./ --visualize

# Author(s): Kate Habich
.PHONY: run
run:
	make api parse-data visualize
