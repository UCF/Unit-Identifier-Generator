# UID Generator

Creates Unit Identifier logos and stores form submissions using Django and ImageMagick.

Note:  This project is NOT complete and does not fully function.


## Requirements
- libjpeg (system level)
- freetype (system level)
- virtualenv (system level)
- Django
- Pillow (PIL fork/Python ImageMagick wrapper)


## Installation (local)

1. Install system-level dependencies (OSX, Homebrew:  `brew install libjpeg freetype`)
2. Create a new virtualenv and clone this repo inside of it
  - `virtualenv my-directory`
  - `git clone git@github.com:UCF/Unit-Identifier-Generator.git src`
3. Navigate to the repo's root directory and install dependencies via pip
  - `cd src`
  - `pip install requirements.txt`
4. Set up testing db:  `python manage.py migrate --run-syncdb`
5. Collect static files:  `python manage.py collectstatic`
6. Run app:  `python manage.py runserver`
