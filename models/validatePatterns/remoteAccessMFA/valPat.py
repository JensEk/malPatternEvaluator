import logging

import maltoolbox
from maltoolbox.language import LanguageGraph, LanguageClassesFactory
from maltoolbox.model import Model, AttackerAttachment
from maltoolbox.attackgraph import AttackGraph, query
from maltoolbox.attackgraph.analyzers import apriori
from maltoolbox.ingestors import neo4j


logger = logging.getLogger(__name__)

lang_file = '../../../org.mal-lang.coreLang-1.0.0.mar'
lang_graph = LanguageGraph.from_mar_archive(lang_file)
lang_classes_factory = LanguageClassesFactory(lang_graph)
model = Model('M1', lang_classes_factory)

# badPattern structure

app_2_0 = lang_classes_factory.ns.Application(name = "App 2.0_Server_Windows")
app_2_1 = lang_classes_factory.ns.Application(name = "App 2.1_RemoteAccess_TeamViewer")
model.add_asset(app_2_0)
model.add_asset(app_2_1)

assoc_app_2_0_app_2_1 =\
    lang_classes_factory.ns.AppExecution(
    hostApp = [app_2_0],
    appExecutedApps = [app_2_1]
    )
model.add_association(assoc_app_2_0_app_2_1)

id_u2 = lang_classes_factory.ns.Identity(name = "Id Employee_1")
cred_u2 = lang_classes_factory.ns.Credentials(name = "Cred Employee_1")
model.add_asset(id_u2)
model.add_asset(cred_u2)

assoc_exec_privs_exec_u2 =\
    lang_classes_factory.ns.ExecutionPrivilegeAccess(
    executionPrivIAMs = [id_u2],
    execPrivApps = [app_2_1]
    )
model.add_association(assoc_exec_privs_exec_u2)


# mitigationPattern structure

cred_mfa = lang_classes_factory.ns.Credentials(name = "MFA")
#model.add_asset(cred_mfa)

assoc_cred_u2_mfa =\
    lang_classes_factory.ns.ConditionalAuthentication(
    credentials = [cred_u2],
    requiredFactors = [cred_mfa]
    )
#model.add_association(assoc_cred_u2_mfa)


# Attack Vectors Section

# Attacker section
attacker1 = AttackerAttachment()
model.add_attacker(attacker1)


# Save model configurations to a JSON file
model.save_to_file('patternInstance.json')


#Attack Graph Section
graph = AttackGraph(lang_graph, model)
graph.attach_attackers()

# Start and end node to validate the pattern
initial_node = graph.get_node_by_full_name('Cred Employee_1:attemptCredentialTheft')
initial_node_np = graph.get_node_by_full_name('Cred Employee_1:attemptCredentialTheft')
#initial_node_np.defense_status = 0.0

target_node = graph.get_node_by_full_name('App 2.1_RemoteAccess_TeamViewer:fullAccess')


graph.save_to_file('ag.yml')
apriori.calculate_viability_and_necessity(graph)
graph.save_to_file('post_ag.yml')

attacker = graph.attackers[0]
attacker.compromise(initial_node)



with open('validateLog_bad.txt', 'w') as log_file:
    print('Reached attack steps:', file=log_file)
    for step in graph.attackers[0].reached_attack_steps:
        print(step.full_name, file=log_file)

    print('\nAttack Surface:', file=log_file)
    for step in query.get_attack_surface(graph.attackers[0]):
        print(step, file=log_file)

    print('\nDefense Surface:', file=log_file)
    for step in query.get_defense_surface(graph):
        print(step.full_name, file=log_file)

    print('\nEnabled Defenses:', file=log_file)
    for step in query.get_enabled_defenses(graph):
        print(step.full_name, file=log_file)

    print('\nTarget node can be reached:', file=log_file)
    if query.is_node_traversable_by_attacker(target_node, attacker1):
        print(f'{target_node.full_name} is traversable by attacker', file=log_file)


model.save_to_file('processed_model.yml')

neo4j.ingest_model(model,
                "bolt://localhost:7687", 
                "neo4j",
                "dynp12345!",
                "neo4j",
            delete=True)
 
neo4j.ingest_attack_graph(graph,
                "bolt://localhost:7687", 
                "neo4j",
                "dynp12345!",
                "neo4j",
            delete=False)


