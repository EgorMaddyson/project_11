#

import sender_stand_request
import data


# Тест "Получение информации о заказе по его треку":
def test_get_info_about_the_order_by_track():
    order_track = sender_stand_request.post_new_orders(data.orders_body).json()["track"]
    resp_info = sender_stand_request.get_order_by_track(order_track)
    assert resp_info.status_code == 200