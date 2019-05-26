# This target is the command for a human to read the test output
# to follow a BDD style loop
test:
	ls features/*.feature features/steps/*.py | entr -c behave 

test-allure-results:
	behave -f allure_behave.formatter:AllureFormatter \
	    -o $HOME/lib/allure-results ./features
	
container-image:
	docker build -t allure-experiments .
