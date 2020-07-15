SHELL=/bin/bash -O extglob -c

.PHONY: activate_env clean_pyc docker lint test coverage

# activate pipenv
activate:
	-pipenv shell

# clean up pyc files
clean_pyc:
	find . -name '*.py[co]' -exec rm {} \;

# build and run development docker container
docker:
	scripts/docker_build.sh
	scripts/docker_run.sh

# run sphinx documentation
doc:
	echo "Please commit your changes or stash them before running documentation."
	make activate
	-rm -rf docs/build
	-cd docs && sphinx-apidoc -o source/ ../iexcloud
	cd docs && make clean && make html
	git checkout gh-pages  2>/dev/null || git checkout --orphan gh-pages
	rm -rf !(.git|docs)
	mv docs/build/html/* .
	touch .nojekyll
	rm -rf docs
	git add --all
	git commit -m "Update Documentation"
	git checkout master

# lint code
lint:
	make activate
	black ./iexcloud
	black ./tests
	flake8 ./iexcloud
	flake8 ./tests

# create test
test:
	make lint
	pytest tests --cov

# create coverage report
coverage:
	make activate
	coverage run -m pytest tests
	coverage html

requirements:
	pipenv lock -r > requirements.txt