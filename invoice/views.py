from http import client
from multiprocessing.connection import Client
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Invoice,clientAddress,Items,senderAddress


  
def invoice_list(request):
    invoice_list = Invoice.objects.all()
    context = {'invoices': invoice_list}
    
    
    "get form data and create invoice in the database "
    template = loader.get_template('invoice/invoice_list.html')
    if request.method == 'POST':
        invoice = Invoice()
        
        #calculate and set custom default field
        invoice.id = invoice.generate_id()
        invoice.generate_due_date()
        
        if request.POST.get('save_as_draft'):
            #save invoice as draft even with no fields
            
            invoice.status = 'Draft'
            invoice.save()
        if request.POST.get('save_main'):
            #create client address
            sender_address = client_address = None
            if request.POST.get('to_street_address'):
                client_address = clientAddress()
                client_address.street = request.POST.get('to_street_address')
                client_address.city = request.POST.get('to_city')
                client_address.postCode = request.POST.get('to_post_code')
                client_address.country = request.POST.get('to_country')
                client_address.save()
            #create sender address
            if request.POST.get('from_street_address'):
                sender_address = senderAddress()
                sender_address.street = request.POST.get('from_street_address')
                sender_address.city = request.POST.get('from_city')
                sender_address.postCode = request.POST.get('from_post_code')
                sender_address.country = request.POST.get('from_country')
                sender_address.save()
            
            
            invoice.description = request.POST.get('description')
            invoice.clientName= request.POST.get('client_name')
            invoice.clientEmail= request.POST.get('client_email')
            invoice.createdAt = request.POST.get('createdAt')
            invoice.paymentTerms = request.POST.get('due_date')
            invoice.status= 'Pending'
            invoice.total = request.POST.get('sum_item_total')
            
            if client_address and sender_address:
                invoice.client_address = client_address
                invoice.sender_address = sender_address
            if request.POST.get('due_date'):
                invoice.paymentDue = invoice.generate_due_date(days=int(request.POST.get('due_date')))
            invoice.save()
            
            # #create items and add foreign key invoice
            # item = Items()
            # item.name = request.POST.get('item_name')
            # item.quantity = request.POST.get('item_qty')
            # item.price = request.POST.get('item_price')
            # item.total = request.POST.get('item_total')
            # if invoice:
            #     item.invoice  = invoice
            return HttpResponse(template.render(context, request))
        
        else:
            return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
    
    #return render(request, 'invoice/invoice_list.html',)