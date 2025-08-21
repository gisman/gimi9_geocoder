import pytest


@pytest.fixture(scope="module")
def sample_data():
    return {"address": "서울시 중구 을지로 170", "coordinates": (37.566385, 126.997475)}
