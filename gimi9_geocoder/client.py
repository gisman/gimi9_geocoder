import httpx


class GeocoderClient:
    def __init__(
        self, base_url: str = "https://geocode-api.gimi9.com", token: str = None
    ):
        self.base_url = base_url
        self.token = token

    def geocode(self, address: str):
        with httpx.Client() as client:
            response = client.get(
                f"{self.base_url}/geocode", params={"q": address, "token": self.token}
            )
            response.raise_for_status()
            return response.json()

    def reverse_geocode(self, x: float, y: float):
        with httpx.Client() as client:
            response = client.get(
                f"{self.base_url}/reverse_geocode",
                params={"x": x, "y": y, "token": self.token},
            )
            response.raise_for_status()
            return response.json()

    def bulk_geocode(self, addresses: list):
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/geocode",
                headers={"Authorization": self.token},
                json={"q": addresses},
            )
            response.raise_for_status()
            return response.json()

    def region(self, type="hd", code="1114055000,4111760000", yyyymm="202506"):
        params = {"type": type, "code": code, "yyyymm": yyyymm, "token": self.token}
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/region", params=params)
            response.raise_for_status()
            return response.json()

    def hd_history(self, x, y, yyyymm="202506"):
        params = {"x": x, "y": y, "yyyymm": yyyymm, "token": self.token}
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/hd_history", params=params)
            response.raise_for_status()
            return response.json()

    def token_stats(self):
        params = {"token": self.token}
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/token/stats", params=params)
            response.raise_for_status()
            return response.json()

    async def upload_file(self, file_path: str, target_crs: str = "EPSG:4326"):
        with open(file_path, "rb") as file:
            files = {"file": file}
            data = {"uploaded_filename": file_path, "target_crs": target_crs}
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/upload", data=data, files=files
                )
                response.raise_for_status()
                return response.json()

    async def geocode_file(
        self, file_path: str, download_dir: str, target_crs: str = "EPSG:4326"
    ):
        data = {
            "filepath": file_path,
            "download_dir": download_dir,
            "target_crs": target_crs,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/geocode_file", json=data)
            response.raise_for_status()
            return response.json()
