import random
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


report = Report()



driver: WebDriver = webdriver.Chrome(executable_path="D:\\3-2 All subject\\web-directory\\chromedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Device',
    release_name='Test V1',
    selenium_driver=driver
)

driver.get('http://127.0.0.1:8000')

# Test Case 1

try:
    report.write_step(
        'Login in a n user',
        status=report.status.Start,
        test_number=1
    )


    driver.find_element(By.LINK_TEXT, 'Sign in').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('emoncse')
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys('Emon@#123')
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/input').click()
    assert (driver.title == 'eWallet - Profile')
    report.write_step(
        'Successfully login ',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to login',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


# Test Case 1

try:
    report.write_step(
        'Loan Apply',
        status=report.status.Start,
        test_number=2
    )

    driver.find_element(By.XPATH, '/html/body/main/section[2]/div/div/div[1]/button[1]').click()
    driver.find_element(By.NAME, 'amount').send_keys('500')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[2]/div/div/div[2]/div/div/form/div/div/input[2]').click()
    assert (driver.title == 'eWallet - Profile')

    report.write_step(
        'Successfully Loan apply',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Loan apply',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

finally:
    report.generate_report()
    driver.quit()