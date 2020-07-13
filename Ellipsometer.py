import math
#四步相移法取Psi與Delta
min=float(2.2250738585072014**-308)
class four_step:
    def __init__(self,I0=0,I90=0,I180=0,I270=0):
        self.I0 = I0
        self.I90 = I90
        self.I180 = I180
        self.I270 = I270
        try:
            self.I1 = float((self.I0-self.I180)/(self.I0+self.I180))
            self.I2 = float((self.I90-self.I270)/(self.I90+self.I270))
        except ZeroDivisionError:
            self.I1 = float((self.I0-self.I180)/(self.I0+self.I180+min))
            self.I2 = float((self.I90-self.I270)/(self.I90+self.I270+min))
    def delta(self):
        try:
            Delta = math.tan(self.I2/self.I1)*(180/math.pi)
        except ZeroDivisionError:
            Delta = math.tan(self.I2/(self.I1+min))*(180/math.pi)
        if Delta > 0:
            while Delta >= 360:
                Delta = Delta-360
        elif Delta < 0:
            while Delta <= 360:
                Delta = Delta+360           
        else:
            Delta = Delta 
        return Delta
    def psi(self):
        try:
            Psi = 0.5*math.asin((self.I1**2+self.I2**2)**0.5)*(180/math.pi)
        except ValueError:
            Psi = 0
        return Psi
#三步相移法取Psi與Delta
class three_step:
    def __init__(self,I45_0=0,I45_60=0,I45_120=0,I135_0=0,I135_60=0,I135_120=0):
        self.I45_0 = I45_0
        self.I45_60 = I45_60
        self.I45_120 = I45_120
        self.I135_0 = I135_0
        self.I135_60 = I135_60
        self.I135_120 = I135_120
       # self.I1 = float((self.I0-self.I180)/(self.I0+self.I180))
       # self.I2 = float((self.I90-self.I270)/(self.I90+self.I270))
    def delta(self):
        return  #math.tan(self.I2/self.I1)*(180/math.pi)
    def psi(self):
        return  #0.5*math.asin((self.I1**2+self.I2**2)**0.5)*(180/math.pi)  
    def alpha(self):
        return
    def beta(self):
        return
    