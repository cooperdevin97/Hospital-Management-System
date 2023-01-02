from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter
from tkinter import messagebox

# Dataframe Left


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        cmbNamTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowtoUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNo = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()

        # Functions

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Hospital Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def iPrescription():

            self.txtPrescription.insert(
                END, 'Name of Tablets: \t\t\t' + cmbNamTablets.get() + "\n")
            self.txtPrescription.insert(
                END, 'Ref: \t\t\t' + Ref.get() + "\n")
            self.txtPrescription.insert(
                END, 'Dose: \t\t\t' + Dose.get() + "\n")
            self.txtPrescription.insert(
                END, 'NumberTablets: \t\t\t' + NumberTablets.get() + "\n")
            self.txtPrescription.insert(
                END, 'Lot: \t\t\t' + Lot.get() + "\n")
            self.txtPrescription.insert(
                END, 'IssuedDate: \t\t\t' + IssuedDate.get() + "\n")
            self.txtPrescription.insert(
                END, 'ExpDate: \t\t\t' + ExpDate.get() + "\n")
            self.txtPrescription.insert(
                END, 'DailyDose: \t\t\t' + DailyDose.get() + "\n")
            self.txtPrescription.insert(
                END, 'PossibleSideEffects: \t\t\t' + PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(
                END, 'FurtherInformation: \t\t\t' + FurtherInformation.get() + "\n")
            self.txtPrescription.insert(
                END, 'StorageAdvice: \t\t\t' + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(
                END, 'DrivingUsingMachines: \t\t\t' + DrivingUsingMachines.get() + "\n")
            self.txtPrescription.insert(
                END, 'HowtoUseMedication: \t\t\t' + HowtoUseMedication.get() + "\n")
            self.txtPrescription.insert(
                END, 'PatientID: \t\t\t' + PatientID.get() + "\n")
            self.txtPrescription.insert(
                END, 'PatientNHSNo: \t\t\t' + PatientNHSNo.get() + "\n")
            self.txtPrescription.insert(
                END, 'PatientName: \t\t\t' + PatientName.get() + "\n")
            self.txtPrescription.insert(
                END, 'DateofBirth: \t\t\t' + DateofBirth.get() + "\n")
            self.txtPrescription.insert(
                END, 'PatientAddress: \t\t\t' + PatientAddress.get() + "\n")

            return

        def iPrescriptionData():
            self.txtFrameDetail.insert(END, cmbNamTablets.get()+"\t\t"+Ref.get()+"\t"+Dose.get()+"\t\t"+NumberTablets.get()+"\t"+Lot.get() +
                                       "\t"+IssuedDate.get()+"\t\t"+ExpDate.get()+"\t"+DailyDose.get()+"\t\t" +
                                       StorageAdvice.get()+"\t"+PatientNHSNo.get()+"\t"+PatientName.get() +
                                       "\t"+DateofBirth.get()+"\t"+PatientAddress.get()+"\n")

            return

        def iReceipt():

            return

        def iDelete():

            cmbNamTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetail.delete("1.0", END)

            return

        def iReset():
            cmbNamTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetail.delete("1.0", END)
            return

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=(
            'arial', 40, 'bold'), text="Hospital Management System", padx=2)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350,
                            height=400, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350,
                            height=100, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350,
                          height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, width=800,
                                   height=300, padx=20, relief=RIDGE, font=(
                                       'arial', 12, 'bold'), text="Patient Information:")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=10, width=450,
                                    height=300, padx=20, relief=RIDGE, font=(
                                        'arial', 12, 'bold'), text="Prescription:")
        DataFrameRight.pack(side=RIGHT)

        self.lblNameTablet = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Name of Tablets:", padx=2, pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(
            DataFrameLeft, textvariable=cmbNamTablets, state='readonly', font=(
                'arial', 12, 'bold'), width=23)

        self.cboNameTablet['value'] = (
            '', 'Ibuprofen', 'Co-codamol', 'Paracetamol', 'Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInfo = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Further Information:", padx=2, pady=4)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)

        self.txtFurtherInfo = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=FurtherInformation, width=25)
        self.txtFurtherInfo.grid(
            row=0, column=3)

        self.lblRef = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Reference No:", padx=2, pady=4)
        self.lblRef.grid(row=1, column=0, sticky=W)

        self.txtRef = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(
            row=1, column=1)

        self.lblStorage = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Storage Advice:", padx=2, pady=4)
        self.lblStorage.grid(row=1, column=2, sticky=W)

        self.txtStorage = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=StorageAdvice, width=25)
        self.txtStorage.grid(
            row=1, column=3)

        self.lblDose = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Dose:", padx=2, pady=2)
        self.lblDose.grid(row=2, column=0, sticky=W)

        self.txtDose = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=Dose, width=25)
        self.txtDose.grid(
            row=2, column=1)

        self.lblDUseMachine = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Driving Machines:", padx=2, pady=2)
        self.lblDUseMachine.grid(row=2, column=2, sticky=W)

        self.txtDUsemachine = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=DrivingUsingMachines, width=25)
        self.txtDUsemachine.grid(
            row=2, column=3)

        self.lblNumberTablets = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Number Tablets:", padx=2, pady=2)
        self.lblNumberTablets.grid(row=3, column=0, sticky=W)

        self.txtNumberTablets = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=NumberTablets, width=25)
        self.txtNumberTablets.grid(
            row=3, column=1)

        self.lblUseMedications = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Driving Machines:", padx=2, pady=2)
        self.lblUseMedications.grid(row=3, column=2, sticky=W)

        self.txtUseMedications = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=HowtoUseMedication, width=25)
        self.txtUseMedications.grid(
            row=3, column=3)

        self.lblLot = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Lot:", padx=2, pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)

        self.txtLot = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=Lot, width=25)
        self.txtLot.grid(
            row=4, column=1)

        self.lblPatientID = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Patient ID:", padx=2, pady=2)
        self.lblPatientID.grid(row=4, column=2, sticky=W)

        self.txtPatientID = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=PatientID, width=25)
        self.txtPatientID.grid(
            row=4, column=3)

        self.lblIssuedDate = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Issued Date:", padx=2, pady=2)
        self.lblIssuedDate.grid(row=5, column=0, sticky=W)

        self.txtlblIssuedDate = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=IssuedDate, width=25)
        self.txtlblIssuedDate.grid(
            row=5, column=1)

        self.lblNHSNumber = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="NHS Number:", padx=2, pady=2)
        self.lblNHSNumber.grid(row=5, column=2, sticky=W)

        self.txtlblNHSNumber = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=PatientNHSNo, width=25)
        self.txtlblNHSNumber.grid(
            row=5, column=3)

        self.lblExpDate = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="NHS Number:", padx=2, pady=2)
        self.lblExpDate.grid(row=6, column=0, sticky=W)

        self.txtlblExpDate = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=ExpDate, width=25)
        self.txtlblExpDate.grid(
            row=6, column=1)

        self.lblPatientName = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Patient Name:", padx=2, pady=2)
        self.lblPatientName.grid(row=6, column=2, sticky=W)

        self.txtlblPatientName = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=PatientName, width=25)
        self.txtlblPatientName.grid(
            row=6, column=3)

        self.lblDailyDose = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Daily Dose:", padx=2, pady=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)

        self.txtlblDailyDose = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=DailyDose, width=25)
        self.txtlblDailyDose.grid(
            row=7, column=1)

        self.lblDateofBirth = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Date of Birth:", padx=2, pady=2)
        self.lblDateofBirth.grid(row=7, column=2, sticky=W)

        self.txtlblDateofBirth = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=DateofBirth, width=25)
        self.txtlblDateofBirth.grid(
            row=7, column=3)

        self.lblSideEffects = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Side Effects:", padx=2, pady=2)
        self.lblSideEffects.grid(row=8, column=0, sticky=W)

        self.txtlblSideEffects = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=PossibleSideEffects, width=25)
        self.txtlblSideEffects.grid(
            row=8, column=1)

        self.lblPatientAddress = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Patient Address:", padx=2, pady=2)
        self.lblPatientAddress.grid(row=8, column=2, sticky=W)

        self.txtlblPatientAddress = Entry(DataFrameLeft, font=(
            'arial', 12, 'bold'), textvariable=PatientAddress, width=25)
        self.txtlblPatientAddress.grid(
            row=8, column=3)


