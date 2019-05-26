@given(u'a local container image called \'blah\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a local container image called \'blah\'')


@when(u'I issue the command \'docker run blah --version')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I issue the command \'docker run blah --version')


@then(u'the result should be x.y.z')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the result should be x.y.z')

