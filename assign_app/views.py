from django.shortcuts import render
from .models import *
from .forms import *
import datetime


# from rest_framework.decorators import api_view


# Create your views here.

def home(request):
    para = "ELearn Infotech is a Realtime Training Company offering Courses on varied IT Technologies like Web Design & PHP with MySQL, Digital Marketing, UI/UX Designing & Development, Oracle Modules, Angularjs, Node.js, Python, Fullstack Development, SAP Moddules, Cloud Computing, Graphic Designing, Tally ERP9, Autocad etc. Established in 2016 ELearn Infotech has successfully Trained upwards of 150+ Students. ELearn Infotech offers Excellent Software courses with end to end support to the candidates. ELearn Infotech is a one stop shop for IT services & Training in Madhapur,Hyderabad "
    para_1 = "ELearn Infotech is a Professional Software Courses Training Company like Web Design & Digital Marketing, Oracle, UI/IX Designing & Development, Graphic Designing, Cloud Modules, SAP Modules Training Company from Madhapur,Hyderabad. We Provide Training for Design Unique websites & Develope Web Application, Digital Marketing Solutions like SEO,SMM,PPC (Google Adwords) and help businesses create their brand. ELearn Infotech build a Relationship with Students, who allows us to build up a tailored branding plan advance. ELearn Infotech offers Excellent Training Software Courses with end to end support to the candidates."
    name_1 = "WELCOME TO ELEARN INFOTECH"
    name_2 = "COURSE LIST"
    courses = courses_table.objects.all()
    z = datetime.datetime.now()
    return render(request, 'home_page.html',
                  {'p': para, 'p_1': para_1, 'h': name_1, 'h_1': name_2, 'c': courses, 'dt': z})


def about(request):
    heading = "ABOUT US"
    heading_1 = "WHY CHOOSE US"
    para = "ELearn Infotech is a Professional Software Courses Training Company like Web Design & Digital Marketing, " \
           "Oracle, UI/IX Designing & Development, Graphic Designing, Cloud Modules, SAP Modules Training Company " \
           "from Madhapur,Hyderabad. We Provide Training for Design Unique websites & Develope Web Application, " \
           "Digital Marketing Solutions like SEO,SMM,PPC (Google Adwords) and help businesses create their brand. " \
           "ELearn Infotech build a Relationship with Students, who allows us to build up a tailored branding plan " \
           "advance. ELearn Infotech offers Excellent Training Software Courses with end to end support to the " \
           "candidates. "
    list_1 = "--> Quality of Training as per International Standards."
    list_2 = "--> Provide Real time Training with Live Project."
    list_3 = "-->  Students satisfaction is the ultimate goal for us."
    list_4 = "--> Business ethics is more important than money."
    list_5 = "--> Help students to reach their true potential with Personality Development."
    list_6 = "-->  Help students to become entrepreneurs with motivation and support"
    z = datetime.datetime.now()
    return render(request, 'about.html',
                  {'h': heading, 'p_1': para, 'h_1': heading_1, 'l_1': list_1, 'l_2': list_2, 'l_3': list_3,
                   'l_4': list_4, 'l_5': list_5, 'l_6': list_6, 'dt': z})


