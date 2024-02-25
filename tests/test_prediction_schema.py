import pytest
from marshmallow import ValidationError
from schemas.PredictionRequestSchema import PredictionRequestSchema
from tests.constants.constants import SUCCESS_TEST_DATA, FAILURE_TEST_DATA


class MockModelsConstants:
    available_models = ["bean_leaf", "potato_leaf"]


ModelsConstants = MockModelsConstants()


class TestPredictionRequestSchema:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.schema = PredictionRequestSchema()

    @pytest.mark.parametrize("test_case", SUCCESS_TEST_DATA)
    def test_success_scenario(self, test_case):
        try:
            result = self.schema.load(test_case)

            assert result is not None, "Expected valid data to be loaded successfully"
        except Exception as error:
            pytest.fail(f"Unexpected exception: {error}")

    @pytest.mark.parametrize("test_case", FAILURE_TEST_DATA)
    def test_failure_scenario(self, test_case):
        payload = test_case["payload"]
        expected_status = test_case["expected_status"]

        if expected_status == 400:
            with pytest.raises(ValidationError):
                self.schema.load(payload)
        else:
            pytest.fail(f"Unsupported expected_status: {expected_status}")
