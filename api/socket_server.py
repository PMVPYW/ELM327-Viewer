import socketio
import uvicorn

# Create Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")
    await sio.emit('welcome', {'msg': 'Hello!'}, to=sid)

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

# Run Uvicorn programmatically
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
