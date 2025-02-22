# EVO2 API

A FastAPI-based service that interfaces with NVIDIA's API for sequence generation.

## Project Structure
```
ARC-EVO2-40B/
├── evo2-api/
├── routes/
│   └── views/
│       └── gen_seq.py
├── .dockerignore
├── .env
├── .env-dev
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── test.py
```

## Description

This API service provides an interface for sequence generation using NVIDIA's backend service. It's built using FastAPI and includes endpoint testing capabilities.

## Features

- Sequence generation endpoint
- Configurable parameters for sequence generation
- Environment-based configuration
- Docker support
- Automated testing

## Prerequisites

- Python 3.x
- Docker (optional)
- NVIDIA API access credentials

## Environment Variables

Create a `.env-dev` file with the following variables:
```
URL=your_host_url
PORT=your_port_number
NVIDIA_URL=nvidia_api_endpoint
NVCF_RUN_KEY=your_nvidia_api_key
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd ARC-EVO2-40B
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the API Server

```bash
python main.py
```

The server will start on the configured host and port specified in your environment variables.

### API Endpoints

#### GET /
- Returns a hello message
- Response format: `{"message": "hello, I am EVO2"}`

#### POST /genSeq
- Generates sequences based on input parameters
- Request body schema:
```json
{
    "sequence": "ACTGACTGACTGACTG",
    "num_tokens": 8,
    "top_k": 1,
    "enable_sampled_probs": false
}
```

### Running Tests

Execute the test suite:
```bash
python test.py
```

## Docker Support

Build the Docker image:
```bash
docker docker build -t <Image name >:<Tag > .
```

Run the container:
```bash
docker run --env-file .env-dev --name <Your desired name > -d -p <Local Port >:<ContainerPort> evo2:v1.0.0
```

## API Parameters

The `Params` model accepts the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| sequence | string | "ACTGACTGACTGACTG" | Input sequence |
| num_tokens | integer | 8 | Number of tokens to generate |
| top_k | integer | 1 | Top K parameter for sequence generation |
| enable_sampled_probs | boolean | false | Enable sampling probabilities |

## Error Handling

The API includes basic error handling for:
- Invalid requests
- NVIDIA API connection issues
- General exceptions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]
