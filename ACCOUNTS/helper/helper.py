import base64
import os
import smtplib

from Crypto.Cipher import XOR
from ACCOUNTS.models import *
secret_key = "12345678"
email_address = "pwork09@gmail.com"
email_password = "groupwork"

def custom_save(user):
	user.is_active = False
	user.save()


def encrypt(key, plaintext):
	cipher = XOR.new(key)
	return base64.b64encode(cipher.encrypt(plaintext))


def decrypt(key, ciphertext):
	cipher = XOR.new(key)
	return cipher.decrypt(base64.b64decode(ciphertext))


def send_verification_mail(email, activation_key, msg):
	print("send verificaion mail")
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email_address, email_password)
	server.sendmail(email_address, email, msg)
	server.quit()


def validate_username_email(username, email):
	try:
		user_name = StudentDetail.objects.get(SId=username)
		print(user_name)
	except StudentDetail.DoesNotExist:
		user_name = None

	try:
		e_mail = StudentDetail.objects.filter(Email=email)
	except StudentDetail.DoesNotExist:
		e_mail = None

	if user_name is None and e_mail is None:
		user_exists = False
		message = ""
	else:
		if user_name is None and e_mail is not None:
			user_exists = True
			message = "user is already regsitered with this email address"
		else:
			if user_name is not None and e_mail is None:
				user_exists = True
				message = "username already exists"
			else:
				user_exists = True
				message = "username and email already exists"

	return user_exists, message
