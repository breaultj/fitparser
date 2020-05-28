import os
import fitConstants as fit
import fittypes as fittypes

headerRecord = 0
headerLength = 12
headerType = 0              # 0 Normal 1 Time Compressed
messageType = 1             # 1 Definition Message 0 Data Message
messageTypeSpecific = 0     # set when developer fields present
localMessageType = 0        # local mesg_num   
dataLength = 0
fileHeaderCRC = 0
localMessageDict = {}       # stores the definition based on the local message number as an index
timeOffset = 0
lastTimeStamp = 0

#*************************
# read a file header record
#*************************
def readFileHeaderRecord():
    global headerLength
    global dataLength
    global FileHeaderCRC

    byte = bytearray(f.read(12))

    if byte[0] == 14:
      headerLength = 14
      crcBytes = bytearray(f.read(2))
      fileHeaderCRC = int.from_bytes([crcBytes[0],crcBytes[1]],"little",signed=False)
    else:
      headerLength = 12

    #print("Profile Version ",int.from_bytes([byte[2],byte[3]],"little",signed=False)
    dataLength = int.from_bytes([byte[4],byte[5],byte[6],byte[7]],"little",signed=False)
    str = chr(byte[8]) + chr(byte[9]) + chr(byte[10]) + chr(byte[11])

    print("File Header","Length",headerLength,"Protocol Version",byte[1],"Record Length",dataLength,"Data Tyepe",str)

#***************************
# read the header record
#***************************
def readHeaderRecord():
    global messageType
    global headerType
    global messageTypeSpecific
    global localMessageType
    global headerRecord
    global timeOffset

    headerRecord = bytearray(f.read(1))[0]
    # bit 7 = 0 Normal = 1 Compressed Timestamp
    # bit 6 = 0 Definition Message = 1 Data Message
    # bit 5 = 0 default, 1 developer defined data
    # bit 4 = 0 Reserved
    # bit 0 - 3 Local Message Type

    headerType = (headerRecord & 128)           # 0 Normal 1 Time Compressed, bit 7
    messageType = (headerRecord & 64)           # 1 Definition Message 0 Data Message, bit 6
    messageTypeSpecific = (headerRecord & 32)   # set when developer fields present, bit 5
    localMessageType = (headerRecord & 15)      # mesg_num  bit 0-4 

    if (headerType == 0):
        # Normal header record
        if (messageType == 64):
            # definition record
            print("Definition Message Message Specific",messageTypeSpecific,"Local Message Num",localMessageType,end = '')
            return processDefinitionRecord() + 1
        else:
            # data record
            print("Data Record Message Specific",messageTypeSpecific,"Local Message Num",localMessageType,end = '')
            return processDataRecord() + 1
    else:
        # compressed time record
        # bit 7 = 1 compressed timestamp
        # bit 5-6 local message type
        # bit 0-4 time offset
        
        localMessageType = (headerRecord & 96) >> 5
        timeOffset = (headerRecord & 31)
        print("Compressed Time Message Local Message Num",localMessageType,"Time Offset",timeOffset,end = '') 

        return processCompressedRecord() + 1
# end of def
 
# *****************************    
# process a definition record 
# *****************************
def processDefinitionRecord():
    global fieldDefinitionList
    global localMessageType
    global localMessageDict
    byte_count = 5
    numberOfFields = 0

    # read next 5 bytes to get start of Definition Message
    # byte 1 Reserved
    # byte 2 Architecture 0 Little Endian 1 Big Endian
    # byte 3 4 Global Message Number
    # byte 5 Number of fields
    definitionMessage = bytearray(f.read(5))
    numberOfFields = definitionMessage[4]
    
    globalMessageNum = 0
    endianOrder = "big"
    if definitionMessage[1] == 0:
        endianOrder = "little"

    globalMessageNum = int.from_bytes([definitionMessage[2],definitionMessage[3]],endianOrder,signed=False)
    globalMessageNumName = fittypes.mesg_num[globalMessageNum]
    
    print(" Architecture (Endian)",definitionMessage[1],"Number of fields",numberOfFields,"Global Message Number",globalMessageNum,"Global Message Name",globalMessageNumName)

    # read each of the Field Definitions
    fieldDefinitionList = []
    for x in range(numberOfFields):
        fileDict = readDefinition(globalMessageNumName,globalMessageNumName,endianOrder)
        byte_count = byte_count + 3
        fieldDefinitionList.append(fileDict)   
    
    # read developer fields when messageTypeSpecifc from header is 1
    if (messageTypeSpecific == 32):
        numberOfDevFields = bytearray(f.read(1))[0]
        byte_count = byte_count + 1
        print("Definition Header Number of Developer Fields",numberOfDevFields)

        for x in range(numberOfDevFields):
            fileDict = readDefinition(globalMessageNumName,globalMessageNumName,endianOrder)
            byte_count = byte_count + 3
            fieldDefinitionList.append(fileDict)   

    # save the definitions based on the local message type (number)
    localMessageDict[localMessageType] = fieldDefinitionList

    # return number of bytes that were read
    return byte_count
