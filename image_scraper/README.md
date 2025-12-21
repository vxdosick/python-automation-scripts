# Image Scraper

A simple Python script to scrape images from a web page and download them locally.

## Features

- Fetches all images (`<img>` tags) from a given webpage
- Handles relative URLs
- Saves image URLs to `images_data.txt`
- Downloads images to the `images/` folder
- Prints progress and downloaded images in the console

## Usage

1. Activate virtual environment:
Mac / Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install requests beautifulsoup4
```

3. Run the scraper:
```bash
python scraper.py
```

4. Check the output:
- Image URLs → images_data.txt
- Downloaded images → images/ folder

## Dependencies

- Python 3
- requests
- beautifulsoup4

## Notes

- This script works best on static pages. React/JS-heavy sites may not return all images.

- Relative URLs are automatically handled.

- For large websites, consider adding delays or exception handling for failed downloads.