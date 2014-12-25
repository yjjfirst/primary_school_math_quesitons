.PHONY: all clean

check:
	@if [ "$(MAX)" = "" -o "$(MIN)" = "" -o "$(PAGES)" = "" ]; then \
	          echo You need to specify right parameters ;exit 1; \
        fi	
ks.txt: 
	@echo "Generating txt file"
	./ks_gen.py -m $(MAX) -n $(MIN) -p $(PAGES) > ks.txt
ks.tex: ks.txt
	@echo "Generating tex file"
	./latex_gen.py < ks.txt > ks.tex
ks.dvi: ks.tex
	@echo "Generating dvi file"
	latex ks.tex
ks.ps: ks.dvi
	@echo "Generating ps file"
	dvips -Ppdf -G0 ks.dvi
ks.pdf :ks.ps
	@echo "Generating pdf file"
	ps2pdf ks.ps

all: ks.pdf

clean:
	rm ks.*
