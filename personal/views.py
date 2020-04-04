from django.shortcuts import render



def homepage(request):

	return render(request,'home.html', {} )



#def base(request): # test views

	#return render(request,'base.html', {} )

