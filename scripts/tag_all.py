import sys
import nbformat
import copy

def usage():
    print("python3 tag_all <input-filename> <tag1> <tag2> .... <tagn>")
    print("This script adds the given tags to all cells in a file.")
    return


def add_tags(filename, tags):
    """
    Add the list of tags to each cell in a given notebook.
    """
    nb = nbformat.read(filename, nbformat.NO_CONVERT)
    cells = []
    for cell in nb.cells:
        tcell = copy.deepcopy(cell)
        if "tags" in tcell["metadata"]:
            tcell["metadata"]["tags"].extend(tags)
        else:
            tcell["metadata"]["tags"] = list(tags)
        cells.append(tcell)
    new_nb = nbformat.NotebookNode(cells=cells, metadata=nb.metadata,
                                   nbformat=nb.nbformat, 
                                   nbformat_minor=nb.nbformat_minor)
    nbformat.write(new_nb, filename)
    return True


def main():
    if len(sys.argv) >= 3:
        in_filename = sys.argv[1]
        tags = sys.argv[2:]
    else:
        usage()
        return
    print("Tagging all cells in {} with tag(s) {}".format(in_filename, tags))
    if add_tags(in_filename, tags):
        print("Successfully tagged")

if __name__ == "__main__":
    main()
