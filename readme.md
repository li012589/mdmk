# MDMK

Continually generate pdf from a markdow file.

## Usage

### parameters

**pdf_engine**: latex engine to use, default is "xelatex";

**highlight_style**: code block highlight style, default is "zenburn";

**urlcolor**: URL color, default is "NavyBlue";

**file**: md file path;

**o**: output pdf file path;

**CJKmainfont**: 中文字体, 默认为"Kai";

**geometry**: layout of the pdf, default is "top=2cm, bottom=1.5cm, left=2cm, right=2cm";

**per**: time to wait, default is 5.

## Example

**example section**

latex:
$$
\begin{equation}
\mathbf{h} = \begin{bmatrix}

\frac{\kappa}{2}\cdot2 &\frac{\kappa}{2}\cdot-1 & & \\
 \frac{\kappa}{2}\cdot-1 &\frac{\kappa}{2}\cdot2 &\frac{\kappa}{2}\cdot-1 &\\
 & & \ddots & \\
 & &\frac{\kappa}{2}\cdot-1 &\frac{\kappa}{2}\cdot2 &\frac{\kappa}{2}\cdot-1 & \\
 & & &\frac{\kappa}{2}\cdot-1& \frac{\kappa}{2}\cdot2 \\
 & & & & &\frac{1}{2} \\
 & & & & & &\ddots \\
 & & & & & & &\frac{1}{2}
\end{bmatrix}
\end{equation}
$$
python code:

```python
# This is pseudocode
sum = 0
factor = 1 # for EXPMV this is lambda
accumulator = 1
for i in range(infty):
    if |accumulator| >= epsilon:
        break
    accumulator *= Q
    sum += factor/n.dot(accumulator)
 return sum
```

**Run this**:

```bash
python ./mdmk.py -file ./readme.md
```



