#!/usr/bin/python

def create_guangshuai_table(dict,list):
	
#	switch_list = dict.keys()
	#the function will eventually return the string opject table to the html
	table = ""
	#count numbers of every switch
	interface_number = []
	for i in list:
		interface_number.append(str(len(dict[i])-1))	
	colors = ["danger","info"]

		
	#create table with forloop

	for i in range(len(list)):
		interface = [ j for j in dict[list[i]].keys() if j != 'sysname']
		print interface
		#define the color 
		if i % 2 == 0 :
			color = colors[0]
		else:
			color = colors[1]
		#identify how many numbers does the switch has
		#if interface_number >1 ,merge the row 

		if int(interface_number[i]) > 1:
			if len(dict[list[i]][interface[0]].keys()) == 2:
				table += '<tr class='+color+'><td rowspan="' + interface_number[i] +'">'+list[i]+'</td>'
				table += '<td rowspan="' + interface_number[i] +'">'+dict[list[i]]['sysname']+'</td>'
				table += '<td>'+interface[0]+'</td>'+'<td>'+str(dict[list[i]][interface[0]]['rx'])+'</td>'+\
					'<td>'+str(dict[list[i]][interface[0]]['tx'])+'</td></tr>'
			elif len(dict[list[i]][interface[0]].keys()) == 1:
				table += '<tr class='+color+'><td rowspan="' + interface_number[i] +'">'+list[i]+'</td>'
				table += '<td rowspan="' + interface_number[i] +'">'+dict[list[i]]['sysname']+'</td>'
				table += '<td>'+interface[0]+'</td>'+'<td colspan="2" align="right">'+str(dict[list[i]][interface[0]]['info'])+'</td></tr>'
			
			interface = interface[1:]
			for j in interface:
				if len(dict[list[i]][j].keys()) == 2:
					table += '<tr class='+color+'><td>'+j+'</td>'+'<td>'+str(dict[list[i]][j]['rx'])+'</td>'+'<td>'+str(dict[list[i]][j]['tx'])+'</td></tr>'	
				elif len(dict[list[i]][j].keys()) == 1:
					table += '<tr class='+color+'><td>'+j+'</td>'+'<td colspan="2" align="right">'+str(dict[list[i]][j]['info'])+'</td></tr>'	
			
		else:
			interface = dict[list[i]].keys()
			if len(dict[list[i]][interface[0]].keys()) == 2:
				table += '<tr class='+color+'><td>'+list[i]+'</td><td>'+dict[list[i]]['sysname']+'<td>'+interface[0]+'</td>'+'<td>'+str(dict[list[i]][interface[0]]['rx'])+\
					'</td>'+'<td>'+str(dict[list[i]][interface[0]]['tx'])+'</td></tr>'
			elif len(dict[list[i]][interface[0]].keys()) == 1:
				table += '<tr class='+color+'><td>'+list[i]+'</td><td>'+dict[list[i]]['sysname']+'<td>'+interface[0]+'</td>'+'<td colspan="2" align="right">'+\
					str(dict[list[i]][interface[0]]['info'])+'</td></tr>'	
	return table


def create_false_table(dict,list):
#	ip_list = dict.keys()
	ip_list = list
        table = ''
        for ip in ip_list:
                table += '<tr><td>'+ip+'</td>'+'<td>'+dict[ip]+'</td></tr>'
        return table


def create_module_number_table(dict,list):
	table = ""
	for ip in list:
		table += '<tr><td>'+ip+'</td>'+'<td>'+dict[ip]['sysname']+'</td>'+'<td>'+str(dict[ip]['module_number'])+'</td></tr>'
	return table




###############################################################################################################################
if __name__ == "__main__":
	dict = {'1.1.1.1':{'ge0':{'info':'not support'},'ge1':{'rx':1,'tx':5},'ge2':{'rx':1,'tx':3}},'2.2.2.2':{'ge3':{'rx':4,'tx':5},'ge1':{'rx':1,'tx':2}},'3.3.3.3':{'tge3':{'rx':-1,'tx':-2.5},'Tge2':{'rx':0.1,'tx':2},'tge1':{'rx':1,'tx':2},'tge0':{'rx':1,'tx':2}},'4.4.4.4':{'ge1':{'info':'not support 2'}}
		}

	t = create_table(dict)
	print t
