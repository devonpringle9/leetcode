class Solution(object):

    '''
    A set for each connected graph.
    Check for every single pair being connected.
    '''

    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        connected_graphs = [[x] for x in range(n)]
        for edge in edges:
            print(f"adding {edge} to {connected_graphs}")
            graph_0 = graph_1 = []
            for i, graph in enumerate(connected_graphs):
                if edge[0] in graph:
                    print(f'vertex {edge[0]} is in {graph}')
                    graph_0 = i
                if edge[1] in graph:
                    print(f'vertex {edge[1]} is in {graph}')
                    graph_1 = i

            # skip if there are the same graph
            if graph_0 == graph_1:
                continue
            else:
                # add the second graph to the first one and delete the second graph
                connected_graphs[graph_0] = list(set(connected_graphs[graph_0] + connected_graphs[graph_1]))
                connected_graphs.pop(graph_1)
            print(f'Now there is {connected_graphs}')
        print(f'Final set of graphs are {connected_graphs}')

        # Objective: return True if the set of vertices is a complete graph
        # Recursive function
        # if the list is 1 then return True
        # Check that the first vertex is connected with the ones after it
        # Recurse with the list excluding the first index
        def complete_graph(graph, edges):
            if len(graph) == 1:
                return True
            else:
                check_these = [[graph[0], i] for i in graph[1:]]
                if all([x in edges for x in check_these]):
                    return True and complete_graph(graph[1:], edges)
                else:
                    return False

        total_complete_graphs = 0
        for graph in connected_graphs:
            print(f"Checking completeness of {graph}")
            if complete_graph(graph, edges):
                total_complete_graphs += 1
            print(complete_graph(graph, edges))
        print(f"Total complete graphs is {total_complete_graphs}")
        return total_complete_graphs

Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]])
