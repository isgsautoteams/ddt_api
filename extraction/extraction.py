import cv2
from pathlib import Path
from matplotlib import pyplot as plt
from IPython.display import display, HTML
import os
os.environ["USE_DD_PILLOW"]="True"
os.environ["USE_DD_OPENCV"]="False"
import deepdoctection as dd

def extract_text(file_path): 
    analyzer =dd.get_dd_analyzer(config_overwrite=
    ["PT.LAYOUT.WEIGHTS=microsoft/table-transformer-detection/pytorch_model.bin",
        "PT.ITEM.WEIGHTS=microsoft/table-transformer-structure-recognition/pytorch_model.bin",
        "PT.ITEM.FILTER=['table','column_header','projected_row_header','spanning']",
        "OCR.USE_DOCTR=True",
        "OCR.USE_TESSERACT=False",
        "TEXT_ORDERING.INCLUDE_RESIDUAL_TEXT_CONTAINER=True",
        "TEXT_ORDERING.PARAGRAPH_BREAK=0.01", 
        "TEXT_ORDERING.BROKEN_LINE_TOLERANCE= 0.2",
        "TEXT_ORDERING.HEIGHT_TOLERANCE= 2.0",
        "TEXT_ORDERING.FLOATING_TEXT_BLOCK_CATEGORIES=['text']",
        "TEXT_ORDERING.TEXT_BLOCK_CATEGORIES=['table','text', 'list']",
        "TEXT_ORDERING.PARAGRAPH_BREAK=0.1",
        "USE_TABLE_REFINEMENT=True",
                            ])
    data = []
    df = analyzer.analyze(path=file_path)
    df.reset_state()
    doc=iter(df)
    try:
        for i in range(5):
            page = next(doc)
            data.append(page.text)
    except StopIteration:
        print("The PDF has only one page.")
        data.append(page.text)
    return data
