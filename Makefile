.PHONY: format
format:
	black ./__main__.py ./api/ ./test/ ./visualizations/ ./data_handling/ --line-length=80

.PHONY: test
test:
	pytest -vs ./test/

.PHONY: test-and-fail
test-and-fail:
	pytest -vsx ./test/

.PHONY: lint
lint:
	pylint ./api/ ./test/ ./visualizations/ ./data_handling/

.PHONY: api
api:
	python ./ --api

.PHONY: parse-data
parse-data:
	python ./ --parse-data

.PHONY:visualize
visualize:
	python ./ --visualize
