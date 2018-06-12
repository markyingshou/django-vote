# django-vote
Voting system written in Django

Django is a high-level Python Web framework that encourages rapid development and clean,you can complete your project easily
 official website is https://www.djangoproject.com/

**Xadmin** is more humanized,you can use all the plugins that you want,eg:I customized the Ueditor in the **project** 
 official website is http://sshwsfc.github.io/xadmin/    but the offical website is not useful in my memory

Develop IDE:

​	Pycharm 2018



**Environment:**

1.   first:  You should make a python3 virtualenvironment
2.   Python 3.6
3.   Django 1.11.8 ---> pip install django==1.11.8  #django framework
4.   mysqlclient  ----> pip install mysqlclient  #connect to mysql database
5.   Pillow  --> pip install Pillow   #deal with images
6.   django-crispy-forms >=1.6.0 (For xadmin crispy forms)
7.   django-reversion ([OPTION] For object history and reversion feature, please select right version by your django, see changelog )
8.   django-formtools ([OPTION] For wizward form)
9.   xlwt ([OPTION] For export xls files)
10.   xlsxwriter ([OPTION] For export xlsx files)
11.   django-crispy-forms>=1.6.0
12.   django-import-export>=0.5.1
13.   django-reversion>=2.0.0
14.   django-formtools==1.0
15.   future==0.15.2
16.   httplib2==0.9.2
17.   six==1.10.0 



****

In the project ,I download xadmin that as a extra_app.In this way ,I can customlize the theme and model that I want

the tree dictory:

![1528823211473](C:\Users\kuby\AppData\Local\Temp\1528823211473.png)



apps    ---place the app module

extra_apps  --- place the apps that are not in django

media  ---place the image or file by upload

static   ----place the website static files like css,js,image,font

survey -----the website entrance

template  ---  dynamic website template file





