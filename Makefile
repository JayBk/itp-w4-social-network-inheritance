.PHONY: test test-cov

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PROJECT_PACKAGE=social_network


test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test -s tests

test-posts:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test -s tests/test_posts.py
	
test-accounts:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test -s tests/test_accounts.py

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=$(PROJECT_PACKAGE) tests

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=$(PROJECT_PACKAGE) $(shell which py.test) ./tests -q --tb=no >/dev/null; true
	@coverage report
