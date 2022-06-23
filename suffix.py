def suffix(ID17):
	 return "10X98765432"[sum(int(ID17[i])*[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2][i] for i in range(0,len(ID17)))%11]
