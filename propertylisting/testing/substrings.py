word = 'geeks for geeks'

endpoint1 = 'siem/offenses?fields=follow_up,inactive,assigned_to,id,domain_id,description,magnitude,credibility,relevance,severity,start_time,last_persisted_time&'
endpoint2 = 'config/domain_management/domains?fields=id,name'

# Substring is searched in 'geeks for geeks'
print(word.find('ge', 0))

# Substring is searched in 'eks for geeks'
print(word.find('ge', 2))

# Substring is searched in 'eks for geeks'
print(word.find('geeks ', 2))

# Substring is searched in 's for g'
print(word.find('g', 4, 10))

# Substring is searched in 's for g'
print(word.find('for ', 4, 11))

print(endpoint1.find('siem ', 1))

print(endpoint2.find('siem ', 1))