from contextlib import contextmanager

import pytest
from marshmallow import ValidationError

from main import predict, app
from schemas.PredictionResponseSchema import PredictionResponseSchema
from tests.constants.constants import SUCCESS_TEST_DATA, FAILURE_TEST_DATA


@contextmanager
def simulate_flask_request_context(json_data):
    with app.test_request_context(method="POST", json=json_data):
        yield


class TestPredictionFunction:
    success_test_data = SUCCESS_TEST_DATA
    failure_test_data = FAILURE_TEST_DATA

    def validate_response_data(self, response_data):
        schema = PredictionResponseSchema()

        try:
            schema.load(response_data)

            return True
        except ValidationError:
            return False

    @pytest.mark.parametrize("payload", success_test_data)
    def test_predict_function(self, payload):
        with simulate_flask_request_context(payload):
            response = predict()
            response_data = response.get_json()

            assert self.validate_response_data(response_data), "Response data should be valid according to the schema"

    @pytest.mark.parametrize("test_case", failure_test_data, ids=[case['description'] for case in failure_test_data])
    def test_predict_function_failure(self, test_case):
        with simulate_flask_request_context(test_case["payload"]):
            response_data, response_status = predict()

            assert response_status == test_case[
                "expected_status"], f"{test_case['description']} should return status code {test_case['expected_status']}"
