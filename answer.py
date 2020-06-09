import time
import requests
import os
import uuid
from multiprocessing import Pool
import hashlib

links = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg", "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

os.system("clear")

def download_file(links, file_name=None):
	r = requests.get(links, allow_redirects=True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)

#QUESTION 1:
c = os.fork() 
# c greater than 0  means parent process 
if n > 0:
    os.waitpid(pid, 0) #Avoid Orphans - QUESTION 3:
    print("Parent process and id is : ", os.getpid()) 
    # c equals to 0 means child process 
else: 
    # QUESTION 2:
    print("Child process and id is : ", os.getpid())
    print("{} files downloading...\n".format(len(links)))
    for i in range(len(links)):
		download_file(links[i], "file{}".format(i))
		print("file{0} downloaded from\n{1}\n".format(i, links[i]))
        
def unique(liste): 
    ulist = [] 
    for x in liste: 
        if x == None:
            liste.remove(None)
        elif x not in ulist: 
            ulist.append(x)
    return ulist

def md5(file_name):
    do_md5 = hashlib.md5()
    with open(file_name, "rb") as file1:
        for chunk in iter(lambda: file1.read(4096), b""):
            do_md5.update(chunk)
    return do_md5.hexdigest()

def check_duplicate(element, list_md5):
	dupcount = 0
	indexes = []
	for i in range(len(list_md5)):
		if list_md5[i] == element:
			dupcount += 1
			indexes.append(i)
	if dupcount > 1:
		return indexes
#QUESTION 4:
files_n = os.listdir() 
files_n.remove("ceng_2034_final_answer.py")
list_md5 = []
print("Checking checksum md5 values...\n")
start_duplicate_time = time.time()
with Pool(5) as p:
	list_md5 = p.map(md5,files_n)
print("Checking duplicate values...\n")
with Pool(5) as p:
	list_duplicate = p.starmap(check_duplicate,([list_md5[0],
	list_md5],[list_md5[1], list_md5], 
	[list_md5[2], list_md5], [list_md5[3],
	list_md5], [list_md5[4], list_md5]))
list_duplicates = list(list_duplicate)
print("Last fixes...\n")
unique_duplicates = unique(list_duplicates)
for j in range(len(unique_duplicates)):
	print("{0} and {1} duplicate files.".format(files_n[unique_duplicates[j][0]],
	files_n[unique_duplicates[j][1]]))
	end_duplicate_time = time.time()
	subtract_duplicate_time = end_duplicate_time - start_duplicate_time
	print("\nTotal execution time to check duplicate = {}".format(subtract_duplicate_time))
    
#clear orphan 
  process= subprocess.Popen( ('ls', '-l', '/tmp'), stdout=subprocess.PIPE)
  for line in process.stdout:
        pass
    
  subprocess.call( ('ps', '-l') )
  process.wait()
  print("\n")
  print( "Clearing...\n")
  print("------------------------------------------------------------")
  subprocess.call( ('ps', '-l') )