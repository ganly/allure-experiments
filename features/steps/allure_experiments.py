import os
import subprocess

# Note: discussion of running shell commands in Python:
#  https://stackoverflow.com/questions/89228/calling-an-external-command-in-python


@given(u'a local container image called \'{text}\'')
def step_impl(context, text):
    # The 'docker images' command always returns 0 regardless
    # of whether the image exists or not. So we grep the
    # output to get a return value.
    command = f"docker images {text} | grep {text}"

    retval = os.system(command)

    assert retval == 0


@when(u'I issue the command "{command}"')
def step_impl(context, command):

    completed_process = subprocess.run(command, shell=True, 
            stdout=subprocess.PIPE, encoding='UTF8')

    context.output = completed_process.stdout.rstrip()

    if completed_process.returncode == 0:
        pass
    else:
        print(f'expected command to run correctly, but got return code of {completed_process.returncode}')


@then(u'the result should be "{string}"')
def step_impl(context, string):
    if context.output == string:
        pass
    else:
        print(f'(expected {string} but got {context.output}')
        assert False

