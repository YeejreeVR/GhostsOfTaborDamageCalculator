import customtkinter as tk
import math
FMJdam0 = [50.5, 41.0, 47.3, 46.5, 42.9, 48.6, 47.6, 43.6, 39.8, 74.6, 46.2, 44.9, 46.9, 69, 43.6, 41, 41.9, 49, 49, 49, 48.6, 31.9, 36.5, 41.1, 29.5, 33.9, 34.6, 28.0, 34.5, 37.4, 37.4, 42.3, 37.4, 39.7, 31.3, 38.8, 45.3, 45.3, 47.0, 36.5, 41.8, 41.8, 87, 34.2, 35.3, 35.3, 42.4, 31, 15, 35.9, 121.3, 81.4, 62.6, 94.9, 215.7, 81.4, 67.3, 78.3]
FMJdam1 = [42.9, 34.9, 40.2, 39.5, 36.5, 41.3, 40.5, 37.1, 33.8, 63.4, 39.3, 38.2, 39.9, 58.7, 37.1, 34.9, 35.6, 41.7, 41.7, 41.7, 41.3, 14.4, 16.4, 22.2, 13.3, 15.3, 15.6, 12.6, 15.5, 16.8, 16.8, 28.6, 16.8, 26.8, 14.1, 26.2, 20.4, 20.4, 21.2, 16.4, 18.8, 18.8, 58.7, 23.1, 15.9, 15.9, 19.1, 14.0, 6.8, 24.2, 103.1, 69.2, 53.2, 80.7, 183.3, 69.2, 57.2, 66.6]
FMJdam2 = [32.8, 26.7, 30.7, 30.2, 27.9, 31.6, 30.9, 28.3, 25.9, 63.4, 30.0, 29.2, 30.5, 58.7, 28.3, 26.7, 27.2, 31.9, 31.9, 31.9, 31.6, 11.2, 12.8, 14.4, 10.3, 11.9, 12.1, 9.8, 12.1, 13.1, 13.1, 20.5, 13.1, 19.3, 11.0, 18.8, 15.9, 15.9, 16.5, 12.8, 14.6, 14.6, 30.5, 16.6, 12.4, 12.4, 14.8, 10.9, 5.3, 17.4, 103.1, 69.2, 53.2, 80.7, 183.3, 69.2, 57.2, 66.6]
FMJdam3 = [21.7, 17.6, 20.3, 20.0, 18.4, 20.9, 20.5, 18.7, 17.1, 63.4, 19.9, 19.3, 20.2, 58.7, 18.7, 17.6, 18.0, 21.1, 21.1, 21.1, 20.9, 8.0, 9.1, 10.3, 7.4, 8.5, 8.7, 7.0, 8.6, 9.4, 9.4, 10.6, 9.4, 9.9, 7.8, 9.7, 11.3, 11.3, 11.8, 9.1, 10.5, 10.5, 21.8, 8.6, 8.8, 8.8, 10.6, 7.8, 3.8, 9.0, 103.1, 69.2, 53.2, 80.7, 183.3, 69.2, 57.2, 66.6]
FMJdam4 = [9.6, 7.8, 9.0, 8.8, 8.2, 9.2, 9.0, 8.3, 7.6, 44.8, 8.8, 8.5, 8.9, 41.4, 8.3, 7.8, 8.0, 9.3, 9.3, 9.3, 9.2, 4.8, 5.5, 6.2, 4.4, 5.1, 5.2, 4.2, 5.2, 5.6, 5.6, 6.3, 5.6, 6.0, 4.7, 5.8, 6.8, 6.8, 7.1, 5.5, 6.3, 6.3, 13.1, 5.1, 5.3, 5.3, 6.4, 4.7, 2.3, 5.4, 103.1, 48.8, 37.6, 56.9, 183.3, 48.8, 40.4, 47.0]
FMJdam5 = [5.1, 4.1, 4.7, 4.7, 4.3, 4.9, 4.8, 4.4, 4.0, 25.9, 4.6, 4.5, 4.7, 24.0, 4.4, 4.1, 4.2, 4.9, 4.9, 4.9, 4.9, 3.2, 3.7, 4.1, 3.0, 3.4, 3.5, 2.8, 3.5, 3.7, 3.7, 4.2, 3.7, 4.0, 3.1, 3.9, 4.5, 4.5, 4.7, 3.7, 4.2, 4.2, 8.7, 3.4, 3.5, 3.5, 4.2, 3.1, 1.5, 3.6, 103.1, 28.3, 21.8, 33.0, 183.3, 28.3, 23.4, 27.2]
FMJdam6 = [3.5, 2.9, 3.3, 3.3, 3.0, 3.4, 3.3, 3.1, 2.8, 8.8, 3.2, 3.1, 3.3, 4.8, 3.1, 2.9, 2.9, 3.4, 3.4, 3.4, 3.4, 2.2, 2.6, 2.9, 2.1, 2.4, 2.4, 2.0, 2.4, 2.6, 2.6, 3.0, 2.6, 2.8, 2.2, 2.7, 3.2, 3.2, 3.3, 2.6, 2.6, 2.6, 6.1, 2.4, 2.5, 2.5, 3.0, 2.2, 1.1, 2.5, 103.1, 9.6, 7.4, 11.2, 183.3, 9.6, 7.9, 9.2]

