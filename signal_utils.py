import matplotlib.pyplot as plt

def custom_plot(graphs, title, x_label, y_label, legends=None, x_axis=None, colors=None, stem=False):
    legends = legends if legends != None else [f"graph {i}" for i in range(len(graphs))]
    colors = colors if colors != None else ["blue" for i in graphs]
    if stem:
        for graph, legend, color in zip(graphs, legends, colors):
            plt.stem(graph, markerfmt=color, linefmt=color, label=legend)
    else:
        for graph, legend, color in zip(graphs, legends, colors):
            plt.plot(graph, label=legend, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()

def is_periodic(signal, period):
    for i in range(period, len(signal)):
        if signal[i] != signal[i - period]:
            return False
    return True