import time
time.sleep(5)


class StudentResult:
    def __init__(self,name,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9,sub10,sub11,sub12,sub13,
                 sub14,sub15,sub16,sub17,sub18,sub19,sub20,sub21,sub22,sub23,sub24,sub25,
                 sub26,sub27,sub28,sub29,sub30,sub31,sub32,sub33,sub34,sub35,sub36,sub37,
                 sub38,sub39,sub40,sub41,sub42,sub43,sub44,sub45,sub46,sub47,sub48):
        
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.sub5=sub5
        self.sub6=sub6
        self.sub7=sub7
        self.sub8=sub8
        self.sub9=sub9
        self.sub10=sub10
        self.sub11=sub11
        self.sub12=sub12
        self.sub13=sub13
        self.sub14=sub14
        self.sub15=sub15
        self.sub16=sub16
        self.sub17=sub17
        self.sub18=sub18
        self.sub19=sub19
        self.sub20=sub20
        self.sub21=sub21
        self.sub22=sub22
        self.sub23=sub23
        self.sub24=sub24
        self.sub25=sub25
        self.sub26=sub26
        self.sub27=sub27
        self.sub28=sub28
        self.sub29=sub29
        self.sub30=sub30
        self.sub31=sub31
        self.sub32=sub32
        self.sub33=sub33
        self.sub34=sub34
        self.sub35=sub35
        self.sub36=sub36
        self.sub37=sub37
        self.sub38=sub38
        self.sub39=sub39
        self.sub40=sub40
        self.sub41=sub41
        self.sub42=sub42
        self.sub43=sub43
        self.sub44=sub44
        self.sub45=sub45
        self.sub46=sub46
        self.sub47=sub47
        self.sub48=sub48
        self.name=name

        self.BTech_1st_sem_total=sub1+sub2+sub3+sub4+sub5+sub6
        self.BTech_1st_sem_avg=float(sub1+sub2+sub3+sub4+sub5+sub6)/6

        self.BTech_2nd_sem_total=sub7+sub8+sub9+sub10+sub11+sub12
        self.BTech_2nd_sem_avg=float(sub7+sub8+sub9+sub10+sub11+sub12)/6

        self.BTech_3rd_sem_total=sub13+sub14+sub15+sub16+sub17+sub18
        self.BTech_3rd_sem_avg=float(sub13+sub14+sub15+sub16+sub17+sub18)/6

        self.BTech_4th_sem_total=sub19+sub20+sub21+sub22+sub23+sub24
        self.BTech_4th_sem_avg=float(sub19+sub20+sub21+sub22+sub23+sub24)/6

        self.BTech_5th_sem_total=sub25+sub26+sub27+sub28+sub29+sub30
        self.BTech_5th_sem_avg=float(sub25+sub26+sub27+sub28+sub29+sub30)/6

        self.BTech_6th_sem_total=sub31+sub32+sub33+sub34+sub35+sub36
        self.BTech_6th_sem_avg=float(sub31+sub32+sub33+sub34+sub35+sub36)/6

        self.BTech_7th_sem_total=sub37+sub38+sub39+sub40+sub41+sub42
        self.BTech_7th_sem_avg=float(sub37+sub38+sub39+sub40+sub41+sub42)/6

        self.BTech_8th_sem_total=sub43+sub44+sub45+sub46+sub47+sub48
        self.BTech_8th_sem_avg=float(sub43+sub44+sub45+sub46+sub47+sub48)/6

        self.total_mark_in_BTech=int(sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9+sub10+sub11+sub12+sub13+
                                sub14+sub15+sub16+sub17+sub18+sub19+sub20+sub21+sub22+sub23+sub24+
                                sub25+sub26+sub27+sub28+sub29+sub30+sub31+sub32+sub33+sub34+sub35+sub36+sub37+
                                sub38+sub39+sub40+sub41+sub42+sub43+sub44+sub45+sub46+sub47+sub48)

        self.avg_percentage_in_BTech=float(sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9+sub10+sub11+sub12+sub13+
                                sub14+sub15+sub16+sub17+sub18+sub19+sub20+sub21+sub22+sub23+sub24+
                                sub25+sub26+sub27+sub28+sub29+sub30+sub31+sub32+sub33+sub34+sub35+sub36+sub37+
                                sub38+sub39+sub40+sub41+sub42+sub43+sub44+sub45+sub46+sub47+sub48)/48
        
                                      

    def BTech_1st_sem_Result_display(self):
        print ".......................This is For B.Tech 1 st Sem Result....................................."
        if(self.sub1>100 or self.sub2>100 or self.sub3>100 or self.sub4>100 or self.sub5>100 or self.sub6>100):
            if(self.sub1>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub2>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub3>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub4>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub5>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub1<30 or self.sub2<30 or self.sub3<30 or self.sub4<30 or self.sub5<30 or self.sub6<30):
            if(self.sub1<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub2<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub3<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub4<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub5<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub1>=30 and self.sub2>=30 and self.sub3>=30 and self.sub4>=30 and self.sub5>=30 and self.sub6>=30 and
              self.BTech_1st_sem_total>=480 and  self.BTech_1st_sem_total<=600):
            
            print "PHYSICS MARK--------------:",self.sub1
            print "CHEMISTRY MARK------------:",self.sub2
            print "MATHMETICS MARK-----------:",self.sub3
            print "ENGLISH MARK--------------:",self.sub4
            print "HINDI MARK----------------:",self.sub5
            print "DRAWING MARK--------------:",self.sub6
            print "Got Total Mark------------:",self.BTech_1st_sem_total
            print self.name,"Got Percentage--=",self.BTech_1st_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub1>=30 and self.sub2>=30 and self.sub3>=30 and self.sub4>=30 and self.sub5>=30 and self.sub6>=30 and
              self.BTech_1st_sem_total>=360 and  self.BTech_1st_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub1
            print "CHEMISTRY MARK------------:",self.sub2
            print "MATHMETICS MARK-----------:",self.sub3
            print "ENGLISH MARK--------------:",self.sub4
            print "HINDI MARK----------------:",self.sub5
            print "DRAWING MARK--------------:",self.sub6
            print "Got Total Mark------------:",self.BTech_1st_sem_total
            print self.name,"Got Percentage=",self.BTech_1st_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub1>=30 and self.sub2>=30 and self.sub3>=30 and self.sub4>=30 and self.sub5>=30 and self.sub6>=30 and
              self.BTech_1st_sem_total>=270 and  self.BTech_1st_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub1
            print "CHEMISTRY MARK------------:",self.sub2
            print "MATHMETICS MARK-----------:",self.sub3
            print "ENGLISH MARK--------------:",self.sub4
            print "HINDI MARK----------------:",self.sub5
            print "DRAWING MARK--------------:",self.sub6
            print "Got Total Mark------------:",self.BTech_1st_sem_total
            print self.name,"Got Percentage--=",self.BTech_1st_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub1>=30 and self.sub2>=30 and self.sub3>=30 and self.sub4>=30 and self.sub5>=30 and self.sub6>=30 and
              self.BTech_1st_sem_total>=180 and  self.BTech_1st_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub1
            print "CHEMISTRY MARK------------:",self.sub2
            print "MATHMETICS MARK-----------:",self.sub3
            print "ENGLISH MARK--------------:",self.sub4
            print "HINDI MARK----------------:",self.sub5
            print "DRAWING MARK--------------:",self.sub6
            print "Got Total Mark------------:",self.BTech_1st_sem_total
            print self.name,"Got Percentage--:",self.BTech_1st_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time."
            
            
            
    def BTech_2nd_sem_Result_display(self):
        print "....................This is for B.tech 2nd sem Result......................................"
        if(self.sub7>100 or self.sub8>100 or self.sub9>100 or self.sub10>100 or self.sub11>100 or self.sub12>100):
            if(self.sub7>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub8>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub9>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub10>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub11>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub7<30 or self.sub8<30 or self.sub9<30 or self.sub10<30 or self.sub11<30 or self.sub12<30):
            if(self.sub7<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub8<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub9<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub10<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub11<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub7>=30 and self.sub8>=30 and self.sub9>=30 and self.sub10>=30 and self.sub11>=30 and self.sub12>=30 and
              self.BTech_2nd_sem_total>=480 and  self.BTech_2nd_sem_total<=600):
            
            print "PHYSICS MARK--------------:",self.sub7
            print "CHEMISTRY MARK------------:",self.sub8
            print "MATHMETICS MARK-----------:",self.sub9
            print "ENGLISH MARK--------------:",self.sub10
            print "HINDI MARK----------------:",self.sub11
            print "DRAWING MARK--------------:",self.sub12
            print "Got Total Mark------------:",self.BTech_2nd_sem_total
            print self.name,"Got Percentage=",self.BTech_2nd_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub7>=30 and self.sub8>=30 and self.sub9>=30 and self.sub10>=30 and self.sub11>=30 and self.sub12>=30 and
             self.BTech_2nd_sem_total>=360 and  self.BTech_2nd_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub7
            print "CHEMISTRY MARK------------:",self.sub8
            print "MATHMETICS MARK-----------:",self.sub9
            print "ENGLISH MARK--------------:",self.sub10
            print "HINDI MARK----------------:",self.sub11
            print "DRAWING MARK--------------:",self.sub12
            print "Got Total Mark------------:",self.BTech_2nd_sem_total
            print self.name,"Got Percentage=",self.BTech_2nd_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub7>=30 and self.sub8>=30 and self.sub9>=30 and self.sub10>=30 and self.sub11>=30 and self.sub12>=30 and
              self.BTech_2nd_sem_total>=270 and  self.BTech_2nd_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub7
            print "CHEMISTRY MARK------------:",self.sub8
            print "MATHMETICS MARK-----------:",self.sub9
            print "ENGLISH MARK--------------:",self.sub10
            print "HINDI MARK----------------:",self.sub11
            print "DRAWING MARK--------------:",self.sub12
            print self.name,"Got Total Mark=",self.BTech_2nd_sem_total
            print self.name,"Got Percentage=",self.BTech_2nd_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub7>=30 and self.sub8>=30 and self.sub9>=30 and self.sub10>=30 and self.sub11>=30 and self.sub12>=30 and
              self.BTech_2nd_sem_total>=180 and  self.BTech_2nd_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub7
            print "CHEMISTRY MARK------------:",self.sub8
            print "MATHMETICS MARK-----------:",self.sub9
            print "ENGLISH MARK--------------:",self.sub10
            print "HINDI MARK----------------:",self.sub11
            print "DRAWING MARK--------------:",self.sub12
            print self.name,"Got Total Mark=",self.BTech_2nd_sem_total
            print self.name,"Got Percentage=",self.BTech_2nd_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time." 
            
            
            
    def BTech_3rd_sem_Result_display(self):
        print "....................This is for B.tech 3rd sem Result......................................"
        if(self.sub13>100 or self.sub14>100 or self.sub15>100 or self.sub16>100 or self.sub17>100 or self.sub18>100):
            if(self.sub13>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub14>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub15>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub16>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub17>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub13<30 or self.sub14<30 or self.sub15<30 or self.sub16<30 or self.sub17<30 or self.sub18<30):
            if(self.sub13<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub14<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub15<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub16<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub17<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub13>=30 and self.sub14>=30 and self.sub15>=30 and self.sub16>=30 and self.sub17>=30 and self.sub18>=30 and
              self.BTech_3rd_sem_total>=480 and  self.BTech_3rd_sem_total<=600):
            print "PHYSICS MARK--------------:",self.sub13
            print "CHEMISTRY MARK------------:",self.sub14
            print "MATHMETICS MARK-----------:",self.sub15
            print "ENGLISH MARK--------------:",self.sub16
            print "HINDI MARK----------------:",self.sub17
            print "DRAWING MARK--------------:",self.sub18
            print self.name,"Got Total Mark=",self.BTech_3rd_sem_total
            print self.name,"Got Percentage=",self.BTech_3rd_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub13>=30 and self.sub14>=30 and self.sub15>=30 and self.sub16>=30 and self.sub17>=30 and self.sub18>=30 and
             self.BTech_3rd_sem_total>=360 and  self.BTech_3rd_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub13
            print "CHEMISTRY MARK------------:",self.sub14
            print "MATHMETICS MARK-----------:",self.sub15
            print "ENGLISH MARK--------------:",self.sub16
            print "HINDI MARK----------------:",self.sub17
            print "DRAWING MARK--------------:",self.sub18
            print self.name,"Got Total Mark=",self.BTech_3rd_sem_total
            print self.name,"Got Percentage=",self.BTech_3rd_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub13>=30 and self.sub14>=30 and self.sub15>=30 and self.sub16>=30 and self.sub17>=30 and self.sub18>=30 and
              self.BTech_2nd_sem_total>=270 and  self.BTech_2nd_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub13
            print "CHEMISTRY MARK------------:",self.sub14
            print "MATHMETICS MARK-----------:",self.sub15
            print "ENGLISH MARK--------------:",self.sub16
            print "HINDI MARK----------------:",self.sub17
            print "DRAWING MARK--------------:",self.sub18
            print self.name,"Got Total Mark=",self.BTech_2nd_sem_total
            print self.name,"Got Percentage=",self.BTech_2nd_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub13>=30 and self.sub14>=30 and self.sub15>=30 and self.sub16>=30 and self.sub17>=30 and self.sub18>=30 and
              self.BTech_2nd_sem_total>=180 and  self.BTech_2nd_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub13
            print "CHEMISTRY MARK------------:",self.sub14
            print "MATHMETICS MARK-----------:",self.sub15
            print "ENGLISH MARK--------------:",self.sub16
            print "HINDI MARK----------------:",self.sub17
            print "DRAWING MARK--------------:",self.sub18
            print self.name,"Got Total Mark=",self.BTech_2nd_sem_total
            print self.name,"Got Percentage=",self.BTech_2nd_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time."  
            
            
            
    def BTech_4th_sem_Result_display(self):
        print "....................This is for B.tech 4th sem Result......................................"
        if(self.sub19>100 or self.sub20>100 or self.sub21>100 or self.sub22>100 or self.sub23>100 or self.sub24>100):
            if(self.sub19>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub20>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub21>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub22>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub23>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub19<30 or self.sub20<30 or self.sub21<30 or self.sub22<30 or self.sub23<30 or self.sub24<30):
            if(self.sub19<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub20<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub21<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub22<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub23<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub19>=30 and self.sub20>=30 and self.sub21>=30 and self.sub22>=30 and self.sub23>=30 and self.sub24>=30 and
              self.BTech_4th_sem_total>=480 and  self.BTech_4th_sem_total<=600):
            print "PHYSICS MARK--------------:",self.sub19
            print "CHEMISTRY MARK------------:",self.sub20
            print "MATHMETICS MARK-----------:",self.sub21
            print "ENGLISH MARK--------------:",self.sub22
            print "HINDI MARK----------------:",self.sub23
            print "DRAWING MARK--------------:",self.sub24
            print self.name,"Got Total Mark=",self.BTech_4th_sem_total
            print self.name,"Got Percentage=",self.BTech_4th_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub19>=30 and self.sub20>=30 and self.sub21>=30 and self.sub22>=30 and self.sub23>=30 and self.sub24>=30 and
             self.BTech_4th_sem_total>=360 and  self.BTech_4th_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub19
            print "CHEMISTRY MARK------------:",self.sub20
            print "MATHMETICS MARK-----------:",self.sub21
            print "ENGLISH MARK--------------:",self.sub22
            print "HINDI MARK----------------:",self.sub23
            print "DRAWING MARK--------------:",self.sub24
            print self.name,"Got Total Mark=",self.BTech_4th_sem_total
            print self.name,"Got Percentage=",self.BTech_4th_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub19>=30 and self.sub20>=30 and self.sub21>=30 and self.sub22>=30 and self.sub23>=30 and self.sub24>=30 and
              self.BTech_4th_sem_total>=270 and  self.BTech_4th_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub19
            print "CHEMISTRY MARK------------:",self.sub20
            print "MATHMETICS MARK-----------:",self.sub21
            print "ENGLISH MARK--------------:",self.sub22
            print "HINDI MARK----------------:",self.sub23
            print "DRAWING MARK--------------:",self.sub24
            print self.name,"Got Total Mark=",self.BTech_4th_sem_total
            print self.name,"Got Percentage=",self.BTech_4th_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub19>=30 and self.sub20>=30 and self.sub21>=30 and self.sub22>=30 and self.sub23>=30 and self.sub24>=30 and
              self.BTech_4th_sem_total>=180 and  self.BTech_4th_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub19
            print "CHEMISTRY MARK------------:",self.sub20
            print "MATHMETICS MARK-----------:",self.sub21
            print "ENGLISH MARK--------------:",self.sub22
            print "HINDI MARK----------------:",self.sub23
            print "DRAWING MARK--------------:",self.sub24
            print self.name,"Got Total Mark=",self.BTech_4th_sem_total
            print self.name,"Got Percentage=",self.BTech_4th_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time." 
            
            
            
    def BTech_5th_sem_Result_display(self):
        print "....................This is for B.tech 5th sem Result......................................"
        if(self.sub25>100 or self.sub26>100 or self.sub27>100 or self.sub28>100 or self.sub29>100 or self.sub30>100):
            if(self.sub25>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub26>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub27>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub28>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub29>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub25<30 or self.sub26<30 or self.sub27<30 or self.sub28<30 or self.sub29<30 or self.sub30<30):
            if(self.sub25<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub26<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub27<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub28<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub29<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub25>=30 and self.sub26>=30 and self.sub27>=30 and self.sub28>=30 and self.sub29>=30 and self.sub30>=30 and
              self.BTech_5th_sem_total>=480 and  self.BTech_5th_sem_total<=600):
            print "PHYSICS MARK--------------:",self.sub25
            print "CHEMISTRY MARK------------:",self.sub26
            print "MATHMETICS MARK-----------:",self.sub27
            print "ENGLISH MARK--------------:",self.sub28
            print "HINDI MARK----------------:",self.sub29
            print "DRAWING MARK--------------:",self.sub30
            print self.name,"Got Total Mark=",self.BTech_5th_sem_total
            print self.name,"Got Percentage=",self.BTech_5th_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub25>=30 and self.sub26>=30 and self.sub27>=30 and self.sub28>=30 and self.sub29>=30 and self.sub30>=30 and
             self.BTech_5th_sem_total>=360 and  self.BTech_5th_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub25
            print "CHEMISTRY MARK------------:",self.sub26
            print "MATHMETICS MARK-----------:",self.sub27
            print "ENGLISH MARK--------------:",self.sub28
            print "HINDI MARK----------------:",self.sub29
            print "DRAWING MARK--------------:",self.sub30
            
            print self.name,"Got Total Mark=",self.BTech_5th_sem_total
            print self.name,"Got Percentage=",self.BTech_5th_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub25>=30 and self.sub26>=30 and self.sub27>=30 and self.sub28>=30 and self.sub29>=30 and self.sub30>=30 and
              self.BTech_5th_sem_total>=270 and  self.BTech_5th_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub25
            print "CHEMISTRY MARK------------:",self.sub26
            print "MATHMETICS MARK-----------:",self.sub27
            print "ENGLISH MARK--------------:",self.sub28
            print "HINDI MARK----------------:",self.sub29
            print "DRAWING MARK--------------:",self.sub30
            
            print self.name,"Got Total Mark=",self.BTech_5th_sem_total
            print self.name,"Got Percentage=",self.BTech_5th_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub25>=30 and self.sub26>=30 and self.sub27>=30 and self.sub28>=30 and self.sub29>=30 and self.sub30>=30 and
              self.BTech_5th_sem_total>=180 and  self.BTech_5th_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub25
            print "CHEMISTRY MARK------------:",self.sub26
            print "MATHMETICS MARK-----------:",self.sub27
            print "ENGLISH MARK--------------:",self.sub28
            print "HINDI MARK----------------:",self.sub29
            print "DRAWING MARK--------------:",self.sub30
           
            print self.name,"Got Total Mark=",self.BTech_5th_sem_total
            print self.name,"Got Percentage=",self.BTech_5th_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time." 
            
            
    def BTech_6th_sem_Result_display(self):
        print "....................This is for B.tech 6th sem Result......................................"
        if(self.sub31>100 or self.sub32>100 or self.sub33>100 or self.sub34>100 or self.sub35>100 or self.sub36>100):
            if(self.sub31>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub32>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub33>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub34>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub35>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub31<30 or self.sub32<30 or self.sub33<30 or self.sub34<30 or self.sub35<30 or self.sub36<30):
            if(self.sub31<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub32<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub33<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub34<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub35<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub31>=30 and self.sub32>=30 and self.sub33>=30 and self.sub34>=30 and self.sub35>=30 and self.sub36>=30 and
              self.BTech_6th_sem_total>=480 and  self.BTech_6th_sem_total<=600):
            print "PHYSICS MARK--------------:",self.sub31
            print "CHEMISTRY MARK------------:",self.sub32
            print "MATHMETICS MARK-----------:",self.sub33
            print "ENGLISH MARK--------------:",self.sub34
            print "HINDI MARK----------------:",self.sub35
            print "DRAWING MARK--------------:",self.sub36
            
            
            print self.name,"Got Total Mark=",self.BTech_6th_sem_total
            print self.name,"Got Percentage=",self.BTech_6th_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub31>=30 and self.sub32>=30 and self.sub33>=30 and self.sub34>=30 and self.sub35>=30 and self.sub36>=30 and
             self.BTech_6th_sem_total>=360 and  self.BTech_6th_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub31
            print "CHEMISTRY MARK------------:",self.sub32
            print "MATHMETICS MARK-----------:",self.sub33
            print "ENGLISH MARK--------------:",self.sub34
            print "HINDI MARK----------------:",self.sub35
            print "DRAWING MARK--------------:",self.sub36
            
            print self.name,"Got Total Mark=",self.BTech_6th_sem_total
            print self.name,"Got Percentage=",self.BTech_6th_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub31>=30 and self.sub32>=30 and self.sub33>=30 and self.sub34>=30 and self.sub35>=30 and self.sub36>=30 and
              self.BTech_6th_sem_total>=270 and  self.BTech_6th_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub31
            print "CHEMISTRY MARK------------:",self.sub32
            print "MATHMETICS MARK-----------:",self.sub33
            print "ENGLISH MARK--------------:",self.sub34
            print "HINDI MARK----------------:",self.sub35
            print "DRAWING MARK--------------:",self.sub36
           
            print self.name,"Got Total Mark=",self.BTech_6th_sem_total
            print self.name,"Got Percentage=",self.BTech_6th_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub31>=30 and self.sub32>=30 and self.sub33>=30 and self.sub34>=30 and self.sub35>=30 and self.sub36>=30 and
              self.BTech_6th_sem_total>=180 and  self.BTech_6th_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub31
            print "CHEMISTRY MARK------------:",self.sub32
            print "MATHMETICS MARK-----------:",self.sub33
            print "ENGLISH MARK--------------:",self.sub34
            print "HINDI MARK----------------:",self.sub35
            print "DRAWING MARK--------------:",self.sub36
           
            print self.name,"Got Total Mark=",self.BTech_6th_sem_total
            print self.name,"Got Percentage=",self.BTech_6th_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time." 
            
            
            
            
            
    def BTech_7th_sem_Result_display(self):
        print "....................This is for B.tech 7th sem Result......................................"
        if(self.sub37>100 or self.sub38>100 or self.sub39>100 or self.sub40>100 or self.sub41>100 or self.sub42>100):
            if(self.sub37>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub38>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub39>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub40>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub41>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub37<30 or self.sub38<30 or self.sub39<30 or self.sub40<30 or self.sub41<30 or self.sub42<30):
            if(self.sub37<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub38<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub39<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub40<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub41<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub37>=30 and self.sub38>=30 and self.sub39>=30 and self.sub40>=30 and self.sub41>=30 and self.sub42>=30 and
              self.BTech_7th_sem_total>=480 and  self.BTech_7th_sem_total<=600):
            print "PHYSICS MARK--------------:",self.sub37
            print "CHEMISTRY MARK------------:",self.sub38
            print "MATHMETICS MARK-----------:",self.sub39
            print "ENGLISH MARK--------------:",self.sub40
            print "HINDI MARK----------------:",self.sub41
            print "DRAWING MARK--------------:",self.sub42
            
            
            print self.name,"Got Total Mark=",self.BTech_7th_sem_total
            print self.name,"Got Percentage=",self.BTech_7th_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub37>=30 and self.sub38>=30 and self.sub39>=30 and self.sub40>=30 and self.sub41>=30 and self.sub42>=30 and
             self.BTech_7th_sem_total>=360 and  self.BTech_7th_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub37
            print "CHEMISTRY MARK------------:",self.sub38
            print "MATHMETICS MARK-----------:",self.sub39
            print "ENGLISH MARK--------------:",self.sub40
            print "HINDI MARK----------------:",self.sub41
            print "DRAWING MARK--------------:",self.sub42
            
            print self.name,"Got Total Mark=",self.BTech_7th_sem_total
            print self.name,"Got Percentage=",self.BTech_7th_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub37>=30 and self.sub38>=30 and self.sub39>=30 and self.sub40>=30 and self.sub41>=30 and self.sub42>=30 and
              self.BTech_7th_sem_total>=270 and  self.BTech_7th_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub37
            print "CHEMISTRY MARK------------:",self.sub38
            print "MATHMETICS MARK-----------:",self.sub39
            print "ENGLISH MARK--------------:",self.sub40
            print "HINDI MARK----------------:",self.sub41
            print "DRAWING MARK--------------:",self.sub42
            
            print self.name,"Got Total Mark=",self.BTech_7th_sem_total
            print self.name,"Got Percentage=",self.BTech_7th_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub37>=30 and self.sub38>=30 and self.sub39>=30 and self.sub40>=30 and self.sub41>=30 and self.sub42>=30 and
              self.BTech_7th_sem_total>=180 and  self.BTech_7th_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub37
            print "CHEMISTRY MARK------------:",self.sub38
            print "MATHMETICS MARK-----------:",self.sub39
            print "ENGLISH MARK--------------:",self.sub40
            print "HINDI MARK----------------:",self.sub41
            print "DRAWING MARK--------------:",self.sub42
            
            print self.name,"Got Total Mark=",self.BTech_7th_sem_total
            print self.name,"Got Percentage=",self.BTech_7th_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time." 
            
            
            
            
    def BTech_8th_sem_Result_display(self):
        print "....................This is for B.tech 8th sem Result......................................"
        if(self.sub43>100 or self.sub44>100 or self.sub45>100 or self.sub46>100 or self.sub47>100 or self.sub48>100):
            if(self.sub43>100):
                print "Sub1 Mark is not Valid please Enter Valid Mark"
            if(self.sub44>100):
                print "Sub2 Mark is Not Valid Please Enter Valid Mark"
            if(self.sub45>100):
                print "Sub3 Mark is not Valid Please Enter Valid Mark"
            if(self.sub46>100):
                print "Sub4 Mark is not Valid Please Enter Valid Mark"
            if(self.sub47>100):
                print "Sub5 Mark is not Valid Please Enter Valid Mark"
            else:
                print "Sub6 Mark is not Valid please Enter Valid Mark"

        elif(self.sub43<30 or self.sub44<30 or self.sub45<30 or self.sub46<30 or self.sub47<30 or self.sub48<30):
            if(self.sub43<30):
                print self.name,"is Failed in Sub1","....backlog...."
            if(self.sub44<30):
                print self.name,"is Failed in Sub2","....backlog...."
            if(self.sub45<30):
                print self.name,"is Failed in Sub3","....backlog...."
            if(self.sub46<30):
                print self.name,"is Failed in Sub4","....backlog...."
            if(self.sub47<30):
                print self.name,"is Failed in Sub5","....backlog...."
            else:
                print self.name,"is Failed in Sub6","....backlog...."

        elif(self.sub43>=30 and self.sub44>=30 and self.sub45>=30 and self.sub46>=30 and self.sub47>=30 and self.sub48>=30 and
              self.BTech_8th_sem_total>=480 and  self.BTech_8th_sem_total<=600):
            print "PHYSICS MARK--------------:",self.sub43
            print "CHEMISTRY MARK------------:",self.sub44
            print "MATHMETICS MARK-----------:",self.sub45
            print "ENGLISH MARK--------------:",self.sub46
            print "HINDI MARK----------------:",self.sub47
            print "DRAWING MARK--------------:",self.sub48
            
            
            print self.name,"Got Total Mark=",self.BTech_8th_sem_total
            print self.name,"Got Percentage=",self.BTech_8th_sem_avg
            print "Congrats",self.name,"is Passed First Class with Distinction."

        elif(self.sub43>=30 and self.sub44>=30 and self.sub45>=30 and self.sub46>=30 and self.sub47>=30 and self.sub48>=30 and
             self.BTech_8th_sem_total>=360 and  self.BTech_8th_sem_total<=480):
            print "PHYSICS MARK--------------:",self.sub43
            print "CHEMISTRY MARK------------:",self.sub44
            print "MATHMETICS MARK-----------:",self.sub45
            print "ENGLISH MARK--------------:",self.sub46
            print "HINDI MARK----------------:",self.sub47
            print "DRAWING MARK--------------:",self.sub48
            
            print self.name,"Got Total Mark=",self.BTech_8th_sem_total
            print self.name,"Got Percentage=",self.BTech_8th_sem_avg
            print "Congrats",self.name,"is Passed with First Class."

        elif(self.sub43>=30 and self.sub44>=30 and self.sub45>=30 and self.sub46>=30 and self.sub47>=30 and self.sub48>=30 and
              self.BTech_8th_sem_total>=270 and  self.BTech_8th_sem_total<=360):
            print "PHYSICS MARK--------------:",self.sub43
            print "CHEMISTRY MARK------------:",self.sub44
            print "MATHMETICS MARK-----------:",self.sub45
            print "ENGLISH MARK--------------:",self.sub46
            print "HINDI MARK----------------:",self.sub47
            print "DRAWING MARK--------------:",self.sub48
            
            print self.name,"Got Total Mark=",self.BTech_8th_sem_total
            print self.name,"Got Percentage=",self.BTech_8th_sem_avg
            print self.name,"is Passed  with 2nd Division."

        elif(self.sub43>=30 and self.sub44>=30 and self.sub45>=30 and self.sub46>=30 and self.sub47>=30 and self.sub48>=30 and
              self.BTech_8th_sem_total>=180 and  self.BTech_8th_sem_total<=270):
            print "PHYSICS MARK--------------:",self.sub43
            print "CHEMISTRY MARK------------:",self.sub44
            print "MATHMETICS MARK-----------:",self.sub45
            print "ENGLISH MARK--------------:",self.sub46
            print "HINDI MARK----------------:",self.sub47
            print "DRAWING MARK--------------:",self.sub48
            
            print self.name,"Got Total Mark=",self.BTech_8th_sem_total
            print self.name,"Got Percentage=",self.BTech_8th_sem_avg
            print self.name,"is Passed  with 3rd Division."

        else:
            print "Opps !",self.name,"is Failed"
            print "Best of Luck for Next Time."


    def BTech_all_sem_Result_display(self):
        if(self.total_mark_in_BTech>=3840 and self.total_mark_in_BTech<=4800):
            print "___________________________________________________________"

            print "Total Mark in B.Tech:",self.total_mark_in_BTech
            print "Average Percentage In B.Tech:",self.avg_percentage_in_BTech
            print self.name,"Congrates you passed with Distinction"
        
        elif(self.total_mark_in_BTech>=2880 and self.total_mark_in_BTech<=3840):
            print "___________________________________________________________"

            print "Total Mark in B.Tech:",self.total_mark_in_BTech
            print "Average Percentage In B.Tech:",self.avg_percentage_in_BTech
            print self.name,"Congrates you passed with First Class"
            
        elif(self.total_mark_in_BTech>=2160 and self.total_mark_in_BTech<=2880):
            print "___________________________________________________________"

            print "Total Mark in B.Tech:",self.total_mark_in_BTech
            print "Average Percentage In B.Tech:",self.avg_percentage_in_BTech
            print self.name," you passed with Second Class"
            
            
        elif(self.total_mark_in_BTech>=1440 and self.total_mark_in_BTech<=2160):
            print "___________________________________________________________"

            print "Total Mark in B.Tech:",self.total_mark_in_BTech
            print "Average Percentage In B.Tech:",self.avg_percentage_in_BTech
            print self.name," you passed with Third Class"
            
        else:
            print "___________________________________________________________"

            print "Total Mark in B.Tech:",self.total_mark_in_BTech
            print "Average Percentage In B.Tech:",self.avg_percentage_in_BTech
            print "Failed"
            print  "Oops !",self.name,"best of Luck next Time"
            
            
            
    
            
            
            
     
            
            
            
        
            
            
