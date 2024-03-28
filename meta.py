#AUTHOR DATUK DIE4U FEAT Yuli Arida Seo Seepabx

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import dotenv_values

# Membaca nilai dari berkas .env
env_values = dotenv_values(".env")

# Path ke Chromedriver.exe
PATH = env_values['CHROMEDRIVER_PATH']

# Path profil (jika perlu)
profile_path = env_values['PROFILE_PATH']

# Membuat objek ChromeOptions
options = webdriver.ChromeOptions()

# Menambahkan argumen untuk path profil jika diperlukan
if profile_path:
    options.add_argument(f"--user-data-dir={profile_path}")

# Menambahkan argumen untuk menonaktifkan fitur SameSite cookies
options.add_argument("--disable-features=SameSiteByDefaultCookies")

# Membuat objek WebDriver dengan Chromedriver
driver = webdriver.Chrome(service=Service(PATH), options=options)

# Mengakses halaman Facebook
driver.get(env_values['FACEBOOK_URL'])

time.sleep(500000)

# Mengisi formulir login
element = driver.find_element(By.XPATH, '//*[@id="email"]/input')
element.send_keys(env_values['USERNAME'])

element = driver.find_element(By.XPATH, '//*[@id="passContainer"]/input')
element.send_keys(env_values['PASSWORD'])

element.send_keys(Keys.RETURN)

# Tunggu beberapa saat setelah login sebelum memuat halaman berikutnya
time.sleep(10)

# Memuat halaman inbox
driver.get(env_values['INBOX_URL'])

# Tunggu 10 detik lagi setelah memuat halaman inbox
time.sleep(8)

driver.quit()
