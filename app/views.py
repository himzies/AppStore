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

def database_provider(request):
    """Shows the main page"""

    ## Delete provider
    if request.POST:
        if request.POST['action'] == 'delete':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM provider WHERE id = %s", [request.POST['id_user']])

    ## Use raw query to get all objects
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM provider ORDER BY id")
        users = cursor.fetchall()

    result_dict = {'records': users}

    return render(request,'app/database_provider.html',result_dict)

# Create your views here.
def view(request, id):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        user = cursor.fetchone()
    result_dict = {'cust': user}

    return render(request,'app/view.html',result_dict)

def view_provider(request, id):
    """Shows the main page"""
    
    ## Use raw query to get a customer
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM provider WHERE id = %s", [id])
        user = cursor.fetchone()
    result_dict = {'cust': user}

    return render(request,'app/view_provider.html',result_dict)

# Create your views here.
def add(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if userid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customer WHERE id = %s", [request.POST['user']])
            user = cursor.fetchone()
            ## No user with same id
            if user == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['user'], request.POST['password'], request.POST['first_name'],
                           request.POST['last_name'] , request.POST['gender'], request.POST['email'], request.POST['address'] ])
                return redirect('login')    
            else:
                status = 'User with ID %s already exists' % (request.POST['user'])


    context['status'] = status
 
    return render(request, "app/add.html", context)

def add_provider(request):
    """Shows the main page"""
    context = {}
    status = ''

    if request.POST:
        ## Check if userid is already in the table
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM provider WHERE id = %s", [request.POST['user']])
            user = cursor.fetchone()
            ## No user with same id
            if user == None:
                ##TODO: date validation
                cursor.execute("INSERT INTO provider VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        , [request.POST['user'], request.POST['password'], request.POST['first_name'], request.POST['last_name'],
                           request.POST['gender'], request.POST['email'], request.POST['expertise'], request.POST['address'] ])
                return redirect('login_provider')    
            else:
                status = 'User with ID %s already exists' % (request.POST['user'])


    context['status'] = status
 
    return render(request, "app/add_provider.html", context)

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

def edit_provider(request, id):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM provider WHERE id = %s", [id])
        obj = cursor.fetchone()

    status = ''
    # save the data from the form

    if request.POST:
        ##TODO: date validation
        with connection.cursor() as cursor:
            cursor.execute("UPDATE provider SET password = %s, first_name = %s, last_name = %s, gender = %s, email = %s, address = %s WHERE id = %s"
                    , [request.POST['password'], request.POST['first_name'], request.POST['last_name'],
                        request.POST['gender'] , request.POST['email'], request.POST['address'], id ])
            status = 'User edited successfully!'
            cursor.execute("SELECT * FROM provider WHERE id = %s", [id])
            obj = cursor.fetchone()


    context["obj"] = obj
    context["status"] = status
 
    return render(request, "app/edit_provider.html", context)

def home(request):
    return render(request,'app/home.html')

def test(request):
    return render(request,'app/test.html')

def cleaning(request):
    return render(request,'app/cleaning.html')

def tuition(request):
    return render(request,'app/tuition.html')

def petcare(request):
    return render(request,'app/petcare.html')

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

def login_provider(request):
    context = {}
    status = ""
    if request.POST:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password FROM provider WHERE id = %s", [request.POST["user"]])
            providers = cursor.fetchone()
        if providers == None:
            status = "Login failed, no such user. Please create an account."
        else:
            if providers[1] == request.POST["user_pass"]:
                status = "Login successful."
                return redirect('prov_home', request.POST["user"])
            else:
                status = "Login failed, wrong password."
                
    context["status"] = status
    return render(request,'app/login_provider.html', context)

def login_req(request):
    return render(request,'app/login.php', context)

def services(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT category FROM jobs ORDER BY category")
        category = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.first_name, p.last_name, SUM(t.price) FROM transaction t, provider p WHERE t.provider_id = p.id " +
                       "GROUP BY p.first_name, p.last_name ORDER BY SUM(t.price) DESC FETCH FIRST 3 ROWS WITH TIES")
        top_provider = cursor.fetchall()
    return render(request,'app/services.html', {'cust': customer, 'cat': category, 'top_p': top_provider})

def prov_home(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM transaction WHERE provider_id = %s", [id])
        transaction = cursor.fetchall()
    return render(request,'app/prov_home.html', {'trans': transaction})

def history(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.first_name, p.last_name, t.expertise, t.price FROM transaction t,\
                        provider p WHERE t.customer_id = %s AND t.provider_id = p.id", [id])
        history = cursor.fetchall()
    return render(request, 'app/history.html', {'hist': history, 'cust': id})

def job_req(request, id, service, expertise):
    with connection.cursor() as cursor:
        cursor.execute("SELECT p.id, p.first_name, p.last_name, p.gender, coalesce(jobs1, 0) as jobs2\
                        FROM provider p\
                        LEFT JOIN (SELECT t.provider_id, COUNT(*) as jobs1\
                        FROM transaction t\
                        WHERE t.expertise = %s\
                        AND t.customer_id = %s\
                        GROUP BY t.provider_id\
                        ORDER BY COUNT(*) DESC) AS s\
                        ON p.id = s.provider_id\
                        WHERE p.expertise = 'Housekeeping'\
                        ORDER BY jobs2 DESC", [expertise, id])
        provider = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    return render(request,'app/job_req.html', {'prov': provider, 'cust': customer, 'exp': expertise})

def job_cat(request, id, service):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM jobs WHERE category = %s', [service])
        category = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    
    return render(request,'app/job_cat.html', {'cat': category, 'cust': customer, 'serv': service})

def transaction(request, id, service, expertise, prov_id):
    context = {}
    status = ''
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customer WHERE id = %s", [id])
        customer = cursor.fetchone()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM provider WHERE id = %s", [prov_id])
        provider = cursor.fetchone()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM jobs WHERE name = %s", [expertise])
        job_title = cursor.fetchone()
    if request.POST:
        if request.POST['confirm'] == 'yes':
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO transaction VALUES (%s, %s, %s, %s, %s)", [id, prov_id, customer[6], expertise, job_title[2]])
                return redirect(services, id)
    return render(request, "app/transaction.html", {'job': job_title, 'cust': customer, 'prov': provider})
