import pytest
from flask.testing import FlaskClient
from marshmallow import ValidationError
from main import app
from schemas.PredictionResponseSchema import PredictionResponseSchema
from tests.constants.constants import SUCCESS_TEST_DATA, FAILURE_TEST_DATA

class TestPredictionAPI:
    success_test_data = SUCCESS_TEST_DATA
    failure_test_data = FAILURE_TEST_DATA

    def validate_response_data(self, response_data):
        schema = PredictionResponseSchema()

        try:
            schema.load(response_data)

            return True
        except ValidationError:
            return False

    @pytest.fixture
    def client(self) -> FlaskClient:
        with app.test_client() as client:
            yield client

    @pytest.mark.parametrize("payload", success_test_data)
    def test_prediction_endpoint(self, client: FlaskClient, payload):
        response = client.post('/api/predict', json=payload)

        assert response.status_code == 200, "HTTP status code should be 200"

        response_data = response.json

        assert self.validate_response_data(response_data), "Response data should be valid according to the schema"

    @pytest.mark.parametrize("test_case", failure_test_data, ids=[case["description"] for case in failure_test_data])
    def test_failure_scenarios(self, client: FlaskClient, test_case):
        response = client.post('/api/predict', json=test_case["payload"])

        assert response.status_code == test_case["expected_status"], f"{test_case['description']} should return status code {test_case['expected_status']}"
