from core.redis  import rds
from core.parser import ScanParser
from db.db_ports import svc_ports

class Rule:
  def __init__(self):
    self.rule = 'SVC_F88A'
    self.rule_severity = 3
    self.rule_description = 'This rule checks for open Service Ports'
    self.rule_confirm = 'Exposed Service Port'
    self.rule_details = ''
    self.rule_mitigation = '''Bind all possible network services to localhost, and configure only those which require remote clients on an external interface.'''
    self.intensity = 0

  def check_rule(self, ip, port, values, conf):
    p = ScanParser(port, values)
    
    domain = p.get_domain()
    
    if port in svc_ports:
      self.rule_details = 'Server is listening on remote port: {} ({})'.format(port, svc_ports[port])
      rds.store_vuln({
        'ip':ip,
        'port':port,
        'domain':domain,
        'rule_id':self.rule,
        'rule_sev':self.rule_severity,
        'rule_desc':self.rule_description,
        'rule_confirm':self.rule_confirm,
        'rule_details':self.rule_details,
        'rule_mitigation':self.rule_mitigation
      })

    return
