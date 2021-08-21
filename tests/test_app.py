from app import practicaeli01x


def test_get_price():
    cocacola_price = practicaeli01x('KO').json
    print(cocacola_price)

    assert cocacola_price['price'] > 0
    assert cocacola_price['name'] == 'The Coca-Cola Company'
    assert cocacola_price['exchange'] == 'NYSE'
    assert cocacola_price['currency'] == 'USD'

    assert get_price('KSLAFSADF').status_code == 404


test_get_price()
