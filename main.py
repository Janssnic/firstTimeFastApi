import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#8210-8219
PORT=8210

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def hello():
    soa_protcols = ["SOAP" ,"REST" ,"GraphQL", "gRPC"]
    msg = "några populära SOA"
    my_dict = { 'message': msg,
                'myList': soa_protcols
              }
    return my_dict

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )
