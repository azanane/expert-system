
from Parsing import Parser
from GlobalGraph import GlobalGraph

if __name__ == "__main__":
    try:
        parser = Parser()

        global_graph = GlobalGraph(parser)
        global_graph.print_result()
        global_graph.run()
        global_graph.print_result()

    except Exception as e:
        print(f'{str(e)}')
        exit(1)