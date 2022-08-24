print("Name: {Taramart Kaewmanee}")
print("SID: {364211760015}")
print("Group: {MIT221}")
print("********************")
def getPID():
 pid = input ('Enter your pid:') #str
 lpid = [int(x) for x in pid]
 return lpid

def getFortune(var):
    if var % 2 == 0:
      print('Your Fortune Is Good')
    else:
      print('Your Fortune Is Very Good')

PID = getPID()
print(f'เลขบัตรประชาชน: {sum(PID)}')
print(f'ทำนายดวงชะตา: {getFortune(sum(PID))}')
print("********************")


print ("hello,MIT221")
