import pytest

def pytest_configure(config):
    """pytest 설정 - 마커 등록"""
    config.addinivalue_line("markers", "success: mark test as success case")
    config.addinivalue_line("markers", "failure: mark test as failure case")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "integration: mark test as integration test")

# 공통 fixture들
@pytest.fixture
def sample_data():
    return {"num1": 2, "num2": 5}

@pytest.fixture(scope="session")
def test_environment():
    """테스트 환경 설정"""
    return "test"