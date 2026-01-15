"""
graph_representation.py

Exercises on graph representations.

Author: Christopher Romo
"""

import networkx as nx
import matplotlib.pyplot as plt


def expect_equal(a: any, b: any) -> None:
    """
    Compares two values and prints a message if they are not equal.

    Args:
        a (any): The first value.
        b (any): The second value.
    """

    if a != b:
        print("FAIL expected:", b, " got:", a)


def check_undirected(adj_list: dict) -> None:
    """
    Checks if the given adjacency list represents an undirected graph.

    Args:
        adj_list (dict): The adjacency list of the graph.
    """

    for node in adj_list:
        for neighbor in adj_list[node]:
            try:
                if not node in adj_list[neighbor]:
                    print("FAIL: graph is not undirected: " + str(adj_list))
                    return
            except KeyError:
                print("FAIL: missing node in adjacency list for graph " + str(adj_list))
                return


def check_self_loops(adj_list: dict) -> None:
    """
    Checks if the given adjacency list has any self-loops.

    Args:
        adj_list (dict): The adjacency list of the graph.
    """

    for node in adj_list:
        if node in adj_list[node]:
            print("FAIL: graph has a self-loop: " + str(adj_list))
            return


def list_to_dict(input_list: list) -> dict:
    """
    Converts a list of pairs into a dictionary with sets as values.

    Args:
        input_list (list): A list of pairs [(a_1,b_1),...,(a_n,b_n)].

    Returns:
        dict: A dictionary with keys a_1,a_2,...,a_n and values as sets
        {b_k such that a_k=a_i}.
    """

    return_dict = {}

    for pair in input_list:
        a = pair[0]
        b = pair[1]

        # check for key, and add the value
        if a in return_dict.keys():
            return_dict[a].add(b)
        else:
            return_dict[a] = {b}

    return return_dict


def draw_graph(adj_list, actually_draw=True) -> None:
    """
    Draws the graph represented by the given adjacency list.

    Args:
        adj_list (dict): The adjacency list of the graph.
        actually_draw (bool): Whether to actually draw the graph.
    """

    G = nx.Graph()
    for node in adj_list:
        G.add_node(node)
        G.add_edges_from([(node, neighbor) for neighbor in adj_list[node]])
    if actually_draw:
        nx.draw_spring(G, with_labels=True, font_weight="bold")
        plt.show()


def edge_list_to_adj_list(edge_list: list) -> dict:
    """
    Converts a list of edges into an adjacency list representation.

    Args:
        edge_list (list): A list of edges [(a_1,b_1),...,(a_n,b_n)].

    Returns:
        dict: An adjacency list representation of the graph.
    """

    adj_list = {}

    for pair in edge_list:
        a = pair[0]
        b = pair[1]

        # check for key, and add the value
        if a in adj_list.keys():
            adj_list[a].add(b)
        else:
            adj_list[a] = {b}

        # since edges work both ways, repeat the opposite way
        if b in adj_list.keys():
            adj_list[b].add(a)
        else:
            adj_list[b] = {a}

    return adj_list


def eulerian(edge_list: list) -> bool:
    """
    Determines if the graph represented by the given edge list is Eulerian.

    Args:
        edge_list (list): A list of edges [(a_1,b_1),...,(a_n,b_n)].

    Returns:
        bool: True if the graph is Eulerian, False otherwise.
    """

    adj_list = edge_list_to_adj_list(edge_list)
    is_eulerian = False

    for node in adj_list.keys():
        even_count = 0
        odd_count = 0

        # number of edges per node
        edge_count = len(adj_list[node])

        # increment counts
        if edge_count % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # the graph is eulerian if it can start and end on a node with an odd
    # number of edges so 2 nodes being odd, or if all of the nodes are even.
    if odd_count == 2 or odd_count == 0:
        is_eulerian = True

    return is_eulerian


