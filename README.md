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

Run `make clean build` to get set up.

Run `make test` in one window, hack around in others.

Later, in a CI tool, run `make test-allure-results` to get the test data
added to the report.


Usage
-----

Once set up,
you can run commands like:
```
docker run allure-cli allure --help
```

Making some results
-------------------

The main goal for these experiments is to work out a good setup for using
BDD with a Python toolchain.

The BDD tool of choice seems is currently
[behave](https://behave.readthedocs.io/en/latest/tutorial.html)
and there is an allure integration described at
[the behave section](https://docs.qameta.io/allure/#_behave)
of the manual.

It uses a Python package called `allure-behave`

In the `simplest_behave_example` directory,
I've created the minimal files to get some sample output.
```
cd simplest_behave_example
```


A normal behave run looks like this:
```
$ behave
Feature: minimal behave example # features/minimal.feature:1

  Scenario: very basic test  # features/minimal.feature:3
    Given it just works      # features/steps/minimal.py:1 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
1 step passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```

We get output written to STDOUT/STDERR to direct the developer to the next
step.

To get the system to also save information to be used in an Allure report,
we need to add the allure-behave package then add some info to our test run
command:
```
$ cat requirements.txt
allure-behave

$ pip install -r requirements.txt
  ...


$ mkdir allure-results
$ behave -f allure_behave.formatter:AllureFormatter -o allure-results
1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
1 step passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000
```

This gives us less information of use to the programmer (though the output can
be configured).

But it creates a file in the results directory:
```
$ ls -l allure-results
  ... 496 ... ee505daf-a4e4-40d3-a34d-8d3ce3f390de-result.json
```

It's a single line json file, best viewed formatted by `jq`
```
$ jq . allure-results/ee*json
{
  "name": "very basic test",
  "status": "passed",
  "steps": [
    {
      "name": "Given it just works",
      "status": "passed",
      "start": 1558954490929,
      "stop": 1558954490930
    }
  ],
  "start": 1558954490928,
  "stop": 1558954490930,
  "uuid": "b805b164-0bfa-4c89-ac4f-80f2daae29ff",
  "historyId": "77b5204a4f0a82929cf71a61b75ba525",
  "labels": [
    {
      "name": "severity",
      "value": "normal"
    },
    {
      "name": "feature",
      "value": "minimal behave example"
    },
    {
      "name": "framework",
      "value": "behave"
    },
    {
      "name": "language",
      "value": "cpython3"
    }
  ]
}
```


