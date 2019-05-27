Allure experiments
==================

Experiments with the Allure test reporting Framework 
* [docs](https://docs.qameta.io/allure/)
* [source](https://github.com/allure-framework/allure2)


Background
----------

Briefly, the idea is that each test run 
can produce output that includes:
* meta information such as the date/time of each test run
* breakdown information per behaviour/step/test, such as
  * timing information
  * test name or behaviour/feature description
  * success/failure codes

The Allure Framework has integrations with various test or BDD systems to capture 
this information and store it in a common format.

It can then produce dashboard style HTML files (technically an interactive report)
to show trends.

A [demo report](https://demo.qameta.io/allure/) by the package authors is illustrative,
but the focus seems to be more about showing system capabilities than giving examples of
a well run project.


Inspiration
-----------

Frank Escobar's 
[Allure Docker Service Image](https://hub.docker.com/r/frankescobar/allure-docker-service)
was great inspiration.
Source of this is at https://github.com/fescobar/allure-docker-service

It showed how the system worked, but that wasn't quite how I wanted to use it.


My use case
-----------

I'd like a docker image that has a bunch of commands I can use from shell
scripts, makefiles and ideally with the
[entr](https://bitbucket.org/eradman/entr/src/default/)
command.
This image should be as small and lightweight as possible.

Then, I'd like another docker image (or images) that has a good selection of test frameworks
to produce sample data that we can examine the structure of and do some reporting on.


Hacking
-------

I'm using a [Google Cloud Shell](https://cloud.google.com/shell/docs/)
to play with this;
as the virtual machine is ephemeral the docker images often need to be re-created.

Run `make test` in one window, hack around in others.

Later, in a CI tool, run `make test-allure-results` to get the test data
added to the report.

