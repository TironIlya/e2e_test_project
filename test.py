from selenium import webdriver
import time

def main():
    # Запуск браузера Chrome и открытие сайта
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")

    # Авторизация
    username = "standard_user"
    password = "secret_sauce"
    login_button = driver.find_element_by_id("login-button")
    login_form = driver.find_element_by_id("login-form")
    login_form.send_keys(username)
    login_form.send_keys(password)
    login_button.click()

    # Выбор товара
    product_name = "Sauce Labs Backpack"
    add_to_cart_button = driver.find_element_by_xpath(
        f"//a[contains(@data-test='{product_name}')]"
    )
    add_to_cart_button.click()

    # Переход в корзину
    go_to_cart_button = driver.find_element_by_link_text("Cart")
    go_to_cart_button.click()

    # Проверка наличия товара в корзине
    item_in_cart = driver.find_elements_by_class_name("item-price")[0].text
    assert "Backpack" in item_in_cart

    # Оформление покупки
    checkout_button = driver.find_element_by_link_text("Checkout")
    checkout_button.click()

    # Заполнение формы доставки и оплаты
    address_fields = ["firstName", "lastName", "address1", "city", "zipCode"]
    for field in address_fields:
        element = driver.find_element_by_id(field)
        element.clear()
        element.send_keys("Test User")

    credit_card_number = driver.find_element_by_id("creditCardNumber")
    credit_card_number.clear()
    credit_card_number.send_keys("4321111111111111")

    expiration_date = driver.find_element_by_id("expirationDate")
    expiration_date.clear()
    expiration_date.send_keys("11/26")

    cvv = driver.find_element_by_id("cvv")
    cvv.clear()
    cvv.send_keys("123")

    submit_button = driver.find_element_by_css_selector(".btn-primary")
    submit_button.click()

    # Проверка успешного завершения покупки
    confirmation_message = driver.find_element_by_class_name("success-msg").text
    assert "Thank you!" in confirmation_message

    # Закрытие окна браузера
    driver.quit()


if __name__ == "__main__":
    main()
