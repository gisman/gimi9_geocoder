# Gimi9 Geocoder

Gimi9 Geocoder is a Python library designed to provide easy access to geocoding services for Korean addresses. It allows users to convert addresses into geographic coordinates and vice versa, making it a valuable tool for data analysis and geographic information systems (GIS).

## Features

- **Multiple Input Types**: Support for single addresses (str), address lists (List[str]), and pandas DataFrames
- **Geocoding**: Convert Korean addresses to latitude and longitude coordinates
- **Reverse Geocoding**: Convert geographic coordinates back to address information
- **Pandas Integration**: Seamless integration with pandas DataFrames for batch processing
- **Administrative Region Data**: Access to Korean administrative region information
- **Historical Data**: Query historical administrative division changes
- **Token Management**: Built-in API token usage statistics

## Installation

You can install the Gimi9 Geocoder library using pip:

```bash
pip install gimi9-geocoder
```

## Quick Start

### Basic Usage

```python
from gimi9_geocoder.client import GeocoderClient

# Initialize client
geocoder = GeocoderClient(token="your_api_token")

# Single address geocoding
result = geocoder.geocode("서울특별시 강남구 테헤란로 152")
print(result)

# Multiple addresses
addresses = [
    "서울특별시 강남구 테헤란로 152",
    "부산광역시 해운대구 해운대해변로 264"
]
result = geocoder.geocode(addresses)
print(result)
```

### DataFrame Integration

```python
import pandas as pd
from gimi9_geocoder.client import GeocoderClient

# Create DataFrame with addresses
df = pd.DataFrame({
    'name': ['Place 1', 'Place 2'],
    'address': [
        '서울특별시 강남구 테헤란로 152',
        '부산광역시 해운대구 해운대해변로 264'
    ]
})

# Geocode using DataFrame
geocoder = GeocoderClient(token="your_api_token")
result = geocoder.geocode(df, address_col='address')
print(result)
```

### Reverse Geocoding

```python
# Reverse geocode coordinates to address
result = geocoder.reverse_geocode(127.1146829, 37.5138498)
print(result)
```

## API Methods

- `geocode(address, address_col=None)`: Geocode addresses (supports str, list, DataFrame)
- `reverse_geocode(x, y)`: Convert coordinates to address
- `region(type, code, yyyymm)`: Get administrative region shapes
- `hd_history(x, y, yyyymm)`: Get administrative division history
- `token_stats()`: Get API token usage statistics

## Examples

Check the `examples` and `sample` directories for more usage examples.

## Documentation

For detailed API documentation, please refer to the `docs/api.md` file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.