import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

imageurls = {
    "campus":
    "https://i.ibb.co/8NbCyb9/campus.jpg",
    "tripleroom_url":
    "https://scontent.fpnq4-1.fna.fbcdn.net/v/t1.0-9/122140166_815645489197544_8328917430186400303_o.jpg?_nc_cat=111&ccb=2&_nc_sid=dbeb18&_nc_ohc=_qjpA4PQQCoAX9sLkGC&_nc_oc=AQkOWMHtD18797KPIq3SchTfFDnk2x4r-r1UwXiNeFDS1J12HwhL90DjzzmoKLktkz8&_nc_ht=scontent.fpnq4-1.fna&oh=800ac0b364d58711717baeaa4b4bfc24&oe=60219B0C",
    "doubleroom_url":
    "https://scontent.fpnq4-1.fna.fbcdn.net/v/t1.0-9/122107179_3351982168247612_3874733656374962850_o.jpg?_nc_cat=111&ccb=2&_nc_sid=dbeb18&_nc_ohc=6K758cHE_JgAX_ZLsh3&_nc_ht=scontent.fpnq4-1.fna&oh=22e78e68d3b474f0894c1caab5264403&oe=60209BBC",
    "mess_url":
    "https://scontent.fpnq4-1.fna.fbcdn.net/v/t1.0-9/122370919_2289019017911512_7022478130559725125_o.jpg?_nc_cat=100&ccb=2&_nc_sid=dbeb18&_nc_ohc=IRLhvHpHRY0AX8TOQ1J&_nc_ht=scontent.fpnq4-1.fna&oh=38da5aa0e4db37b35987e70fee6356f7&oe=601FFFB2"
}

