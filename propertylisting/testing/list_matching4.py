from collections import defaultdict

def get_item2(index):
    key = 'qradar_instance_ip'

    j = 0
    while j < len(api_domain_result_list):

        print(api_domain_result_list[j]['qradar_instance_ip'])
        if api_domain_result_list[j]['qradar_instance_ip'] == api_result_list[index][key]:
            if api_result_list[index]['domain_id'] == api_domain_result_list[j]['id']:
                api_result_list[index]['domain_name'] = api_domain_result_list[j]['name']
        j += 1

api_domain_result_list = [
    {'id': 0, 'name': '', 'qradar_instance_ip': '10.5.164.210'},
    {'id': 1, 'name': 'Ward-Production', 'qradar_instance_ip': '10.5.164.210'},
    {'id': 2, 'name': 'Ward-INS-LAB', 'qradar_instance_ip': '10.5.164.210'},
    {'id': 0, 'name': '', 'qradar_instance_ip': '172.27.69.10'},
    {'id': 10, 'name': 'IRFU', 'qradar_instance_ip': '172.27.69.10'},
    {'id': 11, 'name': 'Aviva', 'qradar_instance_ip': '172.27.69.10'},
    {'id': 12, 'name': 'Actavo', 'qradar_instance_ip': '172.27.69.10'},
    {'id': 13, 'name': 'applus', 'qradar_instance_ip': '172.27.69.10'},
    {'id': 14, 'name': 'IDA', 'qradar_instance_ip': '172.27.69.10'},
    {'id': 15, 'name': 'incident Response', 'qradar_instance_ip': '172.27.69.10'}
]

