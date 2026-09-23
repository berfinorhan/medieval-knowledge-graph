from rdflib import Graph
from pyshacl import validate

def run_validation():
    print("Loading graph data and SHACL shapes...")
    data_graph = Graph().parse("medieval-mini.ttl", format="turtle")
    shapes_graph = Graph().parse("shapes/medieval.shacl.ttl", format="turtle")

    # Run validation
    conforms, results_graph, results_text = validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        inference='rdfs',
        debug=False
    )

    if conforms:
        print(" SUCCESS: All data conforms to the SHACL shapes.")
    else:
        print(" ERROR: Validation errors detected:\n")
        print(results_text)

if __name__ == "__main__":
    run_validation()