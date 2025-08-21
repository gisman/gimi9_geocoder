#!/usr/bin/env python3
"""
Enhanced geocode function test
"""

import pandas as pd
from gimi9_geocoder.client import GeocoderClient


def test_string_geocode():
    """문자열 주소 테스트"""
    client = GeocoderClient()

    try:
        result = client.geocode("서울특별시 강남구 테헤란로 152")
        print("문자열 geocode 결과:")
        print(result)
        print()
    except Exception as e:
        print(f"문자열 geocode 오류: {e}")
        print()


def test_list_geocode():
    """리스트 주소 테스트"""
    client = GeocoderClient()

    try:
        addresses = [
            "서울특별시 강남구 테헤란로 152",
            "서울특별시 종로구 세종대로 175",
            "부산광역시 해운대구 해운대해변로 264",
        ]
        result = client.geocode(addresses)
        print("리스트 geocode 결과:")
        print(result)
        print()
    except Exception as e:
        print(f"리스트 geocode 오류: {e}")
        print()


def test_dataframe_geocode():
    """DataFrame 주소 테스트"""
    client = GeocoderClient()

    try:
        # 테스트용 DataFrame 생성
        df = pd.DataFrame(
            {
                "name": ["장소1", "장소2", "장소3"],
                "address": [
                    "서울특별시 강남구 테헤란로 152",
                    "서울특별시 종로구 세종대로 175",
                    "부산광역시 해운대구 해운대해변로 264",
                ],
            }
        )

        print("원본 DataFrame:")
        print(df)
        print()

        # geocoding 수행
        result = client.geocode(df, address_col="address")

        print("geocoding 결과:")
        print(result)
        print()

    except Exception as e:
        print(f"DataFrame geocode 오류: {e}")
        print()


def test_error_handling():
    """에러 처리 테스트"""
    client = GeocoderClient()

    print("에러 처리 테스트:")

    # 잘못된 타입 테스트
    try:
        result = client.geocode(123)  # 숫자는 지원하지 않음
        print("잘못된 타입 테스트 실패: 에러가 발생해야 함")
    except TypeError as e:
        print(f"✓ 타입 에러 (예상됨): {e}")

    # DataFrame에서 address_col 누락 테스트
    try:
        df = pd.DataFrame({"name": ["test"], "location": ["서울"]})
        result = client.geocode(df)  # address_col 누락
        print("address_col 누락 테스트 실패: 에러가 발생해야 함")
    except ValueError as e:
        print(f"✓ 값 에러 (예상됨): {e}")

    # DataFrame에서 잘못된 컬럼명 테스트
    try:
        df = pd.DataFrame({"name": ["test"], "address": ["서울"]})
        result = client.geocode(df, address_col="wrong_column")  # 잘못된 컬럼명
        print("잘못된 컬럼명 테스트 실패: 에러가 발생해야 함")
    except ValueError as e:
        print(f"✓ 값 에러 (예상됨): {e}")

    print()


if __name__ == "__main__":
    print("Enhanced geocode function test")
    print("=" * 50)

    test_string_geocode()
    test_list_geocode()
    test_dataframe_geocode()
    test_error_handling()

    print("테스트 완료!")
