# malPatternEvaluator


1. git clone https://github.com/JensEk/malPatternEvaluator.git
2. pip install -r requirements.txt
3. Connect to Neo4j desktop instance:
     uri="bolt://localhost:7687",
     username="neo4j",
     password="dynp12345!",
     dbname="neo4j",
5. python3 mpe.py -m models/mX/model_X.json -p patterns.json



## Pattern collections
| Group of patterns | Pattern name | Pattern description | Pattern impact/abuse case | Target assets | ATT&CK Techniques | ATT&CK Mitigation | Model | Adversery Prerequisite |
| ----------------- | ------------ | ------------------- | ------------------------- | ------------- | ----------------- | ----------------- | ----- | ---------------------- |
| Identity & Access | remoteAccessMFA | Identifies [Credentials] linked to [Application] with name matching of remote access where association {ConditionalAuthentication} is missing. | Missing Multi-Factor Authentication (MFA) on a remote access service may enable successful authentication by brute force attacks or login with compromised credentials. | Identity, Credentials | T1110, T1133, T1078 | M1036, M1032, M1030, M1017 | M1 | - |
| Identity & Access | highPrivAccountsMFA | Identifies [Credentials] linked to a [User] associated [Identity] with extended privileges where association {ConditionalAuthentication} is missing. | Missing Multi-Factor Authentication (MFA) on accounts with high privileges may enable lateral movements and unauthorized access to resources. | Identity, Credentials | T1078, T1110 | M1032, M1027, M1026 | M1 | Compromised network/system |
| Identity & Access | shadowAdmin | Identifies [User] associated [Identity] with {highPrivAppIAMs} association to [Application] where name is not matching admin/root. | User accounts that have inadvertently been assigned admin privilege may enable attackers to control accounts with unrestricted access and movement | Identity | T1199, T1078 | M1032, M1018, M1026, M1036 | M1 | Compromised network/system |
| Identity & Access | groupIdentityAppMismatch | Identifies [Identity] with {memberOf} association to a [Group] where the [Identity] has different privileges than the [Group] on an [Application]. | Misconfigured privileges may enable unauthorized access and permissions to applications in a network. | Identity, Group, Privileges | T1078, T1613, T1046 | M1026 | M1 | Compromised network/system |
| Identity & Access | groupIdentityDataMismatch | Identifies [Identity] with {memberOf} association to a [Group] where the [Identity] has different privileges than the [Group] on a [Data]. | Misconfigured privileges may enable unauthorized access and permissions to resources. | Identity, Group, Privileges | T1078, T1613, T1046 | M1026 | M1 | Compromised network/system |
| Identity & Access | highPrivServiceAccounts | Identifies [Identity] with name matching of service account  with {highPrivAppIAMs} association. | Existence of service, support or any other non user accounts with excessive privileges may facilitate lateral movement and access to network resources. | Identity | T1078,T1087,T1072,T1021 | M1027,M1036,M1035,M1030,M1033 | M1 | Compromised network/system |
| Identity & Access | accountManagerMFA | Identifies [Identity] with {managers} association to another [Group], [Identity], or [Privileges] where association {ConditionalAuthentication} is missing. | Adversaries may modify permissions or credentials to compromised accounts to maintain or elevate access to a network and its systems. | Identity, Credentials | T1098, T1136,T1531 | M1032, M1026 | M1 | Compromised network/system |
| Identity & Access | identityDiscovery | Identifies [Application] with multiple associated [Identity] with different types of privileges on the [Application]. | Adversaries may attempt to enumerate valid accounts on compromised networks or systems to facilitate lateral movement and privilege escalation. | Identity | T1087 | M1028 | M1 | Compromised network/system |
| DataResource | unencryptedData | Identifies [Data] linked to an [Application] where associated {encryptCreds} are missing. | Sensitive data (e.g., credentials, keys, tokens) stored in plaintext without encryption may be susceptible to unauthorized access and compromise. | Data | T1552, T1539, T1555, T1005, T1565 | M1041, M1047, M1027, M1057 | M2 | Compromised network/system |
| DataResource | unencryptedInfo | Identifies [Information] linked to a [Data] where associated {encryptCreds} are missing. | Sensitive information (e.g., credentials, keys, tokens) stored in plaintext without encryption may be susceptible to unauthorized access and compromise. | Information | T1552, T1539, T1555, T1005, T1565 | M1041, M1047, M1027, M1057 | M2 | Compromised network/system |
| DataResource | dataAiTM | Identifies [Data] with association {transitData} to a [Network] where [User] have physical access to the [Network]. | An adversary may attempt to position themselves to intercept data in transit between two network devices to intercept and collect data. | Data | T1557,T1040 | M1041, M1037, M1035 | M2 | Physical access |
| DataResource | dataDestruction | Identifies [Data] where [Identity] is associated with {writingIAMs} or {deletingIAMs} | Adversaries may attempt to destroy data to disrupt operations by deleting or corrupting data. | Data | T1485, T1486, T1561 | M1053 | M2 | Compromised network/system |
| User | userExposedNetworks | Identifies [Network] where [User] exists but [IDPS] or other [Application] matching a security tool is missing. | Networks without any security tool may facilitate user targeted attack such as phishing to deliver malicious attachments or links which are not detected and blocked. | User, Network | T1566, T1204, T1534 | M1049, M1031, M1017 | M1, M2,M3 | - |
| User | userImpersonation | Identifies [User] with an associated [Identity] that is linked to another [User]. | Adversaries may try to impersonate a trusted person in order to persuade and trick other users conduct actions on their behalf. | User | T1656 | M1019, M1017 | M1, M2 | - |
| Vulnerability | exploitVulnerablePublicApp | Identifies [Application] linked to a [SoftwareVulnerability] with association {ingoingAppConnections} to a [Network] not identified as DMZ. | Application with known vulnerabilities accessible from the internet may be exploited by attackers to gain unauthorized access to the network and resources. | Application, SoftwareVulnerability | T1190 | M1030, M1051, M1016 | M2 | - |
| Vulnerability | exploitVulnerableApp | Identifies [SoftwareVulnerability] linked to an [Application] or [SoftwareProduct] with associated [Identity]. | Applications with known vulnerabilities may be exploited by attackers to elevate privileges or to bypass security features. | Application, SoftwareProduct, SoftwareVulnerability | T1203, T1211,T1068 | M1051, M1048 | M2 | Compromised network/system |
| Network | activeNetworkScan | Identifies [Network] with linked [Application] which is not identified as DMZ but with {ingoingNetConnections} association to a [RoutingFirewall]. | A network that allows ingoing traffic may enable active reconnaissance scans that probes infrastructure via network traffic to gather information. | Network, ConnectionRule | T1595, T1590 | M1056 | M2,M3 | - |
| Network | nonSegmentedPublicApp | Identifies [Application] with name matching as an internet-facing service with {ingoingAppConnections} association to a [Network] that is not identified as DMZ. | Internet facing applications that are not segmented from the internal network may be exploited by attackers to gain unauthorized access to the network and resources. | Network, ConnectionRule, Application | T1190, T1133, T1210 | M1030 | M3 | - |
| Network | networkPerimeterCompromise | Identifies [RoutingFirewall] with associated [Application] or [Hardware] with an [Identity] linked to it. | By compromising perimeter network devices adversaries may try to bridge network boundaries to bypass restrictions on traffic routing. | RoutingFirewall | T1599 | M1043, M1032, M1027 | M3 | Compromised network/system |
| ComputeResource | userExposedHardware | Identifies [Hardware] with {hostHardware} association to a [Network] linked [Application] where a [User] is not matching name of [Hardware]. | Adversaries may deliver malware through removable media such as USB and use the Autorun features when inserted into hardware to gain access to the network and resources. Alternatively, adversaries may introduce hardware devices into a system or network to gain access. | Hardware | T1200, T1091 | M1034, M1040 | M2,M3 | Physical access |
| ComputeResource | zoneExposedHardware | Identifies [Hardware] where a [User] is not associated with the [PhysicalZone] linked to the [Hardware]. | Adversaries may deliver malware through removable media such as USB and use the Autorun features when inserted into hardware to gain access to the network and resources. Alternatively, adversaries may introduce hardware devices into a system or network to gain access. | Hardware, PhysicalZone | T1200, T1091 | M1034, M1040 | M3 | Physical access |
| ComputeResource | supplyChainVulnApp | Identifies [Application] with associated [SoftwareProduct] where no {protectedApps} association to an [IDPS] exists. | Supply chain compromise may enable adversaries to exploit vulnerabilities in software to gain unauthorized access to the network and resources. | Application, SoftwareProduct | T1195 | M1016, M1051, M1033 | M2 | - |
| ComputeResource | containerCompromise | Identifies [Application] with name matching of containerized services where [Identity] with extended privileges exists. | Adversaries may deploy malicious containers to facilitate execution or evade defenses. Alternatively, they may try to break out of a container to gain access to the underlying host. | Application | T1610, T1611, T1613 | M1047, M1048, M1038 | M3 | Compromised network/system |
| ComputeResource | taintSharedStorage | Identifies [Data] that is hosted on [Hardware] or contained in [Application] where multiple [Identity] have write privileges indicating shared storage. | Shared storage locations may be abused by adversaries to deliver payloads or move laterally within a network. | Application,Hardware | T1080 | M1022, M1049 | M2 | Compromised network/system |
| ComputeResource | remoteAccessC2 | Identifies [Application] with name matching of remote access tools where no {protectedApps} association to an [IDPS] exists. | Legitimate remote access tools may be exploited by adversaries to establish command and control channels to control compromised systems and exfiltrate data. | Application | T1219,T1041 | M1031, M1037 | M1 | Compromised network/system |
