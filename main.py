import random
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


report = Report()



driver: WebDriver = webdriver.Chrome(executable_path="C:\\Users\\Imran Nazir Emon\\Downloads\\chromedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Device',
    release_name='Test V1',
    selenium_driver=driver
)

driver.get('http://127.0.0.1:8000/')

# Test Case 1

try:
    report.write_step(
        'Go to Landing Page',
        status=report.status.Start,
        test_number=1
    )

    assert (driver.title == 'Welcome To eWallet!')
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


# Test Case 2

try:
    report.write_step(
        'Signup for a user',
        status=report.status.Start,
        test_number=2
    )


    driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[5]/a').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('nishat')
    driver.find_element(By.NAME, 'name').send_keys('Nishat Khatun')
    driver.find_element(By.NAME, 'email').send_keys('Nishat@gmail.com')
    driver.find_element(By.ID, 'password').send_keys('Nishat@#123')
    driver.find_element(By.NAME, 'occupation').send_keys('Student')
    time.sleep(1)
    driver.find_element(By.NAME, 'institution').send_keys('UAP')
    driver.find_element(By.NAME, 'dob').send_keys('11/02/2001')
    driver.find_element(By.NAME, 'nid').send_keys('1102002010')
    driver.find_element(By.NAME, 'address').send_keys('Dhaka, Bangladesh')
    driver.find_element(By.NAME, 'phone').send_keys('01773580899')
    time.sleep(1)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/form/div[2]/div[6]/input').click()
    assert (driver.title == 'Sign in - eWallet')
    report.write_step(
        'Successfully Signup ',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Signup',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 3
try:
    report.write_step(
        'Login for a user',
        status=report.status.Start,
        test_number=3
    )

    driver.find_element(By.NAME, 'username').send_keys('nishat')
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys('Nishat@#123')
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


# Test Case 4

try:
    report.write_step(
        'Loan Apply',
        status=report.status.Start,
        test_number=4
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


# Test Case 5

try:
    report.write_step(
        'Go to Loan Status Page',
        status=report.status.Start,
        test_number=5
    )

    driver.find_element(By.XPATH, '/html/body/main/section[2]/div/div/div[1]/button[4]/span').click()
    assert (driver.title == 'Transaction History-Member')

    report.write_step(
        'Loan Status Page Loaded',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Load Loan Status Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 6

try:
    report.write_step(
        'Back to Profile',
        status=report.status.Start,
        test_number=6
    )

    driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[1]/a').click()
    assert (driver.title == 'eWallet - Profile')

    report.write_step(
        'Back to Profile Page',
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

# Test Case 7

try:
    report.write_step(
        'Goto to Password Change Page',
        status=report.status.Start,
        test_number=7
    )

    driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[3]/a').click()
    assert (driver.title == 'Change Password - eWallet')

    report.write_step(
        'Change Password Page Loaded',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Load Change password page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 8

try:
    report.write_step(
        'Password Change',
        status=report.status.Start,
        test_number=8
    )

    driver.find_element(By.NAME, 'old_password').send_keys('Nishat@#123')
    time.sleep(1)
    driver.find_element(By.NAME, 'new_password').send_keys('Emon@#123')
    time.sleep(1)
    driver.find_element(By.NAME, 'new_password').send_keys('Emon@#123')
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/button').click()
    time.sleep(1)
    assert (driver.title == 'Sign in - eWallet')

    report.write_step(
        'Password Changed',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Password Change',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 9

try:
    report.write_step(
        'Logout User',
        status=report.status.Start,
        test_number=9
    )

    driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/header/div/nav/ul/li[4]/a').click()
    time.sleep(1)
    assert (driver.title == 'Welcome To eWallet!')

    report.write_step(
        'User has been logged out.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Logout',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 10
try:
    report.write_step(
        'Login user with new password',
        status=report.status.Start,
        test_number=10
    )

    driver.find_element(By.NAME, 'username').send_keys('nishat')
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys('Emon@#123')
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/form/div[3]/input').click()
    time.sleep(1)
    assert (driver.title == 'eWallet - Profile')
    report.write_step(
        'Successfully login with new password',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to login with new password',
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