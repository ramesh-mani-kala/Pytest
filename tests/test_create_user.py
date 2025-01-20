import time

import pytest
from time import sleep

from locators.create_account_locators import email_address
from pages.account_settings import account_settings
from pages.account_settings import Edit



@pytest.mark.usefixtures("setup")
class TestEdit:
    def test_to_verify_the_change_in_mail_while_editing(self):
        edit_driver = Edit(self.driver)
        # edit_driver.clicking_on_create_account_button()
        # sleep(2)
        # edit_driver.enter_the_email("reet@yopmail.com")
        # edit_driver.clicking_on_verify_email()
        # edit_driver.verifying_the_email("reet@yopmail.com")
        # edit_driver.enter_name("Sakshi")
        # edit_driver.enter_last_name("Gupta")
        # edit_driver.enter_password("Sak@1410")
        # edit_driver.confirm_password("Sak@1410")
        # sleep(2)
        # edit_driver.clicking_on_india()
        # sleep(2)
        # edit_driver.clicking_on_checkbox()
        # sleep(3)
        # edit_driver.clicking_on_next()
        # sleep(3)
        edit_driver.open_login_page()
        edit_driver.enter_username('unique00@yopmail.com')
        edit_driver.enter_password('Sak@1410')
        edit_driver.clicking_on_sign_in()
        edit_driver.click_on_edit_profile_settings()
        edit_driver.clicking_on_update_profile()
        edit_driver.clicking_on_verify_your_email_in_popup()
        edit_driver.switching_to_new_window()
        edit_driver.entering_yopmail_mail('unique00@yopmail.com')
        edit_driver.clicking_on_arrow()
        # edit_driver.clicking_on_double_verify()
        #edit_driver.clicking_on_resend_email()
        #edit_driver.clicking_on_refresh()
        #tiedit_driver.clicking_on_netgear()
        #edit_driver.clicking_on_done()
        #edit_driver.clicking_on_login_settings_button()
        #edit_driver.clicking_on_changing_mail()
        #edit_driver.entering_current_email('unique56@yopmail.com')
        #edit_driver.confirm_new_email_address('unique56@yopmail.com')
        #edit_driver.enter_current_password('Sak@1410')
        #edit_driver.clicking_on_submit()
        #edit_driver.enter_username('unique56@yopmail.com')
        #edit_driver.enter_password('Sak@1410')
       # edit_driver.clicking_on_sign_in()

   # def test_to_verify_the_change_in_password(self):
        #edit_driver = Edit(self.driver)
        #edit_driver.open_login_page()
        #edit_driver.enter_username('unique00@yopmail.com')
        #edit_driver.enter_password('Sak@1410')
        #edit_driver.clicking_on_sign_in()
        #edit_driver.click_on_edit_profile_settings()
        #edit_driver.clicking_on_update_profile()
        # edit_driver.clicking_on_verify_your_email_in_popup()
        # edit_driver.switching_to_new_window()
        # edit_driver.entering_yopmail_mail('unique56@yopmail.com')
        # edit_driver.clicking_on_arrow()
        # edit_driver.clicking_on_resend_email()
        # edit_driver.clicking_on_refresh()
        # time.sleep(3)
        # edit_driver.clicking_on_netgear()
        # edit_driver.clicking_on_done()
        # edit_driver.clicking_on_cancel_button_landing()
        edit_driver.clicking_on_login_settings_button()
        edit_driver.clicking_on_change_password_button()
        # edit_driver.entering_old_password('Sak@1406')
        # edit_driver.entering_new_password('Sak@1421')
        # edit_driver.entering_confirm_new_password('Sak@1421')
        # edit_driver.clicking_on_submit_locator()
        # time.sleep(10)

    def test_to_verify_the_two_step_verification(self):
        edit_driver = Edit(self.driver)
        edit_driver.open_login_page()
        edit_driver.enter_username('unique56@yopmail.com')
        edit_driver.enter_password('Sak@1421')
        edit_driver.clicking_on_sign_in()
        edit_driver.click_on_edit_profile_settings()
        edit_driver.clicking_on_update_profile()
        edit_driver.clicking_on_login_settings_button()
        edit_driver.clicking_on_two_step_verification()
        edit_driver.clicking_on_enable_button()
        #edit_driver.clicking_on_checkmark()
        #edit_driver.clicking_on_continue()
        #edit_driver.test_to_scroll_and_find_element()
        #time.sleep()

        # edit_driver.selecting_country()
        # edit_driver.selecting_number()
        # edit_driver.entering_number_france('745751531')
        # edit_driver.get_otp_from_the_target_page('745751531')












