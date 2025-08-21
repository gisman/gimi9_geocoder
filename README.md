# Korean Geocoder

Korean Geocoder is a Python library designed to provide easy access to geocoding services for Korean addresses. It allows users to convert addresses into geographic coordinates and vice versa, making it a valuable tool for data analysis and geographic information systems (GIS).

## Features

- Geocode Korean addresses to latitude and longitude.
- Reverse geocode geographic coordinates to obtain address information.
- Seamless integration with pandas for data analysis.
- Custom exceptions for error handling.
- Comprehensive API documentation.

## Installation

You can install the Korean Geocoder library using pip:

```bash
pip install korean-geocoder
```

## Usage

### Basic Geocoding

To perform basic geocoding, you can use the `KoreanGeocoder` client:

```python
from gimi9_geocoder import KoreanGeocoder

geocoder = KoreanGeocoder()
result = geocoder.geocode("서울특별시 강남구 역삼동")
print(result)
```

### Pandas Integration

The library provides utility functions to work with pandas DataFrames:

```python
import pandas as pd
from gimi9_geocoder import pandas_utils

df = pd.DataFrame({"addresses": ["서울특별시 강남구 역삼동", "부산광역시 해운대구"]})
geocoded_df = pandas_utils.geocode_addresses(df, "addresses")
print(geocoded_df)
```

## Examples

Check the `examples` directory for more usage examples, including basic usage and pandas integration.

## Documentation

For detailed API documentation, please refer to the `docs/api.md` file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.