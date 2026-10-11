PAPER := paper
PDF   := $(PAPER)/main.pdf
SRCS  := $(PAPER)/main.tex $(PAPER)/declarations.tex $(PAPER)/refs.bib

.PHONY: all clean

all: $(PDF)

$(PDF): $(SRCS)
	cd $(PAPER) && tectonic -X compile main.tex

clean:
	rm -f $(PDF)
