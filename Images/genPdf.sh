#!/bin/sh
#ls *.svg | xargs -I{} basename {} .svg | xargs -I {} inkscape {}.svg --export-area-drawing --batch-process --export-type=pdf --export-filename={}.pdf

ls *.svg | xargs -I{} basename {} .svg | xargs -I {} convert {}.svg {}.png
