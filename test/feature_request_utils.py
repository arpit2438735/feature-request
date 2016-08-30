import datetime

from feature_request.request.model import Client, Product, Request


class FeatureRequestUtils:

    @staticmethod
    def create_request():
        client_1 = Client('ClientA')
        client_1.insert(client_1)

        client_2 = Client('ClientB')
        client_2.insert(client_2)

        client_3 = Client('ClientC')
        client_3.insert(client_3)

        Client.save()

        product_1 = Product('Policies')
        product_1.insert(product_1)

        product_2 = Product('Billing')
        product_2.insert(product_2)

        Product.save()

        request = Request(title='Add Login Page',
                          description='Client want to have oauth base login',
                          client=client_1.id,
                          client_priority=1,
                          target_date=datetime.datetime.now(),
                          product_area=product_1.id)
        request.insert(request)

        request = Request(title='Add Bootstrap in User Module',
                          description='Client want to have bootstrap framework in user module',
                          client=client_2.id,
                          client_priority=2,
                          target_date=datetime.datetime.now(),
                          product_area=product_2.id)
        request.insert(request)

        request = Request(title='Implement Send Mail Feature',
                          description='Client want to mail where he/she can send direct mail to them from own domain',
                          client=client_1.id,
                          client_priority=2,
                          target_date=datetime.datetime.now(),
                          product_area=product_1.id)
        request.save()

