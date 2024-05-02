# malPatternEvaluator


1. git clone https://github.com/JensEk/malPatternEvaluator.git
2. pip install -r requirements.txt
3. Connect to Neo4j desktop instance:
     uri="bolt://localhost:7687",
     username="neo4j",
     password="dynp12345!",
     dbname="neo4j",
5. python3 mpe.py -m models/model_1.json -p patterns.json
