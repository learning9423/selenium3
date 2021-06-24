import unittest
from time import sleep

from selenium import webdriver

class register(unittest.TestCase):
    '''注册账号'''

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        # cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://m-t1.vova.com.hk/index.php?q=admin/register/index')

    def test_register_user(self):
        sponsor=self.driver.find_elements_by_xpath("//*[@id='settle_sponsor']")
        for i in sponsor:

            print(i.text)

    # driver.find_element_by_class_name('email_verify_code').send_keys('123456')
    # driver.find_element_by_class_name('phone').send_keys('15667021976')
    # driver.find_element_by_class_name('sms_verify_code').send_keys('123456')
    # driver.find_element_by_class_name('acct_alias').send_keys('auto')
    # driver.find_element_by_class_name('password').send_keys('Lb123456')
    # driver.find_element_by_class_name('password_again').send_keys('Lb123456')
    # driver.find_element_by_class_name('store_name').send_keys('auto_store')
    # driver.find_element_by_class_name('contacts').send_keys('nico')
    # driver.find_element_by_class_name('register_coupon_code').send_keys('312332323')
    # driver.find_element_by_class_name('register_coupon_code').send_keys('312332323')
    # sleep(5)
    # sleep(5)
    # search.clear()
    # sleep(5)
    # search.send_keys('知乎')
    # sleep(5)
    # search.submit()
    # driver.quit()
# navigate to the application home page
# driverget("http://demo.magentocommerce.com/")
# get the search textbox
# search field driver find element by_ name ("q")
# search field. clear
# enter search keyword and submit
# search field. send keys("phones
# search field. submit
if __name__ == '__main__':
    unittest.main(verbosity=2)