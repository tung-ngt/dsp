import matplotlib.pyplot as plt

def custom_plot(graphs, title, x_label, y_label, legends=None, x_axis=None, colors=None, stem=False, overlapped = True, hstack = True):
    legends = legends if legends != None else [f"graph {i}" for i in range(len(graphs))]
    colors = colors if colors != None else ["blue" for i in graphs]

    if overlapped:
        if stem:
            for graph, legend, color in zip(graphs, legends, colors):
                plt.stem(graph, markerfmt=color, linefmt=color, label=legend)
        else:
            for graph, legend, color in zip(graphs, legends, colors):
                if x_axis is None:
                    plt.plot(graph, label=legend, color=color)
                else:
                    plt.plot(x_axis, graph, label=legend, color=color)
                
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.show()

    else:
        fig, plots = plt.subplots(len(graphs), 1, sharex=True)
        fig.tight_layout()
        if stem:
            for plot, graph, legend, color in zip(plots, graphs, legends, colors):
                plot.stem(graph, markerfmt=color, linefmt=color)
                plot.title.set_text(legend)
        else:
            for plot, graph, legend, color in zip(plots, graphs, legends, colors):
                if x_axis is not None:
                    plot.plot(x_axis, graph, label=legend, color=color)
                else:
                    plot.plot(graph, label=legend, color=color)

                plot.title.set_text(legend)

        fig.suptitle(title)
        fig.supylabel(y_label)
        plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.9)
        plt.xlabel(x_label)
        plt.show()

def is_periodic(signal, period):
    for i in range(period, len(signal)):
        if signal[i] != signal[i - period]:
            return False
    return True