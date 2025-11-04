import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from myapp.models import *


def logout(request):
    request.session.flush()  # Clear session
    response = redirect('/myapp/login/')  # Redirect to login page
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    request.session['lid']=''
    return redirect('/myapp/login/')


def login(request):
    request.session["lid"]=""
    return render(request, 'loginindex.html')


def login_post(request):
    uname = request.POST['name']
    password = request.POST['pass']
    L = Login.objects.filter(username=uname, password=password)
    if L.exists():
        a = Login.objects.get(username=uname, password=password)
        request.session['lid']=a.id
        if a.type == "admin":
            return HttpResponse('''<script>alert("SUCCESSFULLY LOGIN");window.location='/myapp/adminhome/'</script>''')
        elif a.type=='staff':
            return HttpResponse('''<script>alert("SUCCESSFULLY LOGIN");window.location='/myapp/staffhome/'</script>''')



    return HttpResponse('''<script>alert("invalid user");window.location='/myapp/login/'</script>''')


def check_session(request):
    is_logged_in = request.session['lid']

    if is_logged_in=="":
        is_logged_in="no"
    else:
        is_logged_in="yes"

    # Check if session exists
    return JsonResponse({'is_logged_in': is_logged_in})

def addcourse(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res = Department.objects.all()
    return render(request, 'ADMIN/ADD_COU.html', {"data": res})


def addcourse_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    department = request.POST['dep']
    coursename = request.POST['textfield2']
    sem = request.POST['textfield3']
    ob = Course()
    ob.coursename = coursename
    ob.DEPARTMENT_id = department
    ob.semester = sem
    ob.save()
    return HttpResponse('''<script>alert("SUCCESS");window.location='/myapp/adminhome/'</script>''')


def delcourse(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Course.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addept(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    return render(request, 'ADMIN/ADD_DEPT.html')


def addept_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    department = request.POST['textfield']
    ob = Department()
    ob.departmentname = department
    ob.save()
    return HttpResponse('''<script>alert("SUCCESS");window.location='/myapp/adminhome/'</script>''')


def deldept(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    l = []

    s = Staff.objects.filter(DEPRTMENT_id=id)

    l = []
    for i in s:
        l.append({
            "id": i.id,
        })

    s.delete()


    Department.objects.get(id=id).delete()

    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')

def eddept(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    d=Department.objects.get(id=id)
    return render(request,'ADMIN/UPDATE_DEPT.html',{'data':d})

def eddept_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    departmentname=request.POST['textfield']
    id=request.POST['id']
    Department.objects.filter(id=id).update(departmentname=departmentname)
    return HttpResponse('''<script>alert("EDIT DEPARTMENT");window.location='/myapp/adminhome/'</script>''')


# def addevent(request):
#     return render(request, 'ADMIN/ADD_EVENT.html')
#
#
# def addevent_post(request):
#     type = request.POST['textfield3']
#     time = request.POST['textfield4']
#     venue = request.POST['textfield5']
#     date = request.POST['textfield']
#     ob = Events()
#     ob.date = date
#     ob.type = type
#     ob.venue = venue
#     ob.time = time
#     ob.save()
#     return HttpResponse('''<script>alert("EVENT ADDED");window.location='/myapp/adminhome/'</script>''')


def delevent(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    Events.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addfacility(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    return render(request, 'ADMIN/ADD_FACILITY.html')


def addfacility_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    name = request.POST['select']
    image = request.FILES['fileField']

    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, image)
    path = fs.url(date)
    ob = Facility()
    ob.name = name
    ob.image = path
    ob.save()
    return HttpResponse('''<script>alert("FACILITY ADDED");window.location='/myapp/adminhome/'</script>''')


def delfacility(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Facility.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addschedule(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/ADD_SCHEDULE.html')


def addschedule_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    date = request.POST['textfield']
    program_name = request.POST['textfield22']
    time = request.POST['textfield2']
    obg=Schedule()
    obg.programname=program_name
    obg.date=date
    obg.time=time
    obg.save()
    return HttpResponse('''<script>alert("SCHEDULE ADDED");window.location='/myapp/adminhome/'</script>''')


def delschedule(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Schedule.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addstaff(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    rus = Department.objects.all()
    return render(request, 'ADMIN/ADD_STAFF.html', {"data": rus})

def email_exist(request):
    email = request.POST['email']
    status = Staff.objects.filter(email = email).exists()
    return JsonResponse({'status':status})

def addstaff_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    department = request.POST['stf']
    name = request.POST['textfield']
    designation = request.POST['textfield1']
    print(designation)
    place = request.POST['textfield2']
    district = request.POST['District']
    phone = request.POST['textfield4']
    email = request.POST['email']
    gender = request.POST['RadioGroup1']
    yoj = request.POST['textfield6']
    qualification = request.POST['textfield7']
    experience = request.POST['textfield8']
    photo = request.FILES['fileField']

    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)
    L = Login()
    L.username = email
    import random
    L.password = random.randint(0000, 9999)
    L.type = 'staff'
    L.save()

    ob = Staff()
    ob.name = name
    ob.DEPRTMENT_id = department
    ob.designation = designation
    ob.place = place
    ob.phone = phone
    ob.district = district
    ob.email = email
    ob.photo = path
    ob.qualification = qualification
    ob.experience = experience
    ob.gender = gender
    ob.yoj = yoj
    ob.LOGIN = L
    ob.save()
    return HttpResponse('''<script>alert("STAFF ADDED");window.location='/myapp/adminhome/'</script>''')


def delstaff(request, id):
    Staff.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addstudent(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    s = Course.objects.all()
    return render(request, 'ADMIN/ADD_STU.html', {"data": s})


def addstudent_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    course = request.POST['std']
    admno = request.POST['textfield']
    name = request.POST['textfield2']
    dob = request.POST['textfield3']
    place = request.POST['textfield5']
    email = request.POST['email']
    phone = request.POST['textfield7']
    pin = request.POST['textfield8']
    ob = Student()
    ob.admissionNo = admno
    ob.name = name
    ob.dob = dob
    ob.COURSE_id = course
    ob.place = place
    ob.email = email
    ob.phone = phone
    ob.pin = pin
    ob.save()
    return HttpResponse('''<script>alert("STUDENT ADDED");window.location='/myapp/adminhome/'</script>''')


def delstudent(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Student.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addsub(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    abc = Course.objects.all()
    return render(request, 'ADMIN/ADD_SUB.html', {"data": abc})


def addsub_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    course = request.POST['std']
    subname = request.POST['textfield']
    sem = request.POST['textfield2']
    ob = Subject()
    ob.subjectname = subname
    ob.sem = sem
    ob.COURSE_id = course
    ob.save()
    return HttpResponse('''<script>alert("SUBJECT ADDED");window.location='/myapp/adminhome/'</script>''')


def delsub(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Subject.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def addsupport(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/ADD_SUPPORT.html')


def addsupport_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    category = request.POST['select']
    ob = Support()
    ob.category = category
    ob.save()

    return HttpResponse('''<script>alert("SUPPORT");window.location='/myapp/adminhome/'</script>''')


def delsupport(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Support.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/adminhome/'</script>''')


def allostaff(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    staff=Staff.objects.all()
    sub=Subject.objects.all()
    return render(request, 'ADMIN/ALLOCATE_STAFF.html',{'staff':staff,'sub':sub})


def allostaff_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    staff = request.POST['select1']
    suject = request.POST['select']
    ob=Allocate()
    ob.STAFF_id=staff
    ob.SUBJECT_id=suject
    ob.status='allocate'
    ob.date=datetime.datetime.now().date()
    ob.save()

    return HttpResponse('''<script>alert("STAFF ALLOCATED");window.location='/myapp/adminhome/'</script>''')


def delallostaff(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Allocate.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETTED");window.location='/myapp/adminhome/'</script>''')


def edallostaff(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    a=Staff.objects.all()
    g=Subject.objects.all()
    ob=Allocate.objects.get(id=id)
    return render(request, 'ADMIN/EDIT ALLOCATE_STAFF.html',{'data':ob,'data1':a,'g':g})


def edallostaff_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    staff = request.POST['select']
    subject = request.POST['select']
    ed=request.POST['id']
    eda=Allocate.objects.get(id=ed)
    eda.STAFF_id=staff
    eda.SUBJECT_id=subject
    eda.save()
    return HttpResponse('''<script>alert("EDIT STAFF");window.location='/myapp/adminhome/'</script>''')


def edcourse(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    d = Department.objects.all()
    ob = Course.objects.get(id=id)
    return render(request, 'ADMIN/EDIT_COU.html', {'data': ob, 'data1': d })


def edcourse_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    department = request.POST['select']
    coursename = request.POST['textfield2']
    semester = request.POST['textfield3']
    cid = request.POST['id']
    sh = Course.objects.get(id=cid)
    sh.coursename = coursename
    sh.semester = semester
    sh.DEPARTMENT_id = department
    sh.save()
    return HttpResponse('''<script>alert("EDIT COURSE");window.location='/myapp/viewcou/'</script>''')


def edevent(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/EDIT_EVENT.html')


def edevent_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    date = request.POST['textfield']
    type = request.POST['textfield2']
    time = request.POST['textfield3']
    venue = request.POST['textfield4']
    return HttpResponse('''<script>alert("EDIT EVENT");window.location='/myapp/adminhome/'</script>''')


def edfacility(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    f=Facility.objects.get(id=id)
    return render(request, 'ADMIN/EDIT_FACILITY.html',{'data':f})

def edfacility_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    name = request.POST['select']

    fa=request.POST['id']
    fac = Facility.objects.get(id=fa)
    fac.name = name

    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date,image )
        path = fs.url(date)


        fac.image=path
    fac.save()

    return HttpResponse('''<script>alert("EDIT FACILITY");window.location='/myapp/viewfacility/'</script>''')


def edschedule(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    a=Schedule.objects.get(id=id)
    return render(request, 'ADMIN/EDIT_SCHEDULE.html',{'data':a})


def edschedule_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    programname = request.POST['textfield11']
    date = request.POST['textfield']
    time = request.POST['textfield2']
    she=request.POST['id']
    sh=Schedule.objects.get(id=she)
    sh.programname=programname
    sh.date=date
    sh.time=time
    sh.save()
    return HttpResponse('''<script>alert("EDIT SCHEDULE");window.location='/myapp/viewschedule/'</script>''')


def edstaff(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    b = Department.objects.all()
    s = Staff.objects.get(id=id)
    return render(request, 'ADMIN/EDIT_STAFF.html',{"data":s,"data1":b})


def edstaff_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    department = request.POST['select']
    name = request.POST['textfield']
    designation=request.POST['textfield1']
    place = request.POST['textfield2']
    descript = request.POST['textfield3']
    pin = request.POST['textfield4']
    email = request.POST['textfield5']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield6']
    qualification = request.POST['textfield7']
    experience = request.POST['textfield8']
    print(department)
    st = request.POST['id']
    sta = Staff.objects.get(id=st)
    if 'fileField' in request.FILES:

        photo = request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        sta.photo=path
        sta.save()


    sta.name = name
    sta.DEPRTMENT_id = department
    sta.place = place
    sta.designation = designation
    sta.pin = pin
    sta.district = descript
    sta.email = email
    sta.qualification = qualification
    sta.experience = experience
    sta.gender = gender
    sta.yoj = dob
    sta.save()

    return HttpResponse('''<script>alert("EDIT STAFF");window.location='/myapp/viewstaff/'</script>''')


def edstud(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    a=Course.objects.all()
    s=Student.objects.get(id=id)

    return render(request, 'ADMIN/EDIT_STUDENT.html',{"data":s,"data1":a})


def edstud_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    course = request.POST['select']
    admno = request.POST['textfield2']
    name = request.POST['textfield3']
    dob = request.POST['textfield4']
    place = request.POST['textfield5']
    email = request.POST['textfield6']
    phone = request.POST['textfield7']
    pin = request.POST['textfield8']

    ab=request.POST['id']
    abc=Student.objects.get(id=ab)
    abc.COURSE.id=course
    abc.admissionNo=admno
    abc.name=name
    abc.dob=dob
    abc.place=place
    abc.email=email
    abc.phone=phone
    abc.pin=pin
    abc.save()
    return HttpResponse('''<script>alert("EDIT STUDENT");window.location='/myapp/viewstu/'</script>''')


def edsub(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    c = Course.objects.all()
    ed = Subject.objects.get(id=id)
    return render(request, 'ADMIN/EDIT_SUB.html', {'data': ed, 'data1': c})


def edsub_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    prg=request.POST['select']
    subname = request.POST['textfield']
    sem=request.POST['textfield2']
    aid = request.POST['id']
    ab = Subject.objects.get(id=aid)
    ab.COURSE_id=prg
    ab.subjectname = subname
    ab.sem=sem
    ab.save()
    return HttpResponse('''<script>alert("EDIT SUBJECT");window.location='/myapp/viewsub/'</script>''')


def edsuprt(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    su=Support.objects.get(id=id)
    return render(request, 'ADMIN/EDIT_SUPPORT.html',{'data':su})


def edsuprt_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    category = request.POST['select']
    id = request.POST['id']

    Support.objects.filter(id=id).update(category=category)

    return HttpResponse('''<script>alert("EDIT SUPPORT");window.location='/myapp/viewsuprt/'</script>''')


def feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Feedback.objects.all()
    return render(request,'ADMIN/FEEDBACK.html',{'data':ob})

def feedback_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    return HttpResponse('''<script>alert("OK");window.location='/myapp/adminhome/'</script>''')


def gallery(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/GALLERY.html')


def gallery_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    image = request.FILES['fileField']
    date = request.POST['textfield']
    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, image)
    path = fs.url(date)
    ob=Gallary()

    return HttpResponse('''<script>alert("OK");window.location='/myapp/adminhome/'</script>''')


def sendrply(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/SEND_RLPY.html',{"id":id})


def sendrply_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    reply = request.POST['textfield']
    id = request.POST['id']
    obj=Complaints.objects.get(id=id)
    obj.reply=reply
    obj.status='replied'
    obj.save()
    return HttpResponse('''<script>alert("SEND");window.location='/myapp/adminhome/'</script>''')


def updept(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/UPDATE_DEPT.html')


def updept_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    department = request.POST['textfield']
    return HttpResponse('''<script>alert("UPDATE");window.location='/myapp/adminhome/'</script>''')


def viewallo(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    data=Allocate.objects.all()
    course=Course.objects.all()
    return render(request, 'ADMIN/VIEW_ALLOCATE.html',{'data':data,'data1':course})


def viewallo_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    subject = request.POST['select']
    # staff = request.POST['textfield']
    search = request.POST['textfield']
    course=Course.objects.all()

    data=Allocate.objects.filter(SUBJECT__subjectname__icontains=search,)
    return render(request, 'ADMIN/VIEW_ALLOCATE.html', {'data':data,"data1":course})


def viewcmpnt(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Complaints.objects.all()
    return render(request, 'ADMIN/VIEW_COMPLAINT.html', {'data': ob})


def viewcmpnt_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    ob = Complaints.objects.filter(date__range=[fromdate,todate])
    return render(request, 'ADMIN/VIEW_COMPLAINT.html', {'data': ob})


def viewcou(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Course.objects.all()
    return render(request, 'ADMIN/VIEW_COU.html', {'data':ob})


def viewcou_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    ob = Course.objects.filter(coursename__icontains=search)
    return render(request, 'ADMIN/VIEW_COU.html',{'data':ob})


def viewdept(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Department.objects.all()
    return render(request, 'ADMIN/VIEW_DEPT.html', {'data': ob})


def viewdept_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    search = request.POST['textfield']
    ob = Department.objects.filter(departmentname__icontains=search)
    return render(request, 'ADMIN/VIEW_DEPT.html', {'data': ob})


def viewevent(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    e=Events.objects.all()
    return render(request, 'ADMIN/VIEW_EVENT.html', {'data':e})

def viewevent_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    e=Events.objects.filter(date__range=[fromdate,todate])
    return render(request, 'ADMIN/VIEW_EVENT.html', {'data':e})

def viewfacility(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Facility.objects.all()
    n=Facility.objects.all()
    return render(request,'ADMIN/VIEW_FACILITY.html', {'data': ob,'n':n})


def viewfacility_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    name = request.POST['select']
    # search=request.POST['textfield']
    fa=Facility.objects.filter(name__contains=name)
    n = Facility.objects.all()
    return render(request,'ADMIN/VIEW_FACILITY.html',{'data':fa,'n':n})


def viewgallery(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob=Gallary.objects.all()
    return render(request, 'ADMIN/VIEW_GALLARY.html',{'data':ob})


def viewgallery_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    ob = Gallary.objects.filter(date__range=[fromdate,todate])
    return render(request, 'ADMIN/VIEW_GALLARY.html', {'data': ob})

def viewschedule(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    obg=Schedule.objects.all()
    return render(request, 'ADMIN/VIEW_SCHEDULE.html',{'data':obg})


def viewschedule_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    programname = request.POST['form2']
    n=Schedule.objects.all()
    return render(request, 'ADMIN/VIEW_SCHEDULE.html',{'data':n})


def viewstaff(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Staff.objects.all()
    return render(request, 'ADMIN/VIEW_STAFF.html', {'data': ob})


def viewstaff_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    ob=Staff.objects.filter(DEPRTMENT__departmentname__icontains=search)
    return render(request,'ADMIN/VIEW_STAFF.html',{'data':ob})


def viewstu(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Student.objects.all()
    co=Course.objects.all()
    return render(request, 'ADMIN/VIEW_STU.html', {'data': ob,'co':co})


def viewstu_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    course = request.POST['textfield']
    search=request.POST['textfield']
    ob=Student.objects.filter(admissionNo__contains=search)
    return render(request,'ADMIN/VIEW_STU.html',{'data':ob})


def viewsub(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    ob = Subject.objects.all()
    co = Course.objects.all()
    c=Department.objects.all()

    return render(request, 'ADMIN/VIEW_SUB (2).html', {'data': ob, 'co': co,'c':c})


def viewsub_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    co = Course.objects.all()
    s=request.POST['select']
    ob = Subject.objects.filter(COURSE_id=s)


    return render(request, 'ADMIN/VIEW_SUB (2).html', { 'data':ob,'co': co })


def viewsuprt(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob = Support.objects.all()
    return render(request, 'ADMIN/VIEW_SUPPORT.html', {'data': ob})


def viewsuprt_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    s=Support.objects.filter(category__contains=search)
    return render(request,'ADMIN/VIEW_SUPPORT.html',{'data':s})

def addhostel(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    r=Hostel.objects.all()
    return render(request, 'ADMIN/ADD_hostel.html',{'data':r})


def addhostel_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    facility=request.POST['textfield']
    description=request.POST['textfield1']
    ob = Hostel()
    ob.facility = facility
    ob.description = description
    ob.save()
    return HttpResponse('''<script>alert("Sccessfully Added");window.location='/myapp/adminhome/'</script>''')

def viewhostel(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob=Hostel.objects.all()
    return render(request,'ADMIN/View_hostel.html',{'data':ob})

def edhostel(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    a=Hostel.objects.get(id=id)
    return render(request,'ADMIN/EDIT_hostel.html',{'data':a})

def edhostel_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    facility=request.POST['textfield2']
    description=request.POST['textfield3']

    r=request.POST['id']
    ob=Hostel.objects.get(id=r)
    ob.facility=facility
    ob.description=description
    ob.save()
    return HttpResponse('''<script>alert("EDITED");window.location='/myapp/viewhostel/'</script>''')

def delhostel(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Hostel.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/viewhostel/'</script>''')

def adminhome(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    return render(request, 'ADMIN/admin_index.html')
#############################################################################################################3
def staffhome(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob=Staff.objects.get(LOGIN_id=request.session['lid'])
    request.session['photo']=ob.photo
    request.session['name']=ob.name
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_index.html',{'photo':n,'name':p})

def s_viewprofile(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob=Staff.objects.get(LOGIN_id=request.session['lid'])
    request.session['photo'] = ob.photo
    request.session['name'] = ob.name
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/viewprofile.html',{'data':ob,'photo':n,'name':p})

def changepass(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/CHANGE_PASS.html',{'photo':n,'name':p})


def changepass_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    ob=Login.objects.get(id=request.session['lid'])
    if ob.password==currentpassword:
        if newpassword==confirmpassword:
            ob.password=newpassword
            ob.save()
            return HttpResponse('''<script>alert('CHANGE PASSWORD');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("INVALID PASSWORD");window.location='/myapp/changepass/'</script>''')

    else:
        return HttpResponse('''<script>alert("INVALID PASSWORD");window.location='/myapp/changepass/'</script>''')


def s_addevent(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    # res=Staff.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_ADD_EVENT.html',{'photo':n,'name':p})
def s_addeventpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    a=request.POST['date']
    b=request.POST['type']
    c=request.POST['venue']
    d=request.POST['time']


    obc=Events()
    obc.date=a
    obc.type=b
    obc.venue=c
    obc.time=d
    obc.STAFF=Staff.objects.get(LOGIN_id=request.session['lid'])
    obc.save()
    return HttpResponse('''<script>alert("EVENT ADDED");window.location='/myapp/s_addevent/'</script>''')


def s_viewevent(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Events.objects.filter(STAFF__LOGIN_id=request.session['lid'])
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_VIEW_EVENT.html',{'data':res,'photo':n,'name':p})
def s_vieweventpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']

    res = Events.objects.filter(STAFF__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
    return render(request, 'STAFF/staff_VIEW_EVENT.html', {'data': res})

def s_viewdept(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Department.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_VIEW_DEPT.html',{'data':res,'photo':n,'name':p})
def s_viewdeptpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    departmentname=request.POST['textfield']
    res=Department.objects.filter(departmentname__icontains=departmentname)
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_VIEW_DEPT.html',{'data':res,'photo':n,'name':p})

def s_viewcou(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Course.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_VIEW_COU.html',{'data':res,'photo':n,'name':p})
def s_viewcoupost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    coursename=request.POST['textfield']
    res=Course.objects.filter(coursename__icontains=coursename)
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_COU.html', {'data': res, 'photo': n, 'name': p})

def s_viewallo(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Allocate.objects.filter(STAFF__LOGIN_id= request.session['lid'])
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_VIEW_ALLOCATE.html',{'data':res,'photo':n,'name':p})

def s_viewfacility(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Facility.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_FACILITY.html',{'data':res,'photo':n,'name':p})

def s_viewfacilitypost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    name=request.POST['text']
    res=Facility.objects.filter(name__icontains=name)
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_FACILITY.html', {'data': res,'photo':n,'name':p})

def s_addsfacility(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Facility.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_ADD_FACILITY.html',{'data':res,'photo':n,'name':p})

def s_viewschedule(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Schedule.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_SCHEDULE.html',{'data':res,'photo':n,'name':p})

def s_viewsupport(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Support.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_SUPPORT.html',{'data':res,'photo':n,'name':p})

def s_viewsupportpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    s=Support.objects.filter(category__contains=search)
    return render(request, 'STAFF/staff_VIEW_SUPPORT.html',{'data':s,})

def s_sendcmplnt(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Complaints.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_send_complaint.html',{'data':res,'photo':n,'name':p})
def s_sendcmplntpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    complaints=request.POST["textfield"]

    c=Complaints()
    c.complaint=complaints
    c.date=datetime.datetime.now()
    c.reply=""
    c.status="pending"
    c.STAFF=Staff.objects.get(LOGIN_id=request.session['lid'])
    c.save()
    return HttpResponse('''<script>alert("Complaint send ");window.location='/myapp/staffhome/'</script>''')
def s_viewrply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Complaints.objects.filter(STAFF__LOGIN_id= request.session['lid'])
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_reply.html',{'data':res,'photo':n,'name':p})

def s_viewrplypost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']

    res = Complaints.objects.filter(STAFF__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
    return render(request, 'STAFF/staff_VIEW_reply.html', {'data': res})


def s_sendfeed(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_send_feed.html',{'photo':n,'name':p})

def s_sendfeedpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    feedback= request.POST["textfield"]

    f=Feedback()
    f.feedback=feedback
    f.date=datetime.datetime.now()
    f.STAFF=Staff.objects.get(LOGIN_id=request.session['lid'])
    f.save()
    return HttpResponse('''<script>alert("Feedback send ");window.location='/myapp/staffhome/'</script>''')

def s_addgallery(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_addgallery.html',{'photo':n,'name':p})

def s_addgallerypost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    image=request.FILES['fileField']

    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, image)
    path = fs.url(date)
    ob=Gallary()
    ob.image=path
    ob.date=datetime.now().today()
    ob.STAFF=Staff.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("IMAGE ADDED");window.location='/myapp/staffhome/'</script>''')
def s_edgallery(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    n = request.session['photo']
    p = request.session['name']
    ob=Gallary.objects.get(id=id)
    return render(request, 'STAFF/staffed_EDITGALLERY.html',{'data':ob,'photo':n,'name':p})
def s_edgallerypost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    id=request.POST['id']
    ob = Gallary.objects.get(id=id)

    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        fs = FileSystemStorage()
        fs.save(date, image)
        path = fs.url(date)
        ob.image=path
        ob.save()

    ob.date=datetime.now().today()
    ob.STAFF=Staff.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("IMAGE EDIT");window.location='/myapp/s_viewgallery/'</script>''')

def s_dltgallery(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob=Gallary.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("IMAGE DELETED");window.location='/myapp/s_viewgallery/'</script>''')


def s_viewgallery(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Gallary.objects.filter(STAFF__LOGIN_id=request.session['lid'])
    n = request.session['photo']
    p = request.session['name']

    return render(request,'STAFF/staff_VIEW_GALLARY.html',{'data':res,'photo':n,'name':p})
def s_viewgallerypost(request):
   fromdate=request.POST['textfield']
   todate=request.POST['textfield2']
   # search=request.POST['button']
   res=Gallary.objects.filter(STAFF__LOGIN_id=request.session['lid'],date__range=[fromdate,todate])
   if request.session['lid'] == '':
       return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
   return render(request, 'STAFF/staff_VIEW_GALLARY.html', {'data': res})

def s_viewstudent(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Student.objects.filter(COURSE__DEPARTMENT= Staff.objects.get(LOGIN_id= request.session['lid']).DEPRTMENT)
    v=Course.objects.all()
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_STU.html', {'data': res,'data1':v,'photo':n,'name':p})
def s_viewstudentpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    v = Course.objects.all()
    s=request.POST['textfield']
    c=request.POST['select']
    res=Student.objects.filter(Q(admissionNo__icontains=s) & Q(COURSE_id=c))
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_VIEW_STU.html', {'data': res,'data1':v,'photo':n,'name':p})


def s_addfacility(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_ADD_FACILITY.html',{'photo':n,'name':p})

def s_addfacility_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    name = request.POST['select']
    image = request.FILES['fileField']

    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, image)
    path = fs.url(date)
    ob = Facility()
    ob.name = name
    ob.image = path
    ob.save()
    return HttpResponse('''<script>alert("FACILITY ADDED");window.location='/myapp/staffhome/'</script>''')

def s_edfacility(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    f=Facility.objects.get(id=id)
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_EDIT_FACILITY.html',{'data':f,'photo':n,'name':p})

def s_edfacilitypost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    name = request.POST['select']

    fa=request.POST['id']
    fac = Facility.objects.get(id=fa)
    fac.name = name

    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date,image )
        path = fs.url(date)
        fac.image=path
    fac.save()
    return HttpResponse('''<script>alert("EDIT FACILITY");window.location='/myapp/s_viewfacility/'</script>''')

def s_dlfacility(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Facility.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/staffhome/'</script>''')

def s_edevent(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Events.objects.get(id=id)
    n = request.session['photo']
    p = request.session['name']
    return render(request,'STAFF/staff_EDIT_EVENT.html',{'photo':n,'name':p,'data':res})
def s_edeventpost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    a=request.POST['date']
    b=request.POST['type']
    c=request.POST['venue']
    d=request.POST['time']

    ev=request.POST['id']
    ob=Events.objects.get(id=ev)
    ob.date=a
    ob.type=b
    ob.venue=c
    ob.time=d
    ob.STAFF = Staff.objects.get(LOGIN_id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("EVENT EDITED");window.location='/myapp/s_viewevent/'</script>''')


def s_delevent(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Events.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/s_viewevent/'</script>''')

def s_bus(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    res=Bus.objects.all()
    obs = Staff.objects.get(LOGIN_id=request.session['lid'])
    request.session['photo'] = obs.photo
    request.session['name'] = obs.name
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_ADD_BUS.html' ,{"data":res,'photo': n, 'name': p})

def s_buspost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')

    busno = request.POST['textfield']
    place = request.POST['textfield1']
    ob = Bus()
    ob.busno = busno
    ob.place = place
    ob.save()
    return HttpResponse('''<script>alert("INSERTED");window.location='/myapp/viewbus/'</script>''')

def edbus(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    b=Bus.objects.get(id=id)
    obs = Staff.objects.get(LOGIN_id=request.session['lid'])
    request.session['photo'] = obs.photo
    request.session['name'] = obs.name
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/staff_EDBUS.html' ,{"data":b,'photo': n, 'name': p})

def edbus_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    busno=request.POST['textfield']
    place=request.POST['textfield2']
    aid=request.POST['id']
    ab=Bus.objects.get(id=aid)
    ab.busno=busno
    ab.place=place
    ab.save()
    return HttpResponse('''<script>alert("EDIT BUS DETAILS");window.location='/myapp/viewbus/'</script>''')

def delbus(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    Bus.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED");window.location='/myapp/staffhome/'</script>''')

def viewbus(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    ob=Bus.objects.all()
    obs = Staff.objects.get(LOGIN_id=request.session['lid'])
    request.session['photo'] = obs.photo
    request.session['name'] = obs.name
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/VIEW_BUS.html' ,{"data":ob,'photo': n, 'name': p})

def viewbus_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    ob=Bus.objects.filter(place__contains=search)
    obs = Staff.objects.get(LOGIN_id=request.session['lid'])
    request.session['photo'] = obs.photo
    request.session['name'] = obs.name
    n = request.session['photo']
    p = request.session['name']
    return render(request, 'STAFF/VIEW_BUS.html' ,{"data":ob,'photo': n, 'name': p})



###################################################################################################################
def phome(request):
    return render(request,'PUBLIC/public_index.html')


def p_viewdept(request):
    p=Department.objects.all()
    return render(request,'PUBLIC/P_VIEW_DEPT.html',{'data':p})

def p_viewstaff(request):
    ps=Staff.objects.all()
    p=Department.objects.all()
    return render(request,'PUBLIC/P_VIEW_STAFF.html',{'data':ps,'data1':p})

def p_viewstaffpost(request):
    departmentname=request.POST['select']
    ps=Staff.objects.filter(DEPRTMENT_id=departmentname)
    p=Department.objects.all()
    return render(request,'PUBLIC/P_VIEW_STAFF.html',{'data':ps,'data1':p})

def p_viewgallery(request):
    g=Gallary.objects.all()
    return render(request,'PUBLIC/P_VIEW_GALLARY.html',{'data':g})

def p_viewgallerypost(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    g=Gallary.objects.filter(date__range=[fromdate,todate])
    return render(request, 'PUBLIC/P_VIEW_GALLARY.html', {'data': g})

def p_viewfacility(request):
    f=Facility.objects.all()
    return render(request, 'PUBLIC/P_VIEW_FACILITY.html', {'data':f})

def p_viewfacilitypost(request):
    s=request.POST['text']
    f=Facility.objects.filter(name__icontains=s)
    return render(request, 'PUBLIC/P_VIEW_FACILITY.html',{'data': f})

def p_viewschedule(request):
    s=Schedule.objects.all()
    return render(request, 'PUBLIC/P_VIEW_SCHEDULE.html', {'data':s})

def p_viewcource(request):
    c=Course.objects.all()
    return render(request, 'PUBLIC/P_VIEW_COU.html', {'data':c})

def p_viewcourcepost(request):
    s=request.POST['textfield']
    c=Course.objects.filter(coursename__icontains=s)
    return render(request, 'PUBLIC/P_VIEW_COU.html', {'data':c})

def p_viewsub(request):
    s=Subject.objects.all()
    c=Course.objects.all()
    return render(request, 'PUBLIC/P_VIEW_SUB .html', {'data':s,'data1':c})

def p_viewsubpost(request):
    sub=request.POST['select']
    s=Subject.objects.filter(COURSE_id=sub)
    c=Course.objects.all()
    return render(request, 'PUBLIC/P_VIEW_SUB .html', {'data':s,'data1':c})

def p_viewsupport(request):
    sp=Support.objects.all()
    return render(request, 'PUBLIC/P_VIEW_SUPPORT.html', {'data':sp})

def p_viewsupportpost(request):
    s=request.POST['textfield']
    sp=Support.objects.filter(category__icontains=s)
    return render(request, 'PUBLIC/P_VIEW_SUPPORT.html', {'data':sp})

def p_viewevent(request):
    e=Events.objects.all()
    return render(request, 'PUBLIC/P_VIEW_EVENT.html', {'data':e})

def p_vieweventpost(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    e=Events.objects.filter(date__range=[fromdate,todate])
    return render(request, 'PUBLIC/P_VIEW_EVENT.html', {'data':e})

def p_sendfeedback(request):
    return render(request, 'PUBLIC/P_send_feed.html')

def p_sendfeedbackpost(request):
    feedback=request.POST['textfield']
    email=request.POST['textfield2']

    f=Feedbackpublic()
    f.feedback=feedback
    f.date=datetime.datetime.now().today()
    f.Email=email
    f.save()
    return HttpResponse('''<script>alert("FEEDBACK SEND");window.location='/myapp/p_sendfeedback/'</script>''')

def p_viewbus(request):
    ob=Bus.objects.all()
    return render(request, 'PUBLIC/p_VIEW_BUS.html' ,{'data':ob})

def p_viewbus_post(request):
    search=request.POST['textfield']
    ob=Bus.objects.filter(place__contains=search)
    return render(request, 'PUBLIC/p_VIEW_BUS.html',{'data':ob})

def p_vfeedback(request):
    ob = Feedbackpublic.objects.all()
    return render(request,'PUBLIC/p_viewFEEDBACK.html',{'data':ob})

def p_viewhostel(request):
    ob=Hostel.objects.all()
    return render(request,'PUBLIC/View_hostel.html',{'data':ob})


# def p_vfeedback_post(request):
#     if request.session['lid']=='':
#         return HttpResponse('''<script>alert("Please Login");window.location='/myapp/login/'</script>''')
#     return HttpResponse('''<script>alert("OK");window.location='/myapp/phome/'</script>''')





from sentence_transformers import SentenceTransformer, util
import numpy as np
import json

# def chat(request,msg):
#     print(msg)
#     print(len(msg),"fffffffffffffffffffffffffffff")
#
#
#     if len(msg)<10:
#         return JsonResponse({'status':'no'})
#
#         # return HttpResponse('''<script>alert("Enter more information");window.location='/myapp/chat1/'</script>''')
#     else:
#
#     # p=json.loads(request.body).get('msg')
#
#     # Initialize the Sentence-BERT model
#         model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
#
#         # Define the question-answer pairs for the chatbot
#         qa_pairs = [
#             # General College Information
#             ("What is the history of the college?",
#              """Noble Women’s College, Manjeri, established in 2011 by Islahi Educational Society, provides quality, moral-based education to uplift the Muslim community and society. Affiliated with the University of Calicut, it offers UG/PG programs with add-on courses for skill and personality development under a self-financing stream."""),
#
#
#             ("What is the college's vision and mission ?",
#               """
#                              VISION<br>
#             Empowerment of women with excellent and value-added education for the total upliftment of the young generation and society.<br>
#
#                             MISSION<br>
#
#             Provide modern and holistic education in diverse discip
# ines using modern technology and teaching methods in a safe and serene environment."""),
#                     ("What is the college's vision?",
#                      """
#                                     VISION<br>
#             Empowerment of women with excellent and value-added education for the total upliftment of the young generation and society."""),
#
#             ("What is the college's mission?",
#              """MISSION<br> Provide modern and holistic education in diverse disciplines using modern technology and teaching methods in a safe and serene environment."""),
#             ("Who is the current pricipal of the college?",
#              "Dr. U. Saidalvi (Principal, NWC)"),
#             ("Who are the formal principals of the college?",
#              """Prof. P.N. Abdurahiman  (2011 - 2016)<br>
#                 Prof.K Kunhimuhammed  (2016 - 2018)<br>
#                 Dr. P.K. Abdussalam 	(2018 - 2019)<br>
#                 Dr. (Lt.Cdr.)(Rtd.) C.K. Abdul Rabbi Nistar  (2020 - 2022)<br>
#                 Dr. U. Saidalvi  (Present)"""),
#             ("What is the admission procedure for this college?",
#              """UG ADMISSION<br><br>
#
#             Admission as per university schedule under single window system. Candidates need to register online through University online facility and should obtain CAP ID. For Merit seats a candidate shall apply online to University under Single Window system and admission will be as per allotment from University. For management seats the candidate shall apply to the course desired in the prescribed application form which can be had from the college office by payment of Rs. 200/-. Online registration for management seats can be done at www.noblewomenscollege.edu.in. The allotted/ selected candidate will be called for an interview and shall produce/bring the following during admission:<br>
#
#             1. CAP registration form<br>
#             2. Payment receipt of Mandatory Fee<br>
#             3. All Original certificate ( SSLC, +2)<br>
#             4. TC and Conduct Certificate from the institution last attended<br>
#             5. 4 Copies of passport size colour photograph<br><br>
#
#             PG ADMISSION<br>
#             <br>
#             Admission as per university schedule under single window system. Candidates need to register online through University online facility and should obtain CAP ID. For Merit seats a candidate shall apply online to University under Single Window system and admission will be as per allotment from University. For management seats the candidate shall apply to the course desired in the prescribed application form which can be had from the college office by payment of Rs. 200/-. Online registration for management seats can be done at www.noblewomenscollege.edu.in. The allotted/ selected candidate will be called for an interview and shall produce/bring the following during admission:<br>
#
#             1. CAP registration form<br>
#             2. Payment receipt of Mandatory Fee<br>
#             3. All Original certificate ( SSLC, +2)<br>
#             4. TC and Conduct Certificate from the institution last attended<br>
#             5. 4 Copies of passport size colour photograph.
#             ONLINE REGISTRATION<br><br>
#             1. Refer the instructions available in the college website.<br>
#             2. Do you have a valid email id? The credential accessing to Online Registration Dashboard will be forwarded to your email. If does not have, create one.<br>
#             3. Note down your application number, which you receive through Email (Check Spam folder also). Please fill up the Form carefully (the Application will be rejected, if your entries are not correct).<br>
#             4. You can edit your application later by using your username and password. Fill all the mandatory data fields and click "Submit" button.<br>
#             """),
#             ("What is the admission procedure for UG",
#              """UG ADMISSION<br>
#
#              Admission as per university schedule under single window system. Candidates need to register online through University online facility and should obtain CAP ID. For Merit seats a candidate shall apply online to University under Single Window system and admission will be as per allotment from University. For management seats the candidate shall apply to the course desired in the prescribed application form which can be had from the college office by payment of Rs. 200/-. Online registration for management seats can be done at www.noblewomenscollege.edu.in. The allotted/ selected candidate will be called for an interview and shall produce/bring the following during admission:<br>
#
#              1. CAP registration form<br>
#              2. Payment receipt of Mandatory Fee<br>
#              3. All Original certificate ( SSLC, +2)<br>
#              4. TC and Conduct Certificate from the institution last attended<br>
#              5. 4 Copies of passport size colour photograph. """),
#
#             # Faculty and Staff Information
#             ("How can I contact my professor?",
#              "You can contact your professors via email, or during their scheduled office hours. Office hours and contact information can be found on the faculty directory page on the website."),
#
#             ("How do I become a professor at the college?",
#              "To become a professor at the college, you typically need a Ph.D. in your field, a record of academic research, and teaching experience. Open faculty positions are posted on the college's career page."),
#
#             ("Is there a faculty development program?",
#              "Yes, the college offers continuous professional development programs for faculty members to enhance their teaching, research, and leadership skills."),
#
#             ("What staff services are available on campus?",
#              "The college provides a range of staff services including HR support, counseling, wellness programs, and professional development workshops."),
#
#             # Academic Programs and Departments
#             ("What departments are available at the college?",
#              "The college has a wide range of departments including Arts, Science, Engineering, Business Administration, Computer Science, Social Sciences, and Health Sciences."),
#
#             ("What programs are available in Computer Science?",
#              "The Computer Science department offers undergraduate and graduate programs such as B.Sc. in Computer Science, M.Sc. in Computer Science, and specialized courses like Artificial Intelligence, Data Science, and Cybersecurity."),
#
#             ("What courses are offered in Business Administration?",
#              "The Business Administration department offers courses in Finance, Marketing, Management, Entrepreneurship, and Business Ethics. You can check the course catalog for the full list."),
#
#             ("What is the admissions process for graduate programs?",
#              "To apply for graduate programs, you need to complete an online application form, submit your academic transcripts, provide letters of recommendation, and in some cases, take an entrance exam or interview."),
#
#             ("Are there any dual-degree programs?",
#              "Yes, the college offers dual-degree programs in fields such as Engineering and Business Administration, allowing students to earn two degrees in a shorter time frame."),
#
#             ("How do I apply for honors programs?",
#              "To apply for an honors program, you must meet the GPA requirements and submit an application during the registration period. Specific details can be found on the college website."),
#
#             # Campus and Student Life
#             ("What is the campus size?",
#              "The college campus spans 100 acres and features state-of-the-art classrooms, research labs, recreational facilities, and green spaces for students and faculty."),
#
#             ("Are there on-campus housing options?",
#              "Yes, there are multiple dormitories available for both undergraduate and graduate students. You can apply for campus housing through the student portal."),
#             ("What is there to do for fun on campus?",
#              "The campus offers various recreational activities including sports, student clubs, a music room, drama workshops, and several student-run events throughout the year."),
#
#             ("Is there a student union?",
#              "Yes, the student union organizes campus events, social gatherings, and provides support for student rights and academic needs."),
#
#             ("How do I get involved in clubs and student organizations?",
#              "You can sign up for clubs and student organizations through the student portal. The campus has a variety of clubs ranging from academic to recreational and social interests."),
#
#             ("Can I participate in sports?",
#              "Yes, the college has sports program where students can participate in sports like basketball, soccer, and volleyball. Registration details are available through the campus sports office."),
#
#             ("Is there a student newspaper?",
#              "Yes, the college has a student-run newspaper that covers campus news, events, and academic achievements. You can contribute as a writer, editor, or photographer."),
#
#             # Sports and Recreation
#             ("What sports are offered on campus?",
#              "The college offers various sports including soccer, basketball, volleyball, tennis, swimming, and athletics. The sports complex has dedicated facilities for both team and individual sports."),
#
#             ("Are there varsity teams?",
#              "Yes, the college has competitive varsity teams in football, basketball, track and field, and other sports. Tryouts are held at the beginning of each semester."),
#
#             ("How can I join a sports team?",
#              "To join a sports team, you need to attend tryouts, which are held by the respective department at the start of each semester. Information is posted on the sports office bulletin board."),
#
#             ("Is there a swimming pool on campus?",
#              "Yes, the college has an Olympic-sized swimming pool located in the sports complex. Students can access it during designated hours with their student ID."),
#
#             ("What fitness classes are offered on campus?",
#              "The college offers fitness classes including yoga, pilates, Zumba, and strength training. Classes are held in the gym and are free for students with a valid ID."),
#
#             # Events and Festivals
#             ("What events are held on campus?",
#              "The college hosts a variety of events including 'College Fest', sports competitions, guest lectures, cultural festivals, career fairs, and workshops throughout the year."),
#
#             ("What is the annual College Fest?",
#              "The College Fest is the college's annual celebration that features music, dance performances, workshops, and guest speakers. It's a major highlight of the academic year."),
#
#             ("How can I participate in campus events?",
#              "You can participate in campus events by registering on the event page or contacting the event organizers. Many events are open to all students."),
#
#             ("Are there any guest speakers visiting soon?",
#              "Yes, the college regularly hosts guest speakers from various fields including technology, business, politics, and the arts. Check the campus events page for upcoming talks."),
#
#             # Campus Facilities
#             ("Are there research labs on campus?",
#              "Yes, the college has dedicated research labs in fields like Chemistry, Computer Science, Engineering, and Medical Sciences. These labs are available for students involved in research projects."),
#
#             ("What kind of dining options are available on campus?",
#              "The campus has multiple dining facilities including the main cafeteria, a coffee shop, and a food court. There are also vending machines and snack bars located around the campus."),
#
#             ("Are there any quiet study areas?",
#              "Yes, the library and several designated study rooms across campus provide quiet environments for studying. The study areas can be booked online through the student portal."),
#
#             ("Is there a student lounge?",
#              "Yes, the student lounge is located near the student center. It is a relaxed space where students can socialize, study, or relax between classes."),
#
#             ("How do I access campus Wi-Fi?",
#              "Campus Wi-Fi is available to all students. You can connect using your student credentials. If you encounter any issues, the IT support office can assist."),
#
#             # Financial Aid and Scholarships
#             ("What types of financial aid are available?",
#              "The college offers financial aid through scholarships, grants, and student loans. You can apply for aid through the Financial Aid Office on the website."),
#
#
#             ("How do I apply for a scholarship?",
#              "To apply for scholarships, visit the Financial Aid section of the website. Applications are typically due in March and April."),
#
#             ("Are there work-study programs?",
#              "Yes, the college offers work-study programs that allow students to work part-time on campus while earning academic credit. Jobs are listed on the student portal."),
#
#             ("What are the tuition fees?",
#              "Tuition fees vary depending on the program you choose. You can check the fee schedule on the admissions page or contact the bursar’s office for detailed information."),
#
#             ("How can I apply for a student loan?",
#              "You can apply for a student loan through the Financial Aid Office. The application process includes submitting financial documents and meeting eligibility criteria."),
#
#             # General Questions
#             ("Thank you for the information!", "You're welcome! If you have any more questions, feel free to ask!"),
#             ("Goodbye!", "Goodbye! Have a wonderful day!"),
#
#             ("Thank you"),
#             ("Goodbye!", "Goodbye! Have a wonderful day!"),
#
#             ("Hi","Hi"),
#
#             ("Hello","Hello"),
#
#         ]
#
#         # Prepare the questions and answers
#         questions = [qa[0] for qa in qa_pairs]
#         answers = [qa[1] for qa in qa_pairs]
#
#         # Encode the questions using Sentence-BERT model
#         question_embeddings = model.encode(questions, convert_to_tensor=True)
#
#         # Function to handle chatbot interaction
#         def chatbot(query):
#             # Encode the user's question
#             query_embedding = model.encode(query, convert_to_tensor=True)
#
#             # Compute cosine similarities between the query and all stored questions
#             similarities = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]
#
#             # Find the index of the most similar question
#             best_match_idx = np.argmax(similarities)
#             best_match_similarity = similarities[best_match_idx]
#
#
#             print(best_match_similarity,"HIIII")
#
#             # If the similarity is high enough, return the corresponding answer
#             if best_match_similarity > 0.7:  # threshold to ensure a good match
#
#                 print(answers[best_match_idx])
#                 return answers[best_match_idx]
#             else:
#
#                 return "I'm sorry, I don't have that information. Please visit the website or your content lenght is too small"
#
#         from autocorrect import Speller
#
#         spell = Speller(lang='en')
#         response = chatbot(spell(msg))
#
#         print(response)
#         return  JsonResponse({'status':'ok','message':response})



from django.http import JsonResponse
from sentence_transformers import SentenceTransformer, util
import numpy as np
from autocorrect import Speller

# def chat(request, msg):
#     print(msg)
#     print(len(msg), "fffffffffffffffffffffffffffff")
#
#     # Check for message length
#     if len(msg) < 5:
#         return JsonResponse({'status': 'no', 'message': 'Please provide more information.'})
#
#     else:
#         # Initialize the Sentence-BERT model
#         model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
#
#
#
#
#
#
#
#         # Define the question-answer pairs for the chatbot
#         qa_pairs = [
#                     ("What is the history of the college?",
#                     """Noble Women’s College, Manjeri, established in 2011 by Islahi Educational Society, provides quality, moral-based education to uplift the Muslim community and society. Affiliated with the University of Calicut, it offers UG/PG programs with add-on courses for skill and personality development under a self-financing stream."""),
#
#                     # General College Information
#                     ("What is the history of the college?",
#                      """Noble Women’s College, Manjeri, established in 2011 by Islahi Educational Society, provides quality, moral-based education to uplift the Muslim community and society. Affiliated with the University of Calicut, it offers UG/PG programs with add-on courses for skill and personality development under a self-financing stream."""),
#
#
#                     ("What is the college's vision and mission ?",
#                       """
#                                      VISION<br>
#                     Empowerment of women with excellent and value-added education for the total upliftment of the young generation and society.<br>
#
#                                     MISSION<br>
#
#                     Provide modern and holistic education in diverse disciplines using modern technology and teaching methods in a safe and serene environment."""),
#                             ("What is the college's vision?",
#                              """
#                                             VISION<br>
#                     Empowerment of women with excellent and value-added education for the total upliftment of the young generation and society."""),
#
#                     ("What is the college's mission?",
#                      """MISSION<br> Provide modern and holistic education in diverse disciplines using modern technology and teaching methods in a safe and serene environment."""),
#                     ("Who is the current pricipal of the college?",
#                      "Dr. U. Saidalvi (Principal, NWC)"),
#                     ("Who are the formal principals of the college?",
#                      """Prof. P.N. Abdurahiman  (2011 - 2016)<br>
#                         Prof.K Kunhimuhammed  (2016 - 2018)<br>
#                         Dr. P.K. Abdussalam 	(2018 - 2019)<br>
#                         Dr. (Lt.Cdr.)(Rtd.) C.K. Abdul Rabbi Nistar  (2020 - 2022)<br>
#                         Dr. U. Saidalvi  (Present)"""),
#                     ("What is the admission procedure for this college?",
#                      """UG ADMISSION<br><br>
#
#                     Admission as per university schedule under single window system. Candidates need to register online through University online facility and should obtain CAP ID. For Merit seats a candidate shall apply online to University under Single Window system and admission will be as per allotment from University. For management seats the candidate shall apply to the course desired in the prescribed application form which can be had from the college office by payment of Rs. 200/-. Online registration for management seats can be done at www.noblewomenscollege.edu.in. The allotted/ selected candidate will be called for an interview and shall produce/bring the following during admission:<br>
#
#                     1. CAP registration form<br>
#                     2. Payment receipt of Mandatory Fee<br>
#                     3. All Original certificate ( SSLC, +2)<br>
#                     4. TC and Conduct Certificate from the institution last attended<br>
#                     5. 4 Copies of passport size colour photograph<br><br>
#
#                     PG ADMISSION<br>
#                     <br>
#                     Admission as per university schedule under single window system. Candidates need to register online through University online facility and should obtain CAP ID. For Merit seats a candidate shall apply online to University under Single Window system and admission will be as per allotment from University. For management seats the candidate shall apply to the course desired in the prescribed application form which can be had from the college office by payment of Rs. 200/-. Online registration for management seats can be done at www.noblewomenscollege.edu.in. The allotted/ selected candidate will be called for an interview and shall produce/bring the following during admission:<br>
#
#                     1. CAP registration form<br>
#                     2. Payment receipt of Mandatory Fee<br>
#                     3. All Original certificate ( SSLC, +2)<br>
#                     4. TC and Conduct Certificate from the institution last attended<br>
#                     5. 4 Copies of passport size colour photograph.
#                     ONLINE REGISTRATION<br><br>
#                     1. Refer the instructions available in the college website.<br>
#                     2. Do you have a valid email id? The credential accessing to Online Registration Dashboard will be forwarded to your email. If does not have, create one.<br>
#                     3. Note down your application number, which you receive through Email (Check Spam folder also). Please fill up the Form carefully (the Application will be rejected, if your entries are not correct).<br>
#                     4. You can edit your application later by using your username and password. Fill all the mandatory data fields and click "Submit" button.<br>
#                     """),
#                     ("What is the admission procedure for UG",
#                      """UG ADMISSION<br>
#
#                      Admission as per university schedule under single window system. Candidates need to register online through University online facility and should obtain CAP ID. For Merit seats a candidate shall apply online to University under Single Window system and admission will be as per allotment from University. For management seats the candidate shall apply to the course desired in the prescribed application form which can be had from the college office by payment of Rs. 200/-. Online registration for management seats can be done at www.noblewomenscollege.edu.in. The allotted/ selected candidate will be called for an interview and shall produce/bring the following during admission:<br>
#
#                      1. CAP registration form<br>
#                      2. Payment receipt of Mandatory Fee<br>
#                      3. All Original certificate ( SSLC, +2)<br>
#                      4. TC and Conduct Certificate from the institution last attended<br>
#                      5. 4 Copies of passport size colour photograph. """),
#
#                     # Faculty and Staff Information
#                     ("How can I contact my professor?",
#                      "You can contact your professors via email, or during their scheduled office hours. Office hours and contact information can be found on the faculty directory page on the website."),
#
#                     ("How do I become a professor at the college?",
#                      "To become a professor at the college, you typically need a Ph.D. in your field, a record of academic research, and teaching experience. Open faculty positions are posted on the college's career page."),
#
#                     ("Is there a faculty development program?",
#                      "Yes, the college offers continuous professional development programs for faculty members to enhance their teaching, research, and leadership skills."),
#
#                     ("What staff services are available on campus?",
#                      "The college provides a range of staff services including HR support, counseling, wellness programs, and professional development workshops."),
#
#                     # Academic Programs and Departments
#                     # ("What departments are available at the college?",
#                     #  "The college has a wide range of departments including Arts, Science, Engineering, Business Administration, Computer Science, Social Sciences, and Health Sciences."),
#
#                     # ("What programs are available in Computer Science?",
#                     #  "The Computer Science department offers undergraduate and graduate programs such as B.Sc. in Computer Science, M.Sc. in Computer Science, and specialized courses like Artificial Intelligence, Data Science, and Cybersecurity."),
#                     #
#                     # ("What courses are offered in Business Administration?",
#                     #  "The Business Administration department offers courses in Finance, Marketing, Management, Entrepreneurship, and Business Ethics. You can check the course catalog for the full list."),
#
#                     ("What is the admissions process for graduate programs?",
#                      "To apply for graduate programs, you need to complete an online application form, submit your academic transcripts, provide letters of recommendation, and in some cases, take an entrance exam or interview."),
#
#                     ("Are there any dual-degree programs?",
#                      "Yes, the college offers dual-degree programs in fields such as Engineering and Business Administration, allowing students to earn two degrees in a shorter time frame."),
#
#                     ("How do I apply for honors programs?",
#                      "To apply for an honors program, you must meet the GPA requirements and submit an application during the registration period. Specific details can be found on the college website."),
#
#                     # Campus and Student Life
#                     ("What is the campus size?",
#                      "The college campus spans 100 acres and features state-of-the-art classrooms, research labs, recreational facilities, and green spaces for students and faculty."),
#
#                     ("Are there on-campus housing options?",
#                      "Yes, there are multiple dormitories available for both undergraduate and graduate students. You can apply for campus housing through the student portal."),
#                     ("What is there to do for fun on campus?",
#                      "The campus offers various recreational activities including sports, student clubs, a music room, drama workshops, and several student-run events throughout the year."),
#
#                     ("Is there a student union?",
#                      "Yes, the student union organizes campus events, social gatherings, and provides support for student rights and academic needs."),
#
#                     ("How do I get involved in clubs and student organizations?",
#                      "You can sign up for clubs and student organizations through the student portal. The campus has a variety of clubs ranging from academic to recreational and social interests."),
#
#                     ("Can I participate in sports?",
#                      "Yes, the college has sports program where students can participate in sports like basketball, soccer, and volleyball. Registration details are available through the campus sports office."),
#
#                     ("Is there a student newspaper?",
#                      "Yes, the college has a student-run newspaper that covers campus news, events, and academic achievements. You can contribute as a writer, editor, or photographer."),
#
#                     # Sports and Recreation
#                     ("What sports are offered on campus?",
#                      "The college offers various sports including soccer, basketball, volleyball, tennis, swimming, and athletics. The sports complex has dedicated facilities for both team and individual sports."),
#
#                     ("Are there varsity teams?",
#                      "Yes, the college has competitive varsity teams in football, basketball, track and field, and other sports. Tryouts are held at the beginning of each semester."),
#
#                     ("How can I join a sports team?",
#                      "To join a sports team, you need to attend tryouts, which are held by the respective department at the start of each semester. Information is posted on the sports office bulletin board."),
#
#                     ("Is there a swimming pool on campus?",
#                      "Yes, the college has an Olympic-sized swimming pool located in the sports complex. Students can access it during designated hours with their student ID."),
#
#                     ("What fitness classes are offered on campus?",
#                      "The college offers fitness classes including yoga, pilates, Zumba, and strength training. Classes are held in the gym and are free for students with a valid ID."),
#
#                     # Events and Festivals
#                     ("What events are held on campus?",
#                      "The college hosts a variety of events including 'College Fest', sports competitions, guest lectures, cultural festivals, career fairs, and workshops throughout the year."),
#
#                     ("What is the annual College Fest?",
#                      "The College Fest is the college's annual celebration that features music, dance performances, workshops, and guest speakers. It's a major highlight of the academic year."),
#
#                     ("How can I participate in campus events?",
#                      "You can participate in campus events by registering on the event page or contacting the event organizers. Many events are open to all students."),
#
#                     ("Are there any guest speakers visiting soon?",
#                      "Yes, the college regularly hosts guest speakers from various fields including technology, business, politics, and the arts. Check the campus events page for upcoming talks."),
#
#                     # Campus Facilities
#                     ("Are there research labs on campus?",
#                      "Yes, the college has dedicated research labs in fields like Chemistry, Computer Science, Engineering, and Medical Sciences. These labs are available for students involved in research projects."),
#
#                     ("What kind of dining options are available on campus?",
#                      "The campus has multiple dining facilities including the main cafeteria, a coffee shop, and a food court. There are also vending machines and snack bars located around the campus."),
#
#                     ("Are there any quiet study areas?",
#                      "Yes, the library and several designated study rooms across campus provide quiet environments for studying. The study areas can be booked online through the student portal."),
#
#                     ("Is there a student lounge?",
#                      "Yes, the student lounge is located near the student center. It is a relaxed space where students can socialize, study, or relax between classes."),
#
#                     ("How do I access campus Wi-Fi?",
#                      "Campus Wi-Fi is available to all students. You can connect using your student credentials. If you encounter any issues, the IT support office can assist."),
#
#                     # Financial Aid and Scholarships
#                     ("What types of financial aid are available?",
#                      "The college offers financial aid through scholarships, grants, and student loans. You can apply for aid through the Financial Aid Office on the website."),
#
#
#                     ("How do I apply for a scholarship?",
#                      "To apply for scholarships, visit the Financial Aid section of the website. Applications are typically due in March and April."),
#
#                     ("Are there work-study programs?",
#                      "Yes, the college offers work-study programs that allow students to work part-time on campus while earning academic credit. Jobs are listed on the student portal."),
#
#                     ("What are the tuition fees?",
#                      "Tuition fees vary depending on the program you choose. You can check the fee schedule on the admissions page or contact the bursar’s office for detailed information."),
#
#                     ("How can I apply for a student loan?",
#                      "You can apply for a student loan through the Financial Aid Office. The application process includes submitting financial documents and meeting eligibility criteria."),
#
#                     # General Questions
#                     ("Thank you for the information!", "You're welcome! If you have any more questions, feel free to ask!"),
#                     ("Goodbye!", "Goodbye! Have a wonderful day!"),
#
#                     ("Thank you"),
#                     ("Goodbye!", "Goodbye! Have a wonderful day!"),
#
#                     ("Hi","Hi"),
#
#                     ("Hello","Hello"),
#
#
#
#
#
#
#         ]
#
#         s = Support.objects.all()
#
#         for i in s:
#
#             qa_pairs.append(
#
#                 (i.category, i.discription)
#             )
#
#         e = Schedule.objects.all()
#
#         for i in e:
#             qa_pairs.append(
#                 (i.programname, i.programname+ " happening on "+i.date.strftime("%Y-%m-%d")+" time  "+ i.time +" at "+i.Venue)
#
#             )
#         ss=""
#         for i in Department.objects.all():
#             ss= ss + i.departmentname +" ,"
#
#         ss=ss[0:len(ss)-1]
#
#         qa_pairs.append(("Department are", ss))
#
#
#
#         for i in Department.objects.all():
#
#             m= Course.objects.filter(DEPARTMENT= i)
#             k=""
#             for j in m:
#                 k= k+ j.coursename +", "
#
#             qa_pairs.append(
#                 (
#                     'Courses offered by department '+ i.departmentname, "Offered courses are " +k
#                 )
#             )
#
#
#
#         for i in Course.objects.all():
#             m = ""
#
#             for j in Subject.objects.filter(COURSE=i):
#
#                 m= m+ j.subjectname +","
#
#             print(m)
#             if len(m)>0:
#                 m=m[:len(m)-1]
#
#                 qa_pairs.append(
#                     (
#                         i.coursename + " offering subjects are", m
#                     )
#                 )
#
#
#
#         s=Department.objects.all()
#
#         for i in s:
#             m = ""
#             for j in Staff.objects.filter(DEPRTMENT=i):
#                 m = m + j.name + ","
#             print(m)
#             if len(m) > 0:
#                 m = m[:len(m) - 1]
#
#                 qa_pairs.append(
#                     (
#                         "Staffs of "+i.departmentname, "Main staffs are  "+m
#                     )
#                 )
#
#
#         s=Staff.objects.all()
#         for k in s:
#
#             qa_pairs.append(
#                 (
#                     "details of "+k.name, "<img src='"+k.photo+"' width='100px' height='100px'/> <br><b> Phone number :"+ k.phone +"</b> <br><b> Email :"+k.email
#                 )
#             )
#
#
#
#
#
#
#             # Prepare the questions and answers
#         questions = [qa[0] for qa in qa_pairs]
#         answers = [qa[1] for qa in qa_pairs]
#         print(qa_pairs, "hello")
#
#         # Encode the questions using Sentence-BERT model
#         question_embeddings = model.encode(questions, convert_to_tensor=True)
#
#         # Function to handle chatbot interaction
#         def chatbot(query):
#             # Encode the user's question
#             query_embedding = model.encode(query, convert_to_tensor=True)
#
#             # Compute cosine similarities between the query and all stored questions
#             similarities = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]
#
#             # Find the index of the most similar question
#             best_match_idx = np.argmax(similarities)
#             best_match_similarity = similarities[best_match_idx]
#
#             print(best_match_similarity, "HIIII")
#
#             # If the similarity is high enough, return the corresponding answer
#             if best_match_similarity > 0.4:  # threshold to ensure a good match
#                 print("Answer found:", answers[best_match_idx])
#                 return answers[best_match_idx]
#             else:
#                 return "I'm sorry, I don't have that information. Please visit the website or your content length is too small."
#
#         # Initialize the autocorrect spell checker
#         # spell = Speller(lang='en')
#         # corrected_msg = spell(msg)
#         corrected_msg=msg
#         print("Corrected message:", corrected_msg)
#
#         # Get the chatbot's response
#         response = chatbot(corrected_msg)
#         print("Response:", response)
#
#         return JsonResponse({'status': 'ok', 'message': response})


from django.http import JsonResponse
from sentence_transformers import SentenceTransformer, util
import numpy as np
from .models import Support, Schedule, Department, Course, Subject, Staff

def chat(request, msg):
    print(msg)
    print(len(msg), "fffffffffffffffffffffffffffff")

    from autocorrect import Speller

    spell = Speller(lang='en')
    msg =spell(msg)





    # Check for message length
    if len(msg) == 0:
        return JsonResponse({'status': 'no', 'message': 'Please provide more information.'})

    else:
        # Initialize the Sentence-BERT model
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

        # Define the question-answer pairs for the chatbot
        qa_pairs = [
            # College general information
            ("What is the history of the college?",
             """Noble Women’s College, Manjeri, established in 2011 by Islahi Educational Society, provides quality, moral-based education to uplift the Muslim community and society. Affiliated with the University of Calicut, it offers UG/PG programs with add-on courses for skill and personality development under a self-financing stream."""),


("Hi","Hi"),
("bye","bye. thanks"),


            ("What is the college's vision and mission?",
             """VISION<br> Empowerment of women with excellent and value-added education for the total upliftment of the young generation and society.<br> MISSION<br> Provide modern and holistic education in diverse disciplines using modern technology and teaching methods in a safe and serene environment."""),
            ("What is the college's vision?",
             """VISION<br> Empowerment of women with excellent and value-added education for the total upliftment of the young generation and society"""),
            ("What is the college's mission?",
             """ MISSION<br> Provide modern and holistic education in diverse disciplines using modern technology and teaching methods in a safe and serene environment."""),
            ("Who is the current principal of the college?",
             "Dr. U. Saidalvi (Principal, NWC)"),

            ("Who are the formal principals of the college?",
             """Prof. P.N. Abdurahiman  (2011 - 2016)<br>
                Prof.K Kunhimuhammed  (2016 - 2018)<br>
                Dr. P.K. Abdussalam 	(2018 - 2019)<br>
                Dr. (Lt.Cdr.)(Rtd.) C.K. Abdul Rabbi Nistar  (2020 - 2022)<br>
                Dr. U. Saidalvi  (Present)"""),

            ("What is the admission procedure for this college?",
             """UG ADMISSION<br> Admission as per university schedule under single window system..."""),

            ("How can I contact my professor?",
             "You can contact your professors via email, or during their scheduled office hours. Office hours and contact information can be found on the faculty directory page on the website."),

            ("How do I become a professor at the college?",
             "To become a professor at the college, you typically need a Ph.D. in your field, a record of academic research, and teaching experience. Open faculty positions are posted on the college's career page."),

            # Staff-related questions - Ensure they're more specific
            ("Who are the staff members of the college?",
             "The staff members of the college include faculty, administrative staff, and support staff. For specific staff categories, visit the staff directory."),

            # More specific department and staff questions
            ("Who are the staff members in the [Department Name]?",
             "Staff details for [Department Name] can be found in the department's page on the website."),

            # Courses and Departments
            ("What is the admissions process for graduate programs?",
             "To apply for graduate programs, you need to complete an online application form, submit your academic transcripts, provide letters of recommendation, and in some cases, take an entrance exam or interview."),

            ("Are there any dual-degree programs?",
             "Yes, the college offers dual-degree programs in fields such as Engineering and Business Administration, allowing students to earn two degrees in a shorter time frame."),

            ("What sports are offered on campus?",
             "The college offers various sports including soccer, basketball, volleyball, tennis, swimming, and athletics. The sports complex has dedicated facilities for both team and individual sports."),
            (" Is there any extracurricular activities  available on campus?",
             "Yes, There are various activities available on campus like NSS, YIP Various Clubs like tourism,health,quiz,ED, Nature,IT etc"),
            ("What student services available on Campus?",
             "There are various Services available on campus like Career guidance, Councelling,Sports activities etc.."),
            ("Is there a Student union in the college?",
             "Yes, Every year there will be held a college election "),
            ("How do I apply for hostel accommodation ",
             "There will be no applying procedure, please contact the office they will provide a application form and fill it"),
            ("What are the library hours?",
             "Library are available at college hours"),
            ("Where can i find campus maps or direction?",
             "It available in College website"),
            ("How do I pay my fees?",
             "Payment through online or by liquid cash"),
            ("Is there any Orientation program for New students ",
             "Yes, there will be various orientation program conducted by various departments for freshers"),
            (" What are the college timings?",
            "Our college timings are from 9:00 AM to 3:30 PM, Monday to Friday."),
            ("What are the facilities available on campus?",
             "Our campus has a library, cafeteria, gym, sports facilities, and more. You can explore our website for a full list of facilities."),
            ("How do I join a club or society?",
             "You can join a club or society by attending their meetings or events."),
            (" What are the campus safety protocols?",
             "Our campus has 24/7 security, CCTV cameras etc."),
            ("What are the college's social media channels?",
             "You can follow us on Instagram, Facebook,YouTube  for the latest updates and news."),
            ("How do I contact the college administration?",
             "You can contact the college administration through our websits."),
            ("What is the attendance policy?",
             "Our college expects students to attend at least 75% of classes. Failure to meet this requirement may result in failure in the course."),
            ("what are the courses available on college",
             "<b>Undergraduate Programmes</b><br> BA English <br>BA Sociology"
             "<br> Bsc Psychology<br>BBA<br>B.Com (Computer Application)<br>BCA<br><b>Right now all UG courses Duration 6 Semester</b> <br><b>Postgraduate Programmes</b>"
             "<br>MA English<br>M.Com<br>Msc Computer Science <br>Msc Psychology<br>Msc Clinical Psychology<br>MA Sociology<br><b>And all PG courses Duration 4 Semester</b>"),
            ("course fees or fee details",
             "<b>Undergraduate Programmes</b><br> BA English      9000/-<br>BA Sociology   9000/-"
             "<br> Bsc Psychology     11250/-<br>BBA     9000/-<br>B.Com (Computer Application)     11250/-<br>BCA     18750**/-<br><b>Right now all UG courses Duration 6 Semester</b> <br><b>Postgraduate Programmes</b>"
             "<br>MA English    18750/-<br>M.Com   18750/-<br>Msc Computer Science   22500/-<br>Msc Psychology    22500/-<br>Msc Clinical Psychology     22500/-<br>MA Sociology   18750/-<br><b>And all PG courses Duration 4 Semester</b>"),
            ("how many departments are there"
             "Our college has 10 departments, including Computer Science<br> Commerce and Management <br> Psychology<br> Oriental Language<br> Mathematics<br>Political Science<br> Journalism<br> Physical Education <br>Librarin "),
            ("Details of Computer Science",
             "The college offers two computer-related programs:<br>-Bachelor of Computer Applications (BCA) – 24 seats<br>-Master of Science in Computer Science (M.Sc. CS) – 20 seats<br>"
             "The programs are supported by 7 faculty members with expertise in various computing domains.<br>"
             "<b>BCA Program:</b>A three-year undergraduate course providing a strong foundation in Programming languages(C, Java, Python etc..),Web development,Networking,Software engineering etc..<br><b>M.Sc. Computer Science Program:</b>"
             "A two-year postgraduate course focusing on advanced computing concepts, including artificial intelligence, machine learning, cybersecurity, cloud computing, and data science, equipping students for careers in research, academia, and high-level IT positions."),
            ("Details of psychology",
             "The college offers Psychology programs with the following seat availability:<br>-B.Sc. Psychology – 60 seats<br>-M.Sc.Psychology – 20 seats<br>-M.Sc.Clinical Psychology – 10 seats<br>The department is supported by 9 experienced faculty members specializing in various psychology fields.<br>"
             "<b>B.Sc. Psychology</b>(3-year undergraduate program): providing knowledge on Cognitive and behavioral psychology,Mental health and human development,Psychological research methods etc..Prepares students for careers in mental health support, counseling, and HR roles.<br>"
             "<b>M.Sc. Psychology:</b>A two-year postgraduate program focusing on Advanced psychological theories,Cognitive neuroscience & psychotherapy,Research & experimental psychology ect..Prepares students for roles in academia, research, and counseling.<br>"
             "<b>M.Sc. Clinical Psychology:</b>A specialized two-year program covering Diagnosis and treatment of mental disorders,Neuropsychology & behavioral therapy,Clinical assessments and interventions etc..Prepares students for careers as clinical psychologists in hospitals, mental health centers, and rehabilitation clinics.<br>"),
            ("Details of Commerce or commerece and management studies",
             "The college offers Commerce and Business Administration programs with the following seat availability:<br>-<b>B.Com</b> (Bachelor of Commerce) – 60 seats<br>-<b>BBA</b>(Bachelor of Business Administration) – 24 seats<br>-<b>M.Com</b>(Master of Commerce) – 15 seats<br>-The department is supported by 11 experienced faculty members specializing in various areas of commerce, finance, and business management.<br>"
             "<b>B.Com </b>(Bachelor of Commerce): 3 years degree, focuses on accounting, taxation, auditing, business law, corporate finance, economics, and marketing management, preparing students for careers in banking, finance, taxation, and entrepreneurship etc..<br>"
             "<b> BBA</b>(Bachelor of Business Administration): three-year course, covers business strategy, entrepreneurship, financial and human resource management, marketing, operations, and business analytics, making it ideal for students aspiring to become business managers, entrepreneurs, and corporate professionals.Suitable for students aspiring to become business managers, entrepreneurs, and corporate professionals etc...<br>"
             "<b> M.Com </b>(Master of Commerce): lasting two years, offers advanced specialization in financial and cost accounting, international business, corporate governance, research methods, and business analytics, equipping graduates for roles in teaching, research, finance, auditing, and corporate sectors.Prepares graduates for careers in teaching, research, finance, auditing, and corporate sectors etc.. "),
            ("Details of Sociology",
             "The college offers Sociology programs, including:<br>-<b>BA Sociology</b> with 60 seats and <b>MA Sociology</b> with 24 seats<br>Supported by <b>9 experienced faculty members </b>specializing in various sociological fields.<br>"
             "<b>BA Sociology</b> (Bachelor of Arts in Sociology) is a three-year undergraduate program that explores society, culture, social institutions, human behavior, social change, and research methodologies. It prepares students for careers in social work, public administration, NGOs, policy-making, and research etc..<br>"
             "<b>MA Sociology </b>(Master of Arts in Sociology) is a two-year postgraduate program that provides an in-depth understanding of social theories, research methodologies, globalization, urbanization, and contemporary social issues. Graduates can pursue academia, research, public policy, social activism, and administrative roles etc.."),
            ("Details of English",
             "The college offers English programs,<br> <b>BA English</b> program has a total of 60 seats, offering students a strong foundation in literature, language, and communication skills. <br> <b>MA English</b> program has 24 seats, focusing on advanced literary studies and research. <br>The department is supported by 9 experienced faculty members who ensure effective teaching and academic guidance."
             " With a balanced student-to-teacher ratio, the department aims to provide an enriching learning experience. "),
            ("motto of the college",
             "Best Education For Better Generation"),
            (" Tell me a joke!",
             "Haha! Sure! Why don’t programmers like nature? Because it has too many bugs! 😆"),
            ("How do you process queries?",
             "I use Sentence Transformers to understand your question and match it with the most relevant answer stored in my database."),
            (" Where is the computer lab?",
             "The computer lab is in Block A, 1nd floor. It’s open from 9 AM to 4 PM"),
            (" What programming languages did you use to build this chatbot?",
             "Great question! I’m built using a combination of:<br>Python 🐍 – for backend logic and AI processing<br>Django 🎯 – for handling web requests and responses<br>SQL 🗄– for storing and retrieving college-related data"
             "<br>JavaScript & HTML 🌐 – for an interactive chatbot interface<br>Bootstrap 🎨 – for a clean, mobile-friendly design <br>-WAMP Server – For local development"),
            (" How would you add voice interaction?",
             " I can use Speech-to-Text (Google Speech API) for voice input and Text-to-Speech (gTTS API) for chatbot replies."),
            (" Can your chatbot support multiple languages?",
             " Currently, it works in English, but I can integrate Google Translate API or Multilingual Sentence Transformers to support Tamil and other languages."),
            ("who is the chairman of the college?",
             " The current Chairman of the Noble Women's College Governing Council is Dr. N. Yoonus."),
            ("who is the secretary of the college?",
             "Mr.Ismail Parakkatt"),
            ("this college is naac accredicted or not?",
             " The college is accredited by the  National Assessment and Accreditation Council(NAAC)and has been awarded an A grade"),
            ("Affiliation of this college?",
             "The college is affiliated to the University of Calicut and recognized by the Government of Kerala under the self-financing stream. "),
            ("naac grade point of this college?",
             " This college is accredited (first cycle)  with 'A' grade (3.23 CGPA) "),
            ("is there nss on this college?",
             "Yes"),
            ("who is the nss programme officer?",
             "Dr,Anupama Sr<br>HoD of Psychology"),
            ("howmany students in this college?",
             "847 students"),
            ("howmany faculties in this college?",
             "48 faculties"),
            ("what is the address of this college?",
             "Noble Campus<br>Vettekode,Pullancheri PO,Manjeri<br>Malappuram Dist,Pin:676122"),
            ("contact number of noble womens college?",
             "0483-2766 364,8643147989,<br>8592999376"),
            ("where is this college located?",
             " Noble Women's College is located in Manjeri, Malappuram district, Kerala. More specifically, the campus is at Noble Campus, Vettekode, Pullancheri P.O., Manjeri."),
            (" What are the college working hours?",
             "The college operates from 9:00 AM to 4:00 PM, Monday to Saturday. Some labs and the library may have different timings."),
            ("What are the library timings?",
             "The library is open from 9:00 AM to 5:00 PM on weekdays and from 9:00 AM to 1:00 PM on Saturdays."),
            ("How do I borrow books from the library?",
             "You need a library card to borrow books. Show your student ID at the library desk to register."),
            ("Is there a canteen on campus?",
             "Yes, we have a canteen that serves snacks and meals at affordable prices."),
            (" Does the college provide Wi-Fi for students?",
             "Yes, Wi-Fi is available for students. You need to get login credentials from the IT department."),
            ("How can I access the computer lab?",
             " You can use the computer lab during assigned lab hours or request access from the lab in-charge."),
            (" Are there sports facilities in the college?",
             "Yes! We have facilities for cricket, football, badminton, and more. You can join the sports club for regular practice."),
            ("Is there a medical room or first aid facility?",
             "Yes, the college has a first aid room. For emergencies, you can contact the administration."),
            (" When will the exams start?",
             "Exam dates are announced by the examination cell. Keep checking the notice board or website for updates."),
            (" How do I get my hall ticket?",
             "Hall tickets will be available online or at the exam office a few days before the exam."),
            (" What is the passing percentage for each subject?",
             "The minimum passing percentage is 40%, but it may vary by course."),
            (" How do I apply for revaluation?",
             "If you want to apply for revaluation, visit the exam office and fill out the revaluation form within the given deadline."),
            ("Does the college provide placement assistance?",
             "Yes, the placement cell organizes training and recruitment drives."),
            ("How do I contact my tutor or teacher or professor?",
             " I can provide the email address or extension number for the respective professor."
             "Can you please provide the name of your tutor"),
            # General Information about chatbot
             ("Who are you?",
              "I am your college assistant chatbot, here to help you with queries about our college."),
             ("What can you do?",
              "I can provide information about college facilities, departments, events, library, computer labs, and more!"),
             ("Are you a human?",
              "No, I’m just a chatbot designed to assist you with college-related queries."),
             ("How do you work?",
              "I process your questions and respond with the best possible answer based on my database of college-related information."),
             ("Can I talk to a real person?",
              "If you need further assistance, you can contact the college administration at [support email] or visit the office."),
             ("How can I ask you questions?",
              "Simply type your question, and I'll do my best to help you!"),
             ("Do you understand all languages?",
              "Right now,I only understand English."),
             ("Can you learn new things?",
              "I work with predefined responses, but my developers update me regularly with new information."),
             ("Are you available 24/7?",
              "Yes! You can ask me anything about the college anytime."),
             ("Do you store my data?",
              "I do not store personal data. I only provide answers based on available college information"),
             ("Do you have a name?",
              "You can call me Eliza😊!"),
             ("Who created you?",
              "I was developed by students and faculty to help answer common questions about our college."),
             ("how are you?",
              "I'm great! Thanks for asking. 😊 How about you?"),
             ("i love you",
              "Aww, that's sweet! 😊 I appreciate you too! 💙 Keep being awesome. What’s on your mind today?"),
             ("Hi or hai Eliza! How are you?",
              "Hey there! 😊 I’m doing great, thanks for asking! How about you?"),
             ("Thanks or thank you Eliza!",
              "You’re always welcome! 😃 Have a great day, and see you around!"),
             ("hai or hi",
              "Hey there! 😊"), ]





            # Dynamic data from models (Staff, Departments, Courses)


        # Add dynamic QA pairs from the database models
        s = Support.objects.all()
        for i in s:
            qa_pairs.append((i.category, i.discription))

        s = Support.objects.filter(category__icontains="scholarship")

        mfg=""
        for i in s:

            mfg= mfg + " "+ i.category


        if len(mfg)>0:
            qa_pairs.append(("offered scholarships are", mfg))

        print("offered scholarships are", mfg)

        e = Schedule.objects.all()
        for i in e:
            qa_pairs.append(
                (i.programname, i.programname + " happening on " + i.date.strftime("%Y-%m-%d") + " at " + i.time )
            )

        ss = ""
        for i in Department.objects.all():
            ss = ss + i.departmentname + ","

        ss = ss[0:len(ss)-1]
        qa_pairs.append(("Departments are", ss))

        for i in Department.objects.all():
            m = Course.objects.filter(DEPARTMENT=i)
            k = ""
            for j in m:
                k = k + j.coursename + ", "

            qa_pairs.append(
                (
                    'Courses offered by department ' + i.departmentname, "Offered courses are " + k
                )
            )

        for i in Course.objects.all():
            m = ""
            for j in Subject.objects.filter(COURSE=i):
                m = m + j.subjectname + ","
            if len(m) > 0:
                m = m[:len(m)-1]

                qa_pairs.append(
                    (
                        i.coursename + " offering subjects are", m
                    )
                )

        # Get department-wise staff details
        for i in Department.objects.all():
            m = ""
            for j in Staff.objects.filter(DEPRTMENT=i):
                m = m + j.name + ","
            if len(m) > 0:
                m = m[:len(m)-1]

                qa_pairs.append(
                    (
                        "Staffs of " + i.departmentname, "Main staffs are  " + m
                    )
                )

        # Add details of individual staff members
        # s = Staff.objects.filter(designation="hod")
        s = Staff.objects.all()
        for k in s:
            qa_pairs.append(
                (
                    "Details of " + k.name,
                    "<img src='" + k.photo + "' width='100px' height='100px'/> <br><b> Phone number: " + k.phone +
                    "</b> <br><b> Email: " + k.email,
                )
            )
        print("pppppppppppppppppppppppppppppppppppppppppp")
        print(qa_pairs)

        s = Staff.objects.filter(designation="Hod")
        for k in s:
            qa_pairs.append(
                (
                    "Hod  (head of department) of" + k.DEPRTMENT.departmentname +" is",
                    "<img src='" + k.photo + "' width='100px' height='100px'/> <br><b> Phone number: " + k.phone +
                    "</b> <br><b> Email: " + k.email,
                )
            )

        s = Staff.objects.filter(designation="Assistant Professor")
        for k in s:
            qa_pairs.append(
                (
                    "Assistannt professor  of  " + k.DEPRTMENT.departmentname + " is",
                    "<img src='" + k.photo + "' width='100px' height='100px'/> <br><b> Phone number: " + k.phone +
                    "</b> <br><b> Email: " + k.email,
                )
            )

        print("pppppppppppppppppppppppppppppppppppppppppp")
        print(qa_pairs)

        # Prepare the questions and answers for Sentence-BERT
        questions = [qa[0] for qa in qa_pairs]
        answers = [qa[1] for qa in qa_pairs]
        print(qa_pairs, "hello")

        # Encode the questions using Sentence-BERT model
        question_embeddings = model.encode(questions, convert_to_tensor=True)

        # Function to handle chatbot interaction
        def chatbot(query):
            # Encode the user's question
            query_embedding = model.encode(query, convert_to_tensor=True)

            # Compute cosine similarities between the query and all stored questions
            similarities = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]

            # Find the index of the most similar question
            best_match_idx = np.argmax(similarities)
            best_match_similarity = similarities[best_match_idx]

            print(best_match_similarity, "HIIII")

            # If the similarity is high enough, return the corresponding answer
            if best_match_similarity > 0.6:  # increased threshold to avoid overlap
                print("Answer found:", answers[best_match_idx])
                return answers[best_match_idx]
            else:
                return "I'm sorry, I don't have that information."

        # Corrected message (potential future correction mechanism)
        corrected_msg = msg
        print("Corrected message:", corrected_msg)

        # Get the chatbot's response
        response = chatbot(corrected_msg)
        print("Response:", response)

        return JsonResponse({'status': 'ok', 'message': response})



def chat1(request):


    return render(request, "PUBLIC/Chat.html", {'photo': "", 'name': "bot", 'toid': "0"})

# def chat_view(request):
#     if request.session['lid']!='':
#         fromid = request.session["lid"]
#         toid = request.session["userid"]
#         qry = User.objects.get(LOGIN=request.session["userid"])
#         from django.db.models import Q
#
#         res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
#         l = []
#
#         for i in res:
#             l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})
#
#         return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})
#     else:
#         return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')
#
#
# def chat_send(request, msg):
#     if request.session['lid']!='':
#         lid = request.session["lid"]
#         toid = request.session["userid"]
#         message = msg
#
#         import datetime
#         d = datetime.datetime.now().date()
#         chatobt = Chat()
#         chatobt.message = message
#         chatobt.TOID_id = toid
#         chatobt.FROMID_id = lid
#         chatobt.date = d
#         chatobt.save()
#     else:
#         return HttpResponse('''<script>alert('You are not Logined');window.location='/myapp/login/'</script>''')
#
#     return JsonResponse({"status": "ok"})
def alg(request):
    return render(request, 'PUBLIC/alg.html')