import unittest
import requests

delivery_url = 'http://localhost:8000'
add_delivery_url = f'{delivery_url}/delivery'
get_delivery_url = f'{delivery_url}/delivery'

class TestIntegration(unittest.TestCase):

    def test_create_delivery(self):
        # Отправляем POST-запрос для создания доставки
        delivery_data = {"order_id": 1}
        res = requests.post(f"{add_delivery_url}/1", json=delivery_data)
        
        # Проверяем, что запрос завершился успешно (HTTP статус 200)
        self.assertEqual(res.status_code, 200)

        # Проверяем, что в ответе есть сообщение о создании доставки и delivery_id
        self.assertTrue('message' in res.json())
        self.assertTrue('delivery_id' in res.json())

        self.delivery_id = res.json()['delivery_id']

    def test_get_data_of_delivery(self):
        # Создаем доставку перед получением данных
        self.test_create_delivery()

        # Отправляем GET-запрос для получения данных о доставке
        res = requests.get(f"{get_delivery_url}/1")

        # Проверяем, что запрос завершился успешно (HTTP статус 200)
        self.assertEqual(res.status_code, 200)

        # Проверяем, что в ответе есть order_id и status
        self.assertTrue('order_id' in res.json())
        self.assertTrue('status' in res.json())

if __name__ == '__main__':
    unittest.main()