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
