Feature: Allure container provides version info

    As someone who wants to use the Allure tool (framework)
    I want a simple way to run commands
    So I can leverage the benefits of Allure reports on my test data.
    That simple way is our docker container.


    Scenario:
        Given a local container image called 'allure-cli'
	When I issue the command "docker run allure-cli allure --version"
	Then the result should be "2.12.1"


