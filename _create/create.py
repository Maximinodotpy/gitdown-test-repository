from essential_generators import DocumentGenerator, MarkovTextGenerator
import os
import glob
from slugify import slugify
from faker import Faker
from mdgen import MarkdownPostProvider


NUM_DOCUMENTS = 20
ROOT = '..'




newpath = os.path.join(ROOT, 'simple')
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Clear Folder
files = glob.glob('../simple/*')
for f in files:
    os.remove(f)

def clean_name(s):
    s = ''.join([i for i in s if not i.isdigit()])
    s = s.replace("'", '')
    s = s.replace(".", '')
    s = s.replace(",", '')
    s = s.replace("-", '')
    s = s.replace("?", '')
    s = s.replace("!", '')
    s = s.replace("°", '')
    s = s.replace("*", '')
    s = s.replace("+", '')
    s = s.replace("/", '')
    s = s.replace(":", '')
    s = s.replace(";", '')
    return s


def simple():
    def markdown_content():
        fake = Faker()
        fake.add_provider(MarkdownPostProvider)
        fake_post = fake.post(size='medium')
        return fake_post

    gen = DocumentGenerator(text_generator=MarkovTextGenerator())

    template = {
        'name': 'sentence',
        'description': 'sentence',
        'content': markdown_content,
        'status': ['draft', 'trash', 'publish'],
        'category': ['programming'],
    }

    gen.set_template(template)
    for i in gen.documents(NUM_DOCUMENTS):

        name = clean_name(i['name'])
        slug = slugify(name)
        content = i['content']
        category = i['category']
        status = i['status']
        description = i['description']

        try:
            with open(f'../simple/{slug}.md', 'w', encoding='utf-8') as f:
                f.write(f"""---
name: '{ name }'
slug: '{ slug }'
status: '{ status }'
description: '{ description }'
category: '{ category }'
---

{ content }
""")    
        except Exception:
            pass
            

simple()