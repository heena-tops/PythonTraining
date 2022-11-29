from django.shortcuts import render,redirect
from .models import User 
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

def index(request):
	return render(request,"index.html")

def about(request):
	return render(request,"about.html")

def typography(request):
	return render(request,"typography.html")

def contacts(request):
	return render(request,"contacts.html")

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print(user.usertype)
			if user.usertype=="User":
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,"index.html")

			else:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,"seller_index.html")

		except Exception as e:
			print(e)
			msg1="Email or Password Does Not Matched!!!"
			return render(request,"login.html",{'msg1':msg1})

	else:
		return render(request,"login.html")

def signup(request):

	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg1="Email Already Exist"
			return render(request,"signup.html",{'msg1':msg1})

		except:
			if request.POST['password'] == request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					mobile=request.POST['mobile'],
					email=request.POST['email'],
					address=request.POST['address'],
					password=request.POST['password'],
					usertype=request.POST['usertype']
				)

				msg="Sign Up Successful"
				return render(request,"signup.html",{'msg':msg})

			else:
				msg1="Password and Confim Password Does Not Matched !!!"
				return render(request,"signup.html",{'msg1':msg1})

	else:
		return render(request,"signup.html")


def logout(request):

	try:

		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	
	except:

		return render(request,'login.html')


def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')

			else:
				msg1="New Password & Confirm New Passwrd Does Not Matched !!!"
				return render(request,'change_password.html',{'msg1':msg1})

		else:
				msg1="Old Passwrd Does Not Matched !!!"
				return render(request,'change_password.html',{'msg1':msg1})

	else:
		return render(request,'change_password.html')


def forgot_password(request):
	if request.method=="POST":
		try:
			print(request.POST['email'])
			user=User.objects.get(email=request.POST['email'])
			otp = random.randint(1000,9999)
			subject = 'OTP - Forgot Password'
			message = "Hello "+user.fname+ ", Your OTP : "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )
			msg="OTP Sent Successful"
			return render(request,'otp.html',{'email':user.email,'otp':otp,'msg':msg})

		except Exception as e:
			print(e)
			print("Hello1")
			msg1="Email Does Not Exist !!!"
			return render(request,'forgot_password.html',{'msg1':msg1}) 

	else:
		return render(request,'forgot_password.html')


def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new_password.html',{'email':email})

	else:
		msg1="OTP Does Not Matched !!!"
		return render(request,'otp.html',{'email':email, 'otp':otp,'msg1':msg1})


def new_password(request):
	email=request.POST['email']
	np=requst.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user = USer.objects.get(email=email)
		user.password=np
		user.save()

		return redirect('login')

	else:
		msg1="New Password & Condirm New password Does Not 'Matched !!!"
		return render(request,'new_password.html',{'email':email, 'msg1':msg1})
