import os

# Note: discussion of running shell commands in Python:
#  https://stackoverflow.com/questions/89228/calling-an-external-command-in-python


@given(u'a local container image called \'{text}\'')
def step_impl(context, text):
    retval = os.system(f"docker images {text} | grep {text}")
    assert retval == 0


@when(u'I issue the command \'docker run blah --version')
def step_impl(context):
    retval = os.system("docker run blah --version")
    assert retval == 0


@then(u'the result should be x.y.z')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the result should be x.y.z')