Stu_1=StudentResult("Moshabbar",67,78,45,89,56,18,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_2=StudentResult("Irshad",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_3=StudentResult("Rahul",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_4=StudentResult("Ashu",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_5=StudentResult("Moinul",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_6=StudentResult("Resmi",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_7=StudentResult("Ameer",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)
Stu_8=StudentResult("Priya",67,78,45,89,56,78,56,78,56,90,56,45,67,74,89,68,75,56,34,90,56,34,78,90,45,67,89,90,45,34,56,89,45,67,67,78,89,
                    67,34,78,67,34,78,67,34,90,56,67)

choice = 0
#while loop == 1:
    #print what options you have
print "........................................Welcome to Your B.Tech Result Portal site....................................."
print "This is a B.Tech Result poratl for all semistar if student will failed any one subject that semistar result will display Failed..."

print "your options are:Which semistar result you want"
print " "
print "1) BTech_1st_sem_Result_display"
print "2) BTech_2nd_sem_Result_display"

print "3) BTech_3rd_sem_Result_display"

print "4) BTech_4th_sem_Result_display"
print "5) BTech_5th_sem_Result_display"
print "6) BTech_6th_sem_Result_display"
print "7) BTech_7th_sem_Result_display"
print "8) BTech_8th_sem_Result_display"
print "9)B.Tech_all_sem_Result_Display"
print" "

choice=int(input("Enter your result option:"))
if choice==1:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==2:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==3:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==4:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==5:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==6:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==7:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==8:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
if choice==9:
    name=raw_input("Enter Your Name:")
    if(name=="Moshabbar" or name=="Irshad" or name=="Ashu" or name=="Rahul" or name=="Resmi" or name=="Priya" or name=="Ameer" or name=="Moinul"):
        if(name=="Moshabbar"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_1.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_1.BTech_8th_sem_Result_display()

            print Stu_1.BTech_all_sem_Result_display()
            
        elif(name=="Irshad"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_2.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_2.BTech_8th_sem_Result_display()

            print Stu_2.BTech_all_sem_Result_display()

           
            
            
        elif(name=="Rahul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_3.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_3.BTech_8th_sem_Result_display()

            print Stu_3.BTech_all_sem_Result_display()

            
            
        
        
        elif(name=="Ashu"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_4.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_4.BTech_8th_sem_Result_display()

            print Stu_4.BTech_all_sem_Result_display()

           
            
            
        elif(name=="Moinul"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_5.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_5.BTech_8th_sem_Result_display()

            print Stu_5.BTech_all_sem_Result_display()

            
            
            
            
        elif(name=="Resmi"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_6.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_6.BTech_8th_sem_Result_display()

            print Stu_6.BTech_all_sem_Result_display()

            
            
        elif(name=="Ameer"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_7.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_7.BTech_8th_sem_Result_display()

            print Stu_7.BTech_all_sem_Result_display()

            
            
            
        elif(name=="Priya"):
            print "Your Result is searching please wait......"
            time.sleep(5)
            print Stu_8.BTech_1st_sem_Result_display()
            print "B.tech 2nd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_2nd_sem_Result_display()
            print "B.tech 3rd sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_3rd_sem_Result_display()
            print "B.tech 4th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_4th_sem_Result_display()
            print "B.tech 5th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_5th_sem_Result_display()
            print "B.tech 6th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_6th_sem_Result_display()
            print "B.tech 7th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_7th_sem_Result_display()
            print "B.tech 8th sem Result is printing please wait...."
            time.sleep(2)
            print Stu_8.BTech_8th_sem_Result_display()

            print Stu_8.BTech_all_sem_Result_display()
           
                
    else:
        print "Please Enter a valid Name your name is not Valid"
        
        
        
    

    




    

    
 
    
    

    

    
   
        
    
#Stu_1.BTech_1st_sem_Result_display()
#Stu_1.BTech_2nd_sem_Result_display()
#Stu_1.BTech_3rd_sem_Result_display()
#Stu_1.BTech_4th_sem_Result_display()
#Stu_1.BTech_5th_sem_Result_display()
#Stu_1.BTech_6th_sem_Result_display()
#Stu_1.BTech_7th_sem_Result_display()
#Stu_1.BTech_8th_sem_Result_display()


                 
        
