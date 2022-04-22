MAKEFILE4LATEX_REVISION = v0.9.0
BUILDDIR = .build

PDFTOPPM_OPT += -r 150 -hide-annotations

POSTPROCESS = conv

conv: pdf
	@$(init_toolchain)
	@for f in $(target_basename); do \
		$(call exec,$(pdftoppm) $(PDFTOPPM_PNG_OPT) $$f.pdf tmp_$$f); \
		convert -trim -strip tmp_$$f.png $$f.png; \
		rm tmp_$$f.png; \
	done
