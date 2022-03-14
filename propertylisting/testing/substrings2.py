

endpoint1 = 'siem/offenses?fields=follow_up,inactive,assigned_to,id,domain_id,description,magnitude,credibility,relevance,severity,start_time,last_persisted_time&'
endpoint2 = 'config/domain_management/domains?fields=id,name'

print('siem/offenses' in endpoint1)
#print('siem/offenses' in endpoint2)

print('--------------------------------------')
#print('config/domain_management' in endpoint1)
print('config/domain_management' in endpoint2)

