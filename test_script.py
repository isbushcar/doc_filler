import os
import re

import pandas as pd
from docx import Document

from typing import Union


print(os.path.exists('test_file.docx'))
document = Document('test_file.docx')
# SEARCH_PATTERN = '{{.*?}}'

SEARCH_PATTERN = 'отпуск'



# variables_table = pd.read_excel('test_table.xlsx')
# print(variables_table)
# print(list(enumerate(variables_table.index)))


def fill_document(
        doc_path: Union[str, os.PathLike],
        variables_table_path: Union[str, os.PathLike],
) -> str:
    variables_table = pd.read_excel(variables_table_path)
    variables_table.columns = [str(x).lower() for x in variables_table.columns]

    document_to_fill = Document(doc_path)

    for row_index in variables_table.index:
        for paragraph in document_to_fill.paragraphs:
            text = paragraph.text
            for match in re.finditer(SEARCH_PATTERN, text):
                start_pos, end_pos = match.regs[0]
                variable_name = text[start_pos:end_pos].strip('{}')
                variable_value = variables_table.loc[row_index, variable_name].lower()
                paragraph.text = paragraph.text.replace('отпуск', 'денег побольше')
                # paragraph.text = text[:start_pos] + variable_value + text[end_pos:]
                # paragraph.style = 'normal'
                print(text)
    document_to_fill.save('test.docx')
    return 'test.docx'


# fill_document('test_file_2.docx', 'test_table_2.xlsx')


from docxtpl import DocxTemplate

doc = DocxTemplate("test_file_3.docx")
context = { 'адрес' : "World company" }
doc.render(context)
doc.save("generated_doc.docx")
