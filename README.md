# FastAPI Rate Limiter with Token Bucket Algorithm

This project demonstrates a simple yet effective **rate limiting solution for FastAPI applications** using the **Token Bucket algorithm**. It helps protect your API endpoints from abuse and ensures fair usage by controlling the number of requests a client can make within a specified time frame.

---

## Features

- **Token Bucket Implementation:** A custom `TokenBucket` class manages request tokens, allowing for burstable traffic while maintaining a steady average rate.
- **Asynchronous Operations:** Fully asynchronous design leveraging `asyncio.Lock` for thread-safe token management, suitable for FastAPI's async nature.
- **Configurable Rate Limits:** Easily adjust the `capacity` (maximum burst) and `refill_time` (tokens added per second) to suit your needs.
- **Clear HTTP Responses:** Returns `HTTP 429 Too Many Requests` when the rate limit is exceeded, informing clients to slow down.
- **Example Endpoints:** Includes both a rate-limited and an unlimited endpoint to showcase the functionality.

---

## API Routes

| METHOD | ROUTE        | FUNCTIONALITY          |
| ------ | ------------ | ---------------------- |
| POST   | `/limited`   | Rate Limited API Route |
| POST   | `/unlimited` | Unlimited API Route    |

---

## How It Works (Token Bucket Algorithm)

The Token Bucket algorithm works like a bucket that holds tokens.

- **Capacity:** The bucket has a maximum `capacity` (e.g., 10 tokens). This represents the maximum burst of requests allowed.
- **Refill Rate:** Tokens are added to the bucket at a steady `refill_time` rate (e.g., 1 token per second).
- **Request Consumption:** Each time a client makes a request, one token is removed from the bucket.
- **Rate Limiting:** If a client tries to make a request and the bucket is empty (no tokens available), the request is rejected (rate-limited).
- **Bursting:** Clients can make requests up to the bucket's capacity in a short period if tokens are available, allowing for short bursts of traffic.

In this implementation, the `get_token()` method handles the logic for refilling the bucket based on the time elapsed since the last refill and consuming a token if available.

---

## Getting Started

These instructions will help you set up and run the FastAPI rate limiter on your local machine.

### Prerequisites

You'll need **Python 3.11.10+** installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bkandh30/rate-limiter-fastapi.git
    cd fastapi-rate-limiter
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

To run the FastAPI application, use `uvicorn`:

```bash
uvicorn main:app --reload
```
