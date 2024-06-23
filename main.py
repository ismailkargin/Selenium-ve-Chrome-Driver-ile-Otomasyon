from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome tarayıcısını başlatma
driver = webdriver.Chrome()

try:
    # Web sayfasını açma
    driver.get("https://belgenet.csb.gov.tr/edys-web/sistemeGiris.xhtml")

    # Butonun yüklenmesini beklemek için bir bekleme zamanlayıcısı ayarlayın
    wait = WebDriverWait(driver, 10)

    # Butonun tıklanabilir olmasını bekleyin (id="girisYapButtonKerb" olan buton)
    giris_button = wait.until(EC.element_to_be_clickable((By.ID, "girisYapButtonKerb")))

    # Butona tıklama
    giris_button.click()

    # Burada istediğiniz ek işlemleri yapabilirsiniz (örneğin, oturumu yönetmek veya başka sayfalara gitmek)
    # Örnek olarak, bir sonraki sayfaya geçiş için bekleyebilirsiniz:
    # wait.until(EC.url_to_be("https://belgenet.csb.gov.tr/sonraki_sayfa"))

finally:
    while True:
        continue

