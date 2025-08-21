import sys
import os
import pandas as pd

# Add the module's directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gimi9_geocoder.client import GeocoderClient


def main():
    # GeocoderClient 초기화
    geocoder = GeocoderClient(
        token="9b4c40c8f5c935ca6524c2ec18aa7c49f4c3b6cb"
    )  # 프로회원
    # geocoder = GeocoderClient(token="DEMO_TOKEN")

    data = {
        "address": [
            "서울특별시 강남구 테헤란로 123",
            "부산광역시 해운대구 해운대해변로 456",
            "대구광역시 중구 동성로 789",
        ]
    }

    df = pd.DataFrame(data)

    # 주소를 좌표로 변환 (지오코딩)
    df = geocoder.geocode(df, "address")
    print(f"지오코딩 결과: {df.head()}")

    # 좌표를 주소로 변환 (역지오코딩)
    data_xy = {"x": df["x_axis"], "y": df["y_axis"]}
    df_xy = pd.DataFrame(data_xy)
    reverse_result = geocoder.reverse_geocode(x_col="x", y_col="y", coordinates=df_xy)
    # reverse_result = geocoder.reverse_geocode(127.1146829, 37.5138498)
    print(f"역지오코딩 결과: {reverse_result}")

    # 코드로 행정구역 형상 검색
    regions = geocoder.region(type="hd", code="1114055000,4111760000", yyyymm="202506")
    print(f"행정구역 형상 검색 결과: {regions}")

    # 행정동 이력
    hd_history = geocoder.hd_history(x=127.075074, y=37.143834, yyyymm="202506")
    print(f"행정동 이력 결과: {hd_history}")

    # 토큰 통계
    token_stats = geocoder.token_stats()
    print(f"토큰 통계 결과: {token_stats}")


if __name__ == "__main__":
    main()
