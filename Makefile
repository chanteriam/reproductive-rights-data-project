.PHONY: format
format:
	black ./apis/* ./models/* ./test/* ./visualizations/*

.PHONY: test
test:
	pytest -vs ./test/*

.PHONY: test-and-fail
test-and-fail:
	pytest -vsx ./test/*
