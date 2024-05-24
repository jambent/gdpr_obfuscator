import pytest
from moto import mock_aws

from obfsc8.src.obfsc8.obfuscate import obfuscate
from test_data.test_json import test_json

@mock_aws
@pytest.mark.skip(reason="Building pytest fixture with session scope first")
def test_that_BytesIO_object_returned():
    result = obfuscate(test_json)

    assert isinstance(result,bytes)