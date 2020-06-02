The online book is available here:

https://primer-computational-mathematics.github.io/book/intro


### Local building instructions

We will assume that your machine has the following software installed

- `git`, e.g. [Git for Windows](https://git-scm.com/downloads)
- `python3` with `pip`, e.g. from the [Anaconda distibution](https://www.anaconda.com/products/individual)
- `ruby`, e.g. from the [RubyInstall for Windows](https://rubyinstaller.org/downloads/) (you will need a version _with_ the devkit, such as Ruby+Devkit 2.6.6-1 )

#### The first time
You will need to do the following pre-setup
1. Download the repository, e.g. by running the following in a git terminal
   ```
   git clone https://github.com/primer-computational-mathematics/book.git
   ```
   
2. Install the Python prerequisits, e.g. by running the following in an Anaconda prompt open inside the new repository.
   ```
   pip install -r requirements.txt.

3. Install the Ruby prerequisits, e.g. by running the foliowing in a Ruby prompt
open inside the new repository
   ```
   gem install bundle
   bundle install
   ```


#### To build and serve the book

1. Run the following in an Anaconda prompt open inside the repository
   ```
   python scripts/generate_toc.py
   jupyter book build .
   ```

2. Run the following in a Ruby prompt open inside the repository
   ```
   bundle exec jekyll serve
   ```
   The finished book will then be available at the URL shown.
   
