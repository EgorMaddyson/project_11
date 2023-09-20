import configuration
import requests
import data

# Функция создания заказа:
def post_new_orders(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH, json=orders_body)

# print(post_new_orders(data.orders_body).json())

# Функция получения заказа по его треку:
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PATH + str(track))
