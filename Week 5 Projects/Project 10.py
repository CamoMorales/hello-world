Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def paymentSchedule(purchasePrice):
    downPayment = 0.10
    annualInterest = 0.12
    monthlyPayment = 0.05
    month = 1
    startingBalance = purchasePrice - (purchasePrice * downPayment)
    monthlyPayment = startingBalance * monthlyPayment
    monthlyInterest = annualInterest / 12
    print()
...     print("%s%19s%18s%19s%10s%17s" % ("Month", "Starting Balance", "Interest to Pay", "Principle to Pay", "Payment", "Ending Balance"))
...     while startingBalance > 0:
...         if startingBalance < monthlyPayment:
...             principleToPay = startingBalance
...             monthlyPayment = startingBalance
...             interestToPay = 0
...         else:
...             interestToPay = startingBalance * monthlyInterest
...             principleToPay = monthlyPayment - interestToPay
... 
...             endingBalance = startingBalance - principleToPay
...             print("%2d%16.2f%16.2f%18.2f%18.2f%15.2f" % (month, startingBalance, interestToPay, principleToPay, monthlyPayment, endingBalance))
...             startingBalance = endingBalance
...             month = month + 1
... 
...             
>>> purchasePrice = float(input("enter the purchase price: "))
enter the purchase price: 2000
>>> paymentSchedule(purchasePrice)

Month   Starting Balance   Interest to Pay   Principle to Pay   Payment   Ending Balance
 1         1800.00           18.00             72.00             90.00        1728.00
 2         1728.00           17.28             72.72             90.00        1655.28
 3         1655.28           16.55             73.45             90.00        1581.83
 4         1581.83           15.82             74.18             90.00        1507.65
 5         1507.65           15.08             74.92             90.00        1432.73
 6         1432.73           14.33             75.67             90.00        1357.05
 7         1357.05           13.57             76.43             90.00        1280.63
 8         1280.63           12.81             77.19             90.00        1203.43
 9         1203.43           12.03             77.97             90.00        1125.47
