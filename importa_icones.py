import os
import base64
import requests

# ================== CONFIG ==================
API_URL   = "http://ipdozabbix/zabbix/api_jsonrpc.php"
API_TOKEN = "aaaaabbbbbcccccddddd"     # Gere no frontend
ICON_DIR  = r"/tool/icones"                  # Pasta raiz
IMAGETYPE = 1                                # 1=Icones, 2=Fundo
TIMEOUT_S = 30
# ============================================

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"    # <<-- Token no header
}

def rpc(method, params, req_id=1):
    payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": req_id}
    r = requests.post(API_URL, json=payload, headers=headers, timeout=TIMEOUT_S)
    r.raise_for_status()
    data = r.json()
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["result"]

def main():
    contador = 1
    for root, _, files in os.walk(ICON_DIR):
        for file in files:
            if not file.lower().endswith(".png"):
                continue
            path = os.path.join(root, file)
            try:
                with open(path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()

                nome_base = os.path.splitext(file)[0]
                nome_icone = f"{nome_base}_{contador}"

                # image.create sem 'auth' no payload
                rpc("image.create", {
                    "name": nome_icone,
                    "imagetype": IMAGETYPE,
                    "image": b64
                }, req_id=contador)

                print(f"[OK] Importado: {nome_icone}")
                contador += 1
            except Exception as e:
                print(f"[ERRO] {file}: {e}")

    print("\n✅ Importação concluída!")

if __name__ == "__main__":
    main()

