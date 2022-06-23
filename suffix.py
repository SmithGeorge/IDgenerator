def suffix(ID17):
	 value = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
	 return "10X98765432"[sum(int(ID17[i])*value[i] for i in range(0,len(ID17)))%11]