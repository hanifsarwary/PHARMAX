from django.urls import path
from .views import *
app_name = 'Inventory'
urlpatterns = [
    path('<str:username>/Inventory',inventoryView.as_view(), name='inventoryView'),

    path('updateinventory',updateinventory,name='inventoryupdate'),
    path('addinventory',addinventory,name='inventoryadd'),
    path('updatemedicine',updateMedicine,name='medicineupdate'),
    path('addmedicine',addMedicine,name='medicineadd'),
    path('<str:username>/Medicine', medicineView.as_view(), name='medicineView'),
    path('<str:username>/Bill', billView.as_view(), name='billView'),
    path('addBill', addBill, name='addbillView'),
    path('<str:username>/Supplier', supplierView.as_view(), name='supplierView'),
    path('addSupplier',addSupplier, name='addsupplierView'),
    path('updateSupplier',updateSupplier, name='updatesupplierView'),
    path('<str:username>/salesmen', salesManView.as_view(), name='salesmenView'),
    path('addsalesman',addsalesman.as_view(),name='addsalesmanView'),
    path('<str:username>/requestTransfer',RequestTransferView.as_view(),name='transferView'),
    path('addRequest', addTransferRequest, name='addTransferRequest'),
    path('<str:username>/requests',RequestsListView.as_view(),name='requestlistView'),
    path('<str:username>/requests/<int:id>',RequestDetails.as_view(),name='requestDetailView'),
    path('<str:username>/bills',BillListView.as_view(),name='billListView'),
    path('deleteInventory/<str:name>',DeleteInventory,name='deleteInventoryView'),
    path('approveRequest/<int:id>',ApproveTransferRequest.as_view(),name='approveRequestView'),
    path('logout',logoutView,name='logoutView'),
]