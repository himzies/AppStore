from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.
def database(request):
    """Shows the main page"""

    ## Delete customer
    if request.POST:
        if request.POST['action'] == 'delete':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM customer WHERE id = %s", [request.POST['id']])

    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer ORDER BY id")
        users = cursor.fetchall()

    result_dict = {'records': users}

    return render(request,'app/database.html',result_dict)

# Create your views here.
def view(request, id):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        user = cursor.fetchone()
    result_dict = {'cust': user}

    return render(request,'app/view.html',result_dict)

# Create your views here.
def add(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if userid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customer WHERE id = %s", [request.POST['id']])
            user = cursor.fetchone()
            ## No user with same id
            if user == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['id'], request.POST['password'], request.POST['first_name'],
                           request.POST['last_name'] , request.POST['gender'], request.POST['email_address'], request.POST['address'] ])
                return redirect('database')    
            else:
                status = 'User with ID %s already exists' % (request.POST['userid'])


    context['status'] = status
 
    return render(request, "app/add.html", context)

# Create your views here.
def edit(request, id):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE customer SET password = %s, first_name = %s, last_name = %s, gender = %s, email = %s, address = %s WHERE id = %s"
                    , [request.POST['password'], request.POST['first_name'], request.POST['last_name'],
                        request.POST['gender'] , request.POST['email'], request.POST['address'], id ])
            status = 'User edited successfully!'
            cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
 
    return render(request, "app/edit.html", context)

def home(request):
    return render(request,'app/home.html')

def test(request):
    return render(request,'app/test.html')

def login(request):
    context = {}
    status = ""
    if request.POST:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password FROM customer WHERE id = %s", [request.POST["user"]])
            customers = cursor.fetchone()
        if customers == None:
            status = "Login failed, no such user. Please create an account."
        else:
            if customers[1] == request.POST["user_pass"]:
                status = "Login successful."
                return redirect('services', request.POST["user"])
            else:
                status = "Login failed, wrong password."
                
    context["status"] = status
    return render(request,'app/login.html', context)

def login_req(request):
    return render(request,'app/login.php', context)

def services(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM job_category")
        category = cursor.fetchall()
    return render(request,'app/services.html', {'cust': customer, 'cat': category})

    return render(request,'app/tuition.html', {'expert': expertise, 'cust': customer})

def job_req(request, id, expertise):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM provider WHERE %s = expertise", [expertise])
        provider = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    
    return render(request,'app/job_req.html', {'prov': provider, 'cust': customer})

def job_cat(request, id, service):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ' + service.lower().replace(" ", "_"))
        category = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    
    return render(request,'app/job_cat.html', {'cat': category, 'cust': customer, 'serv': service})

#Testing for transaction
def transaction(request, id, person):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM customer WHERE id = %s", [request.POST['id']])
            user = cursor.fetchone()
            cursor.execute("INSERT INTO transaction VALUES (%s, %s, %s, %s, %s)"
                        , [request.POST['id'], request.POST['id'], request.POST['first_name'+'last_name'],
                           request.POST['first_name'+'last_name'], request.POST['address']])
            status = 'Transaction with %s successful' % (request.POST['userid'])
        #with connection.cursor() as cursor:
         #       cursor.execute("SELECT * FROM provider WHERE %s = person", [id])
          #      serviceman = cursor.fetchall()
                
    context['status'] = status
    return render(request, "app/transaction.html", context)