def courses(request):
    heading = "COURSES WE OFFER"
    heading_1 = "WEB DESIGNING"
    web_design = "Web Designing is a process of creating websites using graphics and useful functionality. In Website " \
                 "designing process the important factors are content, Website look, good layout and accessibility of " \
                 "the website on all devices. Our Web Designing Course content is created & updated by Industry " \
                 "Experts to match the present standards of web technologies. We provides Web Desinging Course in " \
                 "Madhapur, Hyderabad. "
    heading_2 = "PYTHON"
    python = "Python Training by ELearn Infotech Python Training Institute is designed to help you in this extremely " \
             "popular programming language with ease. Python is a simple interpreter based and high level object " \
             "oriented generic programming language and can be used to design and build application and prototype " \
             "with ease. We are one of the Best Python Institute in Madhapur, Hyderabad. "
    heading_3 = "ANGULAR JS"
    angular = "AngularJs Training in Madhapur Hyderabad. ELearn Infotech AngularJs Training Institute offers " \
              "Real-time Angularjs Training in Madhapur, Hyderabad. We have designed our Angularjs course Curriculam " \
              "based on students Requirement to Achieve Goal. We offer both class room AngularJs Training in Madhapur " \
              "Hyderabad and AngularJs Course online training with Live project. "
    heading_4 = "DIGITAL MARKETING"
    digital = "ELearn Infotech Digital Marketing Training Institute Offers Real-time and Placement focused Digital " \
              "Marketing Training in Madhapur Hyderabad by Experienced Digital Marketing Training Experts from " \
              "Industry. We provide Digital Marketing Classroom Training and Digital Marketing Online Training both " \
              "with Live Project. We helps to Students About their Digital Marketing Resume Preparation. Digital " \
              "Marketing Classes are arranged as per the convenience of the Student Timings.Digital Marketing Course " \
              "Weekend Batches also Available. We offering Affordable Digital Marketing Course in Madhapur. "
    heading_5 = "PHP"
    p = "ELearn Infotech is one of the Best PHP Training Institute in Madhapur Hyderabad.We Offers Real-time and Placement focused PHP Training in Madhapur Hyderabad by Experienced Real time PHP Developers. We provide both PHP Classroom Training and PHP Online Training with Realtime Project. Our ELearn Infotech PHP Course Training classes are conducted by Realtime PHP Development Experts and classes are arranged as per the convenience of the students or Employees."
    heading_6 = "SEO"
    seo = "ELearn Infotech Offers Real-time SEO Training in Madhapur Hyderabad with 100% Job Guarantee by Experienced SEO Experts from Industry. We provide SEO Classroom Training and SEO Online Training both with Realtime Project. We helps to Students About their Resume Preparation and SEO Interview Questions. We Provide Detailed SEO Course Material & classes are arranged as per the convenience of the student Timings"
    heading_7 = "UI"
    u = "ELearn Infotech offers Affordable UI Developer Training in Madhapur, Hyderabad by Industry Experts. Our UI Developer course includes from Basic to Advanced Level UI Developement. We have designed our UI Developer course content based on students Requirement to Achieve their Goal. We offer both UI Developer classroom training in Madhapur and UI Developer online training with real time project. We are one of the top UI Developer Institute in Madhapur, Hyderabad."
    heading_8 = "NODE JS"
    node = "ELearn Infotech offers Real-time Node.JS Training in Madhapur, Hyderabad. Our Node.JS course includes from Basic to Advanced Level Node.JS Course. We have designed our Node.JS course content based on students Requirement to Achieve Goal. We offer both class room Node.JS training in Madhapur and Node.JS Course online training by 6+ years Realtime Experts."
    heading_9 = "GOOGLE ADWORDS"
    adwords = "Elearn Infotech Offers Real-time and placement focused Google Adwords Training in Madhapur Hyderabad " \
              "by Experienced Google Adwords Experts from Industry. We provide Google Adwords Classroom Training and " \
              "Google Adwords Online Training both with Realtime Project. We helps to Students About their Resume " \
              "Preparation and Google Adwords Interview Questions. We Provide INR 500/- Worth for Google Adwords " \
              "Campaign & Google Adwords classes are arranged as per the convenience of the Student Timings. "
    z = datetime.datetime.now()
    return render(request, 'courses.html',
                  {'dt': z, 'h': heading, 'h_1': heading_1, 'w': web_design, 'h_2': heading_2, 'p': python,
                   'h_3': heading_3, 'a': angular, 'h_4': heading_4, 'dm': digital, 'h_5': heading_5, 'php': p,
                   'h_6': heading_6, 'h_7': heading_7, 'h_8': heading_8, 'h_9': heading_9, 'ui': u, 'n': node,
                   'ad': adwords, 's': seo})


def gallery(request):
    galleries = "GALLERY"
    z = datetime.datetime.now()
    return render(request, 'gallery.html', {'g': galleries, 'dt': z})

