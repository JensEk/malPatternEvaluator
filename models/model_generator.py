# Purpose: This script is used to generate a model with coreLang assets and save it to a JSON file.

import logging

import maltoolbox
from maltoolbox.language import classes_factory
from maltoolbox.language import specification
from maltoolbox.model import model as malmodel

logger = logging.getLogger(__name__)

lang_file = '../org.mal-lang.coreLang-1.0.0.mar'
lang_spec = specification.load_language_specification_from_mar(lang_file)
specification.save_language_specification_to_json(lang_spec, 'lang_spec.json')
lang_classes_factory = classes_factory.LanguageClassesFactory(lang_spec)
lang_classes_factory.create_classes()



model = malmodel.Model('M1', lang_spec, lang_classes_factory)

# ComputeResources Section

## Hardware
hw_1 = lang_classes_factory.ns.Hardware(name = "Comp C1")
hw_2 = lang_classes_factory.ns.Hardware(name = "Server S1")

model.add_asset(hw_1)
model.add_asset(hw_2)

## Applications
app_1_0 = lang_classes_factory.ns.Application(name = "App 1.0_OS_Windows")
app_1_1 = lang_classes_factory.ns.Application(name = "App 1.1_VPN")

app_2_0 = lang_classes_factory.ns.Application(name = "App 2.0_Server_Windows")

model.add_asset(app_1_0)
model.add_asset(app_1_1)
model.add_asset(app_2_0)


assoc_hw_1_app_1_0 =\
    lang_classes_factory.ns.SysExecution(
    hostHardware = [hw_1],
    sysExecutedApps = [app_1_0]
    )
model.add_association(assoc_hw_1_app_1_0)

assoc_hw_2_app_2_0 =\
    lang_classes_factory.ns.SysExecution(
    hostHardware = [hw_2],
    sysExecutedApps = [app_2_0]
    )
model.add_association(assoc_hw_2_app_2_0)

assoc_app_1_0_app_1_1 =\
    lang_classes_factory.ns.AppExecution(
    hostApp = [app_1_0],
    appExecutedApps = [app_1_1]
    )
model.add_association(assoc_app_1_0_app_1_1)





# DataResource Section

## Data
data_s1_1 = lang_classes_factory.ns.Data(name = "Data Secret")
model.add_asset(data_s1_1)

assoc_app_2_0_data_s1_1 =\
    lang_classes_factory.ns.AppContainment(
    containedData = [data_s1_1],
    containingApp = [app_2_0]
    )
model.add_association(assoc_app_2_0_data_s1_1)


# Networking Section

## Routing Firewall
fw_1 = lang_classes_factory.ns.RoutingFirewall(name = "Router FW_1")
model.add_asset(fw_1)

## LAN network
net_1 = lang_classes_factory.ns.Network(name = "Net 1_LAN")
model.add_asset(net_1)

### Connection Rules
cr_net_1_fw_1 = lang_classes_factory.ns.ConnectionRule(name = "CR Net_1->Router_FW_1")
cr_net_1_app_1_0 = lang_classes_factory.ns.ConnectionRule(name = "CR Net_1<->App_1.0")
cr_net_1_app_2_0 = lang_classes_factory.ns.ConnectionRule(name = "CR Net_1<->App_2.0")

model.add_asset(cr_net_1_fw_1)
model.add_asset(cr_net_1_app_1_0)
model.add_asset(cr_net_1_app_2_0)

### Associations
assoc_cr_net_1_app_1_0 =\
    lang_classes_factory.ns.ApplicationConnection(
    applications = [app_1_0],
    appConnections = [cr_net_1_app_1_0]
    )
model.add_association(assoc_cr_net_1_app_1_0)

assoc_cr_net_1_app_2_0 =\
    lang_classes_factory.ns.ApplicationConnection(
    applications = [app_2_0],
    appConnections = [cr_net_1_app_2_0]
    )
model.add_association(assoc_cr_net_1_app_2_0)

assoc_netcon_crs_net_1_Out =\
    lang_classes_factory.ns.OutNetworkConnection(
    outNetworks = [net_1],
    outgoingNetConnections = [cr_net_1_fw_1]
    )
model.add_association(assoc_netcon_crs_net_1_Out)

assoc_netcon_crs_net_1 =\
    lang_classes_factory.ns.NetworkConnection(
    networks = [net_1],
    netConnections = [cr_net_1_app_1_0, cr_net_1_app_2_0]
    )
model.add_association(assoc_netcon_crs_net_1)


