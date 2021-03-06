[![CodeFactor](https://www.codefactor.io/repository/github/pupsen-vupsen/trik-testsys-api/badge)](https://www.codefactor.io/repository/github/pupsen-vupsen/trik-testsys-api)
<a href="https://github.com/Pupsen-Vupsen/trik-testsys-telegram-client/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![license](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<a href="https://github.com/Pupsen-Vupsen/trik-testsys-api/actions"><img alt="Actions Status" src="https://github.com/Pupsen-Vupsen/trik-testsys-api/actions/workflows/lint.yml/badge.svg"></a>
# Grading system api for TRIK studio

## Overview
Grading system api for TRIK studio, which allows to create new students and get results.

## Install and Run

### With docker
1. Build image:
`docker build .`
2. Edit settings in `config.py` file
3. Run api:
`docker run 'your_image_id'`

### Without docker
1. Install dependencies:
`pip3 install -r requirements.txt`
2. Edit settings in `config.py` file 
3. Run api:
`python3 main.py`

## Code Style
In this project we use [CodeFactor](https://www.codefactor.io) and [flake8](https://github.com/PyCQA/flake8) to check code style. 
[Black](https://github.com/psf/black) for formatting.

## Contributing
Please, follow [Contributing](CONTRIBUTING.md) page.

## Authors
* Viktor Karasev - [KarasssDev](https://github.com/KarasssDev)

## License
This project is Apache License 2.0 - see the [LICENSE](LICENSE) file for details