# end of processDefinitionRecord()

# ********************************************************
# read the definition from a message definition record
# ********************************************************
def readDefinition(globalMessageNum,globalMessageNumName,endianOrder):
    # read the 3 bytes of the definition
    fieldDefn = bytearray(f.read(3)) 

    # byte 1 Field Definition Number
    # byte 2 Size
    # byte 3 Base Type

    fileDict = {}
    fileDict["GlobalMessageNumber"] = globalMessageNum
    fileDict["GlobalMessageNumberName"] = globalMessageNumName
    fileDict["FieldDefnNumber"] = fieldDefn[0]
    fileDict["FieldDesc"] = fit.getMessage(globalMessageNumName,fieldDefn[0])
    fileDict["Size"] = fieldDefn[1]
    fileDict["BaseType"] = fieldDefn[2]

    # break down of byte 3 Base Type
    # bit 7 Endian Ability 0 Single Byte 1 mutiple byes
    # bit 5-6 Reserved
    # bit 0-4 Base Type Number
    endianAbility = fieldDefn[2] & 128
    baseTypeNumber = fieldDefn[2] & 15

    fileDict["EndianAbility"] = endianAbility
    fileDict["BaseTypeNumber"] = baseTypeNumber
    fileDict["BaseType"] = fit.getBaseType(baseTypeNumber)
    fileDict["MesgType"] = fit.getMessageType(globalMessageNumName,fieldDefn[0])
    fileDict["EndianOrder"] = endianOrder
      
    print("Field Defn Number",fieldDefn[0],fit.getMessage(globalMessageNumName,fieldDefn[0]),"Size",fieldDefn[1],"Base Type",fieldDefn[2],fileDict["BaseType"],fileDict["MesgType"])

    return fileDict
# end of readDefinition

# *****************************    
# process a data record 
# *****************************
def processDataRecord():
    global fieldDefinitionList
    global localMessageType
    byte_count = 0

    # data record     
    fieldDefinitionList = localMessageDict[localMessageType]   
    numberDataDefn = len(fieldDefinitionList)
    print(" Number Data Definitions", numberDataDefn)

    dataDict = {}
    bytesToRead = 0
    for df in range(numberDataDefn):
        dataDict = fieldDefinitionList[df]
        bytesToRead = dataDict["Size"]
        # read the number of bytes as defined in the definitio record
        dataContents = bytearray(f.read(bytesToRead))
        byte_count = byte_count + bytesToRead
        print("Data",df,dataDict["FieldDesc"],"Number of Bytes",bytesToRead)

    # return the number of bytes read
    return byte_count
# end of processDataRecord()

# *****************************    
# process a compressed record
# *****************************
def processCompressedRecord():
    global fieldDefinitionList
    byte_count = 0

    # data record        
    numberDataDefn = len(fieldDefinitionList)
    print("Number of data definitions to read", numberDataDefn)

    dataDict = {}
    bytesToRead = 0
    for df in range(numberDataDefn):
        dataDict = fieldDefinitionList[df]
        bytesToRead = dataDict["Size"]
        # read the number of bytes as defined in the definitio record
        dataContents = bytearray(f.read(bytesToRead))
        byte_count = byte_count + bytesToRead
        print("Data ",df,dataDict["FieldDesc"],"Number of Bytes",bytesToRead)

    # return the number of bytes read
    return byte_count
# end of processDataRecord()

# open the file
total_bytes_read = 0
f = open("activity.fit","rb")
print("Reading testride.fit")

# read the file header 
readFileHeaderRecord()

# read each record
while total_bytes_read < dataLength:
    bytes_read = readHeaderRecord()
    total_bytes_read += bytes_read
    print("REad bytes",total_bytes_read," of ",dataLength)

# read the last 2 CRC bytes

# close the file
f.close()