dict_intents = {
    "branchchange.prospects": [
        """
<b>Branch change</b> depends solely on your CGPA (Cumulative Grade Point Average)
for the first two semesters. For a more details kindly have a   <a href="http://iitmandi.ac.in/academics/branch_change.php"> refer </a> this
Everything is relative and dependent on your batch's performance. Although, if you study diligently (not compromising on the extra-curriculars), I believe you are good to go
• If you attend all your classes diligently, and solve the assignments, etc. you would be able to get a cgpa above 8. Keep in mind that there is relative grading in most courses, and other students will also be working hard to get a nice cgpa. In the end it depends on your hardwork.
• IIT Mandi offers a liberal branch change policy which allows you to study a branch of your interest. But always be prepared for the branch that you are getting.
"""
    ],
    "branchchange.criteria": [
"""
• The student will have to be in good <b>academic standing</b>, having done the full complement of courses and having no backlog. The decision on the student’s application will be made only after the grades of the second semester are received and the CGPA at the end of the semester will be the relevant CGPA.\n
• <u><b>Branch change</b></u> applications will be considered strictly in order of merit as established by the CGPA and only to the extent of the applicant’s choices and in the order of the preferences expressed in the application\n
• The top- ranking student of each discipline may be awarded a branch change if she/he has a CGPA of at least 8.0.\n
• The strength of any branch shall not be allowed to fall below a minimum strength of 20 students because of the branch change\n
"""
        ],
    "hostel.rooms": [
        """
Hostels have rooms of different sizes, single, double and triple occupancy.  
First year students usually get a shared room.In the subsequent years, you may get a single room.
There is a common washroom for the whole floor",imageurls["tripleroom_url"]  ,imageurls["doubleroom_url"]
"""
    ],
    "hostel.carry": [
        """

• Phone/laptop : Although laptop may not be used for academic purposes in the first semester, I strongly recommend carrying one due to its other non academic uses.\n
• Shorts,  Pajamas : Most of the time (99.9 % in my case), you won’t be wearing jeans. I recommend carrying a couple or two of shorts/pajamas for daily use.\n
• Good quality slippers : Same goes for slippers. 99.9765 % of time you will be using slippers. You’ll rarely use shoes unless you have a pair of red chief and you want to show off, so bring good quality slippers which can bear the torture.\n

Also Institute arranges vendors for the sale of hostel necessities like mattresses, pillows, pillow
covers, bed sheets, locks, buckets, mugs etc. on Orientation day\n. 
Local vendors are arranged for the sale of these items inside the Institute.\n 

Daily use things .If you forget any thing various shops are available here\n
"""
    ],
    "hostel.facilities": [
        """
<b>Facilities</b> at hostel include a study room with a heater,common room or TV room for watching TV and playing table tennis or for group activities.\n
You also get a microwave,electric kettle ,refrigerator on each floor and also shared laundry with several washing machines and dryers\n
Hostel provides all basic facilities like Bed,Desk,Chair and closet in your room.\n
Common room has some games😀 like foosball and TT table (depending upon hostel).\n
"""
    ],
    "hostel.life": [
        """
The hostels at  <b> IIT Mandi </b> are some of the best hostels you can find in the country\n
<u>Hostels are alloted Randomly to freshers and sharing room is there in first year , 2 - 3 students in one room</u>\n
​
<b>Yaar baaki saare city wale colleges to aise hi hote hain, kya padhe kya nahi padhe sab bhool jaenge.Lekin iss jagah ko nhi bhool paenge, ye jagah bahut hi faad hain, aur sabse alag hain!\n</b>
I won't be telling much as it will spoil the surprise!😉\n
"""
    ],
    "campus.transportation": [
        """
We have regular buses running between the North campus and South campus every 15 minutes and buses from college to Mandi every hour\n
We have a bus stop in the north campus near the A10 building and in the south campus near the CV Raman canteen \n
"""
    ],
    "campus.mess": [
        """
We have several messes in our campus D1,D2 in the south campus and Pine,Oak in the North Campus."
The mess food is also good
""", imageurls["mess_url"]
    ],
    "fees": ["""
https://iitmandi.ac.in/academics/fees.php
"""],
    "document": [
        """
1.Final course and institute allotment letter received from reporting centre.\n
2 Original admit card of JEE Advanced\n
3. Proof of payment made at the time of seat allocation\n
4.Class X mark sheet and Board Certificate (if applicable) original and two copies\n
5. Class XII mark sheets and pass certificate in original and two copies.\n
6 Medical fitness certificate in case it is not submitted at the reporting centre.\n
7. Photographs: passport size(8) stamp size(4)\n
8.Valid certificate of category in the JEE prescribed format (OBC/NCLYSC/ST/PwD/DS) issued by a competent authority\n
9. Copy of Aadhar Card Any document issued by the Government regarding address proof (if copy of aadhar is not available)\n

"""
    ],
    "fees.waiver": [
        """
In case the you plan to apply for any <b>institute scholarship</b>, You should bring Family <u>Income Certificate</u> issued by the authorized officials in Revenue Dept/DC/SDM/Tehsildar, etc.\n
• A self attested copy of Income Certificate reeds to be deposited at the time of admission and original needs to be submitted at the time of submission of claim for scholarship.\n
• Duly filled up and signed income affidavit\n 
<a href="https://www.iitmandi.ac.in/hn/academics/files/scholarships/affidavit.pdf">Visit for more Info</a>

Different types of scholarships are available for a student of IIT Mandi. Some of these are provided directly by the government and some directly by institute.\n
These can be categorised into these categories:\n
1.Merit-cum-Means scholarships. For further details please visit <a href=https://www.iitmandi.ac.in/academics/scholarship.php>visit</a>\n
2.Central Sector Scholarships for SC students, Top Class Education Scheme for ST students.For further details please visit<a href=https://www. scholarships.gov.in/>visit</a>\n
3.Institute Scholarships for SC/ST students. For further details please visit <a href=https://www.iitmandi.ac.in/academics/scholarship.php>visit</a>\n
4. Scholarships for Female Students: From the academic year 2017-18 onwards, all female students admitted to the B.Tech.\n
program are provided with a merit scholarship including full tuition fee waiver and Rs.1.000/- per month stipend.\n 
This merit scholarship will continue till 4 year subject to good academic performance indicated by a minimum SGPA criteria of 7.0 for the previous two semesters and no disciplinary action of the candidate\n
    
"""
    ],
    "sports": [
        """
Sports activities are coordinated by the Principal Sports Officer and the Faculty Sports Advisor. A team of highly experienced coaches and ground staff work under
their direction to help you take part in the games of your choice.\n
• Participate in various tournaments like Inter-IIT, Aagaaz, Rann-Neeti and other in-house tournaments.\n
• At Kamand, we have <b>Fields</b> for Cricket, Football and Hockey, Basketball, Tennis, Squash, Badminton, TT and Volleyball courts. TT and Foosball tables are also
available in most hostels. There is also Swimming pool, gym and yoga room etc.
• Activities like Hiking and Trekking are also encouraged,under guidance.\n 
• Faculty Advisors: Dr. Rajendra Ray , Dr. Deepak Swami \n
<a href="https://students.iitmandi.ac.in/gymkhana/">Read more</a>\n
"""
    ],
    "programming.development": ["""
    GSOC ROCKS
    """],
    "programming.culture": [
        """
The coding culture in <b>IIT Mandi</b> is very good. Any student can learn to code here if interested.\n
There is programming club called <b>KamandPrompt</b>.This help us in getting started with coding and help us through the journey. They organise various competition to test the coding skills.\n
The seniors will willingly help you with any of your doubts.\n
Moreover with liberal branch change policy,Non CSE student can change the branch to CSE very easily.\n
Lets take a look at our <b>GSOC</b> Stats compare to new IITs:-\n
GSoC selections for 2020:\n
Indore : 3 students\n
Ropar : 2 students\n
Patna : 6 students\n
Hyderabad : 1 student\n
Bhubaneshwar : 1 student\n
Gandhinagar : Noone\n
Mandi : <b>9 students + 6 mentors</b>\n
We are improving upon ICPC year by year.\n
Open source culture is amazing at our college as shown by GSoC selections. Apart from the GSoC selections, many were also selected in Linux community bridge, which is an equally prestigious program.\n
<a href=”https://pc.iitmandi.co.in/icpc/hof.html”>Reference1</a>
<a href=”https://pc.iitmandi.co.in/gsoc/”>Reference2</a>

Happy coding 🙂
"""
    ],
    "programming.compi": [
"""
• Try to follow "C++ for dummies". Focus on first 2 units of the book \n
• You don't need to buy the book, just download pdf version of the book from the internet\n
Happy coding 🙂
"""],

    "programming.os": [
"""
• For good programming practices, you'll need to use ubuntu/unix/linux OSes\n
• Working on linux is <b>faster and more secure</b> and comes with more support.\n
• Please <a href = "http://blog.pc.iitmandi.co.in/Dual-Boot/">Vist</a> for proper guide \n
"""
],
    "programming.laptop": [
        """
<u><b>Guidelines to buy a perfect laptop</b></u>\n
1.Before buying a laptop (or any product for that matter), first of all define the type of work that you will be using it for. For Instance,if you are a light user, there is no point in buying an overkill gaming laptop just for the sake of it.\n
2.Once you have defined your work type, fix a budget according to the suitable configuration.\n
3.Some key points while looking at laptop configs are:\n
• RAM: 8GB is OK, also they are almost always upgradeable\n
• SSD(solid-state drives) offer faster storage than HDD (hard-disk drives).So if you are able to find a laptop with an ssd within your budget it will benefit you a lot.\n
• For basic programming, even simple laptops will suffice, but say you want to perform heavy video editing or android development or gaming, then you will need one with a good GPU and RAM.\n    

"""
    ],
    "ragging": [
        """
Zero Tolerance for ragging. We have the following committees to take care of any issues, Student Welfare and Disciplinary Committee (SWDC), Anti-Ragging
Committee (ARC)\n
There is <b>Student Welfare and Discipline Committee<\b>
"""
    ],
    "library": [
        """
<b>The Central Library, IIT Mandi</b> has a rich collection of books and journals in the field of Engineering, Science & Technology and related areas, the efficiency and effectiveness
of our electronic resources and our professional services.\n 
IIT Mandi Library operations are automated using KOHA. Library currently houses over 26650 books (15650 print books & 11000 e-books) and provide access to more than 10000 e-journals.\n

• In general, you can get the e-books for the materials that the teacher specifies\n
• You can also get them from the library, though the library may have only limited copies. Local bookshops in Mandi or online stores are also of help, so are the
seniors\n
• Moodle web pages on our intranet site have all the course materials posted by faculty and students\n
<a href="http://library.iitmandi.ac.in/">Read more</a>\n
"""
    ],
    "placements": [
        """
Among the elite technology institutes of the country, IIT Mandi embodies technology, research and development in the purest form \n
• The placement statistics of IIT Mandi are impressive, and our students have taken up successful careers in companies and corporations, civil services, entrepreneurship, and academia.\n 
• All the Placement associated activities are handled by the Career and Placement Cell (CnP) of the institute.
• 80-90% students who opt for placement get placed. Salary package comparable to other IITs.\n 
• Placements in the Core profile is not that much fledged in EE. Most of the EE people go for CSE jobs as they are more viable option and open for them by many of the companies.\n

<b>Median Salary: 14LPA </b>
Some of the companies and organizations who came for recruitment in previous years include: ISRO, Amazon, Microsoft, Texas Instruments, Goldman Sachs,
Codenation, irage capital solutions Ltd., Mastercard, Webstaff, Publicis.Sapient, Tonichi insatsu, Optum, Robert bosch,Yodlee, Domino Data lab, SMS datatech,
Samsung Delhi, TCS Research, Internet Academy, Vehant, L&TMumbai, L&T ECC, Truring, Tork Motor Cycles, Novopay, Shopx, MAQ, Assanjob, Eclerx, Tejas
Networks, Siemens, Cortex, Optiver, Flow traders, DEShaw, ServiceNow, Razorpay, Oyo Rooms, 1mg, BOSCH, Works Application, Toppr, Mathworks, Marvell
Semiconductors, HPCL and OLX People.\n

<b>We have an incubation centre (called The Catalyst), so if you ever want to work on your own project or idea you won't have to fall short of resources. The best part is that IIT Mandi is still in a process and processes takes time, so you can play your hand in shaping it in a way that it suit your needs</b>\n

"""
    ],
    "academics.workingdays": [
        """
• Usually we do not have classes on saturdays and sundays but sometimes holidays in the middle of the week are compensated by shifting that day's time table schedule to a weekend day\n
• Various goverments holidays are also there\n
<a href="http://www.iitmandi.ac.in/administration/holidays_2020.php"> Refer </a>        
        """
    ],
    "academics.companycg": [
        """
        CGPA criteria for placement/internship varies from company to company. An ideal CGPA to have is 8.5 or greater.\n
        Most of the companies allow for a CGPA greater than 8.
        """
    ],

    "academics.professors": [
        """
        It varies from professor to professor. Some are of very good nature and empathetic but some are a bit orthodox and expect a lot from their students.
        """
    ],
    "academics.exams": [
        """
        Grading pattern varies across courses.\n
        But most of the courses including the ones in first year have 2 quizzes and one end-sem examination along with some weightage for assignments/practicals/mini-projects.
        """
    ],
    "academics.stationery": [
        """
        You don't need to buy any books or other stationery related to your courses.\n
        We have a huge collection at the library which is sufficient for all the students of a course.\n
        You can also find PDF version of books available on the internet.\n
        Other stationery items can easily be purchased at the local store or ordered online.
        """
    ],

    "academics.studying": [
        """
        It depend on the person. But combining classes, assignments, quizzes and tests it takes around 50-55 hours every week.
        """
    ],
    "hostel.life": [
        """
        The hostels at  <b> IIT Mandi </b> are some of the best hostels you can find in the country. The hostels are equipped with:\n
        <u>Hostels are alloted Randomly to freshers and sharing room is there in first year , 2 - 3 students in one room</u> \n
        <b>Yaar baaki saare city wale colleges to aise hi hote hain, kya padhe kya nahi padhe sab bhool jaenge.Lekin iss jagah ko nhi bhool paenge, ye jagah bahut hi faad hain, aur sabse alag hain!\n</b>
        <a href="https://gymkhana.iitmandi.co.in/hostel.html">Visit</a> 
        """
    ]
}

answers_collection = db.collection(u'answers')

def add_data(dict_intents):
    for key, val in dict_intents.items():
        payload = {"intent":key,"text":val[0]}
        if(len(val)>1):
            payload["imgrefs"] = val[1:]
        else:
            payload["imgrefs"] = []
        answers_collection.add(payload)

add_data(dict_intents)