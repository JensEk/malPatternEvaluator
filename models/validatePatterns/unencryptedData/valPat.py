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

## Applications
app_1_0 = lang_classes_factory.ns.Application(name = "App 1.0_OS_Windows")
model.add_asset(app_1_0)


# DataResource Section

## Data
data_s1_1 = lang_classes_factory.ns.Data(name = "Data Secret")
model.add_asset(data_s1_1)

assoc_app_1_0_data_s1_1 =\
    lang_classes_factory.ns.AppContainment(
    containedData = [data_s1_1],
    containingApp = [app_1_0]
    )
model.add_association(assoc_app_1_0_data_s1_1)

# Mitigation Pattern Structure

# Credentials Section
encr_s1_1 = lang_classes_factory.ns.Credentials(name = "EncryptionKey")
#model.add_asset(encr_s1_1)

assoc_data_s1_1_encr_s1_1 =\
    lang_classes_factory.ns.EncryptionCredentials(
    encryptCreds = [encr_s1_1],
    encryptedData = [data_s1_1]
    )
#model.add_association(assoc_data_s1_1_encr_s1_1)

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
initial_node = graph.get_node_by_full_name('App 1.0_OS_Windows:localAccess')
initial_node_np = graph.get_node_by_full_name('App 1.0_OS_Windows:localAccess')
initial_node_np.defense_status = 1.0

target_node = graph.get_node_by_full_name('Data Secret:dataEncrypted')


#graph.save_to_file('ag.yml')
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