
from .models import *
# Create your views here.
from django.views.generic import ListView
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from datetime import datetime
import json

from .forms import UserForm


class inventoryView(LoginRequiredMixin,ListView):
    login_url = '/'
    model = Inventory
    template_name = 'Inventory.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        array = Inventory.objects.values_list('med_id__name')
        temp = []
        med = Medicine.objects.all()

        flag=0
        for m in med:
            for arr in array:
                if m.name!= arr[0]:
                    flag+=1
            if flag==array.count():
                temp.append(m.name)
            flag=0

        return {'inventory':Inventory.objects.all(),'user':self.request.user,'medicine':temp}



def logoutView(request):


    logout(request)
    return HttpResponseRedirect(reverse('User:loginView'))

def updateinventory(request):

    if request.method =='GET':
        name = request.GET['name']
        temp = Medicine.objects.filter(name=name)
        obj = Inventory.objects.filter(med_id=temp)
        pck = (request.GET['packet'])
        ppl = (request.GET['ppl'])
        plt = (request.GET['plt'])
        print(pck)
        print(ppl)
        print(plt)
        if pck is None:
            pck = obj.packet_count

        if ppl is None:
           ppl = obj.max_leaf_count

        if plt is  None:
            plt = obj.max_leaf_count

        Inventory.objects.filter(med_id__name=name).update(
            packet_count= pck,
            max_leaf_count =ppl,
            max_tablet_count = plt,
            location= request.GET['location']
        )
    return JsonResponse({'success':"succss"})

def addinventory(request):
    if request.method =='POST':
        name = request.POST['name']
        temp = Medicine.objects.get(name=name)
        loc = request.POST['location']
        pck = int(str(request.POST['packet']))
        ppl = int(str(request.POST['ppl']))
        plt = int(str(request.POST['plt']))
        bid = request.user.bid
        Inventory.objects.create(
            med_id=temp,
            packet_count= pck,
            max_leaf_count =ppl,
            max_tablet_count = plt,
            location= loc,
            branch_id=bid
        )
    return JsonResponse({'success':"succss"})


def updateMedicine(request):

    if request.method =='GET':
        name = request.GET['name']
        potency = request.GET['pot']
        price = int(str(request.GET['price']))
        category = request.GET['cat']

        Medicine.objects.filter(name=name).update(potency=potency,price=price,category=category)

        return JsonResponse({'sucess':'Success'})


def addMedicine(request):

    if request.method=='POST':
        name = request.POST['name']
        potency = request.POST['pot']
        price = int(str(request.POST['price']))
        category = request.POST['cat']
        s_name = request.POST['s_name']
        sid = Supplier.objects.get(name=s_name)

        Medicine.objects.create(name=name,sid=sid,potency=potency,price=price,category=category)

        return JsonResponse({'sucess': 'Success'})


class medicineView(LoginRequiredMixin,ListView):
    template_name = 'Medicine.html'
    login_url = '/'
    model = Medicine

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'medicine':    Medicine.objects.all(), 'user': self.request.user, 'supplier':Supplier.objects.all()}


class billView(LoginRequiredMixin,ListView):
    template_name = 'bill.html'
    login_url = '/'
    model = Inventory

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'inventory':Inventory.objects.all(),'user':self.request.user}


