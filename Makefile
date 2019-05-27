# This target is the command for a human to read the test output
# to follow a BDD style loop
test:
	ls features/*.feature features/steps/*.py | entr -c behave 

clean:
	rm -f .allure-cli.inspect-info

build: .allure-cli.inspect-info

test-allure-results:
	behave -f allure_behave.formatter:AllureFormatter \
	    -o $HOME/lib/allure-results ./features
	
.allure-cli.inspect-info: Dockerfile
	docker build --tag allure-cli .
	docker image inspect allure-cli > .allure-cli.inspect-info

