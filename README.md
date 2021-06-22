# 🏗️ PLEASE CHECK OUT [STEP-BY-STEP](.github/STEP_BY_STEP.md)

----

# ✨ TransformerTFTextEncoder

**TransformerTFTextEncoder** is a class that ...

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🌱 Prerequisites](#-prerequisites)
- [🚀 Usages](#-usages)
- [🎉️ Example](#%EF%B8%8F-example)
- [🔍️ Reference](#%EF%B8%8F-reference)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 🌱 Prerequisites

Some conditions to fulfill before running the executor

## 🚀 Usages

### 🚚 Via JinaHub

#### using docker images
Use the prebuilt images from JinaHub in your python codes, 

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://TransformerTFTextEncoder')
```

or in the `.yml` config.
	
```yaml
jtype: Flow
pods:
  - name: encoder
    uses: 'jinahub+docker://TransformerTFTextEncoder'
```

#### using source codes
Use the source codes from JinaHub in your python codes,

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://TransformerTFTextEncoder')
```

or in the `.yml` config.

```yaml
jtype: Flow
pods:
  - name: encoder
    uses: 'jinahub://TransformerTFTextEncoder'
```


### 📦️ Via Pypi

1. Install the `jinahub-TransformerTFTextEncoder` package.

	```bash
	pip install git+https://github.com/jina-ai/EXECUTOR_REPO_NAME.git
	```

1. Use `jinahub-TransformerTFTextEncoder` in your code

	```python
	from jina import Flow
	from jinahub.encoder.TransformerTFTextEncoder import TransformerTFTextEncoder
	
	f = Flow().add(uses=TransformerTFTextEncoder)
	```


### 🐳 Via Docker

1. Clone the repo and build the docker image

	```shell
	git clone https://github.com/jina-ai/executor-text-transformer-tf-encoder.git
	cd executor-text-transformer-tf-encoder
	docker build -t TransformerTFTextEncoder .
	```

1. Use `executor-text-transformer-tf-encoder` in your codes

	```python
	from jina import Flow
	
	f = Flow().add(uses='docker://TransformerTFTextEncoder:latest')
	```
	

## 🎉️ Example 


```python
from jina import Flow, Document

f = Flow().add(uses='jinahub+docker://TransformerTFTextEncoder')

with f:
    resp = f.post(on='foo', inputs=Document(), return_resutls=True)
	print(f'{resp}')
```

### Inputs 

`Document` with `text` .

### Returns

`Document` with `embedding` fields filled with an `ndarray` of the shape `embedding_dim` (=128, by default) with `dtype=nfloat32`.


## 🔍️ Reference
- Some reference

