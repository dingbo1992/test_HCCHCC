from pages.customer_page import CustomerAction
import pytest
from base.base_yml import yml_with_file


@pytest.mark.parametrize('keys', yml_with_file('search_data')['test_search'])
def test_search(keys):

    cs = CustomerAction()
    cs.search(keys)
