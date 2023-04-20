The online book is available here:

https://primer-computational-mathematics.github.io/book/intro


### Local building instructions

We will assume that your machine has the following software installed

- `git`, e.g. [Git for Windows](https://git-scm.com/downloads)
- `python3` with `pip`, e.g. from the [Anaconda distibution](https://www.anaconda.com/products/individual)

#### The first time
You will need to do the following pre-setup
1. Download the repository, e.g. by running the following in a git terminal
   ```
   git clone https://github.com/primer-computational-mathematics/book.git
   ```
   
2. Install the Python prerequisites, e.g. by running the following in an Anaconda prompt open inside the new repository.
   ```
   pip install -r requirements.txt.
   ```
   This is also necessary to update from Jupyter book version 0.6


#### To build and serve the book

1. Run the following in an Anaconda prompt open inside the repository
   ```
   python scripts/generate_new_toc.py
   python3 scripts/add_modules.py
   set PYTHONUTF8=1
   cd _tmp
   jupyter-book toc migrate _toc.yml -o _toc.yml
   jupyter book build .
   ```

   The finished book will then be available at the URL shown.
   