## DMZ network
net_2 = lang_classes_factory.ns.Network(name = "Net 2_DMZ")
model.add_asset(net_2)

### Connection Rules
cr_net_2_fw_1 = lang_classes_factory.ns.ConnectionRule(name = "CR Net_2_DMZ<-Router_FW_1")
cr_net_2_app_1_1 = lang_classes_factory.ns.ConnectionRule(name = "CR Net_2_DMZ->App_1.1")
model.add_asset(cr_net_2_fw_1)
model.add_asset(cr_net_2_app_1_1)

### Associations
assoc_cr_net_2_app_1_1 =\
    lang_classes_factory.ns.InApplicationConnection(
    inApplications = [app_1_1],
    ingoingAppConnections = [cr_net_2_app_1_1]
    )
model.add_association(assoc_cr_net_2_app_1_1)

assoc_netcon_crs_net_2_In =\
    lang_classes_factory.ns.InNetworkConnection(
    inNetworks = [net_2],
    ingoingNetConnections = [cr_net_2_fw_1]
    )
model.add_association(assoc_netcon_crs_net_2_In)

assoc_netcon_crs_net_2_Out =\
    lang_classes_factory.ns.OutNetworkConnection(
    outNetworks = [net_2],
    outgoingNetConnections = [cr_net_2_app_1_1]
    )
model.add_association(assoc_netcon_crs_net_2_Out)


## Routing Firewall and networks associations
assoc_netcon_fwcrs =\
    lang_classes_factory.ns.FirewallConnectionRule(
    routingFirewalls = [fw_1],
    connectionRules = [cr_net_2_fw_1, cr_net_1_fw_1]
    )
model.add_association(assoc_netcon_fwcrs)


## Application and networks associations
#cr_app_1_0_app_2_0 = lang_classes_factory.ns.ConnectionRule(name = "CR App_1.1->App_2.0")
#model.add_asset(cr_app_1_0_app_2_0)




# IAM Section

## Identities

id_u1 = lang_classes_factory.ns.Identity(name = "Id Admin_1")
id_u2 = lang_classes_factory.ns.Identity(name = "Id Employee_1")
id_u3 = lang_classes_factory.ns.Identity(name = "Id ServiceAccount_1")
cred_u1 = lang_classes_factory.ns.Credentials(name = "Cred Admin_1")
cred_u2 = lang_classes_factory.ns.Credentials(name = "Cred Employee_1")
cred_mfa = lang_classes_factory.ns.Credentials(name = "MFA")
model.add_asset(id_u1)
model.add_asset(id_u2)
model.add_asset(id_u3)
model.add_asset(cred_u1)
model.add_asset(cred_u2)
model.add_asset(cred_mfa)

### Associations
assoc_id_u1_cred_u1 =\
    lang_classes_factory.ns.IdentityCredentials(
    identities = [id_u1],
    credentials = [cred_u1]
    )
model.add_association(assoc_id_u1_cred_u1)

assoc_id_u2_cred_u2 =\
    lang_classes_factory.ns.IdentityCredentials(
    identities = [id_u2],
    credentials = [cred_u2]
    )
model.add_association(assoc_id_u2_cred_u2)

assoc_cred_u1_cred_mfa =\
    lang_classes_factory.ns.ConditionalAuthentication(
    credentials = [cred_u1],
    requiredFactors = [cred_mfa]
    )
model.add_association(assoc_cred_u1_cred_mfa)

assoc_exec_privs_u1 =\
    lang_classes_factory.ns.HighPrivilegeApplicationAccess(
    highPrivAppIAMs = [id_u1],
    highPrivApps = [app_1_0, app_2_0]
    )
model.add_association(assoc_exec_privs_u1)

assoc_exec_privs_u2 =\
    lang_classes_factory.ns.ExecutionPrivilegeAccess(
    executionPrivIAMs = [id_u2],
    execPrivApps = [app_1_0, app_1_1]
    )
model.add_association(assoc_exec_privs_u2)

assoc_exec_privs_u3 =\
    lang_classes_factory.ns.HighPrivilegeApplicationAccess(
    highPrivAppIAMs = [id_u3],
    highPrivApps = [app_2_0]
    )
model.add_association(assoc_exec_privs_u3)




# User Section
## User

# Attack Vectors Section

## Software Vulnerabilities


# Attacker section
#attacker1 = malmodel.Attacker()
#attacker1.entry_points = [(net_2, ["fullAccess"])]
#model.add_attacker(attacker1)

# Save model configurations to a JSON file
model.save_to_file('model_1.json')