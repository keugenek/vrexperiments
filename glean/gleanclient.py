import json

nodes = []
with open('flow-facts.json') as f:
    lines = f.readlines()
    for line in lines:
         line_dict = json.loads(line)
         nodes.append({ 'id': line_dict['id'], 'name': line_dict['key'], 'value': 0  })

edges = []
with open('flow-imports.json') as f:
    lines = f.readlines()
    for line in lines:
         line_dict = json.loads(line)
         edges.append({ 'source': line_dict['key']['tuplefield0']['id'], 'target': line_dict['key']['tuplefield1']['id']  })

nodes_and_edges = {'nodes': nodes, 'links': edges }

with open('output/diagram.json', 'w') as json_file:
    json.dump(nodes_and_edges, json_file)

