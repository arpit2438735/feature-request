from feature_request.request.model import Client, Product, Request


class SetupData:
    def __init__(self):
        client_1 = Client('Client_A')
        client_1.insert(client_1)

        client_2 = Client('Client_B')
        client_2.insert(client_2)

        client_3 = Client('Client_C')
        client_3.insert(client_3)

        Client.save()

        product_1 = Product('Policies')
        product_1.insert(product_1)

        product_2 = Product('Billing')
        product_2.insert(product_2)

        product_3 = Product('Claims')
        product_3.insert(product_3)

        product_4 = Product('Reports')
        product_4.insert(product_4)

        Product.save()

        request_1 = Request(title='Public User Profile',
                            description='A public user profile that can be visited by clicking on any users name from the organisation view',
                            client=client_1.id, client_priority=1, product_area=product_2.id,target_date='2017-1-20')

        request_1.insert(request_1)

        request_2 = Request(title='Email system for sending emails and email verification',
                            description='User email validation is where we verify a users email when they sign up with a token/code sent to their inbox',
                            client=client_2.id, client_priority=2, product_area=product_3.id, target_date='2016-12-2')

        request_2.insert(request_2)

        request_3 = Request(title='Add customer satisfaction survey',
                            description='Client wants to be able to send out a survey to evaluate customer satisfaction after issuing a new claim',
                            client=client_3.id, client_priority=1, product_area=product_1.id, target_date='2016-11-11')

        request_3.insert(request_3)

        request_3.save()

        print "Successfully add data to db"

