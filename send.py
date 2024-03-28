#AUTHOR DATUK DIE4U FEAT Yuli Arida Seo Seepabx

import csv
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from dotenv import dotenv_values

# Membaca nilai dari berkas .env
env_values = dotenv_values(".env")

def date():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date

def countdown(seconds):
    for remaining in range(seconds, -1, -1):
        sys.stdout.write(f"\r{Fore.GREEN}[BOT] {date()}{Style.RESET_ALL} Istirahat Sebentar {remaining} Detik...{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")  # Newline after countdown

# Path ke Chromedriver.exe
PATH = env_values['CHROMEDRIVER_PATH']
 
# Path profil (jika perlu)
profile_path = env_values['PROFILE_PATH']
 
# Membuat objek ChromeOptions
options = Options()
 
# Menambahkan argumen untuk path profil jika diperlukan
if profile_path:
    options.add_argument(f"--user-data-dir={profile_path}")
 
# Menambahkan argumen untuk menonaktifkan fitur SameSite cookies
options.add_argument("--disable-features=SameSiteByDefaultCookies")
 
# Menambahkan argumen untuk mode headless
options.add_argument("--headless")

# Menambahkan argumen untuk menonaktifkan tampilan pesan dari DevTools
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")

# Membaca nilai waktu tidur dari .env
sleep_time = int(env_values.get('SLEEP_TIME', 10))
 
# Membuat objek WebDriver dengan Chromedriver
driver = webdriver.Chrome(service=Service(PATH), options=options)
 
# Mengakses halaman Facebook
driver.get(env_values['INBOX_URL'])

# Baca file CSV
with open('./data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
 
    # Iterasi setiap baris dari data CSV
    for index, row in enumerate(csv_reader, start=1):
        print(f"{Fore.GREEN}[BOT] {date()} {Style.RESET_ALL}Mengirim Pesan Whatsapp ke Nomor {Fore.YELLOW}{row['nama']}{Style.RESET_ALL}[{index}]")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span/div/div[2]/div/div")))
        kliknomor = driver.find_element(By.XPATH, "//span/div/div[2]/div/div")
        kliknomor.click()
 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div/div[2]/div[2]/div/span/div/div")))
        klikkontak = driver.find_element(By.XPATH, "//div[2]/div/div[2]/div[2]/div/span/div/div")
        klikkontak.click()
 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div")))
        nomor_telepon = row['nama']
        input_telepon = driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div")
        input_telepon.click()
 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div/div/input")))
        input_62 = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div/div/div[2]/div/div/input")
        input_62.send_keys("62")
 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div")))
        input_62c = driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div")
        input_62c.click()
 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div/div/input")))
        input_telepon2 = driver.find_element(By.XPATH, "//div[2]/div/div/input")
        input_telepon2.send_keys(nomor_telepon)
 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[2]/textarea")))
        pesan = row['pesan']
        input_pesan = driver.find_element(By.XPATH, "//div[2]/textarea")
        input_pesan.send_keys(pesan)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[3]/div[2]/div[2]/div/span/div/div/div")))
        send_pesan = driver.find_element(By.XPATH, "//div[3]/div[2]/div[2]/div/span/div/div/div")
        send_pesan.click()
        
        print(f"{Fore.GREEN}[BOT] {date()} Pesan Berhasil Terkirim {Style.RESET_ALL}")
        
        countdown(sleep_time)
