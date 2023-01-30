.PHONY: format
format:
	black ./apis/* ./models/* ./test/* ./visualizations/*

.PHONY: test
test:
	pytest -vs ./test/*

.PHONY: test-and-fail
test-and-fail:
	pytest -vsx ./test/*

.PHONY: lint
lint:
	pylint ./apis/* ./models/* ./test/* ./visualizations/*

.PHONY: api
api:
	python ./ --api

.PHONY: parse-data
parse-data:
	python ./ --parse-data

.PHONY:visualize
visualize:
	python ./ --visualize
