from django.test import TestCase

from .models import LC, LCItem


class LCItemTests(TestCase):

    def setUp(self):
        lc = LC.objects.create(date="2017-12-08", number="0987654321", spinning_mill="Demo Spinning Mill")
        obj = LCItem.objects.create(
            lc=lc,
            count='24/s',
            composition='100% Cotton',
            quantity=1000,
            unit='kg',
            style_no='Demo Style',
            color='Demo Color',
        )

    def test_receive_yarn_method(self):
        """
        Test all the different outcomes of the LCItem methods.
        """
        lc = LC.objects.get(number="0987654321")
        obj = LCItem.objects.get(lc=lc)
        # Available 1000
        self.assertEqual(obj.available_to_receive(), 1000)
        # Error when amount is more than available
        self.assertEqual(obj.receive_yarn(1200), "Amount to receive cannot be more than amount available.")
        obj.yarn_rcv = 1000
        # Available 0
        self.assertEqual(obj.available_to_receive(), 0)
        # Error when item has been completely received and more is requested
        self.assertEqual(obj.receive_yarn(10), "Quantity issued on LC have already been received.")
        # Error when more quantity requested with edit receive method
        self.assertEqual(obj.edit_receive(100, 200), "Amount to receive cannot be more than amount available.")
        # Amount match to 950 when edit receive used to decrease quantity
        obj.yarn_rcv = 1000
        obj.edit_receive(100, 50)
        self.assertEqual(obj.yarn_rcv, 950)
        # Error when yarn delivery amount is more than yarn balance
        obj.yarn_rcv = 1000
        obj.yarn_bal = 0
        obj.yarn_dlv = 1000
        self.assertEqual(obj.deliver_yarn(100), "Amount to deliver is greater than current yarn balance.")
        # Same error when trying to edit yarn delivery to change to a greater amount
        self.assertEqual(obj.edit_deliver(50, 100), "Amount to deliver is greater than current yarn balance.")

