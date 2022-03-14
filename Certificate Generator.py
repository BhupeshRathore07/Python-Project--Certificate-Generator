from PIL import Image, ImageDraw, ImageFont
import pandas as pd
# import os

#Reading the CSV File
dataFrame = pd.read_csv("D:\SAC Certificate Generator\SAC Details.csv")

 #Converting Columns into Lists
dataName = dataFrame['Name'].tolist()
dataParticipation = dataFrame['Participation'].tolist()
dataActivity = dataFrame['Activity'].tolist()
dataDate = dataFrame['Date'].tolist()
dataRegNoInt = dataFrame['RegNo'].tolist()
dataRegNo = [str(x) for x in dataRegNoInt] #Making int into string

#Finding length of Data Inupted
totalCertificates = len(dataName)


# =============================================================================
# Printing Lists for Checking
# print ("Name", dataName)
# print ("Participation", dataParticipation)
# print ("Activity", dataActivity)
# print ("Date", dataDate)
# print ("RegNo", dataRegNo)
# =============================================================================


#Font Typography and Size
fontTypeSize_Name = ImageFont.truetype("D:\SAC Certificate Generator\Fonts\MTCORSVA.TTF",260)
fontTypeSize_Participation = ImageFont.truetype("D:\SAC Certificate Generator\Fonts\MTCORSVA.TTF",220)
fontTypeSize_Activity = ImageFont.truetype("D:\SAC Certificate Generator\Fonts\BOD_BI.TTF",250)
fontTypeSize_Date = ImageFont.truetype("D:\SAC Certificate Generator\Fonts\BOD_R.TTF",230)
fontTypeSize_RegNo = ImageFont.truetype("D:\SAC Certificate Generator\Fonts\Manrope-VariableFont_wght.ttf",70)

# Working on Certificates
for i in range(0,totalCertificates,1):
    # Opening Image to edit
    certificateImage = Image.open("D:\SAC Certificate Generator\SAC Certificate Template.jpg")
    
    textName = dataName[i]
    textParticipation = dataParticipation[i]
    textActivity = dataActivity[i]
    textDate = dataDate[i]
    textRegNo = dataRegNo[i]
    
    
    # Making Certificate Editable
    writeOnCertificate = ImageDraw.Draw(certificateImage)
   
    #Text Position, Inputed Text, Text Color, Text Font Style
    writeOnCertificate.text(xy=(4560,2330), text= textName, fill = (0,0,0), font=fontTypeSize_Name, anchor="mm")
    writeOnCertificate.text(xy=(4190,2870), text= textParticipation, fill = (0,0,0), font=fontTypeSize_Participation, anchor="mm")
    writeOnCertificate.text(xy=(3710,3180), text= textActivity, fill = (0,0,0), font=fontTypeSize_Activity, anchor="mm")
    writeOnCertificate.text(xy=(4100,3670), text= textDate, fill = (0,0,0), font=fontTypeSize_Date, anchor="mm")
    writeOnCertificate.text(xy=(4140,5100), text= textRegNo, fill = (51,51,51), font=fontTypeSize_RegNo)

    # Saving File as PDF
    fileNaming = textRegNo + " - " + textName
    certificateImage.save('Certificate PDFs/{}.pdf'.format(fileNaming))