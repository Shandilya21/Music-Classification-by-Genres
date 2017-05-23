_Developer_="Arunav Pratap Shandilya"

import os
import numpy as np 
import matplotlib.pyplot as plt 
import sunau





rootDir="//home//arunav//Downloads//genres//"
genres_names=os.listdir(rootDir)

X=[]
Y=[]
ctr=0


def get_Info(full_file_path):
	s=sunau.open(full_file_path,'rb')
	w=s.getnframes()
	data=np.fromstring(s.readframes(w),np.dtype("int16"))
	fs=s.getframerate()
	X=np.array(data)

	Y.append(ctr)
	X=np.reshape(X, (1, X.shape[0]))
	print X.shape
	print Y
	plt.plot(X,Y)
	plt.title("Sound Wave")
	plt.xlabel("Time")
	plt.ylabel("Frequency")

for root in genres_names:
	full_root_path=os.path.join(rootDir,root)
	ctr+=1
	print ctr
	
	flnames=os.listdir(full_root_path)
	for fl in flnames:
		full_file_path=os.path.join(full_root_path,fl)

		Time=np.linspace(0,len(data)/fs,num=len(data))
		print Time
	
		get_Info(full_file_path)
	

	


