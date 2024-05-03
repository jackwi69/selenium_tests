from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get('https://www.amazon.com/')
print('driver.title: ', driver.title) # driver.title: Amazon.com

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Servo Motor')
driver.find_element(By.ID, 'nav-search-submit-button').click()
time.sleep(1)

#elements = driver.find_element(By.XPath('//div[@class]'))
#elements = driver.find_element(By.XPath("//input[@id='twotabsearchtextbox']"))
#print(len(elements))

#driver.find_element(By.CLASS_NAME,'sg-col-inner')
"""
# Find the child element
elementsy = driver.find_elements(By.XPATH, '*')
for x in elementsy:
    tt = str(x.startswith("CNCTOPBAOS"))
    if tt:
        print(x.text)
"""

driver.close()
#Servo Motor 180W 3000rpm

"""
/home/john/anaconda3/bin/python /home/john/PycharmProjects/demo_test_v01/sel_amazon_01.py 
driver.title:  Amazon.com
Skip to main content
Deliver to
Poland
All
All Departments
Arts & Crafts
Automotive
Baby
Beauty & Personal Care
Books
Boys' Fashion
Computers
...
EN
Hello, sign in
Account & Lists
Returns
& Orders
0
Cart
All
We're showing you items that ship to Poland. To see items that ship to a different country, change your delivery address.
Dismiss
Change Address
Today's Deals
Customer Service
Registry
Gift Cards
Sell
1-48 of over 3,000 results for "Servo Motor"
Sort by:
        
            Featured
        
            Price: Low to High
        
            Price: High to Low
        
            Avg. Customer Review
        
            Newest Arrivals
        
            Best Sellers
        
    Sort by:Featured
Results
Sponsored
35kg high Torque Coreless Motor servo Metal Gear Digital and Stainless Steel Gear servo arduino servo for Robotic DIY,RC car (Control Angle 270°)
2,755
400+ bought in past month
$28
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months and up
Sponsored
AC 110V Industrial Sewing Machine Servo Motor Three-Phases Brushless (AC110V 3/5HP (450W))
4
$89
99
Delivery Fri, May 17
Ships to Poland
Sponsored
4Pack MG996R 55g Digital RC Servo Motors High Torque Metal Gear Servo for RC Car Robot Boat Helicopter
166
100+ bought in past month
$17
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months - 2 years
Sponsored
AC 110V Electric Three-Phases Brushless Industrial Sewing Machine Servo Motor with Controller 1000W (1-1/3HP) 50~60Hz
$169
99 List:
$179.99
Delivery Fri, May 10
Ships to Poland
Only 11 left in stock - order soon.
Overall Pick


5 Pcs SG90 Micro Servo Motor Mini Servo SG90 9g Servo Kit Compatible with RC Helicopter Airplane Car Boat Robot Arm/Hand/Walking/Servo Door Lock Control
624
300+ bought in past month
$8
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 years and up
Best Seller
10 Pcs SG90 9G Micro Servo Metal Geared Motor Kit for RC Robot Arm/Hand/Control with Cable, Mini Servos for Arduino Project (10)
1,027
400+ bought in past month
$17
99
Delivery Thu, May 16
Ships to Poland
Ages: 0 - 4 years
Popular Brand Pick


Miuzei 20KG Servo Motor High Torque RC Servo Metal Gear Waterproof for R/C Model DIY Car Robot, DS3218, Control Angle 270°
533
300+ bought in past month
No featured offers available
$13.99(1 new offer)
Today's deals
Sponsored
70kg High Torque 4Lines Brushless Waterproof Steering Servo 16.8V Digital Programmable Servos All Metal Oblique Gear Aluminum Case Suitable 1/8 1/10 Rc Crawler(180°Purple)
1
$85
97
Save 10% with coupon
25g RC Model Digital Metal Gear Servo - High Speed, High Torque, Coreless Motor, Dual Ball Bearing, JR Connector
2
$23
99
Join Prime to buy this item at $21.59
Servo Arms 25T Metal Aluminum Servo Horn M3 Threads Steering Arm for 1/8 1/10 1/12 Scales RC Models -4 Pack
7
$16
99
Join Prime to buy this item at $15.29
More results
SG90 Micro Servo Motor for Arduino Raspberry Pi DIY (3 Pcs)
32
200+ bought in past month
$6
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months - 3 years
Miuzei MG996R 55g Metal Gear Torque Digital Servo Motor for RC Helicopter Car Boat Robot (4 Pack)
41
50+ bought in past month
No featured offers available
$18.99(1 new offer)
Enduro Sewing Machine Motor - 550 Watt Electric Servo Motor
310
50+ bought in past month
$145
00 List:
$155.00
Delivery Thu, May 16
Ships to Poland
Sponsored
Feetech FS90R 360 Degree Continuous Rotation Micro Servo Motor + RC Tire Wheel for Arduino Micro:bit (Pack of 4)
120
$26
99
Delivery Thu, May 16
Ships to Poland
Ages: 16 years and up
Sponsored
45KG Coreless Servo Motor High Torque Steering: Smraza 8.4V Waterproof Servo Digital Full Metal Gear Servo for RC 1/10 1/8 1/12 Scale Car Truck Crawler/Robot/Boat with 25T Servo Horn（180°）
25
50+ bought in past month
$23
99
Save 5% with coupon
Delivery Thu, May 16
Ships to Poland
Ages: 15 years and up
Sponsored
550kg High Torque RC Servo, 2 in 1 Servo and Motor 16V~24V High Voltage Full Metal Gear Digital Servo
23
$129
99
Delivery Thu, May 16
Ships to Poland
Ages: 18 months - 5 years
Sponsored
Micro Brushless DC Servo Motor, MyActuator RMD-L-7015-23T Integrated Servo Motor Controller 200W 24V 1N.M with 18-bit Encoder Position Sensor for Collaborative Robot Arm PTZ BLDC Motor
$156
59
Delivery Fri, May 17
Ships to Poland
Only 15 left in stock - order soon.
Sg90 9g Micro Servo Motor, Miuzei Mini Servos Motor Kit Metal Gear 180 Degree Servo for Rc Car Airplane Plane Arduino 10 Pack
738
100+ bought in past month
No featured offers available
$18.77(1 new offer)
12PCS SG90 Micro Servo Motor, Dorhea Mini Servo SG90 9g Servo Kit for RC Helicopter Airplane Car Boat Robot Arm/Hand/Walking/Servo Door Lock Control
285
100+ bought in past month
$16
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 years and up
Sponsored
35kg high Torque Coreless Motor servo Metal Gear Digital and Stainless Steel Gear servo arduino servo for Robotic DIY,RC car (Control Angle 180°)
2,755
400+ bought in past month
$28
99
Delivery Thu, May 16
Or fastest delivery Fri, May 10
More results
(Ship from USA) Genuine Consew CSM1000 Servo Sewing Machine Motor 3/4HP CS1000 CSM550 SM550-1PLKHG484UY5151
281
50+ bought in past month
$131
99
Delivery Thu, May 16
Ships to Poland
Miuzei MG90S 9G Micro Servo Motor Metal Geared Motor Kit for RC Car Robot Helicopter, Mini Servos for Arduino Project (10)
119
100+ bought in past month
No featured offers available
$27.59(1 new offer)
Sponsored
540 45T 4 Poles Brushed Motor and WP-1060-RTR 60A Waterproof Brushed ESC Electronic Speed Controller with 5V/2A BEC for Axial RC4WD CROSS HPI MIST GMADE D90 D110 TF2 SCX10 ii PG4 MC8 WARAITH Y
82
$39
50
Delivery Thu, May 16
Ships to Poland
Only 14 left in stock - order soon.
Ages: 16 years and up
Sponsored
SG90 Micro Servo Motor for Arduino Raspberry Pi DIY (3 Pcs)
32
200+ bought in past month
$6
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months - 3 years
Sponsored
Aideepen [6-Pack] MG996R Metal Gear High Speed Torque Digital Servo Motor for Futaba JR RC Helicopter Car Boat Robot
114
$27
54 List:
$28.99
Save 10% with coupon
Delivery Fri, May 17
Ships to Poland
Ages: 18 months and up
Sponsored
RDS5180 80kg Digital Metal Robotic Servo Motor High Torque Double-Shaft Robot Servo Arm Waterproof IP66 with U Metal Brackets for RC Car DIY Robot (180°)
$42
59
Delivery Thu, May 16
Ships to Poland
Only 11 left in stock - order soon.
35kg high Torque Coreless Motor servo Metal Gear Digital and Stainless Steel Gear servo arduino servo for Robotic DIY,RC car (Control Angle 270°)
2,755
400+ bought in past month
$28
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months and up
4Pack MG996R 55g Digital RC Servo Motors High Torque Metal Gear Servo for RC Car Robot Boat Helicopter
166
100+ bought in past month
$17
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months - 2 years
2Pack 25KG High Torque RC Servo，Waterproof servo Compatible with 1/6，1/8, 1/10, 1/12 RC Car, Full Metal Gear Steering Servo with 25T Servo Horn（270°）
1,271
200+ bought in past month
$33
99
Delivery Thu, May 16
Ships to Poland
More Buying Choices
$28.05(2 used & new offers)
Ages: 17 years and up
60KG Robot Servo Motor High Torque Stainless Steel Gear Waterproof Digital Steering Large Servos with Mount Brackets
19
$38
57
Save 5% with coupon
Delivery Thu, May 16
Ships to Poland
Ages: 12 months and up
Miuzei 2Pcs 25KG High Torque RC Servo, Waterproof Servo Motor Compatible with 1/8, 1/10 RC Car, Full Metal Gear Steering Servo with 25T Servo Horn（270°）
77
100+ bought in past month
No featured offers available
$28.99(1 new offer)
AC 110V Industrial Three-phases Brushless Sewing Machine Servo Motor with Controller 3/4 HP (550W) 50~60Hz Speed 4500rpm
Metal
3
$89
99 Typical:
$109.99
Delivery Thu, May 16
Ships to Poland
Miuzei 20KG RC Servo High Torque Servo Motors, Waterproof Metal Gear Steering Servo for 1/8 1/10 RC Car Robot DIY, Digital Servo DS3218, Control Angle 270° (2 Pack)
11
50+ bought in past month
No featured offers available
$24.99(1 new offer)
DS3235 35kg Digital RC Servo High Torque All Metal Gear Coreless Motor Waterproof Servo Motors for RC Robot, Car, Truck (Control Angle 270°)
20
50+ bought in past month
$28
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 months - 2 years
Pack of 2 RC Servo 35KG Steering Servo 7.4V Digital Motor Stainless Steel Gear High Torque Waterproof for DIY Robotic RC Cars
783
$52
89
Delivery Thu, May 16
Ships to Poland
Ages: 10 years and up
Servo Motor SG90 180 Degree for Arduino, ESP32, ESP8266, Raspberry Pi, 2 Pieces
$8
99 (
$4.50/Item)
Delivery Thu, May 16
Ships to Poland
Aideepen [6-Pack] MG996R Metal Gear High Speed Torque Digital Servo Motor for Futaba JR RC Helicopter Car Boat Robot
114
$27
54 List:
$28.99
Save 10% with coupon
Delivery Fri, May 17
Ships to Poland
Ages: 18 months and up
Miuzei 5 Pcs SG90 9G Micro Servo Motor Kit for RC Robot Arm/Hand/Walking Helicopter Car Boat Control with Cable, Mini Small Servos for Arduino Project
277
No featured offers available
$8.99(1 new offer)
Ages: 3 months - 8 years
AC 110V Industrial Sewing Machine Servo Motor Three-Phases Brushless (AC110V 3/4HP (550W))
4
$95
99 Typical:
$109.99
Delivery Thu, May 16
Ships to Poland
Industrial Sewing Machine Servo Motor - Genuine Rex SC-600-SYN - 3/4 HP 550 Watt Brushless Servo Motor
BRUSHLESS
48
$149
00
Delivery Fri, May 17
Ships to Poland
Only 7 left in stock - order soon.
SG90 Servo Motor Micro Servo 9G Servo Motor for RC Robot Arm Helicopter Airplane Remote Control (5pcs)
117
$8
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 years and up
Best Seller
PCA9685 16 CH 12Bit PWM Servo Motor Driver Board Controller IIC Interface for Arduino Raspberry Pi Zero/Zero W/Zero WH/2B/3B/3B+ and Robot (2pcs)
96
No featured offers available
$13.99(1 new offer)
20KG Digital Servo High Torque Full Metal Gear Waterproof for RC Model DIY, DS3218MG,Control Angle 270° Red
5,360
300+ bought in past month
$13
65 List:
$28.00
Delivery Thu, May 16
Ships to Poland
Ages: 8 years and up
550kg High Torque RC Servo, 2 in 1 Servo and Motor 16V~24V High Voltage Full Metal Gear Digital Servo
23
$129
99
Delivery Thu, May 16
Ships to Poland
Ages: 18 months - 5 years
CNCTOPBAOS Nema34 12N.m Closed Loop Hybrid Servo Motor Stepper Motor 12nm 1700oz-in 156mm 6A 2 Phase & HSS86 Servo Driver & 3m Wire CNC Controller Kit for CNC Router Engraving Milling Machine
49
$180
00
Delivery Fri, May 10
Ships to Poland
AC 110V Electric Three-Phases Brushless Sewing Machine Servo Motor 450W (3/5HP) 50~60Hz
1
$89
99
Delivery Fri, May 17
Ships to Poland
Only 12 left in stock - order soon.
5PCS SG90 9g Servo Motor + 16 Channel PWM Servo Motor Driver PCA9685 IIC Module 12-Bit DIY Kit for RC Robot Arm Helicopter Airplane Car Boat Remote Control for Arduino for Raspberry pi
23
$16
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 years and up
Miuzei 35kg High Torque RC Servo, Coreless Servo Motor Metal Gear Digital Waterproof Steering Servo for Arduino 1/8 1/10 RC Car Robotic DIY 270 Degree (2)
17
50+ bought in past month
No featured offers available
$39.99(1 new offer)
SunFounder 20KG Servo Motor Waterproof High Torque Servo, SF3218MG Metal Gear Digital Servo, Aluminium Case, Control Angle 270° for RC Robot Cars
1,590
$14
99 List:
$16.99
Delivery Thu, May 16
Ships to Poland
Ages: 14 years and up
Readytosky Waterproof 60kg Servo Metal Gear High Torque Digital Servo Motor for RC Car Robot (Control Angle 270°)
10
$35
89
Delivery Thu, May 16
Ships to Poland
20KG RC Servo High Torque Servo Motors, Waterproof Full Metal Gear Steering Servo for 1/6 1/8 1/10 1/12 RC Car Robot DIY, Digital Servo with 25T Servo Horn, Control Angle 270°
1,676
$16
99
Save 5% with coupon
Delivery Fri, May 17
Ships to Poland
AC 110V Industrial Three-phases Brushless Sewing Machine Servo Motor with Controller 750W (1HP) 50~60Hz Speed 4500rpm
Metal
1
$115
99
Delivery Thu, May 16
Ships to Poland
Consew CSM3000 Sewing Machine Electric Servo Motor, 110 Volt, 1HP, 750W
Metal
120
$165
53
Delivery Fri, May 10
Ships to Poland
Only 6 left in stock - order soon.
6PCS MG996R Servo Motor Metal Gear Servo Motor Torque Digital Servo Motor High Speed Torque Servo Motor for Smart Car Robot Boat RC Helicopter Compatible Arduino Raspberry Pi Project
143
$27
99
Delivery Thu, May 16
Ships to Poland
Ages: 6 months and up
Hanaive 16 Pcs SG90 9g Micro Servo Motor Mini Servo Motors RC Servo Kit for Robot Helicopter Airplane Car Boat Control
22
$26
99
Delivery Thu, May 16
Ships to Poland
Ages: 6 - 12 years
FS90R 360 Degree Continuous Rotation Micro Servo Motor 9g Servo for RC Helicopter Airplane Car Boat Robot Controls
41
$25
99
Delivery Fri, May 17
Ships to Poland
Ages: 8 months and up
Feetech FS90R 360 Degree Continuous Rotation Micro RC Servo Motor 6V for Arduino Microbit Smart Car Robot (Pack of 2)
45
50+ bought in past month
No featured offers available
$13.98(1 new offer)
Servo High Torque Metal Gear Standard Digital Servo 25KG/0.13S 6.8V for 1/8 1/10 RC Cars(Control Angle 180)
892
300+ bought in past month
$17
99
Delivery Thu, May 16
Ships to Poland
Ages: 12 years and up
AITRIP 5 PCS MG90S Servo 9G Micro Servo Motor Metal Geared Micro Servo Motor 9G Smart Robot Car Helicopter Plane Boat Compatible with Arduino Raspberry Pi Project
38
No featured offers available
$13.69(1 new offer)
4PCS MG995 360°High Speed Torque Metal Gear Servo Motor Set Kit Compatible with Boat/RC Helicopter/Car/Airplane/Smart Robot/JR/Futaba
42
$25
99
Save 5% with coupon
Delivery Thu, May 16
Ships to Poland
2 pcs MG996R Servo Motor Metal Gear High-Torque Servo Motor for Smart Car Robot Boat RC Helicopter Mechanical arm Fittings(Control Angle 360)
76
50+ bought in past month
$15
99
$7 delivery May 23 - Jun 14
Servo SG90，Micro Steering Gear Motor kit Suitable for Remote Control Robot Helicopter Airplane Control car Ship (360 Degrees)
13
$7
99
Delivery Thu, May 16
Ships to Poland
2 Pcs MG90S 9g Micro Servo Motor Metal Gear Micro Servos Replace SG90 for Smart RC Robot Helicopter Airplane Controls Car Boat Plane Vehicle Models
93
50+ bought in past month
$7
49
Delivery Thu, May 16
Ships to Poland
Ages: 14 months - 7 years
2Pack SG90 Micro Servo Motor Mini Servo SG90 9g Servo Kit for RC Helicopter Airplane Car Boat Robot Arm/Hand/Walking/Servo Door Lock Control with Cable
78
$7
29
Delivery Thu, May 16
Ships to Poland
Ages: 12 months and up
Sponsored
ButterflyEdufields 20+ STEM Projects for Kids Ages 6 8 10 Years Boys Girls | Ultimate DIY Science Experiments for Kids | Educational Engineering Toys Best Birthday Gift idea
2,246
1K+ bought in past month
$39
47
Save 10% with coupon
Delivery Thu, May 16
Or fastest delivery Fri, May 10
Related searches
servo
servo motor kit
arduino
dc motor
servo motor sewing machine
servo motor arduino
Previous123...7Next
Brands related to your search
Sponsored
RC Motor & RC Servo
Shop F FLASH HOBBY 
Greartisan Focus on High Quality Motor Production
Shop Greartisan 
Need help?
Visit the help section or contact us
Sponsored
Department
RC Servos & Parts
RC Servos
Sewing Machine Accessories
Sewing Machine Parts
Automotive Replacement Gear Kit Motors
Electric Motors
Electronic Components
Motor Drives
Customer Review
& Up
& Up
& Up
& Up
Brands
Miuzei
DORHEA
ZOSKAY
ANNIMOS
Hosyond
LewanSoul
Aideepen
See more
Toy Character
Lego Technic
Toy & Game Price
Under $25
$25 to $50
$50 to $100
$100 to $200
$200 & Above
$
$
Go
Deals & Discounts
All Discounts
Today's Deals
Toys Age Range
Birth to 24 Months
2 to 4 Years
5 to 7 Years
8 to 13 Years
14 Years & Up
All Top Brands
Top Brands
Business Type
Small Business
Seller
Chipsgate US
Zhengbang Automation
CHENGCHUANG
Network Equipment
Udith
Amazon.com
Availability
Include Out of Stock


Back to top
Get to Know Us
Careers
Blog
About Amazon
Investor Relations
Amazon Devices
Amazon Science
Make Money with Us
Sell products on Amazon
Sell on Amazon Business
Sell apps on Amazon
Become an Affiliate
Advertise Your Products
Self-Publish with Us
Host an Amazon Hub
›See More Make Money with Us
Amazon Payment Products
Amazon Business Card
Shop with Points
Reload Your Balance
Amazon Currency Converter
Let Us Help You
Amazon and COVID-19
Your Account
Your Orders
Shipping Rates & Policies
Returns & Replacements
Manage Your Content and Devices
Amazon Assistant
Help
English $USD - U.S. Dollar United States
Amazon Music
Stream millions
of songs Amazon Ads
Reach customers
wherever they
spend their time 6pm
Score deals
on fashion brands AbeBooks
Books, art
& collectibles ACX
Audiobook Publishing
Made Easy Sell on Amazon
Start a Selling Account Amazon Business
Everything For
Your Business
  AmazonGlobal
Ship Orders
Internationally Home Services
Experienced Pros
Happiness Guarantee Amazon Web Services
Scalable Cloud
Computing Services Audible
Listen to Books & Original
Audio Performances Box Office Mojo
Find Movie
Box Office Data Goodreads
Book reviews
& recommendations IMDb
Movies, TV
& Celebrities
  IMDbPro
Get Info Entertainment
Professionals Need Kindle Direct Publishing
Indie Digital & Print Publishing
Made Easy Prime Video Direct
Video Distribution
Made Easy Shopbop
Designer
Fashion Brands Woot!
Deals and
Shenanigans Zappos
Shoes &
Clothing Ring
Smart Home
Security Systems
    eero WiFi
Stream 4K Video
in Every Room Blink
Smart Security
for Every Home Neighbors App
Real-Time Crime
& Safety Alerts Amazon Subscription Boxes
Top subscription boxes – right to your door PillPack
Pharmacy Simplified  
Conditions of Use
Privacy Notice
Consumer Health Data Privacy Disclosure
Your Ads Privacy Choices
© 1996-2024, Amazon.com, Inc. or its affiliates

Process finished with exit code 0

"""