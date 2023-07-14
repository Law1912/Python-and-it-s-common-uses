from django.shortcuts import render
from .models import Professors
# Create your views here.

def comp(profs):
    lines=[]
    with open('prof\\templates\\prof\\search.html', 'r') as pf:
        lines=pf.readlines()
    with open('prof\\templates\\prof\\search.html', 'w') as pf:
        for number, line in enumerate(lines):
            if number<19:
                pf.write(line)
    fun = open('prof\\templates\\prof\\search.html', 'a')
    for profss in profs:
        fun.write("""\n<script>\nvar table = document.getElementById("results");\nvar row = table.insertRow(-1);\nvar cell1 = row.insertCell(0);\nvar cell2 = row.insertCell(1);\nvar cell3 = row.insertCell(2)\ncell1.innerHTML = "<a href='/prof/%s'>%s</a>";\ncell2.innerHTML = "%s";\ncell3.innerHTML = "%s";\n</script>""" %(profss.id, profss.name, profss.department, profss.email))
    fun.close()

def index(request):
    lines=[]
    with open('prof\\templates\\prof\\index.html', 'r') as pf:
        lines=pf.readlines()
    with open('prof\\templates\\prof\\index.html', 'w') as pf:
        for number, line in enumerate(lines):
            if number<97:
                pf.write(line)
    departments=Professors.objects.values_list('department', flat=True)
    departments=list(departments)
    departments=list(dict.fromkeys(departments))
    fun = open('prof\\templates\\prof\\index.html', 'a')
    for dep in departments:
        fun.write('\n<script>\nvar x = document.Srchfrm1.Dept_Stff;\nvar option = document.createElement("option");\noption.text = "%s"\noption.value = "%s"\nx.add(option);\n</script>' %(dep,dep))
    fun.close()
    return render(request, 'prof/index.html')

def search(request):
    values=(request.POST).dict()
    profs=Professors.objects.all()
    if values['Dept_Stff'] == "Choose a department":
        values['Dept_Stff']=''
    else:
        profs=profs.filter(department=values['Dept_Stff'])
    if 'selstffnam' in values.keys():
        profs=profs.filter(name__contains=values['selstffnam'])
    if 'selstffmail' in values.keys():
        profs=profs.filter(email__contains=values['selstffmail'])
    comp(profs)
    context={
        's1': values['selstffnam'],
        's2': values['selstffmail'],
        'deptn': values['Dept_Stff'],
    }
    return render(request, 'prof/search.html', context)

def profinfo(request, prof_id):
    prof=Professors.objects.all().get(id=prof_id)
    context={
        'prof':prof,
    }
    return render(request, 'prof/prof.html', context)
