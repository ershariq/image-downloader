import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from io import BytesIO

def fetch_image_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    return img_urls

def download_images(img_urls):
    images = []
    for url in img_urls:
        try:
            img_data = requests.get(url).content
            img_name = url.split("/")[-1]
            images.append((img_name, img_data))
        except Exception as e:
            print(f"Failed to download {url}: {e}")
    return images

def save_images_to_zip(images, zip_name):
    with ZipFile(zip_name, 'w') as zip_file:
        for img_name, img_data in images:
            zip_file.writestr(img_name, img_data)

def main():
    website_url = 'https://vindhyachalbotanicals.com/products/'  # Replace with the target website URL
    zip_file_name = 'images.zip'

    img_urls = fetch_image_urls(website_url)
    images = download_images(img_urls)
    save_images_to_zip(images, zip_file_name)
    print(f"Downloaded {len(images)} images and saved to {zip_file_name}")

if __name__ == "__main__":
    main()

