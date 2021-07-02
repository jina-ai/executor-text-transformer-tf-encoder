__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import pytest
from jina import Document, DocumentArray
from jinahub.encoder.transformer_tf_text_encode import TransformerTFTextEncoder

target_dim = 768


@pytest.fixture()
def docs_generator():
    return DocumentArray((Document(text='random text') for _ in range(30)))


def test_tf_batch(docs_generator):
    encoder = TransformerTFTextEncoder()
    docs = docs_generator
    encoder.encode(docs, parameters={'batch_size': 10, 'traversal_paths': ['r']})

    assert len(docs.get_attributes('embedding')) == 30
    assert docs[0].embedding.shape == (target_dim,)


def test_traversal_path():
    text = 'blah'
    docs = DocumentArray([Document(id='root1', text=text)])
    docs[0].chunks = [Document(id='chunk11', text=text),
                      Document(id='chunk12', text=text),
                      Document(id='chunk13', text=text)
                      ]
    docs[0].chunks[0].chunks = [
        Document(id='chunk111', text=text),
        Document(id='chunk112', text=text),
    ]

    encoder = TransformerTFTextEncoder()
    encoder.encode(docs, parameters={'batch_size': 10, 'traversal_paths': ['c']})

    for path, count in [[['r'], 0], [['c'], 3], [['cc'], 0]]:
        assert len(docs.traverse_flat(path).get_attributes('embedding')) == count
        if count > 0:
            assert docs.traverse_flat(path).get_attributes('embedding')[0].shape == (target_dim,)

    encoder.encode(docs, parameters={'batch_size': 10, 'traversal_paths': ['cc']})
    for path, count in [[['r'], 0], [['c'], 3], [['cc'], 2]]:
        assert len(docs.traverse_flat(path).get_attributes('embedding')) == count
        if count > 0:
            assert docs.traverse_flat(path).get_attributes('embedding')[0].shape == (target_dim,)


def test_no_documents():
    encoder = TransformerTFTextEncoder()
    docs = DocumentArray([])
    encoder.encode(docs, parameters={'batch_size': 10, 'traversal_paths': ['r']})
    assert not docs
