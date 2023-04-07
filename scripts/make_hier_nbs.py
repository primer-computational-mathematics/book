import nbformat
import sys


def extract_cells_by_tags(filename, tags, **kwargs):
    # TODO: parse notebook file and read cells and tags.
    # Then, extract cells that have the tags we require.
    nb = nbformat.read(filename, nbformat.NO_CONVERT)
    cells = []
    for cell in nb.cells:
        for tag in tags:
            if tag in cell.metadata.tags:
                cells.append(cell)
                break
    return cells


def extract_nb_metadata(filename, **kwargs):
    nb = nbformat.read(filename, nbformat.NO_CONVERT)
    return nb.metadata, nb.nbformat, nb.nbformat_minor


def write_nb_from_cells(filename, metadata, cells, **kwargs):
    nb = nbformat.NotebookNode(
        cells=cells, metadata=metadata[0], nbformat=metadata[1], nbformat_minor=metadata[2])
    nbformat.write(nb, filename)
    return True


def usage():
    print("python3 make_hier_nbs <input-filename> <output-filename> <tag1> <tag2> .... <tagn>")
    print("This splits the notebook and consumes all content with any\
           of the tags tag1, tag2, ..., tagn")
    return


def main():
    if len(sys.argv) >= 4:
        in_filename = sys.argv[1]
        out_filename = sys.argv[2]
        tags = sys.argv[3:]
    else:
        usage()
        return

    print("Attempting to read: {}, searching for tags: {}".format(in_filename, tags))
    cells = extract_cells_by_tags(in_filename, tags)
    if len(cells) > 0:
        print("Successfully extracted cells by tags")
    else:
        print("No cells matching given tags: {}".format(tags))
        return

    print("Attempting write to: {}".format(out_filename))
    metadata = extract_nb_metadata(in_filename)
    if write_nb_from_cells(out_filename, metadata, cells):
        print("Successfully wrote to: {}".format(out_filename))
    else:
        print("Error in writing to file: {}".format(out_filename))

    return


if __name__ == "__main__":
    main()
