import time
import requests
from prometheus_client import start_http_server, Gauge

# Prometheus Gauge metrikleri
ohlc_open = Gauge("kraken_ohlc_open", "OHLC open price", ["pair"])
ohlc_high = Gauge("kraken_ohlc_high", "OHLC high price", ["pair"])
ohlc_low = Gauge("kraken_ohlc_low", "OHLC low price", ["pair"])
ohlc_close = Gauge("kraken_ohlc_close", "OHLC close price", ["pair"])
ohlc_vwap = Gauge("kraken_ohlc_vwap", "OHLC vwap price", ["pair"])
ohlc_volume = Gauge("kraken_ohlc_volume", "OHLC volume price", ["pair"])

# Kraken API ayarları
PAIRS = ["BTCUSD", "ETHUSD", "DOGEUSD", "HNTUSD", "KAVAUSD", "LUNAUSD", "MANAUSD", "SANDUSD", "STORJUSD", "ETHWUSD"]
INTERVAL = 60  # 1 saat aralıklı OHLC verisi (Kraken API'de dakika cinsinden ifade edilir)

def fetch_ohlc(pair):
    """Belirli bir çift için OHLC verilerini al"""
    url = f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval={INTERVAL}"
    headers = {'Accept': 'application/json'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        data = response.json()  # Yanıtı JSON formatında ayrıştır

        # Hata durumlarını kontrol et
        if data["error"]:
            print(f"Error fetching OHLC for {pair}: {data['error']}")
            return None

        # OHLC sonuçlarını al
        kraken_pair = list(data["result"].keys())[0]  # Örn: "XXBTZUSD"
        ohlc_data = data["result"][kraken_pair][-1]  # En son OHLC verisi

        return ohlc_data

    except requests.exceptions.RequestException as e:
        print(f"HTTP Exception for {pair}: {e}")
    except KeyError as e:
        print(f"KeyError for {pair}: {e}")
    except Exception as e:
        print(f"Unexpected error for {pair}: {e}")

    return None

def update_metrics():
    """Kraken API'den alınan OHLC verileri ile Prometheus metriklerini güncelle"""
    for pair in PAIRS:
        ohlc = fetch_ohlc(pair)
        if ohlc:
            try:
                # OHLC değerlerini metriklere yaz
                ohlc_open.labels(pair=pair).set(float(ohlc[1]))
                ohlc_high.labels(pair=pair).set(float(ohlc[2]))
                ohlc_low.labels(pair=pair).set(float(ohlc[3]))
                ohlc_close.labels(pair=pair).set(float(ohlc[4]))
                ohlc_vwap.labels(pair=pair).set(float(ohlc[5]))
                ohlc_volume.labels(pair=pair).set(float(ohlc[6]))
                print(f"Updated metrics for {pair}: Open={ohlc[1]}, High={ohlc[2]}, Low={ohlc[3]}, Close={ohlc[4]}, Vwap={ohlc[5]}, Volume={ohlc[6]}")
            except Exception as e:
                print(f"Exception updating metrics for {pair}: {e}")
        else:
            print(f"Failed to update metrics for {pair}")

def main():
    """Prometheus Exporter ana döngüsü"""
    # Prometheus HTTP sunucusunu başlat
    start_http_server(8000)
    print("Prometheus exporter is running on port 8000...")

    # Sürekli olarak metrikleri güncelle
    while True:
        # OHLC verilerini her 5 dakikada bir sorgula
        update_metrics()
        time.sleep(300)  # 5 dakikada bir yenile

if __name__ == "__main__":
    main()
