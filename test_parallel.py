import pytest
import json

TEST_PARAMS = ["compliance_check_pass", "compliance_check_fail"]


@pytest.fixture(params=TEST_PARAMS, scope="class")
def compliance_job_json_with_mock_users(request):
    """
    Fixture that provides mock compliance job data based on the test case parameter.
    """
    test_name = request.param

    # Mocked compliance job result
    compliance_results = {
        "compliance_check_pass": {"status": "pass", "error": 0},
        "compliance_check_fail": {"status": "fail", "error": 3},
    }

    request.cls.test_name = test_name
    request.cls.output = compliance_results[test_name]


@pytest.mark.usefixtures("compliance_job_json_with_mock_users")
class TestComplianceJob:
    def test_compliance_status(self, request):
        """
        Test case to validate compliance job results.
        """
        expected_results = {
            "compliance_check_pass": {"status": "pass", "error": 0},
            "compliance_check_fail": {"status": "fail", "error": 13},
        }

        test_name = request.cls.test_name
        expected_output = expected_results[test_name]

        print(f"Expected: {json.dumps(expected_output, indent=2)}")
        print(f"Actual: {json.dumps(request.cls.output, indent=2)}")

        assert request.cls.output == expected_output, f"Test failed for {test_name}"