APdam0 = [60.1, 44.4, 49.6, 55.1, 44.9, 51.8, 51.7, 47.2, 43.0, 80.8, 50.2, 48.7, 50.9, 74.5, 47.2, 44.4, 45.3, 58.2, 58.2, 53.4, 51.8 ,33.5, 38.7, 42.0, 30.7, 35.8, 36.5, 29.5, 36.4, 39.7, 39.7, 42.3, 39.7, 44.2, 32.9, 40.1, 53.5, 53.5, 57.0, 38.7, 48.3, 48.3, 114.5, 37.4, 37.3, 37.3, 49.2, 32.5, 15.4, 37.0, 143.1, 86.2, 65.3, 103.0, 0, 86.2, 70.3, 78.3]
APdam1 = [51.1, 37.7, 42.2, 46.8, 38.2, 44.0, 43.9, 40.1, 36.6, 68.7, 42.7, 41.4, 43.3, 63.3, 40.1, 37.7, 38.5, 49.5, 49.5, 45.4, 44.0, 28.5, 32.9, 35.7, 26.1, 30.4, 31.0, 25.1, 30.9, 33.7, 33.7, 36.0, 33.7, 37.6, 28.0, 34.1, 45.5, 45.5, 48.5, 32.9, 41.1, 41.1, 97.3, 31.8, 31.7, 31.7, 41.8, 27.6, 13.1, 31.5, 121.6, 73.3, 55.5, 87.6, 0, 73.3, 59.8, 66.6]
APdam2 = [51.1, 37.7, 42.2, 46.8, 38.2, 44.0, 43.9, 40.1, 36.6, 68.7, 42.7, 41.4, 43.3, 63.3, 40.1, 37.7, 38.5, 49.5, 49.5, 45.4, 44.0, 28.5, 32.9, 35.7, 26.1, 30.4, 31.0, 25.1, 30.9, 33.7, 33.7, 36.0, 33.7, 37.6, 28.0, 34.1, 45.5, 45.5, 48.5, 32.9, 41.1, 41.1, 97.3, 31.8, 31.7, 31.7, 41.8, 27.6, 13.1, 31.5, 121.6, 73.3, 55.5, 87.6, 0, 73.3, 59.8, 66.6]
APdam3 = [51.1, 37.7, 42.2, 46.8, 38.2, 44.0, 43.9, 40.1, 36.6, 68.7, 42.7, 41.4, 43.3, 63.3, 40.1, 37.7, 38.5, 49.5, 49.5, 45.4, 44.0, 20.9, 24.2, 26.3, 19.2, 22.4, 22.8, 18.4, 22.8, 24.8, 24.8, 36.0, 24.8, 37.6, 20.6, 34.1, 33.4, 33.4, 48.5, 24.2, 30.2, 30.2, 97.3, 31.8, 23.3, 23.3, 30.8, 20.3, 9.6, 31.5, 121.6, 73.3, 55.5, 87.6, 0, 73.3, 59.8, 66.6]
APdam4 = [51.1, 37.7, 42.2, 46.8, 38.2, 44.0, 43.9, 40.1, 36.6, 68.7, 42.7, 41.4, 43.3, 63.3, 40.1, 37.7, 38.5, 49.5, 49.5, 45.4, 44.0, 12.6, 14.5, 15.8, 11.5, 13.4, 13.7, 11.1, 13.7, 14.9, 14.9, 25.4, 14.9, 26.5, 12.3, 24.1, 20.1, 20.1, 21.4, 14.5, 14.9, 14.9, 42.9, 22.4, 14.0, 14.0, 18.5, 12.2, 5.8, 22.2, 121.6, 73.3, 55.5, 87.6, 0, 73.3, 59.8, 66.6]
APdam5 = [35.3, 26.1, 29.1, 32.4, 26.4, 30.4, 30.4, 27.7, 25.3, 68.7, 29.5, 28.6, 29.9, 63.3, 27.7, 26.1, 26.6, 34.2, 34.2, 31.4, 30.4, 3.4, 3.9, 4.2, 3.1, 3.6, 3.7, 3.0, 3.6, 4.0, 4.0, 14.7, 4.0, 15.4, 3.3, 13.9, 5.4, 5.4, 5.7, 3.9, 4.8, 4.8, 11.5, 13.0, 3.7, 3.7, 4.9, 3.3, 1.5, 12.9, 121.6, 73.3, 55.5, 87.6, 0, 73.3, 59.8, 66.6]
APdam6 = [19.9, 14.7, 16.4, 18.2, 14.9, 17.1, 17.1, 15.6, 14.2, 68.7, 16.6, 16.1, 16.8, 63.3, 15.6, 14.7, 15., 19.3, 19.3, 17.7, 17.1, 2.3, 2.7, 2.9, 2.1, 2.5, 2.6, 2.1, 2.5, 2.8, 2.8, 3.0, 2.8, 3.1, 2.2, 2.8, 3.7, 3.7, 4.0, 2.7, 3.4, 3.4, 8.0, 2.6, 2.6, 2.6, 3.4, 2.3, 1.1, 2.6, 121.6, 73.3, 55.5, 87.6, 0, 73.3, 59.8, 66.6]

