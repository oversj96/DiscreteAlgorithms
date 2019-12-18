#!/usr/bin/env python

"""reliability_polynomial.py: A python module that, given the network, builds
a reliability polynomial."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj96.github.io"

import networkx as nx
import sympy
p = sympy.symbols('p')


def rel_poly(g):
    poly = ''
    for i in range(len(g.edges()), len(g.nodes()) - 2, -1):
        if i is len(g.edges()):
            n = 1
        else:
            n = get_working_subgraphs(g, len(g.edges()) - i, 0, [])
        poly += f"{str(n) + ' * p**' + str(i) + ' * (1-p)**' + str((len(g.edges()) - i)) + ' + '}"
    poly = poly[:-2]
    return poly
    #print(sympy.sum(poly_list))

def sort_tuples(edge_list):
    n_list = []
    for edge in edge_list:
        n_list.append(sorted(edge))
    return n_list

def sort_edges(edge_list):
    return sorted(edge_list)

def get_working_subgraphs(g, count, work_count, network_list):
    # if count > 0:
    #     for i in range(0, len(g.edges())):
    #         e = sorted(g.edges())[i]
    #         contract = nx.contracted_edge(g, e, self_loops=False)
    #         if nx.is_connected(contract):
    #             get_working_subgraphs(contract, count, work_count)            
    #     return 0   

    if count == 0:
        network = list(g.edges())
        network_2 = sort_tuples(network)
        network_3 = sort_edges(network_2)
        if network_3 not in network_list:
            network_list.append(network_3)
        return len(network_list)
    else:    
        for i in range(0, len(g.edges())):
            e = list(g.edges())[i]
            ngraph = nx.MultiGraph(self_loops=False)
            ngraph.add_edges_from(g.edges())
            ngraph.remove_edge(*e)
            if nx.is_connected(ngraph):
                get_working_subgraphs(ngraph, count - 1, 0, network_list)
        return len(network_list)
        
    




if __name__ == "__main__":
    # Add nodes, then add the edges.
    # Edges are considered bi-directional in this module
    # Below are two example networks.
    # Network 1
    g = nx.MultiGraph(self_loops=False)
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('c', 'b')
    g.add_edge('c', 'd')
    g.add_edge('b', 'd')
    g.add_edge('b', 'e')
    g.add_edge('d', 'e')
    print(f"Reliablility: {rel_poly(g)}")
    # Network 2
    g = nx.MultiGraph(self_loops=False)
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('a', 'e')
    g.add_edge('d', 'e')
    g.add_edge('b', 'e')
    g.add_edge('b', 'c')
    g.add_edge('e', 'f')
    g.add_edge('c', 'f')
    print(f"Reliablility: {rel_poly(g)}")