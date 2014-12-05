from malleefowl.dispel import esgsearch_workflow

from nose import tools
from unittest import TestCase
from nose import SkipTest
from nose.plugins.attrib import attr

from __init__ import SERVICE, TESTDATA, CREDENTIALS

def my_monitor(execution):
    print execution.status
    print execution.percentCompleted
    print execution.statusMessage

@attr('online')
@attr('security')
def test_esgsearch_workflow():
    # TODO: set environ with credentials
    constraints = 'project:CORDEX,experiment:historical,variable:tas,time_frequency:mon'
    result = esgsearch_workflow(
        SERVICE,
        esgsearch_params=dict(constraints=constraints,
                              limit=1, search_type='File', distrib=False),
        wget_params=dict(credentials=CREDENTIALS),
        doit_params=dict(url=SERVICE,
                         identifier='dummy', resource='resource', inputs=[]),
        monitor = my_monitor,
        )
    tools.ok_( len(result) == 1, result)
    tools.ok_('malleefowl' in result[0], result)
    #tools.ok_(False, result)



    
    
    