10         1125.47           11.25             78.75             90.00        1046.72
11         1046.72           10.47             79.53             90.00         967.19
12          967.19            9.67             80.33             90.00         886.86
13          886.86            8.87             81.13             90.00         805.73
14          805.73            8.06             81.94             90.00         723.79
15          723.79            7.24             82.76             90.00         641.02
16          641.02            6.41             83.59             90.00         557.43
17          557.43            5.57             84.43             90.00         473.01
18          473.01            4.73             85.27             90.00         387.74
19          387.74            3.88             86.12             90.00         301.62
20          301.62            3.02             86.98             90.00         214.63
21          214.63            2.15             87.85             90.00         126.78
22          126.78            1.27             88.73             90.00          38.05
23           38.05            0.38             37.67             38.05           0.38
24            0.38            0.00              0.38              0.38           0.00
25            0.00            0.00              0.00              0.00           0.00
26            0.00            0.00              0.00              0.00           0.00
27            0.00            0.00              0.00              0.00           0.00
28            0.00            0.00              0.00              0.00           0.00
29            0.00            0.00              0.00              0.00           0.00
30            0.00            0.00              0.00              0.00           0.00
31            0.00            0.00              0.00              0.00           0.00
32            0.00            0.00              0.00              0.00           0.00
33            0.00            0.00              0.00              0.00           0.00
34            0.00            0.00              0.00              0.00           0.00
35            0.00            0.00              0.00              0.00           0.00
36            0.00            0.00              0.00              0.00           0.00
37            0.00            0.00              0.00              0.00           0.00
38            0.00            0.00              0.00              0.00           0.00
39            0.00            0.00              0.00              0.00           0.00
40            0.00            0.00              0.00              0.00           0.00
41            0.00            0.00              0.00              0.00           0.00
42            0.00            0.00              0.00              0.00           0.00
43            0.00            0.00              0.00              0.00           0.00
44            0.00            0.00              0.00              0.00           0.00
45            0.00            0.00              0.00              0.00           0.00
46            0.00            0.00              0.00              0.00           0.00
47            0.00            0.00              0.00              0.00           0.00
48            0.00            0.00              0.00              0.00           0.00
49            0.00            0.00              0.00              0.00           0.00
50            0.00            0.00              0.00              0.00           0.00
51            0.00            0.00              0.00              0.00           0.00
52            0.00            0.00              0.00              0.00           0.00
53            0.00            0.00              0.00              0.00           0.00
54            0.00            0.00              0.00              0.00           0.00
55            0.00            0.00              0.00              0.00           0.00
56            0.00            0.00              0.00              0.00           0.00
57            0.00            0.00              0.00              0.00           0.00
58            0.00            0.00              0.00              0.00           0.00
59            0.00            0.00              0.00              0.00           0.00
60            0.00            0.00              0.00              0.00           0.00
61            0.00            0.00              0.00              0.00           0.00
62            0.00            0.00              0.00              0.00           0.00
63            0.00            0.00              0.00              0.00           0.00
64            0.00            0.00              0.00              0.00           0.00
65            0.00            0.00              0.00              0.00           0.00
66            0.00            0.00              0.00              0.00           0.00
67            0.00            0.00              0.00              0.00           0.00
68            0.00            0.00              0.00              0.00           0.00
69            0.00            0.00              0.00              0.00           0.00
70            0.00            0.00              0.00              0.00           0.00
71            0.00            0.00              0.00              0.00           0.00
72            0.00            0.00              0.00              0.00           0.00
73            0.00            0.00              0.00              0.00           0.00
74            0.00            0.00              0.00              0.00           0.00
75            0.00            0.00              0.00              0.00           0.00
76            0.00            0.00              0.00              0.00           0.00
77            0.00            0.00              0.00              0.00           0.00
78            0.00            0.00              0.00              0.00           0.00
79            0.00            0.00              0.00              0.00           0.00
80            0.00            0.00              0.00              0.00           0.00
81            0.00            0.00              0.00              0.00           0.00
82            0.00            0.00              0.00              0.00           0.00
83            0.00            0.00              0.00              0.00           0.00
84            0.00            0.00              0.00              0.00           0.00
85            0.00            0.00              0.00              0.00           0.00
86            0.00            0.00              0.00              0.00           0.00
87            0.00            0.00              0.00              0.00           0.00
88            0.00            0.00              0.00              0.00           0.00
89            0.00            0.00              0.00              0.00           0.00
90            0.00            0.00              0.00              0.00           0.00
91            0.00            0.00              0.00              0.00           0.00
92            0.00            0.00              0.00              0.00           0.00
93            0.00            0.00              0.00              0.00           0.00
94            0.00            0.00              0.00              0.00           0.00
95            0.00            0.00              0.00              0.00           0.00
96            0.00            0.00              0.00              0.00           0.00
97            0.00            0.00              0.00              0.00           0.00
98            0.00            0.00              0.00              0.00           0.00
99            0.00            0.00              0.00              0.00           0.00
100            0.00            0.00              0.00              0.00           0.00
101            0.00            0.00              0.00              0.00           0.00
102            0.00            0.00              0.00              0.00           0.00
103            0.00            0.00              0.00              0.00           0.00
104            0.00            0.00              0.00              0.00           0.00
105            0.00            0.00              0.00              0.00           0.00
106            0.00            0.00              0.00              0.00           0.00
107            0.00            0.00              0.00              0.00           0.00
108            0.00            0.00              0.00              0.00           0.00
109            0.00            0.00              0.00              0.00           0.00
110            0.00            0.00              0.00              0.00           0.00
111            0.00            0.00              0.00              0.00           0.00
112            0.00            0.00              0.00              0.00           0.00
113            0.00            0.00              0.00              0.00           0.00
114            0.00            0.00              0.00              0.00           0.00
115            0.00            0.00              0.00              0.00           0.00
116            0.00            0.00              0.00              0.00           0.00
117            0.00            0.00              0.00              0.00           0.00
118            0.00            0.00              0.00              0.00           0.00
119            0.00            0.00              0.00              0.00           0.00
120            0.00            0.00              0.00              0.00           0.00
121            0.00            0.00              0.00              0.00           0.00
122            0.00            0.00              0.00              0.00           0.00
123            0.00            0.00              0.00              0.00           0.00
124            0.00            0.00              0.00              0.00           0.00
125            0.00            0.00              0.00              0.00           0.00
126            0.00            0.00              0.00              0.00           0.00
127            0.00            0.00              0.00              0.00           0.00
128            0.00            0.00              0.00              0.00           0.00
129            0.00            0.00              0.00              0.00           0.00
130            0.00            0.00              0.00              0.00           0.00
131            0.00            0.00              0.00              0.00           0.00
132            0.00            0.00              0.00              0.00           0.00
133            0.00            0.00              0.00              0.00           0.00
134            0.00            0.00              0.00              0.00           0.00
135            0.00            0.00              0.00              0.00           0.00
136            0.00            0.00              0.00              0.00           0.00
137            0.00            0.00              0.00              0.00           0.00
138            0.00            0.00              0.00              0.00           0.00
139            0.00            0.00              0.00              0.00           0.00
140            0.00            0.00              0.00              0.00           0.00
141            0.00            0.00              0.00              0.00           0.00
142            0.00            0.00              0.00              0.00           0.00
143            0.00            0.00              0.00              0.00           0.00
144            0.00            0.00              0.00              0.00           0.00
145            0.00            0.00              0.00              0.00           0.00
146            0.00            0.00              0.00              0.00           0.00
147            0.00            0.00              0.00              0.00           0.00
148            0.00            0.00              0.00              0.00           0.00
149            0.00            0.00              0.00              0.00           0.00
150            0.00            0.00              0.00              0.00           0.00
151            0.00            0.00              0.00              0.00           0.00
152            0.00            0.00              0.00              0.00           0.00
153            0.00            0.00              0.00              0.00           0.00
154            0.00            0.00              0.00              0.00           0.00
155            0.00            0.00              0.00              0.00           0.00
156            0.00            0.00              0.00              0.00           0.00
157            0.00            0.00              0.00              0.00           0.00
158            0.00            0.00              0.00              0.00           0.00
159            0.00            0.00              0.00              0.00           0.00
160            0.00            0.00              0.00              0.00           0.00
161            0.00            0.00              0.00              0.00           0.00
162            0.00            0.00              0.00              0.00           0.00
163            0.00            0.00              0.00              0.00           0.00
164            0.00            0.00              0.00              0.00           0.00
165            0.00            0.00              0.00              0.00           0.00
166            0.00            0.00              0.00              0.00           0.00
167            0.00            0.00              0.00              0.00           0.00
168            0.00            0.00              0.00              0.00           0.00
169            0.00            0.00              0.00              0.00           0.00
170            0.00            0.00              0.00              0.00           0.00
171            0.00            0.00              0.00              0.00           0.00
172            0.00            0.00              0.00              0.00           0.00
173            0.00            0.00              0.00              0.00           0.00
174            0.00            0.00              0.00              0.00           0.00
175            0.00            0.00              0.00              0.00           0.00
176            0.00            0.00              0.00              0.00           0.00
177            0.00            0.00              0.00              0.00           0.00
178            0.00            0.00              0.00              0.00           0.00
179            0.00            0.00              0.00              0.00           0.00
180            0.00            0.00              0.00              0.00           0.00
181            0.00            0.00              0.00              0.00           0.00
182            0.00            0.00              0.00              0.00           0.00
183            0.00            0.00              0.00              0.00           0.00
184            0.00            0.00              0.00              0.00           0.00
185            0.00            0.00              0.00              0.00           0.00
