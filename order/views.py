from rest_framework.views import APIView
from .models import Order, OrderItem
from rest_framework.response import Response
from .serializers import OrderSerializer
from decimal import Decimal
# Models
from address.models import Address
from accounts.models import Account
from warehouse.models import Warehouse
from warehouse_product.models import WarehouseProduct
from cart.models import CartProduct
from wallet.models import Wallet


class OrdersListView(APIView):

    def get(self, request):
        try:
            print(request.GET)
            user_id = request.GET['user_id']
            order_objects = Order.objects.filter(user__id=user_id,
                                                 status__in=['PLACED', 'PACKED',
                                                             'ON_THE_WAY', 'DELIVERED']).order_by('-created_date')
            order_serializer = OrderSerializer(order_objects, many=True)
            return Response(order_serializer.data, status=200)
        except Exception as e:
            print(e)
            return Response(status=500)


class OrderDetailView(APIView):

    def get(self, request):
        try:
            user_id = request.data['user_id']
            order_id = request.data['order_id']
            order_object = Order.objects.get(id=order_id, user__id=user_id)
            order_serializer = OrderSerializer(order_object)
            return Response(order_serializer.data, status=200)
        except Exception as e:
            print(e)
            return Response(status=500)


class PlaceOrderView(APIView):

    def post(self, request):
        try:
            # print(request.data)

            # Fetch User
            user_id = request.data['user_id']
            user_object = Account.objects.get(id=user_id)

            # Fetch Address
            address_id = request.data['address_id']
            address_object = Address.objects.get(id=address_id, user__id=user_id)
            address_string = '{}, {}, {}, {}'.format(address_object.address_line_1, address_object.address_line_2,
                                                     address_object.city.name, address_object.pincode)
            # print(address_string)

            # Fetch Warehouse
            warehouse_id = request.data['warehouse_id']
            warehouse_object = Warehouse.objects.get(id=warehouse_id)

            # Payment
            payment_method = request.data['payment_method']
            card_details = None
            if payment_method == "CARD":
                card_details = request.data['card_details']

            cart_amount = request.data['cart_amount']
            savings = request.data['savings']
            final_amount = request.data['final_amount']
            delivery_fee = request.data['delivery_fee']

            # Delivery Details
            delivery_date_info = request.data['delivery_date'].split(' ')
            delivery_date = '{} {} {}'.format(delivery_date_info[1], delivery_date_info[2], delivery_date_info[3])
            delivery_time = request.data['delivery_time']

            # Cart Items
            cart_items = request.data['cart_items']

            # Create Order
            order_object = Order.objects.create(
                user=user_object,
                warehouse=warehouse_object,
                address=address_string,
                status="PLACED",
                delivery_date=delivery_date,
                delivery_time=str(delivery_time),
                cart_amount=cart_amount,
                savings=savings,
                final_amount=final_amount,
                delivery_fee=delivery_fee,
                city=warehouse_object.name

            )

            if payment_method == 'CARD':
                order_object.payment_method = 'CARD'
                order_object.payment_completed = True
                order_object.card_number = card_details['cardNumber']
            elif payment_method == 'WALLET':
                order_object.payment_method = 'WALLET'
                wallet_object = Wallet.objects.get(user__id=user_id)
                if wallet_object.credit >= final_amount:
                    wallet_object.credit -= Decimal(final_amount)

                    wallet_object.save()
                    order_object.payment_completed = True
                else:
                    print("Not enough balance in wallet")
                    order_object.payment_completed = False
            else:
                order_object.payment_method = 'COD'

            # order_object.save()

            # Create Order Items
            total_cart_items = 0
            for item in cart_items:
                warehouse_product_object = WarehouseProduct.objects.get(id=int(item['warehouse_product']['id']))
                order_item = OrderItem.objects.create(
                    order=order_object,
                    warehouse_item=warehouse_product_object,
                    quantity=item['quantity'],
                )
                warehouse_product_object.stock -= item['quantity']
                total_cart_items += item['quantity']
                warehouse_product_object.save()
                order_item.save()

            order_object.total_items = total_cart_items

            order_object.save()

            CartProduct.objects.filter(user=user_object,
                                       warehouse=warehouse_object).delete()
            response = Response()
            response.data = {'success_message': 'Order placed successfully.'}
            response.status = 200
            return response
        except Exception as e:
            response = Response()
            response.data = {'error_message': 'Some error occurred while placing your order. Please try again later.'}
            response.status = 500
            return response
