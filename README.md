#### cPanel API python script. Getting info about accounts.

If you have a set of cPanels  and you need to know how many accounts in each,
you can use this python script.

Output information about cPanels  will write on `out` file.

If you need to get some different info from each cPanel, you can easy change the code.
(see comments in code)

In the head of script you need to change this data:

	#=============================================================
	admin_login="your_login"

	admin_password="your_password"

	server_list=[# list of your cpanels

		    'cpanel_1.your_domain.com',

		    'cpanel_2.your_domain.com',

		    'cpanel_3.your_domain.com',

		    ]

	#=============================================================

In this variant all cPanels have the same login and password.

#### Requirements
	Python 2.7.10
	pip install pycpanel==0.1.5


#### Usage 
	python acc_list.py

**Note**: this repository contains a set of scripts for create/delete accounts and ip addresses.
`https://github.com/baloon11/cPanel-API-python-scripts`






