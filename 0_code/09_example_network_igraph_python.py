import os
import importlib
import pandas as pd
import igraph as ig
# ============================
#### Import function to use pandas dataframe ####
# ============================
fun2use1 = importlib.import_module(r"10_igraph_from_pandas")
# to reload an already imported (but recently modified) module: importlib.reload(fun2use)


# ============================
#### pandas tables of vertices and edges ####
# ============================
# data URLs
data_dir = os.path.join('..', '1_data')

vertices_table = pd.read_csv(os.path.join(data_dir,'vertices_table.csv'))
edges_table = pd.read_csv(os.path.join(data_dir,'edges_table.csv'))

# ============================
#### build igraph graph from pandas tables ####
# ============================
relations_graph = fun2use1.igraph_from_pandas(edges_table=edges_table, vertices_table=vertices_table, source_cl='start', target_cl='end', vertex_attrs=list(vertices_table.columns), vertex_id_cl='name', directed=True)

# ============================
#### see graph properties ####
# ============================
print(relations_graph.summary())
relations_graph.vs['name']
relations_graph.vs['age']
relations_graph.vs['gender']
relations_graph.vs['education']

# to see node's degree (will return a list)
relations_graph.degree()

# ============================
#### plot ####
# ============================
layout = relations_graph.layout("fr")
visual_style = dict()
visual_style["vertex_size"] = 10
visual_style["vertex_label_size"] = 15
visual_style["vertex_label_dist"] = 2
# visual_style["edge_label_size"] = 10
# visual_style["edge_label_color"] = "red"
visual_style["vertex_color"] = "red"
visual_style["vertex_label_color"] = "blue"
visual_style["vertex_label"] = relations_graph.vs["name"]
visual_style["edge_width"] = 1
visual_style["layout"] = layout
visual_style["margin"] = 100
ig.plot(relations_graph, **visual_style)

# ============================
#### Different way of building graph (to include all edge attributes) ####
# ============================
gg = ig.Graph.DictList(
  vertices=vertices_table.to_dict('records'),
  edges=edges_table.to_dict('records'),
  directed=True,
  vertex_name_attr="name",
  edge_foreign_keys=('start', 'end'))

# check summary
print(gg.summary())

# to see node's degree (will return a list)
gg.degree()

# ============================
#### plot the new network (with weighted edges) ####
# ============================
layout = gg.layout("fr")
visual_style = dict()
visual_style["vertex_size"] = 10
visual_style["vertex_label_size"] = 15
visual_style["vertex_label_dist"] = 2
# visual_style["edge_label_size"] = 10
# visual_style["edge_label_color"] = "red"
visual_style["vertex_color"] = "red"
visual_style["vertex_label_color"] = "blue"
visual_style["vertex_label"] = gg.vs["name"]
visual_style["edge_width"] = [xx*2 for xx in gg.es["weight"]]
visual_style["layout"] = layout
visual_style["margin"] = 100
ig.plot(gg, **visual_style)
