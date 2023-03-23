import subprocess
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os


# profile = webdriver.FirefoxProfile(os.path.expanduser(r"C:\Users\someuser\AppData\Roaming\Mozilla\Firefox\Profiles\rew5lhld.default-release"))

# options = webdriver.FirefoxOptions()
# options.profile = profile
options = Options()
#if need to load defaul user profile
options.add_argument(r"--user-data-dir=C:\Users\someuser\AppData\Local\Google\Chrome\User Data\Default")
#if need to load extension in chrome
options.add_argument(r"--load-extension=C:\Users\someuser\AppData\Local\Google\Chrome\User Data\Default\Extensions\bpconcjcammlapcogcnnelfmaeghhagj\9.9.8.9982_0")
options.add_argument(r"--load-extension=C:\Users\someuser\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0")

# Configura el driver de Chrome
driver = webdriver.Chrome(options=options)
#  .Firefox(options=options)
# Abre la página web
driver.get("https://www.example.com")

# Espera a que se cargue la página
wait = WebDriverWait(driver, 20)
# time.sleep(10)
#play_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "iframe")))
#play_button.requestFullScreen()
# time.sleep(10)



# anunces = driver.find_element(By.CSS_SELECTOR, '.fc-close')
# anunces.click()

# iframe = driver.find_element(By.TAG_NAME, 'iframe')
# iframe.click()

# print(iframe)

# action_chains = ActionChains(driver)
# action_chains.key_down(Keys.F12).key_up(Keys.F12).perform()
# cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "iagree2")))
# cookies_button.click()
# unmute_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tap_to_unmute_button")))
# unmute_button.click()
# driver.switch_to.window(driver.window_handles[1])

# driver.switch_to.frame(1)

# driver.execute_script("let x =window.document.querySelector('iframe')")
# driver.execute_script("console.log(x)")
# driver.execute_script("""
# alert('hola mundo');
# """)


# driver.execute_script("""
# window.document.querySelector('iframe').style.width='100%';
# window.document.querySelector('iframe').style.position='fixed';
# window.document.querySelector('iframe').style.height='100vh';
# window.document.querySelector('iframe').style.top='0';
# window.document.querySelector('iframe').style.left='0';
# window.document.querySelector('.navbar-light').remove();
# """)

time.sleep(60)



# Obtiene la duración del video
# video_element = driver.find_element_by_xpath("//video")
# video_duration = video_element.get_attribute("duration")

# Inicia la grabación de pantalla con OBS Studio
# obs_exe_path = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"  # Cambia esto a la ruta de tu instalación de OBS Studio
# obs_start_recording_cmd = f'"{obs_exe_path}" --startrecording --minimize-to-tray'
# print(obs_start_recording_cmd)
# subprocess.Popen(obs_start_recording_cmd)
# wait = WebDriverWait(driver, 60)
# driver.implicitly_wait(60) # seconds

# Presiona el botón para reproducir el video
# play_button.click()

# Espera hasta que se reproduzca el video
# time.sleep(float(video_duration))

# Detiene la grabación de pantalla con OBS Studio
# obs_stop_recording_cmd = f'"{obs_exe_path}" --stoprecording'
# subprocess.Popen(obs_stop_recording_cmd)

# Cierra el navegador
driver.quit()