# Dataframe Right
        self.txtPrescription = Text(DataFrameRight, font=(
            'arial', 12, 'bold'), width=43,  height=12, padx=2, pady=8)
        self.txtPrescription.grid(row=0, column=0)

        self.btnPrescription = Button(ButtonFrame, text='Prescription', font=(
            'arial', 12, 'bold'), width=24, bd=4, command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(ButtonFrame, text='Prescription Data', font=(
            'arial', 12, 'bold'), width=24, bd=4, command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=(
            'arial', 12, 'bold'), width=24, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=2)

        self.btnReset = Button(ButtonFrame, text='Reset', font=(
            'arial', 12, 'bold'), width=24, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=3)

        self.btniExit = Button(ButtonFrame, text='Exit', font=(
            'arial', 12, 'bold'), width=24, bd=4, command=iExit)
        self.btniExit.grid(row=0, column=4)

        self.lblLabel = Label(FrameDetail, font=(
            'arial', 10, 'bold'), pady=8, text="Name of Tablets\t Reference No.\t Doseage\t No. of Tablets\t Lot\t Issued Date\t Exp. Date\
                Daily Dose\t Storage Adv.\t NHS Number\t DOB\t Address",)
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=(
            'arial', 12, 'bold'), width=130,  height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)


if __name__ == '__main__':
    root = Tk()
    application = Hospital(root)
    root.mainloop()
