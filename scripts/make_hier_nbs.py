import nbformat
import sys

def add_slideshow_tags(cell, **kwargs):
    cell["metadata"]["slideshow"] = {"slide_type": "slide"}
    return cell


def extract_cells_by_tags(filename, tags, **kwargs):
    """
    Create a subset of a notebook by extracting cells that match
    the list of tags ```tags``` provided. Returns a list of cells
    each of which is tagged by at least one of the tags in the list
    provided.
    """
    nb = nbformat.read(filename, nbformat.NO_CONVERT)
    cells = []
    tag_slides = kwargs.pop("tag_slides", False)
    # Add slideshow tags if we are extracting slides
    for tag in tags:
        if "type-slide" in tag:
            tag_slides = True
            break
    else:
        tag_slides = False
    
    for cell in nb.cells:
        for tag in tags:
            if tag in cell.metadata.tags:
                if tag_slides:
                    cell = add_slideshow_tags(cell)
                cells.append(cell)
                break  # Don't double-count cells with multiple tags
    return cells


def extract_nb_metadata(filename, **kwargs):
    """
    Extracts the metadata from a Jupyter notebook as per the format,
    described in documentation found at - 
    https://nbformat.readthedocs.io/en/latest/format_description.html

    This includes nbformat and nbformat_minor which are used by the library
    to render notebooks defined in different version specs.

    Returns a tuple (metadata, nbformat, nbformat_minor).
    """
    nb = nbformat.read(filename, nbformat.NO_CONVERT)
    return nb.metadata, nb.nbformat, nb.nbformat_minor


def write_nb_from_cells(filename, metadata, cells, **kwargs):
    """
    Creates and writes a notebook based on the cells and metadata provided.
    ```cells``` is a list of cells contained in the notebook and 
    ```metadata``` is a tuple containing the (metadata, nbformat, nbformat_minor)
    as per the format described in nbformat documentation - 
    https://nbformat.readthedocs.io/en/latest/format_description.html
    """
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
