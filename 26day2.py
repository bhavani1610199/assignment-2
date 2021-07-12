Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = ["HP","DELL","LENOVO","APPLE","ASUS"]
for x in enumerate(name,10):
    print(x)
    
>>> 
>>> for x in enumerate(name,10):
	print (x)

	
(10, 'HP')
(11, 'DELL')
(12, 'LENOVO')
(13, 'APPLE')
(14, 'ASUS')
>>> 
>>> for count , x in enumerate(name,16):
	y = count,x
	print(list(y))

	
[16, 'HP']
[17, 'DELL']
[18, 'LENOVO']
[19, 'APPLE']
[20, 'ASUS']
>>> 
>>> name =("HP","DELL","LENOVO","APPLE","ASUS")
>>> for x in enumerate (name,101):
	print(x)

	
(101, 'HP')
(102, 'DELL')
(103, 'LENOVO')
(104, 'APPLE')
(105, 'ASUS')
>>> 
>>> for count , x in enumerate(name,200):
	y = count,x
	print(y)

	
(200, 'HP')
(201, 'DELL')
(202, 'LENOVO')
(203, 'APPLE')
(204, 'ASUS')
>>> 