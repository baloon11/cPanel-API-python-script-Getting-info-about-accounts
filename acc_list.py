# coding: utf-8
import os
import pycpanel

#=============================================================
admin_login="your_login"
admin_password="your_password"
server_list=[# list of your cPanels
            'cpanel_1.your_domain.com',
            'cpanel_2.your_domain.com',
            'cpanel_3.your_domain.com'
            ]
#=============================================================

if os.path.exists('out'):
    os.remove('out')

for server_name in server_list:
    out=open('out','a')
    server = pycpanel.conn(hostname=server_name,
                           username=admin_login, 
                           password=admin_password) #Basic user/password authentication
    #server.api('listaccts')['acct'] -list of dict`s (each dict - info about separate account)
    account_list=server.api('listaccts')['acct']
    out.write("%s %s %s"%(server_name,len(account_list),"accouts\n"))
    print 'proccesed server ',server_name
    # for account in account_list: # if you need something else info about account (for example, domain)
    #     out.write(account['domain']+"\n")# uncomment this loop
#    out.write("======================================================\n")
    out.close()