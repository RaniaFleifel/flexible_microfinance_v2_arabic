# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 03:05:16 2023

@author: rania
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:48:54 2023

@author: rania
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 04:54:32 2023

@author: rania
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:41:24 2023

@author: rania
"""

from flask import Flask,render_template,request
from datetime import datetime, timedelta
import pandas as pd
from tabulate import tabulate
import re
from pretty_html_table import build_table
import random

a=[]
b=[]
flag=0
std_loan_noapprox=[]
flexible_loan_noapprox=[]   
entries=[]
app=Flask(__name__,template_folder='templates')
options_month = ['jan', 'feb', 'mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
options_month_ar = ['يناير', 'فبراير', 'مارس','ابريل','مايو','يونيو','يوليو','أغسطس','سبتمبر','أكتوبر','نوفمبر','ديسمبر']
num1 = random.randint(0, 100)
thistab=[]
interest_rate=18/100
rand_num=[]
@app.route("/")
def home():
    thistab=[]

    return render_template('A_ideal_html.html')



@app.route('/calculations',methods=['POST'])
def calculations():
    #a=[]

    data=request.form#.values()

    amount=float(data["amount"])
    std_loan_noapprox=[]
    flexible_loan_noapprox=[] 

    while amount>15000: 
        tmp="المبلغ مينفعش يكون أكبر من  ١٥٠٠٠"
        return render_template('A_ideal_html.html',loan_size_txt_no=tmp)#.append('The size of the loan is {} egp\n'.format(loan_size[0])))
    else:
        a.append(amount)
        thistab.append(amount)

        tmp=f"مبلغ القرض: {amount}"
#        tabs=pd.DataFrame(columns=["rand_generated","amount"])
#        tabs.append([num1,amount])
#        tabs.to_csv("tabs.csv",mode='a')
        with open('data.txt', 'a',encoding='utf-8') as f:
            f.write("\n"+str(num1))
            f.write(","+str(amount))
        return render_template('B_ideal_html.html',loan_size_txt_yes=tmp)#.append('The size of the loan is {} egp\n'.format(loan_size[0])))
    print("############### IN CALCULATIONS",a)
    
@app.route('/payment_schedule',methods=['POST'])
def payment_schedule():
    #if (num1==rand_num[len(rand_num)-1]):
    #    print("proceed?")
    #else:
    #    print("7ALET TWARE2 G")
    try:
        loan_size=a[len(a)-1]#in case of multiple entries 
    except:
        missing_amount_txt="من فضلك  اكتب مبلغ القرض و اختار ""بداية الحسابات l0l0l0l0l0" 
        a.clear()
        b.clear()#b.pop(-1)
        thistab.clear()


        return render_template('A_ideal_html.html',loan_size_txt_no=missing_amount_txt)

    #if loan_size==thistab[0]:
#    print("############### IN PAYMENT SCHEDULE",loan_size,'LEN(A)',len(a),"ALL A",a)

    data=request.form
    b.append(data)
    #print("???????????????????????????????????????????????",data)
    frequency=data["frequency"]
    #if len(a)len(b)
    try:
        if len(a)==len(b):# or (len(a)>len(b) and loan_size==thistab[-1]) :
            holiday_yn=data["holiday"]
         
        #    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>b after append",b,'LEN(B)',len(b))
            if data["grace"]=="no":
                grace_yn=data["grace"]
                grace_dur=0
                grace_txt="مش حابب فترة سماح"
            else:
                grace_yn=re.split(r'(\d+)', data["grace"])[0]
                grace_dur = int(re.split(r'(\d+)', data["grace"])[1])
                if grace_dur==1:
                    grace_dur_ar=" شهر"
                elif grace_dur==2:
                    grace_dur_ar=" شهرين"
                else:
                    grace_dur_ar="3 شهور"
        
                grace_txt=f"هاخد فترة سماح {str(grace_dur_ar)} \n"
            
            if holiday_yn=="no":
                holiday_txt="مش حابب ترحيل السداد"
                holiday_dur=0
                holiday_months=""
            else:
                if data["month1"]==' ':
                    holiday_months=data["month2"].capitalize()
                    holiday_months_ar=options_month_ar[options_month.index(holiday_months.lower())]
                    holiday_dur=1
                    holiday_dur_ar=" شهر"
                elif data["month2"]==' ':
                    holiday_months=data["month1"].capitalize()
                    holiday_months_ar=options_month_ar[options_month.index(holiday_months.lower())]
        
                    holiday_dur=1
                    holiday_dur_ar=" شهر"
                else:
                    holiday_months=[data["month1"],data["month2"]]
                    holiday_months_ar=[options_month_ar[options_month.index(data["month1"].lower())],options_month_ar[options_month.index(data["month2"].lower())]]
                    holiday_dur=2
                    holiday_dur_ar=" شهرين"
        
        
                holiday_txt=f"هرحل السداد لمدة{holiday_dur_ar}: {holiday_months_ar} \n"
        
            # #ideal v1 assumes dispersment starts tomorrow
            # tom_date = datetime.now()+timedelta(1)
            # tom_month=tom_date.strftime("%b")
            # start_month=tom_month.lower()
            # #ideal v2 wants to start next month
            this_month=datetime.now().strftime("%b").lower()
            start_month=options_month[options_month.index(this_month)+1]
            
            
            start_month_ar=options_month_ar[options_month.index(this_month)+1]
            if frequency=="monthly":
                frequency_ar="كل شهر"
            elif frequency=="biweekly":
                frequency_ar="كل اسبوعين (مرتين في الشهر)"
            else:
                frequency_ar="كل اسبوع  (٤ مرات في الشهر)"
        
        
            loan_amount_txt=f"مبلغ القرض: {loan_size} جنيه"
            start_month_txt=f"السداد يبتدي من شهر{str(start_month_ar)}\n"
            frequency_txt=f"هدفع القسط {frequency_ar}"
        #    print(str(start_month_txt),frequency_txt,grace_txt,holiday_txt)
        
        
            # if data["grace"]=="no":
            #     grace_yn=data["grace"]
            #     grace_dur=0
            #     grace_txt="Grace period not applied"
            # else:
            #     grace_yn=re.split(r'(\d+)', data["grace"])[0]
            #     grace_dur = int(re.split(r'(\d+)', data["grace"])[1])
            #     grace_txt=f"Grace period applied for {str(grace_dur)} months \n"
            
            # if holiday_yn=="no":
            #     holiday_txt="Repayment holiday not applied"
            #     holiday_dur=0
            #     holiday_months=""
            # else:
                
            #     if data["month1"]==' ':
            #         holiday_months=data["month2"].capitalize()
            #         holiday_dur=1
            #     elif data["month2"]==' ':
            #         holiday_months=data["month1"].capitalize()
            #         holiday_dur=1
            #     else:
            #         holiday_months=[data["month1"].capitalize(),data["month2"].capitalize()]
            #         holiday_dur=2
        
            #     holiday_txt=f"Repayment holiday applied for {holiday_dur} months: {holiday_months} \n"
        
            # # #ideal v1 assumes dispersment starts tomorrow
            # # tom_date = datetime.now()+timedelta(1)
            # # tom_month=tom_date.strftime("%b")
            # # start_month=tom_month.lower()
            # # #ideal v2 wants to start next month
            # this_month=datetime.now().strftime("%b").lower()
            # start_month=options_month[options_month.index(this_month)+1]
            
            # loan_amount_txt=f"Loan amount is {loan_size} EGP"
            # start_month_txt=f"Dispersment starts in {str(start_month)}\n"
            # frequency_txt=f"{frequency.capitalize()} payment"
        
            df = pd.DataFrame(columns=['الشهر','القرض التقليدي','القرض المرن'])
            monthly_share=(loan_size+(interest_rate*loan_size))/12    
 #           print("monthly_share",monthly_share,start_month)
        
            num_months=12+holiday_dur+grace_dur
            loc_start_month=options_month.index(start_month)
            
            updated_loan_size=loan_size*num_months/12
            updated_monthly_intrest=updated_loan_size*interest_rate/num_months
            flexible_monthly_share=updated_monthly_intrest+(updated_loan_size/num_months)
             
            x=0
            
        #    if holiday_yn=='yes':
        #        if data["month1"]==' ' and data["month2"]==' ':
        #            holiday_txt+="but didn't pick a month! Please enter at least one month"
        
                    
                    
 #           print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',grace_yn,holiday_yn,)
            std_loan_noapprox=[]
            flexible_loan_noapprox=[]    
            if grace_yn=='no' and holiday_yn=='no':
                num_months=12
                loc_start_month=options_month.index(start_month)
                for i in range(num_months):
                    std_loan_noapprox.append(monthly_share)
                    flexible_loan_noapprox.append(monthly_share)
                
                
                if frequency=="monthly":
                    for i in range(num_months):
                        this_month=options_month_ar[(loc_start_month+i)%12]
                        new_line=[this_month,round(monthly_share,2),round(monthly_share,2)]
            
                        df.loc[i]=new_line
#                        print("???????????????,",std_loan_noapprox)
                        
  #                  print("^^^^^^^^^^^^^^^^^^^^^how much is i now?",i, std_loan_noapprox)
                    df.loc[i+1]=["------------------","------------------","------------------"]
        
                    df.loc[i+2]=["Total",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
        
                elif frequency=="biweekly":
                    for i in range(0,num_months*2,2):
                        
                        this_month=options_month_ar[(loc_start_month+int(i/2))%12]
                        new_line=[this_month+", الاسبوع التاني",0,round(monthly_share/2,2)]
                        df.loc[i]=new_line
                        
                        new_line=[this_month+", الاسبوع الرابع",round(monthly_share,2),round(monthly_share/2,2)]
                        df.loc[i+1]=new_line
                        
                    # print("^^^^^^^^^^^^^^^^^^^^^how much is i now?",i)
                    df.loc[i+2]=["------------------","------------------","------------------"]
        
                    df.loc[i+3]=["Total",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
                else:
                    for i in range(0,num_months*4,4):
                        
                        this_month=options_month_ar[(loc_start_month+int(i/4))%12]
                        new_line=[this_month+", اول اسبوع",0,round(monthly_share/4,2)]
                        df.loc[i]=new_line
                        new_line=[this_month+", تاني اسبوع",0,round(monthly_share/4,2)]
                        df.loc[i+1]=new_line
                        new_line=[this_month+", تالت اسبوع",0,round(monthly_share/4,2)]
                        df.loc[i+2]=new_line
                        new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(monthly_share/4,2)]
                        df.loc[i+3]=new_line
                        
                        
          #          print("^^^^^^^^^^^^^^^^^^^^^how much is i now?",i)
                    df.loc[i+4]=["------------------","------------------","------------------"]
        
                    df.loc[i+5]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
                    #print(df)
            elif grace_yn=='yes' and holiday_yn=='no':
                num_months=12+grace_dur
                loc_start_month=options_month.index(start_month)
                        
                updated_loan_size=loan_size*num_months/12
                updated_monthly_intrest=updated_loan_size*interest_rate/num_months
                flexible_monthly_share=updated_monthly_intrest+(updated_loan_size/num_months)
                #print(this_month,monthly_share,round(flexible_monthly_share,1))
        
                if frequency=="monthly":
        
                    for i in range(num_months):
                        this_month=options_month_ar[(loc_start_month+i)%12]
                                
                        if i in range(grace_dur):
                            new_line=[this_month,round(monthly_share,2),round(updated_monthly_intrest,2)]    
                            df.loc[i]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                        elif i>=12:
                            new_line=[this_month,0,round(flexible_monthly_share,2)]  
                            df.loc[i]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month,round(monthly_share,2),round(flexible_monthly_share,2)]    
                            df.loc[i]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                    df.loc[i+1]=["------------------","------------------","------------------"]
               
                    df.loc[i+2]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
                    # print(df)
                elif frequency=="biweekly":
                    for i in range(0,num_months*2,2):
                        
                        this_month=options_month_ar[(loc_start_month+int(i/2))%12]
                        
                        if i in range(grace_dur*2):
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/2,2)]    
                            df.loc[i+1]=new_line
        
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                        elif i>=12*2:
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/2,2)]  
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",0,round(flexible_monthly_share/2,2)]  
                            df.loc[i+1]=new_line
                            
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(flexible_monthly_share/2,2)]    
                            df.loc[i+1]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
                        
       #             print("^^^^^^^^^^^^^^^^^^^^^how much is i now?",i)
                    df.loc[i+2]=["------------------","------------------","------------------"]
        
                    df.loc[i+3]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
                
                else:#if frequency=="biweekly":
                    for i in range(0,num_months*4,4):
                        
                        this_month=options_month_ar[(loc_start_month+int(i/4))%12]
                        
                        if i in range(grace_dur*4):
                            new_line=[this_month+", اول اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/4,2)]    
                            df.loc[i+3]=new_line
        
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                        elif i>=12*4:
                            new_line=[this_month+", اول اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+3]=new_line
                            
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month+", اول اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(flexible_monthly_share/4,2)]    
                            df.loc[i+3]=new_line
                            
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
                        
       #             print("^^^^^^^^^^^^^^^^^^^^^how much is i now?",i)
                    df.loc[i+4]=["------------------","------------------","------------------"]
        
                    df.loc[i+5]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
            
                
            elif grace_yn=='no' and holiday_yn=='yes':
                num_months=12+holiday_dur
                loc_start_month=options_month.index(start_month)
                        
                updated_loan_size=loan_size*num_months/12
                updated_monthly_intrest=updated_loan_size*interest_rate/num_months
                flexible_monthly_share=updated_monthly_intrest+(updated_loan_size/num_months)
                
                
                x=0
                if frequency=="monthly":
        
                    for i in range(num_months):
                        this_month=options_month_ar[(loc_start_month+i)%12]
         #               print(i,this_month)
            
                        if this_month in holiday_months_ar and x<holiday_dur:
                            #covered=1
                            new_line=[this_month,round(monthly_share,2),round(updated_monthly_intrest,2)]    
                            df.loc[i]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                            x+=1
                        
                        elif i>=12:
                            new_line=[this_month,0,round(flexible_monthly_share,2)]  
                            df.loc[i]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month,round(monthly_share,2),round(flexible_monthly_share,2)]    
                            df.loc[i]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
                    df.loc[i+1]=["------------------","------------------","------------------"]
                    df.loc[i+2]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
                    #print(df)
                elif frequency=="biweekly":
                    for i in range(0,num_months*2,2):
                        this_month=options_month_ar[(loc_start_month+int(i/2))%12]
        
                        if this_month in holiday_months_ar and x<holiday_dur:
                            #covered=1
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/2,2)]    
                            df.loc[i+1]=new_line
                            
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                            x+=1
                        
                        elif i>=12*2:
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/2,2)]  
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",0,round(flexible_monthly_share/2,2)]  
                            df.loc[i+1]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(flexible_monthly_share/2,2)]    
                            df.loc[i+1]=new_line
            
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
                    df.loc[i+2]=["------------------","------------------","------------------"]
        
                    df.loc[i+3]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
        
                else:
                    for i in range(0,num_months*4,4):
                        this_month=options_month_ar[(loc_start_month+int(i/4))%12]
        
                        if this_month in holiday_months_ar and x<holiday_dur:
                            #covered=1
                            new_line=[this_month+", اول اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/4,2)]    
                            df.loc[i+3]=new_line
            
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                            x+=1
                        
                        elif i>=12*4:
                            new_line=[this_month+", اول اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+3]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month+", اول اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(flexible_monthly_share/4,2)]    
                            df.loc[i+3]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
                    df.loc[i+4]=["------------------","------------------","------------------"]
                    df.loc[i+5]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
        
            elif grace_yn=='yes' and holiday_yn=='yes':
                num_months=12+holiday_dur+grace_dur
                loc_start_month=options_month.index(start_month)
                
                updated_loan_size=loan_size*num_months/12
                updated_monthly_intrest=updated_loan_size*interest_rate/num_months
                flexible_monthly_share=updated_monthly_intrest+(updated_loan_size/num_months)
                 
                x=0
                if frequency=="monthly":
        
                    for i in range(num_months):
                        this_month=options_month_ar[(loc_start_month+i)%12]
                        #print(i,this_month)
            
                        if this_month in holiday_months_ar and x<holiday_dur and i not in range(grace_dur):
                            #print(this_month)
                            new_line=[this_month,round(monthly_share,2),round(updated_monthly_intrest,2)]    
                            df.loc[i]=new_line
                            
            
                            x+=1
                            if i>=12:#num_months-holiday_dur-grace_dur:
                                new_line=[this_month,0,round(updated_monthly_intrest,2)]  
                                df.loc[i]=new_line
                                std_loan_noapprox.append(0)
                                flexible_loan_noapprox.append(updated_monthly_intrest)
                            else:
                                new_line=[this_month,round(monthly_share,2),round(updated_monthly_intrest,2)]  
                                df.loc[i]=new_line
                                std_loan_noapprox.append(monthly_share)
                                flexible_loan_noapprox.append(updated_monthly_intrest)
                                
                        elif i in range(grace_dur):
                            new_line=[this_month,round(monthly_share,2),round(updated_monthly_intrest,2)]    
                            df.loc[i]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                          
                        elif i>=num_months-holiday_dur-grace_dur:
                            new_line=[this_month,0,round(flexible_monthly_share,2)]  
                            df.loc[i]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month,round(monthly_share,2),round(flexible_monthly_share,2)]    
                            df.loc[i]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                    df.loc[i+1]=["------------------","------------------","------------------"]
                    df.loc[i+2]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
                elif frequency=="biweekly":
                    for i in range(0,num_months*2,2):
                        this_month=options_month_ar[(loc_start_month+int(i/2))%12]
            
                        if this_month in holiday_months_ar and x<holiday_dur and i not in range(grace_dur*2):
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/2,2)]    
                            df.loc[i+1]=new_line
          #                  print('caseA')
                            x+=1
                            if i>=12*2:#(num_months-holiday_dur-grace_dur):
                                new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/2,2)]  
                                df.loc[i]=new_line
                                new_line=[this_month+", رابع اسبوع",0,round(updated_monthly_intrest/2,2)]  
                                df.loc[i+1]=new_line
                                std_loan_noapprox.append(0)
                                flexible_loan_noapprox.append(updated_monthly_intrest)
              #                  print('caseAA')
                            else:
                                new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/2,2)]  
                                df.loc[i]=new_line
                                new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/2,2)]  
                                df.loc[i+1]=new_line
                                std_loan_noapprox.append(monthly_share)
                                flexible_loan_noapprox.append(updated_monthly_intrest)
               #                 print('caseAA')
               #                 print('?????')
                                
                        elif i in range(grace_dur*2):
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/2,2)]    
                            df.loc[i+1]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
                  #          print('caseC')
            
                          
                        elif i>=12*2:#(num_months-holiday_dur-grace_dur)*2:
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/2,2)]  
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",0,round(flexible_monthly_share/2,2)]  
                            df.loc[i+1]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
              #              print('caseD')
            
                        else:
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/2,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(flexible_monthly_share/2,2)]    
                            df.loc[i+1]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
               #             print('caseE')
                    df.loc[i+2]=["------------------","------------------","------------------"]
                    df.loc[i+3]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
        
                else:
                    for i in range(0,num_months*4,4):
                        this_month=options_month_ar[(loc_start_month+int(i/4))%12]
            
                        if this_month in holiday_months_ar and x<holiday_dur and i not in range(grace_dur*4):
                            new_line=[this_month+", اول اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/4,2)]    
                            df.loc[i+3]=new_line
                            
                            x+=1
                            if i>=12*4:#num_months-holiday_dur-grace_dur:
                                new_line=[this_month+", اول اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i]=new_line
                                new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i+1]=new_line
                                new_line=[this_month+", تالت اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i+2]=new_line
                                new_line=[this_month+", رابع اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i+3]=new_line
                                std_loan_noapprox.append(0)
                                flexible_loan_noapprox.append(updated_monthly_intrest)
                            
                            else:
                                
                                
                                new_line=[this_month+", اول اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i]=new_line
                                new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i+1]=new_line
                                new_line=[this_month+", تالت اسبوع",0,round(updated_monthly_intrest/4,2)]  
                                df.loc[i+2]=new_line
                                new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/4,2)]  
                                df.loc[i+3]=new_line
                                
                                std_loan_noapprox.append(monthly_share)
                                flexible_loan_noapprox.append(updated_monthly_intrest)
               #                 print('caseAA')
               #                 print('?????')
                        elif i in range(grace_dur*4):
                            new_line=[this_month+", اول اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(updated_monthly_intrest/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(updated_monthly_intrest/4,2)]    
                            df.loc[i+3]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(updated_monthly_intrest)
            
                          
                        elif i>=12*4:#num_months-holiday_dur-grace_dur:
                            new_line=[this_month+", اول اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",0,round(flexible_monthly_share/4,2)]  
                            df.loc[i+3]=new_line
                            std_loan_noapprox.append(0)
                            flexible_loan_noapprox.append(flexible_monthly_share)
            
                        else:
                            new_line=[this_month+", اول اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i]=new_line
                            new_line=[this_month+", تاني اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+1]=new_line
                            new_line=[this_month+", تالت اسبوع",0,round(flexible_monthly_share/4,2)]    
                            df.loc[i+2]=new_line
                            new_line=[this_month+", رابع اسبوع",round(monthly_share,2),round(flexible_monthly_share/4,2)]    
                            df.loc[i+3]=new_line
                            std_loan_noapprox.append(monthly_share)
                            flexible_loan_noapprox.append(flexible_monthly_share)
                    df.loc[i+4]=["------------------","------------------","------------------"]
                    df.loc[i+5]=["المجموع",round(sum(std_loan_noapprox),2),round(sum(flexible_loan_noapprox),2)]
        
        
        
            # def df_style(val):
            #     return "font-weight: bold"
        
            # # get a handle on the row that starts with `"Total"`, i.e., the last row here
            # last_row = pd.IndexSlice[df.index[-1], :]
            # # and apply styling to it via the `subset` arg; first arg is styler function above
            # dfStyled = df.style.applymap(df_style, subset=last_row)
            # #display(summaryStyled)
        
            html_table_blue_light = build_table(df, 'blue_dark',padding="10px 10px 10px 10px" )
            # Save to html file
            with open('html_table_blue.html', 'w',encoding='utf-8') as f:
                f.write(html_table_blue_light)
 #           print("len(A) vs len(B)",len(a),len(b))
            if frequency=="":
                missing_info_txt="من فضلك جاوب كل الاسئلة اللي فاتت الأول"
                #thistab.clear()
 #               print("***** el mfrod el egabat na2sa 3mtan WARENI",loan_size,thistab)
                thistab.clear()

                return render_template('AB_ideal_html.html',missing_info_txt=missing_info_txt)

            elif loan_size==thistab[-1]:
#                print("***** folla WARENI",loan_size,thistab)
 #               print(a[0],"###################",b)
                thistab.clear()
                a.clear()
                b.clear()
                return render_template('result_ideal_html.html',loan_amount_txt=loan_amount_txt,start_month_txt=start_month_txt,frequency_txt=frequency_txt,grace_txt=grace_txt,holiday_txt=holiday_txt, table_final=html_table_blue_light)
        # elif loan_size==thistab[-1]:
        #     print("***** akher haga raghm en fe 3ak WARENI",loan_size,thistab)
        #     thistab.clear()

        #     a.clear()
        #     b.clear()#b.pop(-1)

        #     return render_template('result_ideal_html.html',loan_amount_txt=loan_amount_txt,start_month_txt=start_month_txt,frequency_txt=frequency_txt,grace_txt=grace_txt,holiday_txt=holiday_txt, table_final=html_table_blue_light)
        
        else:# loan_size!=thistab[0]:
   #         print("***** fe tabs mfto7a",loan_size,thistab)
            missing_amount_txt="من فضلك  اكتب مبلغ القرض و اختار ""بداية الحسابات****" 
            a.clear()
            b.clear()#b.pop(-1)
        #    print("len(A) vs len(B) in exception",len(a),len(b))
            thistab.clear()
            print("????????????????? len(A) vs len(B) in case they're not equal",len(a),a,len(b),b)

            return render_template('A_ideal_html.html',loan_size_txt_no=missing_amount_txt)


     #       print("len(A) vs len(B) in case they're not equal",len(a),a,len(b),b)

    except:
        missing_info_txt="من فضلك جاوب كل الاسئلة اللي فاتت الأول"
#        print("*****EXCEPTION el mfrod el egabat na2sa 3mtan WARENI",loan_size,thistab)

#        thistab.clear()

        a.clear()
        b.clear()#b.pop(-1)
    #    print("len(A) vs len(B) in exception",len(a),len(b))
        thistab.clear()


        return render_template('AB_ideal_html.html',missing_info_txt=missing_info_txt)
# else:
#     missing_amount_txt="من فضلك  اكتب مبلغ القرض و اختار ""بداية الحسابات" 
#     a.clear()
#     b.clear()#b.pop(-1)
#     thistab.clear()
#     print("????????????????? len(A) vs len(B) in case they're not equal",len(a),a,len(b),b)

#     return render_template('A_ideal_html.html',loan_size_txt_no=missing_amount_txt)

        

# @app.route("/",methods=['POST'])
# def home2():
#     clear 
#     return render_template('ideal_html.html')


if __name__=="__main__":
    app.run(debug=True)