api_result_list = [
    {'follow_up': False, 'inactive': True, 'assigned_to': None, 'id': 55578, 'domain_id': 12,
     'description': 'IRC Connections\n preceded by Local IRC Server Detected\n containing Connection Opened.\n',
     'magnitude': 6, 'credibility': 3, 'relevance': 6, 'severity': 8, 'start_time': 1646383965132,
     'last_persisted_time': 1646386430000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': None, 'id': 55572, 'domain_id': 12,
     'description': 'Firewall or ACL Accept Following Recon Activity\n preceded by Local Suspicious Probe Events Detected\n containing Firewall Deny\n',
     'magnitude': 6, 'credibility': 4, 'relevance': 7, 'severity': 5, 'start_time': 1646380945900,
     'last_persisted_time': 1646396544000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': None, 'id': 55552, 'domain_id': 14,
     'description': 'Backdoor.DoublePulsar\n', 'magnitude': 6, 'credibility': 2, 'relevance': 5, 'severity': 8,
     'start_time': 1646339142753, 'last_persisted_time': 1646341452000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': None, 'id': 55553, 'domain_id': 14,
     'description': 'Attack Followed by an Attack Response\n preceded by Exploit Followed by Suspicious Host Activity - Chained\n containing Success Audit: Successful logon with administrative or special privileges\n',
     'magnitude': 5, 'credibility': 3, 'relevance': 5, 'severity': 4, 'start_time': 1646337618393,
     'last_persisted_time': 1646342630000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': None, 'id': 55549, 'domain_id': 12,
     'description': 'Local IRC Server Detected\n containing Connection Opened.\n', 'magnitude': 5, 'credibility': 3,
     'relevance': 5, 'severity': 8, 'start_time': 1646337868592, 'last_persisted_time': 1646386430000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': None, 'id': 55408, 'domain_id': 13,
     'description': 'Systems using many different protocols to the internet\n', 'magnitude': 5, 'credibility': 2,
     'relevance': 4, 'severity': 8, 'start_time': 1646216884230, 'last_persisted_time': 1646396544000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': None, 'id': 55592, 'domain_id': 12,
     'description': 'Mailbox Item Deleted by Another User\n containing Deleted messages from Deleted Items folder\n',
     'magnitude': 4, 'credibility': 2, 'relevance': 2, 'severity': 7, 'start_time': 1646394326314,
     'last_persisted_time': 1646394618000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'rachel.hutchings', 'id': 55338, 'domain_id': 0,
     'description': 'Suspicious IP Address\n and Watch List IP\n and Hostile IP\n', 'magnitude': 4,
     'credibility': 2, 'relevance': 1, 'severity': 9, 'start_time': 1646158740230,
     'last_persisted_time': 1646396514000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'rachel.hutchings', 'id': 55336, 'domain_id': 13,
     'description': 'Systems using many different protocols to the internet\n', 'magnitude': 4, 'credibility': 3,
     'relevance': 5, 'severity': 4, 'start_time': 1646158507342, 'last_persisted_time': 1646396544000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55588, 'domain_id': 11,
     'description': 'RT_FLOW_SESSION_DENY\n', 'magnitude': 3, 'credibility': 2, 'relevance': 2, 'severity': 5,
     'start_time': 1646391133574, 'last_persisted_time': 1646396513000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'leah.brennan', 'id': 55582, 'domain_id': 12,
     'description': 'Attack Followed by an Attack Response\n containing Connection Opened.\n', 'magnitude': 3,
     'credibility': 2, 'relevance': 1, 'severity': 6, 'start_time': 1646382729534,
     'last_persisted_time': 1646396513000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': None, 'id': 55573, 'domain_id': 12,
     'description': 'Kerberos Session Opened\n', 'magnitude': 3, 'credibility': 3, 'relevance': 5, 'severity': 1,
     'start_time': 1646383347182, 'last_persisted_time': 1646395431000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55571, 'domain_id': 12,
     'description': 'Attack Followed by an Attack Response\n containing Update user-success\n', 'magnitude': 3,
     'credibility': 2, 'relevance': 2, 'severity': 4, 'start_time': 1646378677593,
     'last_persisted_time': 1646396469000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55570, 'domain_id': 12,
     'description': 'Detected potential Log4Shell Activity\n containing LogonError-UserAccountNotFound\n',
     'magnitude': 3, 'credibility': 2, 'relevance': 2, 'severity': 5, 'start_time': 1646380028208,
     'last_persisted_time': 1646396513000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': None, 'id': 55555, 'domain_id': 13,
     'description': 'Detected potential Log4Shell Activity\n containing Session Denied\n', 'magnitude': 3,
     'credibility': 2, 'relevance': 1, 'severity': 5, 'start_time': 1646342441984,
     'last_persisted_time': 1646345038000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55550, 'domain_id': 12,
     'description': 'Connection Opened.\n', 'magnitude': 3, 'credibility': 3, 'relevance': 4, 'severity': 1,
     'start_time': 1646337868592, 'last_persisted_time': 1646396513000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55542, 'domain_id': 13,
     'description': 'Detected potential Log4Shell Activity\n containing Session Denied\n', 'magnitude': 3,
     'credibility': 2, 'relevance': 3, 'severity': 5, 'start_time': 1646334128298,
     'last_persisted_time': 1646396513000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'rachel.hutchings', 'id': 55341, 'domain_id': 11,
     'description': 'Systems using many different protocols to the internet\n', 'magnitude': 3, 'credibility': 3,
     'relevance': 5, 'severity': 1, 'start_time': 1646159779733, 'last_persisted_time': 1646396484000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': True, 'inactive': True, 'assigned_to': 'rachel.hutchings', 'id': 55219, 'domain_id': 14,
     'description': 'Mailbox Item Deleted by Another User\n containing Deleted messages from Deleted Items folder\n',
     'magnitude': 3, 'credibility': 3, 'relevance': 0, 'severity': 7, 'start_time': 1646133703682,
     'last_persisted_time': 1646137845000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': True, 'inactive': True, 'assigned_to': 'rachel.hutchings', 'id': 55060, 'domain_id': 12,
     'description': 'Login Failures Followed By Success to the same Destination IP\n preceded by Multiple Login Failures to the Same Destination\n containing User Login Failure\n',
     'magnitude': 3, 'credibility': 2, 'relevance': 2, 'severity': 4, 'start_time': 1645731641214,
     'last_persisted_time': 1646383450000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'leah.brennan', 'id': 55594, 'domain_id': 12,
     'description': 'UBA : User Access from Multiple Locations\n', 'magnitude': 2, 'credibility': 2, 'relevance': 1,
     'severity': 3, 'start_time': 1646395435636, 'last_persisted_time': 1646396492000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'leah.brennan', 'id': 55593, 'domain_id': 12,
     'description': 'Host Port Scan Detected by Remote Host\n', 'magnitude': 2, 'credibility': 2, 'relevance': 1,
     'severity': 5, 'start_time': 1646394367567, 'last_persisted_time': 1646396492000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55587, 'domain_id': 12,
     'description': 'Access Denied\n', 'magnitude': 2, 'credibility': 2, 'relevance': 1, 'severity': 4,
     'start_time': 1646390928984, 'last_persisted_time': 1646396492000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55586, 'domain_id': 12,
     'description': 'UBA : User Access from Multiple Locations\n', 'magnitude': 2, 'credibility': 2, 'relevance': 1,
     'severity': 5, 'start_time': 1646389944352, 'last_persisted_time': 1646396492000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55574, 'domain_id': 12,
     'description': 'UBA : User Access from Multiple Locations\n', 'magnitude': 2, 'credibility': 2, 'relevance': 1,
     'severity': 4, 'start_time': 1646383713849, 'last_persisted_time': 1646396492000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55546, 'domain_id': 12,
     'description': 'Firewall Deny\n preceded by Connection Closed.\n preceded by Connection Opened.\n',
     'magnitude': 2, 'credibility': 2, 'relevance': 1, 'severity': 4, 'start_time': 1646336706104,
     'last_persisted_time': 1646396492000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'leah.brennan', 'id': 55530, 'domain_id': 12,
     'description': 'Attack Followed by an Attack Response\n containing Connection Opened.\n', 'magnitude': 2,
     'credibility': 2, 'relevance': 1, 'severity': 5, 'start_time': 1646321609089,
     'last_persisted_time': 1646396469000, 'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'leah.brennan', 'id': 55589, 'domain_id': 12,
     'description': 'Connection Closed.\n preceded by Connection Opened.\n', 'magnitude': 1, 'credibility': 2,
     'relevance': 1, 'severity': 1, 'start_time': 1646392838561, 'last_persisted_time': 1646396469000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': True, 'assigned_to': 'leah.brennan', 'id': 55568, 'domain_id': 12,
     'description': 'Host Logout\n and User Login Success\n', 'magnitude': 1, 'credibility': 2, 'relevance': 1,
     'severity': 1, 'start_time': 1646379249403, 'last_persisted_time': 1646396469000,
     'qradar_instance_ip': '172.27.69.10'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'AMcCabe', 'id': 11908, 'domain_id': 1,
     'description': 'Suspicious Activity Followed by Endpoint Administration task\n preceded by Recommended Blocked Process Running\n containing Success Audit: A new process has been created\n',
     'magnitude': 6, 'credibility': 3, 'relevance': 6, 'severity': 8, 'start_time': 1646210030237,
     'last_persisted_time': 1646396233000, 'qradar_instance_ip': '10.5.164.210'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'rachel.hutchings', 'id': 11929, 'domain_id': 1,
     'description': 'Suspicious Activity Followed by Endpoint Administration task\n preceded by Excessive Login Failures via Network Connection to the same Machine\n containing Failure Audit: An account failed to log on\n',
     'magnitude': 6, 'credibility': 3, 'relevance': 8, 'severity': 6, 'start_time': 1646336280845,
     'last_persisted_time': 1646396474000, 'qradar_instance_ip': '10.5.164.210'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'AMcCabe', 'id': 11909, 'domain_id': 1,
     'description': 'Ransomware Behaviour: Microsoft Windows System\n', 'magnitude': 6, 'credibility': 3,
     'relevance': 6, 'severity': 7, 'start_time': 1646210520020, 'last_persisted_time': 1646395752000,
     'qradar_instance_ip': '10.5.164.210'},
    {'follow_up': False, 'inactive': False, 'assigned_to': 'rachel.hutchings', 'id': 11930, 'domain_id': 1,
     'description': 'Authentication: Repeat Windows Login Failures\n containing Failure Audit: An account failed to log on\n',
     'magnitude': 5, 'credibility': 3, 'relevance': 6, 'severity': 4, 'start_time': 1646336392439,
     'last_persisted_time': 1646396474000, 'qradar_instance_ip': '10.5.164.210'}
]


print('printing offenses...')

#print(offenses[2])

i = 0

while i < len(api_result_list):
    #print(get_item(i, key, value))
    get_item2(i)
    #print(get_item3(i, key))
    i += 1

print(api_result_list)