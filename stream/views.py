from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from stream.models import anime,user as model_user
from stream.forms import AnimeForm, CreateUser, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
import hashlib as hl
# Create your views here.

def hash_string_256(string):
    """Create a SHA256 hash for a given input string.

    Arguments:
        :string: The string which should be hashed.
    """
    return hl.sha256(string).hexdigest()

def home(request):
    #form=AnimeForm()
    if request.method=='POST':
        #form=AnimeForm(request.POST)
        fom=anime()
        x=request.POST.get('clue')
        fom.clue_id=int(request.POST.get('c_id'))
        fom.clue = hash_string_256(x.encode())
        #fom=anime()
        # fom.size=request.POST.get('my_field')
        #if form.is_valid():
            # fom.name=form.cleaned_data['clue']
            # fom.year=form.cleaned_data['clue_id']
        fom.save()  
        return list(request)
        # else:
        #     return HttpResponse('ERROR')
    return render(request,'home.html')
    #return render(request,'home.html', {'form':form})



def base(request):
    return render(request, 'base.html')



def signup(request):
    form=CreateUser()
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            # user = model_user.objects.get(username=request.POST.get('username'))
            # profile = Profile(user=user)
            # profile.save()
            return base(request)
       # else:
       #     return HttpResponse('ERROR')
    return render(request,'signup.html', {'form':form})

def leader(request):
    row=model_user.objects.all()
    lb=[]
    sub_li2=[]
    sub_li=[]
    for ele in row:
        lb.append([ele.name,ele.c01,ele.c02,ele.c03,ele.c04,ele.c05,ele.c06,ele.c07,ele.c08,ele.c09,ele.c10,ele.c11])
        for x in lb:
            count=0
            for i in x:
                if i==0:
                    count+=1
        sub_li2.append([x[0],11-count])
    sub_li=sub_li2[1:]
    for i in range(0, len(sub_li)):
        for j in range(0, len(sub_li)-i-1):
            if (sub_li[j][1] < sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo

    return render(request, 'leader.html', {'line':sub_li})



@login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile) 
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile') # Redirect back to profile page

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(request, 'profile.html', context)

def index(request):
    #row=[model_user.name., model_user.c01,model_user.c02,model_user.c03,model_user.c04,model_user.c05,model_user.c06,model_user.c07,model_user.c08,model_user.c09,model_user.c10,model_user.c11,]
    cl=anime.objects.all()
    row=model_user.objects.all()
    lb=[]
    sub_li2=[]
    sub_li=[]
    for ele in row:
        lb.append([ele.name,ele.c01,ele.c02,ele.c03,ele.c04,ele.c05,ele.c06,ele.c07,ele.c08,ele.c09,ele.c10,ele.c11])
        for x in lb:
            count=0
            for i in x:
                if i==0:
                    count+=1
        sub_li2.append([x[0],11-count])
    sub_li=sub_li2[1:]
    for i in range(0, len(sub_li)):
        for j in range(0, len(sub_li)-i-1):
            if (sub_li[j][1] < sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo


    #return HttpResponse(l)

            
    obj = request.user
    if obj.c01==0:
        if request.method == 'POST':
            y=request.POST.get('clue')
            if y != None:
                if hash_string_256(y.lower().encode())==cl[0].clue:
                    obj.c01=1
                    obj.index=22
                    obj.save()
                    return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            return render(request, 'cluepage.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})
    
    elif obj.c02==0:
        if request.method == 'POST':
            y=request.POST.get('clue2')
            
            if y != None:
                if hash_string_256(y.lower().encode())==cl[1].clue:
                    obj.c02=1
                    obj.index=30
                    obj.save()
                    return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            return render(request, 'cluepage2.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     if obj.index>=int(x):
            #          return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage2.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})

    elif obj.c03==0:
        if request.method == 'POST':
            y=request.POST.get('clue3')
            if y != None:
                if hash_string_256(y.lower().encode())==cl[2].clue:
                    obj.c03=1
                    obj.index=48
                    obj.save()
                    return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            return render(request, 'cluepage3.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     if obj.index>=int(x):
            #         return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage3.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})
    
    elif obj.c04==0:
        if request.method == 'POST':
            y=request.POST.get('clue4')
            if y != None:
                if hash_string_256(y.lower().encode())==cl[3].clue:
                    obj.c04=1
                    obj.index=63
                    obj.save()
                    return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            return render(request, 'cluepage4.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     if obj.index>=int(x)+1:
            #         return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage4.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})
    
    elif obj.c05==0:
        if request.method == 'POST':
            y=request.POST.get('clue5')
            if y != None:
                if hash_string_256(y.lower().encode())==cl[4].clue:
                    obj.c05=1
                    obj.index=84
                    obj.save()
                    return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            return render(request, 'cluepage5.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     # if obj.index>=int(x)+1:
            #     #     return render(request, 'cluepage5.html', {'v':obj.index,'line':sub_li})
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage5.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})
    
    elif obj.c06==0:
        if request.method == 'POST':
            y=request.POST.get('clue6')
            if y != None:
                if hash_string_256(y.lower().encode())==cl[5].clue:
                    obj.c06=1
                    obj.index=87
                    obj.save()
                    return render(request, 'index.html', {'v':obj.index,'line':sub_li})
            return render(request, 'cluepage6.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     # if obj.index>=int(x)+1:
            #     #     return render(request, 'cluepage6.html', {'v':obj.index,'line':sub_li})
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage6.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})
    
    elif obj.c07==0:
        if request.method == 'POST':
            y=request.POST.get('clue7')
            if y != None:
                if hash_string_256(y.lower().encode())==cl[6].clue:
                    obj.c07=1
                    obj.index=100
                    obj.save()
                    return render(request, 'greetings.html')
            return render(request, 'cluepage7.html', {'v':obj.index,'line':sub_li})
            # x = request.POST.get('index')
            # if x !='':
            #     # if obj.index>=int(x)+1:
            #     #     return render(request, 'cluepage7.html', {'v':obj.index,'line':sub_li})
            #     obj.index = int(x)+1
            #     obj.save()
            #     return render(request, 'cluepage7.html', {'v':obj.index,'line':sub_li})
        return render(request, 'index.html', {'v':obj.index,'line':sub_li})

    elif obj.c07==1:
        return render(request, 'greetings.html')
    
def list(request):
    
    return render(request, 'list.html')
    # return render(request, 'c.html')