ats = [624,706,624,624,624,1000,706,990,706,545,545,800,1000,180,949,596,857,180,923,706,1000,747,1000,1091,1091,1200,1500,1600,600,524,747,1040,947,1111,674,1046,747,600,600,857,180,180,180,180,180,180,180,180,180,180,60,60,60,60,180,180,500,666]

AmSw = {0:[FMJdam0,FMJdam1,FMJdam2,FMJdam3,FMJdam4,FMJdam5,FMJdam6],1:[APdam0,APdam1,APdam2,APdam3,APdam4,APdam5,APdam6]}
Bpr = {0:1,1:1,2:1,3:0.50,4:0.50,5:0.50,6:0.35,7:0.35,8:0.25,9:0.25}
ArCoBp = {0:[],1:[2],2:[1,2],3:[1,2],4:[1,2],5:[1,2,3,4],6:[1,2,3,4,5]}
class DamageCal():
    def __init__(self,GunID,BodypartID,VestID,HelmetID,AmmoID,hp,):

        if BodypartID == "0":
            Armor = HelmetID
        else:
            if BodypartID in ArCoBp[VestID]:
                Armor = VestID
            else:
                Armor = 0
            self.DamagePerShot = AmSw[AmmoID][Armor][GunID] * Bpr[BodypartID]
        if self.DamagePerShot != 0:
            self.ShotsToKill=math.ceil(hp/self.DamagePerShot)
            self.TimeToKill=(math.ceil(hp/self.DamagePerShot)/(ats[GunID]/60))
        else:
            self.ShotsToKill=int("infinite")
            self.TimeToKill = int("infinite")

        self.DPS = self.DamagePerShot * (ats[GunID]/60)

        self.ShotsPerMinute=ats[GunID]
    def GUI(self):
        DPShLabel.configure(text='Damage Per Shot:  '+str(self.DamagePerShot))
        ShotsToKillLabel.configure(text='Shots To Kill:  '+str(self.ShotsToKill))
        TimeToKillLabel.configure(text='Time To Kill:  '+str(self.TimeToKill))
        DPSLabel.configure(text='Damage Per Second:  '+str(self.DPS))
        ShotsPerMinuteLabel.configure(text='Shots Per Minute:  '+str(self.ShotsPerMinute))
