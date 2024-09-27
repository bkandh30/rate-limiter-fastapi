from fastapi import FastAPI, status, HTTPException, Request
import asyncio
import time

app = FastAPI()

class TokenBucket:
    def __init__(self, capacity, refill_time) -> None:
        self.capacity = capacity
        self.refill_time = refill_time
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = asyncio.Lock()

    async def get_token(self):
        async with self.lock:
            now = time.time()
            time_passed = now - self.last_refill
            self.tokens = min(self.capacity, self.tokens + time_passed * self.refill_time)
            self.last_refill = now

            if self.tokens >= 1:
                self.tokens -=1
                return True
            return False
        

# 10 requests per second rate limit
rate_limiter = TokenBucket(capacity=10, refill_time=1)

#Unlimited Route
@app.get("/unlimited")
def unlimited():
    return {"message": "Unlimited! Let's Go!"}

#Rate Limited Route
@app.get("/limited")
async def limited (request: Request):
    if await rate_limiter.get_token():
        return {"message": "Limited, don't over use me!"}
    else:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate Limit exceeded")
    
