# rate-limiter-fastapi

This is a simple rate limiter written in Python using FastAPI and Asyncio.

This Rate Limiter uses Token Bucket Algorithm.

## API Routes

| METHOD | ROUTE        | FUNCTIONALITY          |
| ------ | ------------ | ---------------------- |
| POST   | `/limited`   | Rate Limited API Route |
| POST   | `/unlimited` | Unlimited API Route    |
