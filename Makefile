.PHONY: format
format:
	black ./apis/* ./models/* ./test/* ./visualizations/*

.PHONY: test
test:
	pytest -vs ./test/*
