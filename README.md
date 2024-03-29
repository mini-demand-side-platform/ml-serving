![Build](https://github.com/mini-demand-side-platform/ml-serving/workflows/build/badge.svg)

# ML Serving
This is the machine learning model serving module of the [mini-demand-side-platform](https://github.com/mini-demand-side-platform/mini-demand-side-platform).

The ML Serving server continually polls the object storage for the most up-to-date model to serve.

## Usages
Make click-through-rate prediction. The API has been designed to make multiple predictions at one time. 
The following example is making two predictions at once. Each row of the inputs is a complete feature for the model to make one prediction. 
```bash
curl -X 'POST' \
  'http://localhost:8001/model:predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "inputs": [
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1]
    ]
  }'
```

Expected output:
```json
[
    0.0013854066103122173,
    0.42452723364105566
]
```
## Requirements
- Docker 
- Docker-compose 
- make

## Setup
If you want to run this serving module on docker, please follow the instruction below.
#### 1. Activate databases 
```bash
git clone git@github.com:mini-demand-side-platform/databases.git
cd databases 
make run-all-with-example-data
```

#### 2. Run ML serving 
```bash
docker run -it --rm --network mini-demand-side-platform \
    -p 8002:8002 \
    -e object_storage_host='minio' \
	raywu60kg/ml-serving
```