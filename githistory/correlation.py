from pydriller import Repository
import json

limit = 5000

nodes = {}
edges = []
for commit in Repository('C:/Projects/Projects/temp/UnrealEngine').traverse_commits():
    print(commit.hash)
    print(commit.msg)
    print(commit.author.name)
    print(limit)

    if len(commit.modified_files) > 100:
        continue

    for file in commit.modified_files:
        edges.append({'source': commit.hash, 'target': file.filename})
        nodes[commit.hash] = {'id': commit.hash, 'name': commit.author.name, 'message': commit.msg}
        nodes[file.filename] = {'id': file.filename, 'name': file.filename}

    limit -= 1
    if limit == 0:
        break

nodes_and_edges = {'nodes': list(nodes.values()), 'links': edges }

with open('output/diagram.json', 'w') as json_file:
    json.dump(nodes_and_edges, json_file)

