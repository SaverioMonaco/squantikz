from pathlib import Path

# Paths
tikz_dir = Path('../tikz')
output_file = Path('./files.tex')

# List all .tex files (without the .tex extension)
tex_files = sorted(f.stem for f in tikz_dir.glob('*.tex'))

# Escape underscores for LaTeX
tex_files_escaped = [f.replace('_', r'\_') for f in tex_files]

# Write to files.tex
with output_file.open('w', encoding='utf-8') as f:
    f.write("\\newcommand*{\\showcasefiles}{")
    f.write(',\n'.join(tex_files_escaped))
    f.write("}")