def addBill(request):

    if request.method =='GET':
        names= json.loads(request.GET.get('names'))
        counts =json.loads(request.GET.get('tab_counts'))

        customer_name = request.GET['customer_name']
        customer_phone = request.GET['customer_phone']
        if str(customer_name).isalnum():
            return JsonResponse({"message": "customer value is not valid"})
        customer = Customer.objects.create(name=customer_name,mobile_number=customer_phone)
        bill = Bill.objects.create(date=datetime.now(),cid = customer)
        for n,c in zip(names,counts):
            med = Medicine.objects.get(name=n)
            inven_obj = Inventory.objects.filter(med_id=med)
            max_tab = (inven_obj.values('max_tablet_count')[0]).get('max_tablet_count')
            max_leaf = (inven_obj.values('max_leaf_count')[0]).get('max_leaf_count')
            max_pack = (inven_obj.values('max_pack_count')[0]).get('max_pack_count')
            tab_count = (inven_obj.values('tablet_count')[0]).get('tablet_count')
            leaf_count = (inven_obj.values('leaf_count')[0]).get('leaf_count')
            packet_count = (inven_obj.values('packet_count')[0]).get('packet_count')

            l_c=int(leaf_count)
            p_c = int(packet_count)
            t_c = int(tab_count)-(int(c) % int(max_tab))
            if t_c <0:
                t_c = t_c+int(max_tab)
                l_c -= 1

            l_c = l_c - ((int(c)//int(max_tab)) % int(max_leaf))
            if l_c<0:
                l_c = l_c+int(max_leaf)
                p_c -= 1

            p_c = p_c - ((int(c) // int(max_tab)) // int(max_leaf))
            if(p_c <0):
                return (JsonResponse({"message":"amount of medicine is not available"}))
            else:
                Bill_Details.objects.create(mid=med,bid=bill,quantity=int(c),price=med.price*int(c))
                inven_obj.update(tablet_count=t_c,leaf_count=l_c,packet_count=p_c)
                return JsonResponse({"message":"Successful"})


class supplierView(LoginRequiredMixin,ListView):
    template_name = 'Supplier.html'
    login_url = '/'
    model = Supplier
    def get_context_data(self, *, object_list=None, **kwargs):
        return {'supplier':Supplier.objects.all(),'user':self.request.user}



def addSupplier(request):

    if request.method =='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        email = request.POST['email']
        manu_name = request.POST['manu_name']

        Supplier.objects.create(name=name,phone=phone,city=city,email=email,manu_name=manu_name)

        return JsonResponse({'success':'success'})


def updateSupplier(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        email = request.POST['email']
        manu_name = request.POST['manu_name']

        Supplier.objects.get(name=name).update(name=name, phone=phone, city=city, email=email, manu_name=manu_name)

        return JsonResponse({'success': 'success'})

class salesManView(LoginRequiredMixin,ListView):
    model = CustomUser
    login_url = '/'
    template_name = 'SalesMen.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'form':UserForm(),'users':CustomUser.objects.filter(desgination='s')}


class addsalesman(View):


    def post(self, request, *args, **kwargs):
        first = request.POST['first_name']
        last = request.POST['last_name']
        username =request.POST['username']
        email=request.POST['email']
        dob = request.POST['dob']
        password = request.POST['password']
        phone = request.POST['phone']
        salary = request.POST['salary']
        cnic = request.POST['cnic']
        bid = Branch.objects.filter(id=request.POST['bid'])
        address = request.POST['address']

        CustomUser.objects.create_user(first_name=first,last_name=last,username=username,email=email,password=password,phone=phone,bid=bid[0],desgination='s',dob=dob,
                                       cnic=cnic,address=address,salary=salary)
        return JsonResponse({'success': 'success'})


class RequestTransferView(LoginRequiredMixin,ListView):
    template_name = 'requests_add.html'
    login_url = '/'
    model = Inventory

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'inventory':Inventory.objects.all(),'user':self.request.user}


class RequestsListView(LoginRequiredMixin,ListView):
    template_name = 'RequestList.html'
    login_url = '/'
    model = Transfer_Request

    def get_context_data(self, *, object_list=None, **kwargs):
        #'requests': Transfer_Request.objects.filter(status='P').exclude(branchFromid=self.request.user.bid)
        return {'requests':Transfer_Request.objects.filter(status='P'),
                'user': self.request.user}


def addTransferRequest(request):

    if request.method =='GET':
        names= json.loads(request.GET.get('names'))
        counts =json.loads(request.GET.get('tab_counts'))
        if (len(names) ==0) or (len(counts)==0):
            return JsonResponse({"message":"add proper input"})
        else:
            tr = Transfer_Request.objects.create(branchFromid=request.user.bid,request_date=datetime.now(),status='P')
            for n,c in zip(names,counts):
                med = Medicine.objects.get(name=n)


                Transfer_Request_Details.objects.create(transfer_request=tr,med=med,packet_count=c)

            return JsonResponse({"message":"Successful"})


class RequestDetails(LoginRequiredMixin,ListView):
    template_name = 'request Details.html'
    login_url = '/'
    model = Transfer_Request_Details

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'details':Transfer_Request_Details.objects.filter(transfer_request=self.kwargs.get('id')),
                'user':self.request.user,'id':self.kwargs.get('id')}


class BillListView(LoginRequiredMixin,ListView):
    template_name = 'BillList.html'
    login_url = '/'
    model = Bill

    def get_context_data(self, *, object_list=None, **kwargs):
        #'requests': Transfer_Request.objects.filter(status='P').exclude(branchFromid=self.request.user.bid)
        return {'bills':Bill.objects.all(),
                'user': self.request.user}


class BillDetails(LoginRequiredMixin,ListView):
    template_name = 'Bill Details.html'
    login_url = '/'
    model = Bill_Details

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'details':Bill_Details.objects.filter(bid=self.kwargs.get('id')),
                'user':self.request.user}

class ApproveTransferRequest(View):
    def get(self,request,id):
        trd = Transfer_Request_Details.objects.filter(transfer_request=self.kwargs.get('id'))
        for t in trd:

            obj = Inventory.objects.get(med_id__name=t.med.name)
            p_c = obj.packet_count-t.packet_count
            if(p_c<0):
                return JsonResponse({'message': 'you do not have eneough medicine to serve this request'})

        Transfer_Request.objects.filter(pk=self.kwargs.get('id')).update(status='A')
        for t in trd:
            obj = Inventory.objects.get(med_id__name=t.med.name)
            p_c = obj.packet_count - t.packet_count
            Inventory.objects.filter(med_id__name=t.med.name).update(packet_count=p_c)
        return JsonResponse({'message':'successfully approved'})


def DeleteInventory(request,name):

        obj = Medicine.objects.get(name=name)
        Inventory.objects.get(med_id=obj).delete()
        return HttpResponseRedirect(reverse('Inventory:inventoryView',kwargs={'username':request.user.username}))
