from bookstoreapi.viewsets import CustomerViewset, Place_OrderViewset, BookViewset, BillingViewset, CategoryViewset, CashierViewset, AuthorViewset, PublisherViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register ('Customer', CustomerViewset)
router.register ('Place_Order', Place_OrderViewset)
router.register ('Book', BookViewset)
router.register ('Billing', BillingViewset)
router.register ('Category', CategoryViewset)
router.register ('Cashier', CashierViewset)
router.register ('Author', AuthorViewset)
router.register ('Publisher', PublisherViewset)






