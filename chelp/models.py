from django.db import models

# Create your models here.

class covidHelp(models.Model):

	STATES_CATEGORIES = (

	('Uttar Pradesh','Uttar Pradesh'),
	('Maharastra','Maharastra'),
	('Delhi','Delhi'),
	('Andhra Pradesh','Andhra Pradesh'),
	('Arunachal Pradesh','Arunachal Pradesh'),
	('Assam','Assam'),
	('Bihar','Bihar'),
	('Chhattisgarh','Chhattisgarh'),
	('Goa','Goa'),
	('Himachal Pradesh','Himachal Pradesh'),
	('Haryana','Haryana'),
	('Jharkhand','Jharkhand'),
	('Karnataka','Karnataka'),
	('Keral','Keral'),
	('Madhya Pradesh','Madhya Pradesh'),
	('Manipur','Manipur'),
	('Meghalaya','Meghalaya'),
	('Mizoram','Mizoram'),
	('Nagaland','Nagaland'),
	('Odisha','Odisha'),
	('Rajasthan','Rajasthan'),
	('Punjab','Punjab'),
	('Sikkim','Sikkim'),
	('Tamil Nadu','Tamil Nadu'),
	('Telangana','Telangana'),
	('Tripura','Tripura'),
	('West Bengal','West Bengal'),
	('Uttarakhand','Uttarakhand'),
	('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
	('Daman and Diu','Daman and Diu'),
	('Jammu and Kashmir','Jammu and Kashmir'),
	('Ladakh','Ladakh'),
	('Puducherry','Puducherry'),
	('Lakshadweep','Lakshadweep'),
	)
	
	STATUS = (('Active','Active'),('Inactive', 'Inactive'))

	BLOOD_CATEGORIES = (

	('A+','A+'),
	('A-','A-'),
	('B+','B+'),
	('B-','B-'),
	('AB+','AB+'),
	('AB-','AB-'),
	('O+','O+'),
	('O-','O-'),
	)

	SERVICE_CATEGORIES = (

	('Beds','Beds'),
	('Oxygen','Oxygen'),
	('Plasma','Plasma'),
	('Remdesivir','Remdesivir'),
	
	)

	person_name = models.CharField(max_length=200 , null= True , blank=True)
	person_detail = models.CharField(max_length=400 , null= True , blank=True)
	person_mobile = models.CharField(max_length=30 , null= True , blank=True)
	hospital = models.CharField(max_length=200 , null= True , blank=True)
	state = models.CharField(max_length=100 , choices=STATES_CATEGORIES)
	city= models.CharField(max_length=200, null= True , blank=True) 
	service = models.CharField(max_length=100 , choices=SERVICE_CATEGORIES)
	blood_group = models.CharField(max_length=100 , choices=BLOOD_CATEGORIES, null=True , blank=True)
	status = models.CharField(max_length=50 , choices=STATUS, default='Active')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.service
