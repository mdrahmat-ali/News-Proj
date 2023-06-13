from django.shortcuts import render

def index(request):
    return render(request,'newsapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movies Information'
    msg1='Sonali getting crud without any reason'
    msg2='salman going to marrry with someone special'
    msg3='Modi ji is going to make cinema for wathing movie in free time'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest Sports Information'
    msg1='Kohli is best because of his bating'
    msg2='India win because they palyed very well today'
    msg3='First gold accured by china and second silver accured by India'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Latest Politics Information'
    msg1='Telangana Election will come and everyone will give their vote'
    msg2='Achche din aa gaye we think like that but it is still not come '
    msg3='Kerla money gaya  but where we do not know'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
    
