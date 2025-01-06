from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import yfinance as yf

app = FastAPI()

@app.post("/upload-chart/")
async def upload_chart(file: UploadFile = File(...)):
    """
    Handle chart image upload (Placeholder for future development).
    """
    return {"message": "Image uploaded successfully, analysis coming soon."}

@app.get("/strategies/{ticker}")
async def get_strategies(ticker: str):
    """
    Suggest intraday and long-term trading strategies.
    """
    try:
        data = yf.download(ticker, period="5d", interval="15m")
        recent_close = data['Close'].iloc[-10:]  # Last 10 prices
        support = min(recent_close)
        resistance = max(recent_close)

        return [
            {
                "type": "Intraday",
                "strategy": "Range-Bound",
                "entry": f"Buy near {support}",
                "stop_loss": f"{support - 0.1}",
                "profit_target": f"{support + 0.3}"
            },
            {
                "type": "Long-Term",
                "strategy": "Hold long",
                "entry": "Buy when RSI < 30",
                "stop_loss": "Below swing low",
                "profit_target": "New highs"
            }
        ]
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
