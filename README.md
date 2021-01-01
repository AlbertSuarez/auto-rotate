# Auto Rotate

[![HitCount](http://hits.dwyl.io/AlbertSuarez/auto-rotate.svg)](http://hits.dwyl.io/AlbertSuarez/auto-rotate)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/AlbertSuarez/auto-rotate)
![Python application](https://github.com/AlbertSuarez/auto-rotate/workflows/Python%20application/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/auto-rotate.svg)](https://GitHub.com/AlbertSuarez/auto-rotate/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/auto-rotate.svg)](https://GitHub.com/AlbertSuarez/auto-rotate/network/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/auto-rotate.svg)](https://github.com/AlbertSuarez/auto-rotate/blob/master/LICENSE)

🔁 (Work in Progress Project) Full application for auto-rotating images using [RotNet](https://github.com/d4nst/RotNet).

## Motivation

This repository came up after seeing the amazing work that [Daniel Saez](https://github.com/d4nst) did with the [RotNet](https://github.com/d4nst/RotNet) model for predicting the rotation angle of an image to correct its orientation. I wanted to understand how it actually works and build a easier UI for running inference no matter the knowledge that you have about it to make this more accessible to the community.

## Examples

_Coming soon..._

## API

### Requirements

1. Python 3.7+.
2. docker.
3. docker-compose.

### Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

### Usage

To run the server, please execute the following from the root directory:

1. Change directory into the `api` folder.

  ```bash
  cd api/
  ```

2. Setup virtual environment.

3. Install dependencies.

  ```bash
  pip3 install -r requirements.lock
  ```

4. Run API server as a python module.

  ```bash
  python3 -m src
  ```

Or just simply run the `docker-compose` script from the root directory.

```
docker-compose up -d --build
```

### Endpoints

#### Rotate

Rotate an image given its URL or the image itself.

| Key             | Type     | Description                                                  |
| --------------- | -------- | ------------------------------------------------------------ |
| image_url       | string   | Internet accessible URL of an image.                         |
| image_base64    | string   | URL and filename - safe base64(url) encoded image.           |

##### Request example

```bash
curl -d '{"image_url": URL}' -H "Content-Type: application/json" -X POST https://api.autorotate.asuarez.dev/rotate
```

##### Response example

```json
{
    "error": false,
    "response": {
        "image_base64": "IMAGE_RESULT_ENCODED_IN_BASE64"
    }
}
```

## Run tests

1. Run Auto Rotate locally.

2. Run tests from `api` module.

   ```
   python3 -m unittest discover -v
   ```

## Development

### How to add a new test

Create a new Python file called `test_*.py` in `test.*` (inside `api` folder) with the following structure:

```python
import unittest


class NewTest(unittest.TestCase):

    def test_v0(self):
        expected = 5
        result = 2 + 3
        self.assertEqual(expected, result)

```

## Merits

Again, kudos to [Daniel Saez](https://github.com/d4nst) for this amazing model that he came up.

## License

MIT © Auto Rotate
