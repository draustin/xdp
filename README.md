# Experimental documentation project (XDP)

XDP aims to develop simple, robust and user-friendly tools for interactive authoring of scalable collections of linked dynamic documents.

*Linked document collections* contain rich cross references including figures, headings, formulae, code listings, etc. The collection may be in the form of a static website or a book.

*Scalable* means that documents and collections of documents may be combined without loss of internal organization e.g. the ability to cross reference. This implies a scalable system of identifiers for document elements to support cross referencing.

*Dynamic documents* contain the output of code intermingled with other elements such as text and figures. This is sometimes referred to as literate programming, although LP was originally conceived as a means of documenting the logic of computer programs. While documenting programs is one motivation for XDP, I'm also concerned with the creation of scientific/technical reports. Existing related tools include Jupyter Notebook, Sweave, Knitr, Pweave, and Codebraid.

*Interactive authoring* means live compilation. When combined with the requirement for scalability this means incremental compilation. Simplicity and user-friendlyness require that the result of live compilation is identical to the final output rather than some simplified "live preview".

My preferred programming language is Python and my preferred markup language is Markdown. However I would like XDP to be as extensible to different languages as possible.

## Thoughts and sketches 1 

Main program in Python. It converts source to abstract syntax tree using Pandoc and applies filters such as document inclusion, code execution, evaluation of cross references.

Currently testing concepts for individual components in a series of experiments.  