def idpage():
    window.geometry('1022x500')
    DamageFrame.pack_forget()
    Idlabel=tk.CTkLabel(IdFrame,text='Gun\n\n[    Rifle    ]\n\nAK Alpha: 0         AK5C: 1         AK-74: 2\nAKM: 3          AK74-U: 4          AS VAL: 5\nAug: 6          Famas: 7          G36K: 8\nG3A3: 9          Galil: 10          L85A2: 11\nM16: 12          M1 SASS: 13          M4: 14\nSCAR: 15          SG552: 16          SKS: 17\nSKS (auto): 18          Stoner: 19          VSS: 20\n\n[     SMGs     ]\n\nAgram: 21          Cx8 Storm: 22          Vector10mm: 23\nVector9mm: 24          Luty: 25          Mac 10: 26\nMac 11: 27          MAT-49: 28          MP40: 29\nMP5: 30          MP7: 31          MP9: 32\nP90: 33          PP Bizon: 34          PPSH: 35\nThompson: 36          UMP45: 37          The Fin Reaper: 38\nJW MPX: 39\n\n[   Handguns   ]\n\nColt 1911: 40          JW 2011: 41          Deagle: 42\nFN57: 43          Glock: 44          JW G34: 45\nUSP 45: 46          Makarov: 47          Ruger: 48\nTokarev: 49\n\n[      Bolt-Action Rifles     ]\n\nAWM: 50          Mosin: 51          M1903: 52\nHunter 85: 53\n\n[    Sniper-Rifles    ]\n\nBarret: 54          Dragunov: 55\n\n[       LMGs       ]\n\nBAR: 56          XM250: 57\n\n\n\nBodypart\n\nHead: 0          Neck:1          Torso: 2          Pelvis: 3          Upper Arms: 4\nUpper Legs: 5          Lower Arms: 6          Lower Legs: 7          Hands: 8\nFeet: 9\n\n\n\nVest\n\nNone/A22: 0          LABV: 1          JPC2: 2          VestB: 3\n6B102: 4          6B43: 5          R61: 6\n\n\n\nHelmet\n\nNone: 0          SPH-5: 1          SSh-68: 2          6B47: 3\nATE: 3          C1300: 3          Ronin: 4          Cultist Mask: 4\nKrtek Mask: 4          Altyn: 5          Collector Helmet: 5\n\n\n\nAmmo\n\nFMJ: 0     AP: 1',font=("",16))
    IdCloseButton=tk.CTkButton(IdFrame,text="Close",command=idpageclose)
    IdCloseButton.place(x=0,y=0)
    Idlabel.pack(pady=10)
    IdFrame.place(x=500,y=0)   
def idpageclose():
    window.geometry('500x500')
    DamageFrame.place(x=0,y=0)
    IdFrame.place_forget()
window = tk.CTk()
window.geometry("500x500")
window.title("Ghosts of Tabor Calculator")

IdFrame = tk.CTkScrollableFrame(window,width=500,height=500)
DamageFrame=tk.CTkFrame(window,width=500,height=500)
DamageFrame.pack_propagate(False)
DFLabel=tk.CTkLabel(DamageFrame,text="Damage Calculator",font=("arial",20)).pack()


InputGrid=tk.CTkFrame(DamageFrame)

GunInput=tk.CTkEntry(InputGrid,width=150,justify="center",placeholder_text="GunID")
GunInput.grid(row=0,column=0)

BodyPartInput=tk.CTkEntry(InputGrid,width=150,justify="center",placeholder_text="BodypartID")
BodyPartInput.grid(row=0,column=1)

VestInput=tk.CTkEntry(InputGrid,width=150,justify="center",placeholder_text="VestID")
VestInput.grid(row=0,column=2)

HelmetInput=tk.CTkEntry(InputGrid,width=150,justify="center",placeholder_text="HelmetID")
HelmetInput.grid(row=1,column=0)

AmmoInput=tk.CTkEntry(InputGrid,width=150,justify="center",placeholder_text="AmmoID")
AmmoInput.grid(row=1,column=1)

HpInput=tk.CTkEntry(InputGrid,width=150,justify="center",placeholder_text="HP")
HpInput.grid(row=1,column=2)

CalculateButton=tk.CTkButton(InputGrid,text="Calculate",command=lambda: DamageCal(int(GunInput.get()),int(BodyPartInput.get()),int(VestInput.get()),int(HelmetInput.get()),int(AmmoInput.get()),int(HpInput.get())).GUI())
CalculateButton.grid(row=3,column=1)

IDiButton=tk.CTkButton(InputGrid,text="IDs?",command=idpage)
IDiButton.grid(row=3,column=0)

DPShLabel=tk.CTkLabel(DamageFrame,text="")
ShotsToKillLabel=tk.CTkLabel(DamageFrame,text="")
TimeToKillLabel=tk.CTkLabel(DamageFrame,text="")
DPSLabel=tk.CTkLabel(DamageFrame,text="")
ShotsPerMinuteLabel=tk.CTkLabel(DamageFrame,text="")

DamageFrame.place(x=0,y=0)

InputGrid.pack()

DPShLabel.pack()
ShotsToKillLabel.pack()
TimeToKillLabel.pack()
DPSLabel.pack()
ShotsPerMinuteLabel.pack()

window.mainloop()