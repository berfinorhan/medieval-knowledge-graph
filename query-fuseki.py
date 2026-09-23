import requests

# The URL where the Fuseki server listens for queries
url = "http://localhost:3030/medieval/sparql"

# The SPARQL question to ask
query = """
PREFIX medieval: <https://example.org/medieval-mini#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?personName ?placeName
WHERE {
    ?person a medieval:King ;
        medieval:bornIn ?place ;
        rdfs:label ?personName .
    ?place rdfs:label ?placeName .
}
"""

# Send the question to Fuseki and ask for JSON back
response = requests.get(url, params={'query': query, 'format': 'json'})
data = response.json()

# Print the answers
for result in data['results']['bindings']:
    print(f"{result['personName']['value']} was born in {result['placeName']['value']}")