def main() -> None:
    """Program entry point."""

    # originally a jupyter notebook exercise

    # task 1

    # Create a function called list_to_dict which accepts a list of pairs
    # (a_1,b_1), (a_2,b_2),...,(a_n,b_n) and returns a dictionary with keys
    # a_1,a_2,...,a_n. The dictionary values should be set objects; the value
    # associated with key a_i should be the set {b_k:a_k=a_i}. For example, the
    # input list [(1,2),(3,4),(5,6)] should return the dictionary
    # {1: {2}, 3: {4}, 5: {6}}. Input pairs could contain strings or numbers.
    # Furthermore, you should not assume that the keys a_i are distinct; your
    # code should handle repeated keys by adding extra values to the associated
    # set. For example, the input list [(1,'a'),(1,3)] should return the
    # dictionary {1: {'a', 3}}. A concise description of the function's action
    # is described in the function's docstring below, and tests are provided.

    expect_equal(list_to_dict([]), {})
    expect_equal(list_to_dict([(1, 2), (3, 4)]), {1: {2}, 3: {4}})
    expect_equal(list_to_dict([(1, 2), (1, 3)]), {1: {2, 3}})
    expect_equal(
        list_to_dict([("a", 7), (10, "b"), ("simple key", "simple value")]),
        {"a": {7}, 10: {"b"}, "simple key": {"simple value"}},
    )

    # task 2

    # Create a function called edge_list_to_adj_list which accepts a list of
    # edges (that is, vertex pairs) and returns an adjacency-list
    # representation of the same graph according to the formatting described
    # above. Several tests are provided to help you check your work. If your
    # function works properly, the mystery graph will be visualized and show
    # you a neat pattern.

    expect_equal(edge_list_to_adj_list([]), {})
    expect_equal(edge_list_to_adj_list([("A", "B")]), {"A": {"B"}, "B": {"A"}})
    expect_equal(
        edge_list_to_adj_list([("A", "B"), ("C", "D")]),
        {"A": {"B"}, "B": {"A"}, "C": {"D"}, "D": {"C"}},
    )
    expect_equal(
        edge_list_to_adj_list([("A", "B"), ("C", "D"), ("B", "D")]),
        {"A": {"B"}, "B": {"D", "A"}, "C": {"D"}, "D": {"C", "B"}},
    )
    expect_equal(
        edge_list_to_adj_list(
            [("A", "B"), ("A", "C"), ("A", "D"), ("C", "D"), ("B", "C"), ("B", "D")]
        ),
        {
            "A": {"D", "C", "B"},
            "B": {"D", "A", "C"},
            "C": {"D", "A", "B"},
            "D": {"A", "C", "B"},
        },
    )

    mystery_graph = [
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("A", "E"),
        ("A", "F"),
        ("B", "C"),
        ("B", "D"),
        ("B", "E"),
        ("B", "G"),
        ("C", "D"),
        ("C", "E"),
        ("C", "H"),
        ("D", "E"),
        ("D", "I"),
        ("E", "J"),
    ]
    check_self_loops(edge_list_to_adj_list(mystery_graph))
    check_undirected(edge_list_to_adj_list(mystery_graph))
    draw_graph(edge_list_to_adj_list(mystery_graph))

    # task 3

    # Complete the function definition below for function eulerian. The
    # function's input should be a graph represented as an edge list. If the
    # input graph is Eulerian, the function should output True, and if the
    # input graph is not Eulerian, the function should output False. Note: you
    # can assume that the input graph is connected (that is, that a path exists
    # between every pair of vertices). Use whatever technique you want to
    # determine Eulerianness!

    expect_equal(eulerian([("A", "B")]), False)
    expect_equal(eulerian([("A", "B"), ("B", "C")]), False)
    expect_equal(eulerian([("A", "B"), ("B", "C"), ("A", "C")]), True)
    expect_equal(eulerian([("A", "B"), ("B", "C"), ("A", "D"), ("C", "D")]), True)
    expect_equal(
        eulerian(
            [
                ("A", "B"),
                ("B", "C"),
                ("A", "D"),
                ("C", "D"),
                ("B", "D"),
                ("D", "E"),
                ("E", "B"),
            ]
        ),
        True,
    )
    expect_equal(
        eulerian(
            [
                ("A", "B"),
                ("A", "C"),
                ("A", "D"),
                ("A", "E"),
                ("B", "C"),
                ("B", "D"),
                ("B", "E"),
                ("C", "D"),
                ("C", "E"),
                ("D", "E"),
            ]
        ),
        True,
    )
    expect_equal(eulerian(mystery_graph), False)


if __name__ == "__main__":
    main()
